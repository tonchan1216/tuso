#��������������������������������������������������������������������
#�� ClipMail
#�� check.pl - 2007/05/23
#�� copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������

#-------------------------------------------------
#  �`�F�b�N���[�h
#-------------------------------------------------
sub check {
	print "Content-type: text/html\n\n";
	print <<EOM;
<html><head>
<meta http-equiv="content-type" content="text/html; charset=shift_jis">
<title>�`�F�b�N���[�h</title></head>
<body>
<h3>�`�F�b�N���[�h</h3>
<ul>
EOM

	# sendmail�`�F�b�N
	print "<li>sendmail�p�X�F";
	if (-e $sendmail) {
		print "OK\n";
	} else {
		print "NG �� $sendmail\n";
	}

	# jcode.pl �o�[�W�����`�F�b�N
	print "<li>jcode.pl�o�[�W�����`�F�b�N�F";

	if ($jcode::version < 2.13) {
		print "�o�[�W�������Ⴂ�悤�ł��B�� v$jcode::version\n";
	} else {
		print "OK (v$jcode::version)\n";
	}

	# �e���v���[�g
	foreach ( $tmpl_body, $tmpl_bres, $tmpl_conf, $tmpl_err1, $tmpl_err2, $tmpl_thx ) {
		print "<li>�e���v���[�g ( $_ ) �F";
		if (-f $_) {
			print "�p�XOK!\n";
		} else {
			print "�p�XNG �� $_\n";
		}
	}

	# �ꎞ�f�B���N�g��
	if (-d $tmpdir) {
		print "<li>�ꎞ�f�B���N�g���p�X : OK!\n";

		if (-r $tmpdir && -w $tmpdir && -x $tmpdir) {
			print "<li>�ꎞ�f�B���N�g���p�[�~�b�V���� : OK!\n";
		} else {
			print "<li>�ꎞ�f�B���N�g���p�[�~�b�V���� : NG �� $tmpdir\n";
		}

	} else {
		print "<li>�ꎞ�f�B���N�g���p�X : NG �� $tmpdir\n";
	}

	# �f�[�^�`�F�b�N
	my %file = ($logfile => '���O�t�@�C��', $pwdfile => '�p�X���[�h�t�@�C��');
	foreach ( $logfile, $pwdfile ) {
		if (-f $_) {
			print "<li>$file{$_}�p�X : OK!\n";
		} else {
			print "<li>$file{$_}�p�X : NG �� $_\n";
		}
	}

	print <<EOM;
<li>�o�[�W���� : $ver
</ul>
</body>
</html>
EOM
	exit;
}


1;

