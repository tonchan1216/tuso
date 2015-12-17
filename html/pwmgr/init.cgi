#!/usr/bin/perl

#��������������������������������������������������������������������
#�� PasswordManager v2.23
#�� init.cgi - 2006/08/06
#�� Copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������
$ver = 'PasswordManager v2.23';
#��������������������������������������������������������������������
#�� [���ӎ���]
#�� 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����
#��    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B
#�� 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B
#��    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B
#��������������������������������������������������������������������

#---------------------------------------
# ����{�ݒ�
#---------------------------------------

# �p�X���[�h���s�`��
# 1 : ���[�U����̔��s�������e���\�ɂ���
# 2 : ���s�͊Ǘ��҂̂݁B���[�U�̓����e�̂�
# 3 : ���s�������e�͊Ǘ��҂̂݁ipwmgr.cgi index.html�͕s�v�j
$pwd_regist = 2;

# �p�X���[�h�t�@�C��
# �� ���m�Ƀt���p�X���L�q���邱��
$pwdfile = '/home/sites/www.tohokuuniv-orch.com/web/pwmgr/.htpasswd';

# ����t�@�C��
# �� ���m�Ƀt���p�X���L�q���邱��
$memfile = '/home/sites/www.tohokuuniv-orch.com/web/pwmgr/member_dat.cgi';

# �A�N�Z�X���O�t�@�C��
# �� ���m�Ƀt���p�X���L�q���邱��
$axsfile = '/home/sites/www.tohokuuniv-orch.com/web/pwmgr/pwlog_dat.cgi';

# �A�N�Z�X���O�̍ő吔
$log_max = 300;

# �{�̃v���O����URL
$script = './pwmgr.cgi';

# �Ǘ��v���O����URL
$admin  = './admin.cgi';

# �Ǘ��p�p�X���[�h
$pass = 'tonpei';

# �^�C�g����
$title = "�c����p�y�[�W";

# �߂��URL
$backUrl = 'http://www.tohokuuniv-orch.com/';

# �P�y�[�W�������\������
$pageView = 50;

# �Ǘ��A�h���X
$master = 'shunky1024@msn.com';

# sendmail�p�X
$sendmail = '/usr/sbin/sendmail';

# �t�@�C�����b�N�`��
#  �� 0=no 1=symlink�֐� 2=mkdir�֐�
$lockkey = 2;

# ���b�N�t�@�C����
$lockfile = './lock/pwmgr.lock';

# ���[�U�o�^�A�N�Z�X�����i���p�X�y�[�X�ŋ�؂�j
#  �� ���ۂ���z�X�g������IP�A�h���X���L�q
#  �� �L�q�� $deny = '.anonymizer.com 211.154.120.';
$denyhost = '';

#---------------------------------------
# ���ݒ芮��
#---------------------------------------

#---------------------------------------
#  �t�H�[���f�R�[�h
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

		# �G�X�P�[�v
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
#  HTML�w�b�_
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
#  �G���[����
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
<input type="button" value="�O��ʂɖ߂�" onclick="history.back()">
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
#  crypt�Í�
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
#  crypt�ƍ�
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
#  ���Ԏ擾
#---------------------------------------
sub get_time {
	# �^�C���]�[���ݒ�
	$ENV{'TZ'} = "JST-9";

	local($min,$hour,$mday,$mon,$year) = (localtime(time))[1..5];
	sprintf("%04d/%02d/%02d-%02d:%02d",
			$year+1900,$mon+1,$mday,$hour,$min);
}

#---------------------------------------
#  �z�X�g���擾
#---------------------------------------
sub get_host {
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};

	if ($host eq "" || $host eq $addr) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2) || $addr;
	}
}

#---------------------------------------
#  ���b�N����
#---------------------------------------
sub lock {
	# �Â����b�N�͍폜
	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 30) { &unlock; }
	}
	local($retry) = 5;
	# symlink�֐������b�N
	if ($lockkey == 1) {
		while (!symlink(".", $lockfile)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}
	# mkdir�֐������b�N
	} elsif ($lockkey == 2) {
		while (!mkdir($lockfile, 0755)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}
	}
	$lockflag = 1;
}

#---------------------------------------
#  ���b�N����
#---------------------------------------
sub unlock {
	if ($lockkey == 1) { unlink($lockfile); }
	elsif ($lockkey == 2) { rmdir($lockfile); }

	$lockflag = 0;
}


1;

