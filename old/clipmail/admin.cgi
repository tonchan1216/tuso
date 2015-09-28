#!/usr/bin/perl

#┌─────────────────────────────────
#│ Clip Mail
#│ admin.cgi - 2007/05/26
#│ copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────

# 外部ファイル取り込み
require './init.cgi';
require $jcodepl;

# カラー
$accol_1 = "#004080";
$accol_2 = "#bdbddf";
$accol_3 = "#ffffff";

# フォームデコード
&parse_form;
$mode = $in{'mode'};

# 基本処理
&pwd_check;
if ($mode eq "get_log") { &get_log; }
elsif ($mode eq "pass_chg") { &pass_chg; }
&menu_list;

#-------------------------------------------------
#  管理画面
#-------------------------------------------------
sub menu_list {
	&header("管理メニュー");
	print <<EOM;
<table width="640">
<tr>
  <td align="right">
	<form action="$admincgi" method="post">
	<input type="submit" value="▲ログオフ">
	</form>
  </td>
</tr>
</table>
<blockquote>
<font size="-1">処理を選択して送信ボタンを押してください。</font>
<p>
<form action="$admincgi" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<table cellpadding="5" cellspacing="1" bgcolor="$accol_1" width="350">
<tr>
  <th bgcolor="$accol_2" nowrap><font size="-1">選択</font></th>
  <th bgcolor="$accol_2" nowrap width="100%"><font size="-1">処理項目</font></th>
</tr>
<tr>
  <th bgcolor="$accol_3" nowrap><input type="radio" name="mode" value="get_log"></th>
  <td bgcolor="$accol_3" nowrap width="100%">
	&nbsp; <font size="-1">CSVダウンロード</font></td>
</tr>
<tr>
  <th bgcolor="$accol_3" nowrap><input type="radio" name="mode" value="pass_chg"></th>
  <td bgcolor="$accol_3" nowrap width="100%">
	&nbsp; <font size="-1">管理パスワードの変更</font></td>
</tr>
</table>
<p>
<input type="submit" value="送信する">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  ログダウンロード
#-------------------------------------------------
sub get_log {
	# ダウンロード実行
	if ($in{'downld'}) {

		# 選択チェック
		if (!$in{'br'} || !$in{'tag'}) { &error("オプションに未選択があります"); }

		# 改行コード定義
		my %br = ("win" => "\r\n", "mac" => "\r", "unix" => "\n");

		# ログをオープン
		my ($i, %key, %log);
		open(IN,"$logfile");
		while(<IN>) {
			chomp;

			# 日時, IP, 本文に分割
			my ($log_date, $log_ip, $log) = split(/<>/, $_, 3);

			# HTML変換
			if ($in{'tag'} eq "full") {
				$log =~ s/&lt;/</g;
				$log =~ s/&gt;/>/g;
				$log =~ s/&quot;/"/g;
				$log =~ s/&#39;/'/g;
				$log =~ s/&amp;/&/g;
			} else {
				$log =~ s/&lt;/＜/g;
				$log =~ s/&gt;/＞/g;
				$log =~ s/&quot;/”/g;
				$log =~ s/&#39;/’/g;
				$log =~ s/&amp;/＆/g;
			}

			# 日時＆IPをハッシュ定義
			$i++;
			my ($key, $date) = split(/=/, $log_date);
			$log{"$i:date"} = $date;
			my ($key, $ip) = split(/=/, $log_ip);
			$log{"$i:ip"} = $ip;

			# 本文を各項目ごとに分割
			foreach my $itm ( split(/<>/, $log) ) {
				my ($key, $val) = split(/=/, $itm, 2);

				# 本文をハッシュ定義
				$log{"$i:$key"} = $val;

				# 行ごとの項目名を覚えておく
				# (送信ごとに項目数が異なるケースがあるため)
				$key{$key}++;
			}
		}
		close(IN);

		# ダウンロード用ヘッダー
		print "Content-type: application/octet-stream\n";
		print "Content-Disposition: attachment; filename=postmail.csv\n\n";

		# バイナリーモード出力（Windowsサーバ対策）
		binmode(STDOUT);

		# トップ行の「項目」を表示
		print "日付,IPアドレス,";
		my @keys;
		foreach ( keys(%key) ) {
			print "$_,";

			# 項目名の順番を覚えておく
			push(@keys,$_);
		}
		print $br{$in{'br'}};

		# ログ本体を展開（最後は$i個）
		foreach my $n (1 .. $i) {

			# 日付＆IPを表示
			my $csv;
			$csv .= qq |$log{"$n:date"},|;
			$csv .= qq |$log{"$n:ip"},|;

			# 本体は項目順に表示していく
			foreach my $key (@keys) {
				$csv .= qq |\"$log{"$n:$key"}\",|;
			}
			print "$csv$br{$in{'br'}}";
		}
		exit;
	}

	# ログ個数を数える
	my $i = 0;
	open(IN,"$logfile");
	++$i while(<IN>);
	close(IN);

	# ダウンロード画面
	&header("CSVダウンロード");
	&back_button;
	print <<EOM;
<blockquote>
<font size="-1">
・ 現在のログ個数： <b>$i</b>個<br>
・ 各オプションを選択して、ダウンロードボタンを押してください。<br>
<form action="$admincgi" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<table bgcolor="$accol_1" cellpadding="4" cellspacing="1" width="280">
<tr>
  <th bgcolor="$accol_2" nowrap>
	<font size="-1">改行形式</font>
  </th>
  <td bgcolor="$accol_3" nowrap width="100%">
	<font size="-1">
	<input type="radio" name="br" value="win">Windows形式 （CR+LF）<br>
	<input type="radio" name="br" value="mac">Macintosh形式 （CR）<br>
	<input type="radio" name="br" value="unix">UNIX形式 （LF）
	</font>
  </td>
</tr>
<tr>
  <th bgcolor="$accol_2" nowrap>
	<font size="-1">HTML変換</font>
  </th>
  <td bgcolor="$accol_3" nowrap width="100%">
	<font size="-1">
	<input type="radio" name="tag" value="full">完全復元<br>
	<input type="radio" name="tag" value="zen" checked>全角文字変換（おすすめ）
	</font>
  </td>
</tr>
</table>
<p>
<input type="submit" name="downld" value="ダウンロード">
</form>
<p>
※HTMLは、「&lt;」「&gt;」「&quot;」「&amp;」「&#39;」を指します。
</font>
</blockquote>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  パスワード変更
#-------------------------------------------------
sub pass_chg {
	# 変更実行
	if ($in{'change'}) {

		# 入力チェック
		my $err;
		if ($in{'pass_1'} eq "") {
			$err .= qq |新パスワードが未入力です<br>|;
		}
		if ($in{'pass_1'} ne $in{'pass_2'}) {
			$err .= qq |再入力のパスワードが異なります<br>|;
		}
		if ($err) { &error($err); }

		# パスワードファイル更新
		open(DB,"> $pwdfile");
		print DB &encrypt($in{'pass_1'});
		close(DB);

		# 旧パスを新パスに置き換え
		$in{'pass'} = $in{'pass_1'};

		# 完了メッセージ
		&message("パスワードを変更しました");
	}

	# 変更画面
	&header("パスワード変更");
	&back_button;
	print <<EOM;
<blockquote>
<font size="-1">
新パスワードを入力して送信ボタンを押してください。
</font>
<form action="$admincgi" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<table bgcolor="$accol_1" cellpadding="4" cellspacing="1">
<tr>
  <th bgcolor="$accol_2" nowrap><font size="-1">新パスワード</font></th>
  <td bgcolor="$accol_3" nowrap>
	<input type="password" name="pass_1" value="" size="25">
	<font size="-1">（英数字で8文字以内）</font>
  </td>
</tr>
<tr>
  <th bgcolor="$accol_2" nowrap><font size="-1">再度入力</font></th>
  <td bgcolor="$accol_3" nowrap>
	<input type="password" name="pass_2" value="" size="25">
  </td>
</tr>
</table>
<p>
<input type="submit" name="change" value="送信する">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  認証
#-------------------------------------------------
sub pwd_check {
	# 入室画面
	if ($in{'pass'} eq "") {

		# パスワードファイルが空ファイルならば変更画面へ
		if (-z $pwdfile) { &pass_chg; }

		# 入室画面
		&enter_disp;

	# 認証
	} else {

		# パスファイルをオープン
		open(IN,"$pwdfile");
		my $data = <IN>;
		close(IN);

		# パスワード照合
		if (&decrypt($in{'pass'} ,$data) != 1) {
			&error("認証できません");
		}
	}
}

#-------------------------------------------------
#  入室画面
#-------------------------------------------------
sub enter_disp {
	&header("入室画面");
	print <<EOM;
<blockquote>
<form action="$admincgi" method="post">
<table width="380">
<tr>
  <td height="40" align="center">
	<fieldset><legend><font size="-1">管理パスワード入力</font></legend>
	<br>
	<input type="password" name="pass" value="" size="20">
	<input type="submit" value=" 認証 ">
	<br><br>
	</fieldset>
  </td>
</tr>
</table>
</form>
</blockquote>
<script language="javascript">
<!--
self.document.forms[0].pass.focus();
//-->
</script>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  HTMLヘッダ
#-------------------------------------------------
sub header {
	my $ttl = shift;

	print "Content-type: text/html\n\n";
	print <<"EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=shift_jis">
<title>$ttl</title></head>
<table cellpadding="6" width="640" bgcolor="$accol_1">
<tr>
  <td><font color="$accol_3"><b>$ttl</b></font></td>
</tr>
</table>
EOM
}

#-------------------------------------------------
#  エラー処理
#-------------------------------------------------
sub error {
	my $err = shift;

	&header("ERROR");
	print <<EOM;
<blockquote>
<h3>ERROR !</h3>
<font color="#dd0000" size="-1">$err</font>
<p>
<form>
<input type="button" value="前画面に戻る" onclick="history.back()">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  戻りボタン
#-------------------------------------------------
sub back_button {
	print <<EOM;
<table width="640">
<tr>
  <td align="right">
	<form action="$admincgi" method="post">
	<input type="hidden" name="pass" value="$in{'pass'}">
	<input type="submit" value="&lt; 管理メニュー">
  </td>
</tr>
</table>
</form>
EOM
}

#-------------------------------------------------
#  crypt暗号
#-------------------------------------------------
sub encrypt {
	my $in = shift;

	my @s = ('a'..'z', 'A'..'Z', '0'..'9', '.', '/');
	srand;
	my $salt = $s[int(rand(@s))] . $s[int(rand(@s))];

	crypt($in, $salt) || crypt ($in, '$1$' . $salt);
}

#-------------------------------------------------
#  crypt照合
#-------------------------------------------------
sub decrypt {
	my ($in, $dec) = @_;

	my ($salt) = $dec =~ /^\$1\$(.*)\$/ && $1 || substr($dec, 0, 2);
	if (crypt($in, $salt) eq $dec || crypt($in, '$1$' . $salt) eq $dec) {
		return 1;
	} else {
		return 0;
	}
}

#-------------------------------------------------
#  完了画面
#-------------------------------------------------
sub message {
	my $msg = shift;

	&header($msg);
	print <<EOM;
<blockquote>
<h3>処理完了</h3>
<font color="#dd0000" size="-1">$msg</font>
<form action="$admincgi" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="submit" value="元の画面に戻る">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

