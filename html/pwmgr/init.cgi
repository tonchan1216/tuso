#!/usr/bin/perl

#┌─────────────────────────────────
#│ PasswordManager v2.23
#│ init.cgi - 2006/08/06
#│ Copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────
$ver = 'PasswordManager v2.23';
#┌─────────────────────────────────
#│ [注意事項]
#│ 1. このスクリプトはフリーソフトです。このスクリプトを使用した
#│    いかなる損害に対して作者は一切の責任を負いません。
#│ 2. 設置に関する質問はサポート掲示板にお願いいたします。
#│    直接メールによる質問は一切お受けいたしておりません。
#└─────────────────────────────────

#---------------------------------------
# ▼基本設定
#---------------------------------------

# パスワード発行形態
# 1 : ユーザからの発行＆メンテを可能にする
# 2 : 発行は管理者のみ。ユーザはメンテのみ
# 3 : 発行＆メンテは管理者のみ（pwmgr.cgi index.htmlは不要）
$pwd_regist = 2;

# パスワードファイル
# → 正確にフルパスを記述すること
$pwdfile = '/home/sites/www.tohokuuniv-orch.com/web/pwmgr/.htpasswd';

# 会員ファイル
# → 正確にフルパスを記述すること
$memfile = '/home/sites/www.tohokuuniv-orch.com/web/pwmgr/member_dat.cgi';

# アクセスログファイル
# → 正確にフルパスを記述すること
$axsfile = '/home/sites/www.tohokuuniv-orch.com/web/pwmgr/pwlog_dat.cgi';

# アクセスログの最大数
$log_max = 300;

# 本体プログラムURL
$script = './pwmgr.cgi';

# 管理プログラムURL
$admin  = './admin.cgi';

# 管理用パスワード
$pass = 'tonpei';

# タイトル名
$title = "団員専用ページ";

# 戻り先URL
$backUrl = 'http://www.tohokuuniv-orch.com/';

# １ページ当り会員表示件数
$pageView = 50;

# 管理アドレス
$master = 'shunky1024@msn.com';

# sendmailパス
$sendmail = '/usr/sbin/sendmail';

# ファイルロック形式
#  → 0=no 1=symlink関数 2=mkdir関数
$lockkey = 2;

# ロックファイル名
$lockfile = './lock/pwmgr.lock';

# ユーザ登録アクセス制限（半角スペースで区切る）
#  → 拒否するホスト名又はIPアドレスを記述
#  → 記述例 $deny = '.anonymizer.com 211.154.120.';
$denyhost = '';

#---------------------------------------
# ▲設定完了
#---------------------------------------

#---------------------------------------
#  フォームデコード
#---------------------------------------
sub decode {
	local($buf);
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		$post_flag = 1;
		read(STDIN, $buf, $ENV{'CONTENT_LENGTH'});
	} else {
		$post_flag = 0;
		$buf = $ENV{'QUERY_STRING'};
	}
	%in = ();
	foreach ( split(/&/, $buf) ) {
		local($key, $val) = split(/=/);
		$val =~ tr/+/ /;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;

		&jcode'convert(*val, 'sjis');

		# エスケープ
		$val =~ s/&/&amp;/g;
		$val =~ s/"/&quot;/g;
		$val =~ s/</&lt;/g;
		$val =~ s/>/&gt;/g;
		$val =~ s/\r\n/<br>/g;
		$val =~ s/\r/<br>/g;
		$val =~ s/\n/<br>/g;

		$in{$key} .= "\0" if (defined($in{$key}));
		$in{$key} .= $val;
	}
	$page = $in{'page'};
	$mode = $in{'mode'};

	$lockflag = 0;
	$headflag = 0;
}

#---------------------------------------
#  HTMLヘッダ
#---------------------------------------
sub header {
	if ($headflag) { return; }

	print "Content-type: text/html\n\n";
	print <<"EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<META HTTP-EQUIV="Content-Style-Type" content="text/css">
<STYLE type="text/css">
.l { background-color:#666666; color:#ffffff; }
.r { background-color:#ffffff; color:#000000; }
-->
</STYLE>
<title>PASSWORD MANAGER</title></head>
<body bgcolor="#f0f0f0">
EOM
	$headflag = 1;
}

#---------------------------------------
#  エラー処理
#---------------------------------------
sub error {
	if ($lockflag) { &unlock; }

	&header;
	print <<EOM;
<div align="center">
<table border="1" cellpadding="18" cellspacing="0" width="450">
<tr><td width="500" align="center" class="r">
<h3>ERROR !</h3>
<font color="#dd0000">$_[0]</font>
<p>
<form>
<input type="button" value="前画面に戻る" onclick="history.back()">
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
#  crypt暗号
#---------------------------------------
sub encrypt {
	local($in) = @_;
	local($salt, $enc, @s);

	@s = ('a'..'z', 'A'..'Z', '0'..'9', '.', '/');
	srand;
	$salt = $s[int(rand(@s))] . $s[int(rand(@s))];
	$enc = crypt($in, $salt) || crypt ($in, '$1$' . $salt);
	$enc;
}

#---------------------------------------
#  crypt照合
#---------------------------------------
sub decrypt {
	local($in, $dec) = @_;

	local($salt) = $dec =~ /^\$1\$(.*)\$/ && $1 || substr($dec, 0, 2);
	if (crypt($in, $salt) eq $dec || crypt($in, '$1$' . $salt) eq $dec) {
		return (1);
	} else {
		return (0);
	}
}

#---------------------------------------
#  時間取得
#---------------------------------------
sub get_time {
	# タイムゾーン設定
	$ENV{'TZ'} = "JST-9";

	local($min,$hour,$mday,$mon,$year) = (localtime(time))[1..5];
	sprintf("%04d/%02d/%02d-%02d:%02d",
			$year+1900,$mon+1,$mday,$hour,$min);
}

#---------------------------------------
#  ホスト名取得
#---------------------------------------
sub get_host {
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};

	if ($host eq "" || $host eq $addr) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2) || $addr;
	}
}

#---------------------------------------
#  ロック処理
#---------------------------------------
sub lock {
	# 古いロックは削除
	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 30) { &unlock; }
	}
	local($retry) = 5;
	# symlink関数式ロック
	if ($lockkey == 1) {
		while (!symlink(".", $lockfile)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}
	# mkdir関数式ロック
	} elsif ($lockkey == 2) {
		while (!mkdir($lockfile, 0755)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}
	}
	$lockflag = 1;
}

#---------------------------------------
#  ロック解除
#---------------------------------------
sub unlock {
	if ($lockkey == 1) { unlink($lockfile); }
	elsif ($lockkey == 2) { rmdir($lockfile); }

	$lockflag = 0;
}


1;

