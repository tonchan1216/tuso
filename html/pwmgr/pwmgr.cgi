#!/usr/bin/perl

#┌─────────────────────────────────
#│ PasswordManager v2
#│ pwmgr.cgi - 2006/04/22
#│ Copyright (c) KentWeb
#│ http://www.kent-web.com/
#└─────────────────────────────────

# 外部ファイル取込
require './jcode.pl';
require './init.cgi';

&decode;
if ($mode eq "newUser") { &axsCheck; &newUser; }
elsif ($mode eq "chgUser") { &axsCheck; &chgUser; }
elsif ($mode eq "delUser") { &axsCheck; &delUser; }
elsif ($mode eq "check") { &check; }
&error("不明なアクセスです");

#---------------------------------------
#  アクセス制限
#---------------------------------------
sub axsCheck {
	# ホスト名を取得
	&get_host;

	local($flag);
	foreach ( split(/\s+/, $denyhost) ) {
		if (index($host,$_) >= 0) { $flag = 1; last; }
		if (index($host,$_) >= 0) { $flag = 1; last; }
	}
	if ($flag) { &error("現在登録休止中です"); }
}

#---------------------------------------
#  ユーザ登録
#---------------------------------------
sub newUser {
	# 発行制限
	if ($pwd_regist > 1) { &error("不正なアクセスです"); }

	# チェック
	if ($in{'name'} eq "") { &error("名前が入力モレです"); }
	if ($in{'eml1'} ne $in{'eml2'}) { &error("メールの再度入力が異なります"); }
	if ($in{'eml1'} !~ /^[\w\.\-]+\@[\w\.\-]+\.[a-zA-Z]{2,6}$/) {
		&error("メールの入力内容が不正です");
	}
	if (length($in{'id'}) < 4 || length($in{'id'}) > 8) {
		&error("ログインIDは4～8文字で入力してください");
	}
	if ($in{'id'} =~ /\W/) {
		&error("ログインIDに英数字以外の文字が含まれています");
	}

	# IDの重複チェック
	local($f) = 0;
	open(IN,"$pwdfile") || &error("Open Error: $pwdfile");
	while (<IN>) {
		local($id) = split(/:/);
		if ($in{'id'} eq $id) { $f++; last; }
	}
	close(IN);

	if ($f) {
		&error("$in{'id'}は既に発行済です。<br>他のIDをご指定ください");
	}

	# パス発行
	local(@char) = (0 .. 9, 'a' .. 'z', 'A' .. 'Z');
	local($pw,$pw2);
	srand;
	foreach (1 .. 8) {
		$pw .= $char[int(rand(@char))];
	}

	# 暗号化
	$pw2 = &encrypt($pw);

	# ロック開始
	&lock if ($lockkey);

	# パスファイル追加
	open(OUT,">>$pwdfile") || &error("Write Error: $pwdfile");
	print OUT "$in{'id'}:$pw2\n";
	close(OUT);

	# 会員ファイル
	open(IN,"$memfile") || &error("Open Error: $memfile");
	local(@file) = <IN>;
	close(IN);

	unshift(@file,"$in{'id'}<>$in{'name'}<>$in{'eml1'}<><>\n");
	open(OUT,">$memfile") || &error("Write Error: $memfile");
	print OUT @file;
	close(OUT);

	# ロック解除
	&unlock if ($lockkey);

	# 時間取得
	$date = &get_time;

	# メール本文
	$mbody = <<EOM;
$in{'name'}様

「$title」へのご登録をありがとうございます。
以下のとおりログインIDとパスワードを発行しました。

※パスワードはご自分で自由に変更可能\ですので、覚えやすいものに
  変更しておくことができます。

▼登録内容
登録日時   : $date
ホスト情報 : $host
お名前     : $in{'name'}
E-mail     : $in{'eml1'}

▼ログイン情報
ログインID : $in{'id'}
パスワード : $pw

---
  $title管理人 <$master>
EOM

	# 題名をBASE64化
	local($msub) = &base64("登録の案内");

	# sendmail送信
	open(MAIL,"| $sendmail -t -i") || &error("メール送信失敗");
	print MAIL "To: $in{'eml1'}\n";
	print MAIL "From: $master\n";
	print MAIL "Cc: $master\n";
	print MAIL "Subject: $msub\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-type: text/plain; charset=ISO-2022-JP\n";
	print MAIL "Content-Transfer-Encoding: 7bit\n";
	print MAIL "X-Mailer: $ver\n\n";
	foreach ( split(/\n/, $mbody) ) {
		&jcode'convert(*_, 'jis', 'sjis');
		print MAIL $_, "\n";
	}
	close(MAIL);

	&header;
	print <<EOM;
<div align="center">
<table border="1" cellpadding="20" cellspacing="0" width="450">
<tr><td align="center" class="r">
<font size="-1">
<h3>ご登録ありがとうございました。</h3>
ログインIDとパスワード情報は<br>
<b>$in{'eml1'}</b><br>
へ送信しました。</font>
<p>
<form>
<input type="button" value="TOPに戻る" onclick=window.open("$backUrl","_top")>
</form>
</td></tr>
</table>
<br><br><br>
<!-- 著作権表\示削除不可 -->
<span style="font-size:10px;font-family:Verdana,Helvetica,Arial">
- <a href="http://www.kent-web.com/" target="_top">PasswordManager</a> -
</span></div>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  ユーザPW変更
#---------------------------------------
sub chgUser {
	# 発行制限
	if ($pwd_regist > 2) { &error("不正なアクセスです"); }

	# チェック
	if ($in{'id'} eq "") { &error("ログインIDが入力モレです"); }
	if ($in{'pw'} eq "") { &error("旧パスワードが入力モレです"); }
	if ($in{'pw1'} eq "") { &error("新パスワードが入力モレです"); }
	if ($in{'pw1'} ne $in{'pw2'}) {
		&error("新パスワードで再度入力分が異なります");
	}

	# 暗号化
	local($newpw) = &encrypt($in{'pw1'});

	# IDチェック
	local($f, $enpw, @new);
	open(IN,"$pwdfile") || &error("Open Error: $pwdfile");
	while (<IN>) {
		local($id,$pw) = split(/:/);

		if ($in{'id'} eq $id) {
			$f = 1;
			$enpw = $pw;
			$_ = "$id:$newpw\n";
		}
		push(@new,$_);
	}
	close(IN);

	if (!$f) {
		&error("ログインID ($in{'id'}) は存在しません");
	}

	# 照合
	$enpw =~ s/\n//;
	if ( &decrypt($in{'pw'}, $enpw) != 1 ) {
		&error("パスワードが違います");
	}

	# ロック開始
	&lock if ($lockkey);

	# パスファイル更新
	open(OUT,">$pwdfile") || &error("Write Error: $pwdfile");
	print OUT @new;
	close(OUT);

	# ロック解除
	&unlock if ($lockkey);

	&header;
	print <<EOM;
<div align="center">
<table border="1" cellpadding="20" cellspacing="0" width="450">
<tr><td align="center" class="r">
<font size="-1">
<h3>パスワード変更完了</h3>
ご利用をありがとうございました。
</font>
<form>
<input type="button" value="TOPに戻る" onclick=window.open("$backUrl","_top")>
</form>
</td></tr>
</table>
<br><br><br>
<!-- 著作権表\示削除不可 -->
<span style="font-size:10px;font-family:Verdana,Helvetica,Arial">
- <a href="http://www.kent-web.com/" target="_top">PasswordManager</a> -
</span></div>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  ユーザ削除
#---------------------------------------
sub delUser {
	# 発行制限
	if ($pwd_regist > 2) { &error("不正なアクセスです"); }

	# チェック
	if ($in{'id'} eq "") { &error("ログインIDが入力モレです"); }
	if ($in{'pw'} eq "") { &error("パスワードが入力モレです"); }

	# ロック開始
	&lock if ($lockkey && $in{'job'} eq "del");

	# IDチェック
	local($f, $enpw, @new);
	open(IN,"$pwdfile") || &error("Open Error: $pwdfile");
	while (<IN>) {
		local($id,$pw) = split(/:/);

		if ($in{'id'} eq $id) {
			$f = 1;
			$enpw = $pw;
			next;
		}
		push(@new,$_) if ($in{'job'} eq "del");
	}
	close(IN);

	if (!$f) {
		&error("ログインID ($in{'id'}) は存在しません");
	}

	# 照合
	$enpw =~ s/\n//;
	if ( &decrypt($in{'pw'}, $enpw) != 1 ) {
		&error("パスワードが違います");
	}

	# 実行
	if ($in{'job'} eq "del") {

		# パスファイル更新
		open(OUT,">$pwdfile") || &error("Write Error: $pwdfile");
		print OUT @new;
		close(OUT);

		# 会員ファイル
		local(@file);
		open(IN,"$memfile") || &error("Open Error: $memfile");
		while (<IN>) {
			local($id) = split(/<>/);
			next if ($in{'id'} eq $id);

			push(@file,$_);
		}
		close(IN);

		open(OUT,">$memfile") || &error("Write Error: $memfile");
		print OUT @file;
		close(OUT);

		# ロック解除
		&unlock if ($lockkey);

		# 完了メッセージ
		&header;
		print <<EOM;
<div align="center">
<table border="1" cellpadding="20" cellspacing="0" width="450">
<tr><td align="center" class="r">
<font size="-1">
<h3>登録ID削除完了</h3>
これまでのご利用をありがとうございました。
</font>
<form>
<input type="button" value="TOPに戻る" onclick=window.open("$backUrl","_top")>
</form>
</td></tr>
</table>
<br><br><br>
<!-- 著作権表\示削除不可 -->
<span style="font-size:10px;font-family:Verdana,Helvetica,Arial">
- <a href="http://www.kent-web.com/" target="_top">PasswordManager</a> -
</span></div>
</body>
</html>
EOM
		exit;
	}

	# 確認画面
	&header;
	print <<EOM;
<div align="center">
<table border="1" cellpadding="20" cellspacing="0" width="450">
<tr><td align="center" class="r">
<font size="-1">
<h3>登録の削除</h3>
<form action="$script" method="post">
<input type="hidden" name="mode" value="delUser">
<input type="hidden" name="id" value="$in{'id'}">
<input type="hidden" name="pw" value="$in{'pw'}">
<input type="hidden" name="job" value="del">
ログインID <b>$in{'id'}</b> を本当に削除しますか？
</font>
<p>
<input type="submit" value="登録を削除する">
</form>
</td></tr>
</table>
</div>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  BASE64変換
#---------------------------------------
#	とほほのWWW入門で公開されているルーチンを
#	参考にしました。( http://tohoho.wakusei.ne.jp/ )
sub base64 {
	local($sub) = @_;
	&jcode'convert(*sub, 'jis', 'sjis');

	$sub =~ s/\x1b\x28\x42/\x1b\x28\x4a/g;
	$sub = "=?iso-2022-jp?B?" . &b64enc($sub) . "?=";
	$sub;
}
sub b64enc {
	local($ch)="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
	local($x, $y, $z, $i);
	$x = unpack("B*", $_[0]);
	for ($i=0; $y=substr($x,$i,6); $i+=6) {
		$z .= substr($ch, ord(pack("B*", "00" . $y)), 1);
		if (length($y) == 2) {
			$z .= "==";
		} elsif (length($y) == 4) {
			$z .= "=";
		}
	}
	$z;
}

#---------------------------------------
#  簡易チェック
#---------------------------------------
sub check {
	local($k, $v, %log);

	&header;
	print <<EOM;
<font size="-1">
<h3>チェックモード</h3>
<ul>
EOM

	%log = (
		'パスワードファイル', $pwdfile,
		'会員ファイル', $memfile,
		'アクセスログ (使用する場合)', $axsfile,
	);

	while ( ($k,$v) = each(%log) ) {

		# パス
		if (-e $v) {
			print "<li>$kパス OK!\n";

			# パーミッション
			if (-r $v && -w $v) {
				print "<li>$kパーミッション OK!\n";
			} else {
				print "<li>$kパーミッション NG!\n";
			}
		} else {
			print "<li>$kパスNG! → $v\n";
		}
	}

	# sendmail
	if (-e $sendmail) {
		print "<li>sendmailパス OK!\n";
	} else {
		print "<li>sendmailパス NG! → $sendmail (使用する場合)\n";
	}

	# ロックディレクトリ
	print "<li>ロック形式 → ";
	if ($lockkey == 0) {
		print "設定なし\n";
	} else {
		if ($lockkey == 1) { print "symlink\n"; }
		else { print "mkdir\n"; }

		local($lockdir) = $lockfile =~ /(.*)[\\\/].*$/;
		print "<li>ロックディレクトリ → $lockdir\n";

		if (-d $lockdir) {
			print "<li>ロックディレクトリパスOK!\n";
			if (-r $lockdir && -w $lockdir && -x $lockdir) {
				print "<li>ロックディレクトリパーミッション OK!\n";
			} else {
				print "<li>ロックディレクトリパーミッション NG! → $lockdir\n";
			}
		} else {
			print "<li>ロックディレクトリ NG! → $lockdir\n";
		}
	}

	# 著作権表示（削除不可）
	print <<EOM;
<li>バージョン → $ver
</ul>
</font>
</body>
</html>
EOM
	exit;
}


__END__

