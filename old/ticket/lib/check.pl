#┌─────────────────────────────────
#│ ClipMail
#│ check.pl - 2007/05/23
#│ copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────

#-------------------------------------------------
#  チェックモード
#-------------------------------------------------
sub check {
	print "Content-type: text/html\n\n";
	print <<EOM;
<html><head>
<meta http-equiv="content-type" content="text/html; charset=shift_jis">
<title>チェックモード</title></head>
<body>
<h3>チェックモード</h3>
<ul>
EOM

	# sendmailチェック
	print "<li>sendmailパス：";
	if (-e $sendmail) {
		print "OK\n";
	} else {
		print "NG → $sendmail\n";
	}

	# jcode.pl バージョンチェック
	print "<li>jcode.plバージョンチェック：";

	if ($jcode::version < 2.13) {
		print "バージョンが低いようです。→ v$jcode::version\n";
	} else {
		print "OK (v$jcode::version)\n";
	}

	# テンプレート
	foreach ( $tmpl_body, $tmpl_bres, $tmpl_conf, $tmpl_err1, $tmpl_err2, $tmpl_thx ) {
		print "<li>テンプレート ( $_ ) ：";
		if (-f $_) {
			print "パスOK!\n";
		} else {
			print "パスNG → $_\n";
		}
	}

	# 一時ディレクトリ
	if (-d $tmpdir) {
		print "<li>一時ディレクトリパス : OK!\n";

		if (-r $tmpdir && -w $tmpdir && -x $tmpdir) {
			print "<li>一時ディレクトリパーミッション : OK!\n";
		} else {
			print "<li>一時ディレクトリパーミッション : NG → $tmpdir\n";
		}

	} else {
		print "<li>一時ディレクトリパス : NG → $tmpdir\n";
	}

	# データチェック
	my %file = ($logfile => 'ログファイル', $pwdfile => 'パスワードファイル');
	foreach ( $logfile, $pwdfile ) {
		if (-f $_) {
			print "<li>$file{$_}パス : OK!\n";
		} else {
			print "<li>$file{$_}パス : NG → $_\n";
		}
	}

	print <<EOM;
<li>バージョン : $ver
</ul>
</body>
</html>
EOM
	exit;
}


1;

