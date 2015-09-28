#!/usr/bin/perl

#��������������������������������������������������������������������
#�� PasswordManager v2
#�� pwmgr.cgi - 2006/04/22
#�� Copyright (c) KentWeb
#�� http://www.kent-web.com/
#��������������������������������������������������������������������

# �O���t�@�C���捞
require './jcode.pl';
require './init.cgi';

&decode;
if ($mode eq "newUser") { &axsCheck; &newUser; }
elsif ($mode eq "chgUser") { &axsCheck; &chgUser; }
elsif ($mode eq "delUser") { &axsCheck; &delUser; }
elsif ($mode eq "check") { &check; }
&error("�s���ȃA�N�Z�X�ł�");

#---------------------------------------
#  �A�N�Z�X����
#---------------------------------------
sub axsCheck {
	# �z�X�g�����擾
	&get_host;

	local($flag);
	foreach ( split(/\s+/, $denyhost) ) {
		if (index($host,$_) >= 0) { $flag = 1; last; }
		if (index($host,$_) >= 0) { $flag = 1; last; }
	}
	if ($flag) { &error("���ݓo�^�x�~���ł�"); }
}

#---------------------------------------
#  ���[�U�o�^
#---------------------------------------
sub newUser {
	# ���s����
	if ($pwd_regist > 1) { &error("�s���ȃA�N�Z�X�ł�"); }

	# �`�F�b�N
	if ($in{'name'} eq "") { &error("���O�����̓����ł�"); }
	if ($in{'eml1'} ne $in{'eml2'}) { &error("���[���̍ēx���͂��قȂ�܂�"); }
	if ($in{'eml1'} !~ /^[\w\.\-]+\@[\w\.\-]+\.[a-zA-Z]{2,6}$/) {
		&error("���[���̓��͓��e���s���ł�");
	}
	if (length($in{'id'}) < 4 || length($in{'id'}) > 8) {
		&error("���O�C��ID��4�`8�����œ��͂��Ă�������");
	}
	if ($in{'id'} =~ /\W/) {
		&error("���O�C��ID�ɉp�����ȊO�̕������܂܂�Ă��܂�");
	}

	# ID�̏d���`�F�b�N
	local($f) = 0;
	open(IN,"$pwdfile") || &error("Open Error: $pwdfile");
	while (<IN>) {
		local($id) = split(/:/);
		if ($in{'id'} eq $id) { $f++; last; }
	}
	close(IN);

	if ($f) {
		&error("$in{'id'}�͊��ɔ��s�ςł��B<br>����ID�����w�肭������");
	}

	# �p�X���s
	local(@char) = (0 .. 9, 'a' .. 'z', 'A' .. 'Z');
	local($pw,$pw2);
	srand;
	foreach (1 .. 8) {
		$pw .= $char[int(rand(@char))];
	}

	# �Í���
	$pw2 = &encrypt($pw);

	# ���b�N�J�n
	&lock if ($lockkey);

	# �p�X�t�@�C���ǉ�
	open(OUT,">>$pwdfile") || &error("Write Error: $pwdfile");
	print OUT "$in{'id'}:$pw2\n";
	close(OUT);

	# ����t�@�C��
	open(IN,"$memfile") || &error("Open Error: $memfile");
	local(@file) = <IN>;
	close(IN);

	unshift(@file,"$in{'id'}<>$in{'name'}<>$in{'eml1'}<><>\n");
	open(OUT,">$memfile") || &error("Write Error: $memfile");
	print OUT @file;
	close(OUT);

	# ���b�N����
	&unlock if ($lockkey);

	# ���Ԏ擾
	$date = &get_time;

	# ���[���{��
	$mbody = <<EOM;
$in{'name'}�l

�u$title�v�ւ̂��o�^�����肪�Ƃ��������܂��B
�ȉ��̂Ƃ��胍�O�C��ID�ƃp�X���[�h�𔭍s���܂����B

���p�X���[�h�͂������Ŏ��R�ɕύX�\\�ł��̂ŁA�o���₷�����̂�
  �ύX���Ă������Ƃ��ł��܂��B

���o�^���e
�o�^����   : $date
�z�X�g��� : $host
�����O     : $in{'name'}
E-mail     : $in{'eml1'}

�����O�C�����
���O�C��ID : $in{'id'}
�p�X���[�h : $pw

---
  $title�Ǘ��l <$master>
EOM

	# �薼��BASE64��
	local($msub) = &base64("�o�^�̈ē�");

	# sendmail���M
	open(MAIL,"| $sendmail -t -i") || &error("���[�����M���s");
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
<h3>���o�^���肪�Ƃ��������܂����B</h3>
���O�C��ID�ƃp�X���[�h����<br>
<b>$in{'eml1'}</b><br>
�֑��M���܂����B</font>
<p>
<form>
<input type="button" value="TOP�ɖ߂�" onclick=window.open("$backUrl","_top")>
</form>
</td></tr>
</table>
<br><br><br>
<!-- ���쌠�\\���폜�s�� -->
<span style="font-size:10px;font-family:Verdana,Helvetica,Arial">
- <a href="http://www.kent-web.com/" target="_top">PasswordManager</a> -
</span></div>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  ���[�UPW�ύX
#---------------------------------------
sub chgUser {
	# ���s����
	if ($pwd_regist > 2) { &error("�s���ȃA�N�Z�X�ł�"); }

	# �`�F�b�N
	if ($in{'id'} eq "") { &error("���O�C��ID�����̓����ł�"); }
	if ($in{'pw'} eq "") { &error("���p�X���[�h�����̓����ł�"); }
	if ($in{'pw1'} eq "") { &error("�V�p�X���[�h�����̓����ł�"); }
	if ($in{'pw1'} ne $in{'pw2'}) {
		&error("�V�p�X���[�h�ōēx���͕����قȂ�܂�");
	}

	# �Í���
	local($newpw) = &encrypt($in{'pw1'});

	# ID�`�F�b�N
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
		&error("���O�C��ID ($in{'id'}) �͑��݂��܂���");
	}

	# �ƍ�
	$enpw =~ s/\n//;
	if ( &decrypt($in{'pw'}, $enpw) != 1 ) {
		&error("�p�X���[�h���Ⴂ�܂�");
	}

	# ���b�N�J�n
	&lock if ($lockkey);

	# �p�X�t�@�C���X�V
	open(OUT,">$pwdfile") || &error("Write Error: $pwdfile");
	print OUT @new;
	close(OUT);

	# ���b�N����
	&unlock if ($lockkey);

	&header;
	print <<EOM;
<div align="center">
<table border="1" cellpadding="20" cellspacing="0" width="450">
<tr><td align="center" class="r">
<font size="-1">
<h3>�p�X���[�h�ύX����</h3>
�����p�����肪�Ƃ��������܂����B
</font>
<form>
<input type="button" value="TOP�ɖ߂�" onclick=window.open("$backUrl","_top")>
</form>
</td></tr>
</table>
<br><br><br>
<!-- ���쌠�\\���폜�s�� -->
<span style="font-size:10px;font-family:Verdana,Helvetica,Arial">
- <a href="http://www.kent-web.com/" target="_top">PasswordManager</a> -
</span></div>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  ���[�U�폜
#---------------------------------------
sub delUser {
	# ���s����
	if ($pwd_regist > 2) { &error("�s���ȃA�N�Z�X�ł�"); }

	# �`�F�b�N
	if ($in{'id'} eq "") { &error("���O�C��ID�����̓����ł�"); }
	if ($in{'pw'} eq "") { &error("�p�X���[�h�����̓����ł�"); }

	# ���b�N�J�n
	&lock if ($lockkey && $in{'job'} eq "del");

	# ID�`�F�b�N
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
		&error("���O�C��ID ($in{'id'}) �͑��݂��܂���");
	}

	# �ƍ�
	$enpw =~ s/\n//;
	if ( &decrypt($in{'pw'}, $enpw) != 1 ) {
		&error("�p�X���[�h���Ⴂ�܂�");
	}

	# ���s
	if ($in{'job'} eq "del") {

		# �p�X�t�@�C���X�V
		open(OUT,">$pwdfile") || &error("Write Error: $pwdfile");
		print OUT @new;
		close(OUT);

		# ����t�@�C��
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

		# ���b�N����
		&unlock if ($lockkey);

		# �������b�Z�[�W
		&header;
		print <<EOM;
<div align="center">
<table border="1" cellpadding="20" cellspacing="0" width="450">
<tr><td align="center" class="r">
<font size="-1">
<h3>�o�^ID�폜����</h3>
����܂ł̂����p�����肪�Ƃ��������܂����B
</font>
<form>
<input type="button" value="TOP�ɖ߂�" onclick=window.open("$backUrl","_top")>
</form>
</td></tr>
</table>
<br><br><br>
<!-- ���쌠�\\���폜�s�� -->
<span style="font-size:10px;font-family:Verdana,Helvetica,Arial">
- <a href="http://www.kent-web.com/" target="_top">PasswordManager</a> -
</span></div>
</body>
</html>
EOM
		exit;
	}

	# �m�F���
	&header;
	print <<EOM;
<div align="center">
<table border="1" cellpadding="20" cellspacing="0" width="450">
<tr><td align="center" class="r">
<font size="-1">
<h3>�o�^�̍폜</h3>
<form action="$script" method="post">
<input type="hidden" name="mode" value="delUser">
<input type="hidden" name="id" value="$in{'id'}">
<input type="hidden" name="pw" value="$in{'pw'}">
<input type="hidden" name="job" value="del">
���O�C��ID <b>$in{'id'}</b> ��{���ɍ폜���܂����H
</font>
<p>
<input type="submit" value="�o�^���폜����">
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
#  BASE64�ϊ�
#---------------------------------------
#	�Ƃقق�WWW����Ō��J����Ă��郋�[�`����
#	�Q�l�ɂ��܂����B( http://tohoho.wakusei.ne.jp/ )
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
#  �ȈՃ`�F�b�N
#---------------------------------------
sub check {
	local($k, $v, %log);

	&header;
	print <<EOM;
<font size="-1">
<h3>�`�F�b�N���[�h</h3>
<ul>
EOM

	%log = (
		'�p�X���[�h�t�@�C��', $pwdfile,
		'����t�@�C��', $memfile,
		'�A�N�Z�X���O (�g�p����ꍇ)', $axsfile,
	);

	while ( ($k,$v) = each(%log) ) {

		# �p�X
		if (-e $v) {
			print "<li>$k�p�X OK!\n";

			# �p�[�~�b�V����
			if (-r $v && -w $v) {
				print "<li>$k�p�[�~�b�V���� OK!\n";
			} else {
				print "<li>$k�p�[�~�b�V���� NG!\n";
			}
		} else {
			print "<li>$k�p�XNG! �� $v\n";
		}
	}

	# sendmail
	if (-e $sendmail) {
		print "<li>sendmail�p�X OK!\n";
	} else {
		print "<li>sendmail�p�X NG! �� $sendmail (�g�p����ꍇ)\n";
	}

	# ���b�N�f�B���N�g��
	print "<li>���b�N�`�� �� ";
	if ($lockkey == 0) {
		print "�ݒ�Ȃ�\n";
	} else {
		if ($lockkey == 1) { print "symlink\n"; }
		else { print "mkdir\n"; }

		local($lockdir) = $lockfile =~ /(.*)[\\\/].*$/;
		print "<li>���b�N�f�B���N�g�� �� $lockdir\n";

		if (-d $lockdir) {
			print "<li>���b�N�f�B���N�g���p�XOK!\n";
			if (-r $lockdir && -w $lockdir && -x $lockdir) {
				print "<li>���b�N�f�B���N�g���p�[�~�b�V���� OK!\n";
			} else {
				print "<li>���b�N�f�B���N�g���p�[�~�b�V���� NG! �� $lockdir\n";
			}
		} else {
			print "<li>���b�N�f�B���N�g�� NG! �� $lockdir\n";
		}
	}

	# ���쌠�\���i�폜�s�j
	print <<EOM;
<li>�o�[�W���� �� $ver
</ul>
</font>
</body>
</html>
EOM
	exit;
}


__END__

