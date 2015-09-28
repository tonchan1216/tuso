#!/usr/bin/perl

#��������������������������������������������������������������������
#�� Clip Mail
#�� admin.cgi - 2007/05/26
#�� copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������

# �O���t�@�C����荞��
require './init.cgi';
require $jcodepl;

# �J���[
$accol_1 = "#004080";
$accol_2 = "#bdbddf";
$accol_3 = "#ffffff";

# �t�H�[���f�R�[�h
&parse_form;
$mode = $in{'mode'};

# ��{����
&pwd_check;
if ($mode eq "get_log") { &get_log; }
elsif ($mode eq "pass_chg") { &pass_chg; }
&menu_list;

#-------------------------------------------------
#  �Ǘ����
#-------------------------------------------------
sub menu_list {
	&header("�Ǘ����j���[");
	print <<EOM;
<table width="640">
<tr>
  <td align="right">
	<form action="$admincgi" method="post">
	<input type="submit" value="�����O�I�t">
	</form>
  </td>
</tr>
</table>
<blockquote>
<font size="-1">������I�����đ��M�{�^���������Ă��������B</font>
<p>
<form action="$admincgi" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<table cellpadding="5" cellspacing="1" bgcolor="$accol_1" width="350">
<tr>
  <th bgcolor="$accol_2" nowrap><font size="-1">�I��</font></th>
  <th bgcolor="$accol_2" nowrap width="100%"><font size="-1">��������</font></th>
</tr>
<tr>
  <th bgcolor="$accol_3" nowrap><input type="radio" name="mode" value="get_log"></th>
  <td bgcolor="$accol_3" nowrap width="100%">
	&nbsp; <font size="-1">CSV�_�E�����[�h</font></td>
</tr>
<tr>
  <th bgcolor="$accol_3" nowrap><input type="radio" name="mode" value="pass_chg"></th>
  <td bgcolor="$accol_3" nowrap width="100%">
	&nbsp; <font size="-1">�Ǘ��p�X���[�h�̕ύX</font></td>
</tr>
</table>
<p>
<input type="submit" value="���M����">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  ���O�_�E�����[�h
#-------------------------------------------------
sub get_log {
	# �_�E�����[�h���s
	if ($in{'downld'}) {

		# �I���`�F�b�N
		if (!$in{'br'} || !$in{'tag'}) { &error("�I�v�V�����ɖ��I��������܂�"); }

		# ���s�R�[�h��`
		my %br = ("win" => "\r\n", "mac" => "\r", "unix" => "\n");

		# ���O���I�[�v��
		my ($i, %key, %log);
		open(IN,"$logfile");
		while(<IN>) {
			chomp;

			# ����, IP, �{���ɕ���
			my ($log_date, $log_ip, $log) = split(/<>/, $_, 3);

			# HTML�ϊ�
			if ($in{'tag'} eq "full") {
				$log =~ s/&lt;/</g;
				$log =~ s/&gt;/>/g;
				$log =~ s/&quot;/"/g;
				$log =~ s/&#39;/'/g;
				$log =~ s/&amp;/&/g;
			} else {
				$log =~ s/&lt;/��/g;
				$log =~ s/&gt;/��/g;
				$log =~ s/&quot;/�h/g;
				$log =~ s/&#39;/�f/g;
				$log =~ s/&amp;/��/g;
			}

			# ������IP���n�b�V����`
			$i++;
			my ($key, $date) = split(/=/, $log_date);
			$log{"$i:date"} = $date;
			my ($key, $ip) = split(/=/, $log_ip);
			$log{"$i:ip"} = $ip;

			# �{�����e���ڂ��Ƃɕ���
			foreach my $itm ( split(/<>/, $log) ) {
				my ($key, $val) = split(/=/, $itm, 2);

				# �{�����n�b�V����`
				$log{"$i:$key"} = $val;

				# �s���Ƃ̍��ږ����o���Ă���
				# (���M���Ƃɍ��ڐ����قȂ�P�[�X�����邽��)
				$key{$key}++;
			}
		}
		close(IN);

		# �_�E�����[�h�p�w�b�_�[
		print "Content-type: application/octet-stream\n";
		print "Content-Disposition: attachment; filename=postmail.csv\n\n";

		# �o�C�i���[���[�h�o�́iWindows�T�[�o�΍�j
		binmode(STDOUT);

		# �g�b�v�s�́u���ځv��\��
		print "���t,IP�A�h���X,";
		my @keys;
		foreach ( keys(%key) ) {
			print "$_,";

			# ���ږ��̏��Ԃ��o���Ă���
			push(@keys,$_);
		}
		print $br{$in{'br'}};

		# ���O�{�̂�W�J�i�Ō��$i�j
		foreach my $n (1 .. $i) {

			# ���t��IP��\��
			my $csv;
			$csv .= qq |$log{"$n:date"},|;
			$csv .= qq |$log{"$n:ip"},|;

			# �{�͍̂��ڏ��ɕ\�����Ă���
			foreach my $key (@keys) {
				$csv .= qq |\"$log{"$n:$key"}\",|;
			}
			print "$csv$br{$in{'br'}}";
		}
		exit;
	}

	# ���O���𐔂���
	my $i = 0;
	open(IN,"$logfile");
	++$i while(<IN>);
	close(IN);

	# �_�E�����[�h���
	&header("CSV�_�E�����[�h");
	&back_button;
	print <<EOM;
<blockquote>
<font size="-1">
�E ���݂̃��O���F <b>$i</b>��<br>
�E �e�I�v�V������I�����āA�_�E�����[�h�{�^���������Ă��������B<br>
<form action="$admincgi" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<table bgcolor="$accol_1" cellpadding="4" cellspacing="1" width="280">
<tr>
  <th bgcolor="$accol_2" nowrap>
	<font size="-1">���s�`��</font>
  </th>
  <td bgcolor="$accol_3" nowrap width="100%">
	<font size="-1">
	<input type="radio" name="br" value="win">Windows�`�� �iCR+LF�j<br>
	<input type="radio" name="br" value="mac">Macintosh�`�� �iCR�j<br>
	<input type="radio" name="br" value="unix">UNIX�`�� �iLF�j
	</font>
  </td>
</tr>
<tr>
  <th bgcolor="$accol_2" nowrap>
	<font size="-1">HTML�ϊ�</font>
  </th>
  <td bgcolor="$accol_3" nowrap width="100%">
	<font size="-1">
	<input type="radio" name="tag" value="full">���S����<br>
	<input type="radio" name="tag" value="zen" checked>�S�p�����ϊ��i�������߁j
	</font>
  </td>
</tr>
</table>
<p>
<input type="submit" name="downld" value="�_�E�����[�h">
</form>
<p>
��HTML�́A�u&lt;�v�u&gt;�v�u&quot;�v�u&amp;�v�u&#39;�v���w���܂��B
</font>
</blockquote>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  �p�X���[�h�ύX
#-------------------------------------------------
sub pass_chg {
	# �ύX���s
	if ($in{'change'}) {

		# ���̓`�F�b�N
		my $err;
		if ($in{'pass_1'} eq "") {
			$err .= qq |�V�p�X���[�h�������͂ł�<br>|;
		}
		if ($in{'pass_1'} ne $in{'pass_2'}) {
			$err .= qq |�ē��͂̃p�X���[�h���قȂ�܂�<br>|;
		}
		if ($err) { &error($err); }

		# �p�X���[�h�t�@�C���X�V
		open(DB,"> $pwdfile");
		print DB &encrypt($in{'pass_1'});
		close(DB);

		# ���p�X��V�p�X�ɒu������
		$in{'pass'} = $in{'pass_1'};

		# �������b�Z�[�W
		&message("�p�X���[�h��ύX���܂���");
	}

	# �ύX���
	&header("�p�X���[�h�ύX");
	&back_button;
	print <<EOM;
<blockquote>
<font size="-1">
�V�p�X���[�h����͂��đ��M�{�^���������Ă��������B
</font>
<form action="$admincgi" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<table bgcolor="$accol_1" cellpadding="4" cellspacing="1">
<tr>
  <th bgcolor="$accol_2" nowrap><font size="-1">�V�p�X���[�h</font></th>
  <td bgcolor="$accol_3" nowrap>
	<input type="password" name="pass_1" value="" size="25">
	<font size="-1">�i�p������8�����ȓ��j</font>
  </td>
</tr>
<tr>
  <th bgcolor="$accol_2" nowrap><font size="-1">�ēx����</font></th>
  <td bgcolor="$accol_3" nowrap>
	<input type="password" name="pass_2" value="" size="25">
  </td>
</tr>
</table>
<p>
<input type="submit" name="change" value="���M����">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  �F��
#-------------------------------------------------
sub pwd_check {
	# �������
	if ($in{'pass'} eq "") {

		# �p�X���[�h�t�@�C������t�@�C���Ȃ�ΕύX��ʂ�
		if (-z $pwdfile) { &pass_chg; }

		# �������
		&enter_disp;

	# �F��
	} else {

		# �p�X�t�@�C�����I�[�v��
		open(IN,"$pwdfile");
		my $data = <IN>;
		close(IN);

		# �p�X���[�h�ƍ�
		if (&decrypt($in{'pass'} ,$data) != 1) {
			&error("�F�؂ł��܂���");
		}
	}
}

#-------------------------------------------------
#  �������
#-------------------------------------------------
sub enter_disp {
	&header("�������");
	print <<EOM;
<blockquote>
<form action="$admincgi" method="post">
<table width="380">
<tr>
  <td height="40" align="center">
	<fieldset><legend><font size="-1">�Ǘ��p�X���[�h����</font></legend>
	<br>
	<input type="password" name="pass" value="" size="20">
	<input type="submit" value=" �F�� ">
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
#  HTML�w�b�_
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
#  �G���[����
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
<input type="button" value="�O��ʂɖ߂�" onclick="history.back()">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

#-------------------------------------------------
#  �߂�{�^��
#-------------------------------------------------
sub back_button {
	print <<EOM;
<table width="640">
<tr>
  <td align="right">
	<form action="$admincgi" method="post">
	<input type="hidden" name="pass" value="$in{'pass'}">
	<input type="submit" value="&lt; �Ǘ����j���[">
  </td>
</tr>
</table>
</form>
EOM
}

#-------------------------------------------------
#  crypt�Í�
#-------------------------------------------------
sub encrypt {
	my $in = shift;

	my @s = ('a'..'z', 'A'..'Z', '0'..'9', '.', '/');
	srand;
	my $salt = $s[int(rand(@s))] . $s[int(rand(@s))];

	crypt($in, $salt) || crypt ($in, '$1$' . $salt);
}

#-------------------------------------------------
#  crypt�ƍ�
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
#  �������
#-------------------------------------------------
sub message {
	my $msg = shift;

	&header($msg);
	print <<EOM;
<blockquote>
<h3>��������</h3>
<font color="#dd0000" size="-1">$msg</font>
<form action="$admincgi" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="submit" value="���̉�ʂɖ߂�">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

