#!/usr/bin/perl

#┌────────────────────────
#│ PasswordManager v2
#│ admin.cgi - 2006/08/06
#│ Copyright (c) KentWeb
#│ http://www.kent-web.com/
#└────────────────────────

# 外部ファイル取込
require './jcode.pl';
require './init.cgi';

&decode;
if ($in{'pass'} eq "") { &enter; }
elsif ($in{'pass'} ne $pass) { &error('パスワードが違います'); }
if ($mode eq "member") { &member; }
elsif ($mode eq "axslog") { &axslog; }
&admin;

#---------------------------------------
#  管理TOP
#---------------------------------------
sub admin {
	&header;
	print <<EOM;
<form action="$admin">
<input type=submit value="▲ログオフ">
</form>
<font size="-1">
<ul>
<li>処理を選択してください。
<li>アクセスログは、別途「SSI + pwlog.cgi」による埋め込みが必要です。
</ul>
</font>
<blockquote>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<table border="1" cellspacing="0" cellpadding="4">
<tr>
  <th class="l"><font size="-1">選択</font></th>
  <th class="l"><font size="-1">項目</font></th>
</tr>
<tr>
  <th class="r"><input type=radio name=mode value="member"></th>
  <td class="r"><font size="-1">会員管理（追加・修正・削除）</font></td>
</tr>
<tr>
  <th class="r"><input type=radio name=mode value="axslog"></th>
  <td class="r"><font size="-1">アクセスログ</font></td>
</tr>
</table>
<p>
<input type="submit" value="選択する">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  会員閲覧
#---------------------------------------
sub member {
	# 新規画面
	if ($in{'job'} eq "new") {

		&newform;

	# 新規登録
	} elsif ($in{'job'} eq "new2") {

		local($f,$pwd,@file);

		# チェック
		if ($in{'id'} eq "") { &error("ユーザIDが未入力です"); }
		if ($in{'pw'} eq "") { &error("パスワードが未入力です"); }

		# IDの重複チェック
		$f=0;
		open(IN,"$pwdfile") || &error("Open Error: $pwdfile");
		while (<IN>) {
			($id) = split(/:/);

			if ($in{'id'} eq $id) { $f++; last; }
		}
		close(IN);

		if ($f) { &error("<b>$in{'id'}</b>は既に発行済です"); }

		# PWを暗号化
		$pwd = &encrypt($in{'pw'});

		# ロック開始
		&lock if ($lockkey);

		open(OUT,">>$pwdfile") || &error("Write Error: $pwdfile");
		print OUT "$in{'id'}:$pwd\n";
		close(OUT);

		open(IN,"$memfile") || &error("Open Error: $memfile");
		@file = <IN>;
		close(IN);

		unshift(@file,"$in{'id'}<>$in{'name'}<>$in{'email'}<>$in{'memo'}<>\n");
		open(OUT,">$memfile") || &error("Write Error: $memfile");
		print OUT @file;
		close(OUT);

		# ロック解除
		&unlock if ($lockkey);

		$in{'name'}  ||= '名前なし';
		$in{'email'} ||= 'E-mailなし';
		$in{'memo'}  ||= 'なし';

		&header;
		print <<EOM;
▽以下のとおり発行しました。
<dl>
<dt>【名前】<dd>$in{'name'}
<dt>【E-mail】<dd>$in{'email'}
<dt>【ユーザID】<dd>$in{'id'}
<dt>【パスワード】<dd>$in{'pw'}
<dt>【備考】<dd>$in{'memo'}
</dl>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="submit" value="管理画面TOPへ">
</form>
</body>
</html>
EOM
		exit;

	# 修正フォーム
	} elsif ($in{'job'} eq "edit") {

		if ($in{'id'} =~ /\0/) { &error("修正は複数選択できません"); }

		# PWファイル
		local($f,$id,$nam,$eml,$memo);
		open(IN,"$memfile") || &error("Open Error: $memfile");
		while (<IN>) {
			($id,$nam,$eml,$memo) = split(/<>/);

			if ($in{'id'} eq $id) { $f++; last; }
		}
		close(IN);

		if (!$f) { &error("該当のID情報が見当たりません"); }

		&edit_form($id,$nam,$eml,$memo);

	# 修正実行
	} elsif ($in{'job'} eq "edit2") {

		# ロック開始
		&lock if ($lockkey);

		# 会員ファイル
		local(@new);
		open(IN,"$memfile") || &error("Open Error: $memfile");
		while (<IN>) {
			local($id,$nam,$eml,$memo) = split(/<>/);

			if ($in{'id'} eq $id) {
				$_ = "$id<>$in{'name'}<>$in{'email'}<>$in{'memo'}<>\n";
			}
			push(@new,$_);
		}
		close(IN);

		open(OUT,">$memfile") || &error("Write Error: $memfile");
		print OUT @new;
		close(OUT);

		# ロック解除
		&unlock if ($lockkey);

	# パスワード強制変更
	} elsif ($in{'job'} eq "pwchg") {

		local($pwd,@new);

		# チェック
		if ($in{'pw'} eq "") { &error("パスワードが未入力です"); }

		# PWを暗号化
		$pwd = &encrypt($in{'pw'});

		# ロック開始
		&lock if ($lockkey);

		# PWファイル
		open(IN,"$pwdfile") || &error("Open Error: $pwdfile");
		while (<IN>) {
			local($id) = split(/:/);

			if ($in{'id'} eq $id) { $_ = "$id:$pwd\n"; }

			push(@new,$_);
		}
		close(IN);

		open(OUT,">$pwdfile") || &error("Write Error: $pwdfile");
		print OUT @new;
		close(OUT);

		# ロック解除
		&unlock if ($lockkey);

	# 削除
	} elsif ($in{'job'} eq "dele") {

		local($f,@del,@new);

		# 削除情報
		@del = split(/\0/, $in{'id'});

		# ロック開始
		&lock if ($lockkey);

		# PWファイル
		open(IN,"$pwdfile") || &error("Open Error: $pwdfile");
		while (<IN>) {
			local($id) = split(/:/);

			$f = 0;
			foreach $del (@del) {
				if ($id eq $del) { $f++; last; }
			}
			if (!$f) { push(@new,$_); }
		}
		close(IN);

		open(OUT,">$pwdfile") || &error("Write Error: $pwdfile");
		print OUT @new;
		close(OUT);

		# 会員ファイル
		@new = ();
		open(IN,"$memfile") || &error("Open Error: $memfile");
		while (<IN>) {
			local($id) = split(/<>/);

			$f = 0;
			foreach $del (@del) {
				if ($id eq $del) { $f++; last; }
			}
			if (!$f) { push(@new,$_); }
		}
		close(IN);

		open(OUT,">$memfile") || &error("Write Error: $memfile");
		print OUT @new;
		close(OUT);

		# ロック解除
		&unlock if ($lockkey);
	}

	&header;
	print <<EOM;
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="submit" value="▲管理TOP">
</form>
<font size="-1">
<ul>
<li>処理を選択して送信ボタンを押してください。
</ul>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="page" value="$page">
処理 : <select name="job">
<option value="new">新規
<option value="edit">修正
<option value="dele">削除
</select>
</font>
<input type="submit" value="送信する">
<p>
<table border="1" cellspacing="0" cellpadding="2">
<tr>
  <th class="l"><font size="-1">選択</font></th>
  <th class="l"><font size="-1">ID名</font></th>
  <th class="l"><font size="-1">名前</font></th>
  <th class="l"><font size="-1">備考</font></th>
</tr>
EOM

	local($i) = 0;
	open(IN,"$memfile") || &error("Open Error: $memfile");
	while (<IN>) {
		$i++;
		next if ($i < $page + 1);
		next if ($i > $page + $pageView);

		local($id,$nam,$eml,$memo) = split(/<>/);

		$nam ||= '名前なし';
		$eml &&= "<a href=\"mailto:$eml\">$nam</a>";
		$memo =~ s/<br>/ /g;

		print "<tr class=\"r\"><th><input type=\"checkbox\" name=\"id\" value=\"$id\"></th>";
		print "<td><font size=\"-1\"><b>$id</b></font></td>";
		print "<td><font size=\"-1\">$nam</font></td>";
		print "<td><font size=\"-1\">$memo</font><br></td></tr>\n";
	}
	close(IN);

	print <<EOM;
</table>
</form>
EOM

	local($next) = $page + $pageView;
	local($back) = $page - $pageView;

	print "<table><tr>\n";
	if ($back >= 0) {
		print "<td><form action=\"$admin\" method=\"post\">\n";
		print "<input type=\"hidden\" name=\"pass\" value=\"$in{'pass'}\">\n";
		print "<input type=\"hidden\" name=\"mode\" value=\"member\">\n";
		print "<input type=\"hidden\" name=\"page\" value=\"$back\">\n";
		print "<input type=\"submit\" value=\"前の$pageView件\"></td></form>\n";
	}
	if ($next < $i) {
		print "<td><form action=\"$admin\" method=\"post\">\n";
		print "<input type=\"hidden\" name=\"pass\" value=\"$in{'pass'}\">\n";
		print "<input type=\"hidden\" name=\"mode\" value=\"member\">\n";
		print "<input type=\"hidden\" name=\"page\" value=\"$next\">\n";
		print "<input type=\"submit\" value=\"次の$pageView件\"></td></form>\n";
	}

	print <<EOM;
</tr>
</table>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  登録画面
#---------------------------------------
sub newform {
	&header;
	print <<EOM;
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="page" value="$page">
<input type="submit" value="&lt; 前画面">
</form>
<font size="-1">
<ul>
<li>各項目を入力して送信ボタンを押してください。
<li>ユーザIDとパスワードは必須です。（他は任意）
</ul>
</font>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="job" value="new2">
EOM

	&form();

	print "</body></html>\n";
	exit;
}

#---------------------------------------
#  修正画面
#---------------------------------------
sub edit_form {
	local($id,$nam,$eml,$memo) = @_;

	&header;
	print <<EOM;
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="page" value="$page">
<input type="submit" value="&lt; 前画面">
</form>
<font size="-1">
<ul>
<li>以下のフォームより、<b>$id</b> の属性情報を変更します。
<li>変更する箇所のみ修正して送信ボタンを押してください。
</ul>
</font>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="job" value="edit2">
<input type="hidden" name="id" value="$in{'id'}">
EOM

	&form($id,$nam,$eml,$memo);

	print <<EOM;
<hr>
<font size="-1">
<ul>
<li>以下のフォームより、パスワードを強制変更します。
</ul>
</font>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="job" value="pwchg">
<input type="hidden" name="id" value="$in{'id'}">
<table border="1" cellspacing="0" cellpadding="4">
<tr>
  <th class="l"><font size="-1">パスワード</font></th>
  <td class="r">
	<input type="text" name="pw" size="8" maxlength="8" style="ime-mode:inactive">
	<font color="green" size="-1">(8文字以内)</font></td>
</tr>
</table>
<p>
<input type="submit" value="強制変更する">
</form>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  フォーム
#---------------------------------------
sub form {
	local($id,$nam,$eml,$memo) = @_;
	$memo =~ s/<br>/\r/g;

	print <<EOM;
<table border="1" cellspacing="0" cellpadding="4">
<tr>
  <th class="l"><font size="-1">名前</font></th>
  <td class="r"><input type="text" name="name" size="30" value="$nam"></td>
</tr>
<tr>
  <th class="l"><font size="-1">E-mail</font></th>
  <td class="r"><input type="text" name="email" size="30" value="$eml"></td>
</tr>
<tr>
  <th class="l"><font size="-1">ユーザID</font></th>
EOM

	if ($id eq "") {
		print "<td class=\"r\">";
		print "<input type=\"text\" name=\"id\" size=\"8\" maxlength=\"8\" style=\"ime-mode:inactive\">\n";
		print "<font color=\"green\" size=\"-1\">(8文字以内)</font></td></tr>\n";
		print "<tr><th class=\"l\"><font size=\"-1\">パスワード</font></th>\n";
  		print "<td class=\"r\"><input type=\"text\" name=\"pw\" size=\"8\" maxlength=\"8\" style=\"ime-mode:inactive\">\n";
		print "<font color=\"green\" size=\"-1\">(8文字以内)</font></td></tr>\n";
	} else {
		print "<td class=\"r\"><b>$id</b></td></tr>\n";
	}

	print <<EOM;
<tr>
  <th class="l"><font size="-1">備考</font></th>
  <td class="r"><textarea name="memo" cols="30" rows="4">$memo</textarea></td>
</tr>
</table>
<p>
<input type="submit" value="送信する"><input type="reset" value="リセット">
</form>
EOM
}

#---------------------------------------
#  アクセスログ
#---------------------------------------
sub axslog {
	&header;
	print <<EOM;
<table cellpadding="1" cellspacing="1" border="0">
<tr>
  <td>
    <form action="$admin" method="post">
    <input type="hidden" name="pass" value="$in{'pass'}">
    <input type="submit" value="▲管理TOP">
  </td></form>
  <td>
    <form action="$admin" method="post">
    <input type="hidden" name="mode" value="$mode">
    <input type="hidden" name="pass" value="$in{'pass'}">
    <input type="hidden" name="shukei" value="off">
    <input type="hidden" name="da" value="$da">
    <input type="hidden" name="ho" value="$ho">
    <input type="hidden" name="ag"value="$ag">
    <input type="submit" value="ログ一覧" class="f">
  </td></form>
  <td>
    <form action="$admin" method="post">
    <input type="hidden" name="mode" value="$mode">
    <input type="hidden" name="pass" value="$in{'pass'}">
    <input type="hidden" name="shukei" value="on">
    <input type="hidden" name="da" value="$da">
    <input type="hidden" name="ho" value="$ho">
    <input type="hidden" name="ag" value="$ag">
    <input type="submit" value="ログ集計" class="f">
  </td></form>
</tr>
</table>
<font size="-1">
EOM

	# ログ一覧の場合
	if ($in{'shukei'} ne "on") {

		# ページ繰越
		local($pg) = 0;
		foreach ( keys(%in) ) {
			if (/^pg(\d+)$/) {
				$pg = $1;
				last;
			}
		}

		print "<dl><dt>▼<b>ログ一覧</b>\n";

		local($i) = 0;
		open(IN,"$axsfile");
		while (<IN>) {
			$i++;
			next if ($i < $pg + 1);
			last if ($i > $pg + $pageView);

			local($id,$date,$host,$agent) = split(/<>/);
 
			print "<dt><hr><b>$id</b> - $date\n";
			print "<dd>$host - $agent\n";
		}
		close(IN);

		print "<dt><hr></dl>\n";

		local($next) = $pg + $pageView;
		local($back) = $pg - $pageView;

		if ($back >= 0 || $next < $i) {
			print "<form action=\"$admin\" method=\"post\">\n";
			print "<input type=\"hidden\" name=\"pass\" value=\"$in{'pass'}\">\n";
			print "<input type=\"hidden\" name=\"mode\" value=\"$mode\">\n";

			if ($back >= 0) {
				print "<input type=\"submit\" name=\"pg$back\" value=\"前の$pageView件\">\n";
			}
			if ($next < $i) {
				print "<input type=\"submit\" name=\"pg$next\" value=\"次の$pageView件\">\n";
			}
			print "</form>\n";
		}

	# ログ集計の場合
	} else {
		print "<p>▼<b>ログ集計</b>\n";
		print "<p><table border=\"1\" cellspacing=\"0\" cellpadding=\"2\">\n";
		print "<tr><th class=\"l\"><font size=\"-1\">ユーザID</font></th>";
		print "<th class=\"l\"><font size=\"-1\">アクセス数</font></th></tr>\n";

		# データ集計
		local(%count);
		open(IN,"$axsfile");
		while (<IN>) {
			local($id,$date,$host,$agent) = split(/<>/);

			$count{$id}++;
		}
		close(IN);

		# 配列化
		local($key,$val,@key,@val);
		while ( ($key,$val) = each(%count) ) {

			push(@key,$key);
			push(@val,$val);
		}

		# ソート
		@key = @key[sort {$val[$b] <=> $val[$a]} 0..$#val];

		# セル集計表示
		foreach (@key) {
			print "<tr><td class=\"r\"><font size=\"-1\">$_</font></td>";
			print "<td class=\"r\" align=\"right\"><font size=\"-1\">$count{$_}</font></td></tr>\n";
		}
		print "</table>\n";
	}

	print <<EOM;
</font>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  入室画面
#---------------------------------------
sub enter {
	&header;
	print <<EOM;
<font size="-1">
<div align="center">
<b>パスワードを入力してください</b>
</font>
<form action="$admin" method="post">
<input type="password" name="pass" size="8">
<input type="submit" value="ログイン">
</form>
</div>
</body>
</html>
EOM
	exit;
}

