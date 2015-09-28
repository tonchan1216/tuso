#!/usr/bin/perl

#��������������������������������������������������
#�� PasswordManager v2
#�� admin.cgi - 2006/08/06
#�� Copyright (c) KentWeb
#�� http://www.kent-web.com/
#��������������������������������������������������

# �O���t�@�C���捞
require './jcode.pl';
require './init.cgi';

&decode;
if ($in{'pass'} eq "") { &enter; }
elsif ($in{'pass'} ne $pass) { &error('�p�X���[�h���Ⴂ�܂�'); }
if ($mode eq "member") { &member; }
elsif ($mode eq "axslog") { &axslog; }
&admin;

#---------------------------------------
#  �Ǘ�TOP
#---------------------------------------
sub admin {
	&header;
	print <<EOM;
<form action="$admin">
<input type=submit value="�����O�I�t">
</form>
<font size="-1">
<ul>
<li>������I�����Ă��������B
<li>�A�N�Z�X���O�́A�ʓr�uSSI + pwlog.cgi�v�ɂ�閄�ߍ��݂��K�v�ł��B
</ul>
</font>
<blockquote>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<table border="1" cellspacing="0" cellpadding="4">
<tr>
  <th class="l"><font size="-1">�I��</font></th>
  <th class="l"><font size="-1">����</font></th>
</tr>
<tr>
  <th class="r"><input type=radio name=mode value="member"></th>
  <td class="r"><font size="-1">����Ǘ��i�ǉ��E�C���E�폜�j</font></td>
</tr>
<tr>
  <th class="r"><input type=radio name=mode value="axslog"></th>
  <td class="r"><font size="-1">�A�N�Z�X���O</font></td>
</tr>
</table>
<p>
<input type="submit" value="�I������">
</form>
</blockquote>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  ����{��
#---------------------------------------
sub member {
	# �V�K���
	if ($in{'job'} eq "new") {

		&newform;

	# �V�K�o�^
	} elsif ($in{'job'} eq "new2") {

		local($f,$pwd,@file);

		# �`�F�b�N
		if ($in{'id'} eq "") { &error("���[�UID�������͂ł�"); }
		if ($in{'pw'} eq "") { &error("�p�X���[�h�������͂ł�"); }

		# ID�̏d���`�F�b�N
		$f=0;
		open(IN,"$pwdfile") || &error("Open Error: $pwdfile");
		while (<IN>) {
			($id) = split(/:/);

			if ($in{'id'} eq $id) { $f++; last; }
		}
		close(IN);

		if ($f) { &error("<b>$in{'id'}</b>�͊��ɔ��s�ςł�"); }

		# PW���Í���
		$pwd = &encrypt($in{'pw'});

		# ���b�N�J�n
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

		# ���b�N����
		&unlock if ($lockkey);

		$in{'name'}  ||= '���O�Ȃ�';
		$in{'email'} ||= 'E-mail�Ȃ�';
		$in{'memo'}  ||= '�Ȃ�';

		&header;
		print <<EOM;
���ȉ��̂Ƃ��蔭�s���܂����B
<dl>
<dt>�y���O�z<dd>$in{'name'}
<dt>�yE-mail�z<dd>$in{'email'}
<dt>�y���[�UID�z<dd>$in{'id'}
<dt>�y�p�X���[�h�z<dd>$in{'pw'}
<dt>�y���l�z<dd>$in{'memo'}
</dl>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="submit" value="�Ǘ����TOP��">
</form>
</body>
</html>
EOM
		exit;

	# �C���t�H�[��
	} elsif ($in{'job'} eq "edit") {

		if ($in{'id'} =~ /\0/) { &error("�C���͕����I���ł��܂���"); }

		# PW�t�@�C��
		local($f,$id,$nam,$eml,$memo);
		open(IN,"$memfile") || &error("Open Error: $memfile");
		while (<IN>) {
			($id,$nam,$eml,$memo) = split(/<>/);

			if ($in{'id'} eq $id) { $f++; last; }
		}
		close(IN);

		if (!$f) { &error("�Y����ID��񂪌�������܂���"); }

		&edit_form($id,$nam,$eml,$memo);

	# �C�����s
	} elsif ($in{'job'} eq "edit2") {

		# ���b�N�J�n
		&lock if ($lockkey);

		# ����t�@�C��
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

		# ���b�N����
		&unlock if ($lockkey);

	# �p�X���[�h�����ύX
	} elsif ($in{'job'} eq "pwchg") {

		local($pwd,@new);

		# �`�F�b�N
		if ($in{'pw'} eq "") { &error("�p�X���[�h�������͂ł�"); }

		# PW���Í���
		$pwd = &encrypt($in{'pw'});

		# ���b�N�J�n
		&lock if ($lockkey);

		# PW�t�@�C��
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

		# ���b�N����
		&unlock if ($lockkey);

	# �폜
	} elsif ($in{'job'} eq "dele") {

		local($f,@del,@new);

		# �폜���
		@del = split(/\0/, $in{'id'});

		# ���b�N�J�n
		&lock if ($lockkey);

		# PW�t�@�C��
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

		# ����t�@�C��
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

		# ���b�N����
		&unlock if ($lockkey);
	}

	&header;
	print <<EOM;
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="submit" value="���Ǘ�TOP">
</form>
<font size="-1">
<ul>
<li>������I�����đ��M�{�^���������Ă��������B
</ul>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="page" value="$page">
���� : <select name="job">
<option value="new">�V�K
<option value="edit">�C��
<option value="dele">�폜
</select>
</font>
<input type="submit" value="���M����">
<p>
<table border="1" cellspacing="0" cellpadding="2">
<tr>
  <th class="l"><font size="-1">�I��</font></th>
  <th class="l"><font size="-1">ID��</font></th>
  <th class="l"><font size="-1">���O</font></th>
  <th class="l"><font size="-1">���l</font></th>
</tr>
EOM

	local($i) = 0;
	open(IN,"$memfile") || &error("Open Error: $memfile");
	while (<IN>) {
		$i++;
		next if ($i < $page + 1);
		next if ($i > $page + $pageView);

		local($id,$nam,$eml,$memo) = split(/<>/);

		$nam ||= '���O�Ȃ�';
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
		print "<input type=\"submit\" value=\"�O��$pageView��\"></td></form>\n";
	}
	if ($next < $i) {
		print "<td><form action=\"$admin\" method=\"post\">\n";
		print "<input type=\"hidden\" name=\"pass\" value=\"$in{'pass'}\">\n";
		print "<input type=\"hidden\" name=\"mode\" value=\"member\">\n";
		print "<input type=\"hidden\" name=\"page\" value=\"$next\">\n";
		print "<input type=\"submit\" value=\"����$pageView��\"></td></form>\n";
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
#  �o�^���
#---------------------------------------
sub newform {
	&header;
	print <<EOM;
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="page" value="$page">
<input type="submit" value="&lt; �O���">
</form>
<font size="-1">
<ul>
<li>�e���ڂ���͂��đ��M�{�^���������Ă��������B
<li>���[�UID�ƃp�X���[�h�͕K�{�ł��B�i���͔C�Ӂj
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
#  �C�����
#---------------------------------------
sub edit_form {
	local($id,$nam,$eml,$memo) = @_;

	&header;
	print <<EOM;
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="page" value="$page">
<input type="submit" value="&lt; �O���">
</form>
<font size="-1">
<ul>
<li>�ȉ��̃t�H�[�����A<b>$id</b> �̑�������ύX���܂��B
<li>�ύX����ӏ��̂ݏC�����đ��M�{�^���������Ă��������B
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
<li>�ȉ��̃t�H�[�����A�p�X���[�h�������ύX���܂��B
</ul>
</font>
<form action="$admin" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="mode" value="$mode">
<input type="hidden" name="job" value="pwchg">
<input type="hidden" name="id" value="$in{'id'}">
<table border="1" cellspacing="0" cellpadding="4">
<tr>
  <th class="l"><font size="-1">�p�X���[�h</font></th>
  <td class="r">
	<input type="text" name="pw" size="8" maxlength="8" style="ime-mode:inactive">
	<font color="green" size="-1">(8�����ȓ�)</font></td>
</tr>
</table>
<p>
<input type="submit" value="�����ύX����">
</form>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  �t�H�[��
#---------------------------------------
sub form {
	local($id,$nam,$eml,$memo) = @_;
	$memo =~ s/<br>/\r/g;

	print <<EOM;
<table border="1" cellspacing="0" cellpadding="4">
<tr>
  <th class="l"><font size="-1">���O</font></th>
  <td class="r"><input type="text" name="name" size="30" value="$nam"></td>
</tr>
<tr>
  <th class="l"><font size="-1">E-mail</font></th>
  <td class="r"><input type="text" name="email" size="30" value="$eml"></td>
</tr>
<tr>
  <th class="l"><font size="-1">���[�UID</font></th>
EOM

	if ($id eq "") {
		print "<td class=\"r\">";
		print "<input type=\"text\" name=\"id\" size=\"8\" maxlength=\"8\" style=\"ime-mode:inactive\">\n";
		print "<font color=\"green\" size=\"-1\">(8�����ȓ�)</font></td></tr>\n";
		print "<tr><th class=\"l\"><font size=\"-1\">�p�X���[�h</font></th>\n";
  		print "<td class=\"r\"><input type=\"text\" name=\"pw\" size=\"8\" maxlength=\"8\" style=\"ime-mode:inactive\">\n";
		print "<font color=\"green\" size=\"-1\">(8�����ȓ�)</font></td></tr>\n";
	} else {
		print "<td class=\"r\"><b>$id</b></td></tr>\n";
	}

	print <<EOM;
<tr>
  <th class="l"><font size="-1">���l</font></th>
  <td class="r"><textarea name="memo" cols="30" rows="4">$memo</textarea></td>
</tr>
</table>
<p>
<input type="submit" value="���M����"><input type="reset" value="���Z�b�g">
</form>
EOM
}

#---------------------------------------
#  �A�N�Z�X���O
#---------------------------------------
sub axslog {
	&header;
	print <<EOM;
<table cellpadding="1" cellspacing="1" border="0">
<tr>
  <td>
    <form action="$admin" method="post">
    <input type="hidden" name="pass" value="$in{'pass'}">
    <input type="submit" value="���Ǘ�TOP">
  </td></form>
  <td>
    <form action="$admin" method="post">
    <input type="hidden" name="mode" value="$mode">
    <input type="hidden" name="pass" value="$in{'pass'}">
    <input type="hidden" name="shukei" value="off">
    <input type="hidden" name="da" value="$da">
    <input type="hidden" name="ho" value="$ho">
    <input type="hidden" name="ag"value="$ag">
    <input type="submit" value="���O�ꗗ" class="f">
  </td></form>
  <td>
    <form action="$admin" method="post">
    <input type="hidden" name="mode" value="$mode">
    <input type="hidden" name="pass" value="$in{'pass'}">
    <input type="hidden" name="shukei" value="on">
    <input type="hidden" name="da" value="$da">
    <input type="hidden" name="ho" value="$ho">
    <input type="hidden" name="ag" value="$ag">
    <input type="submit" value="���O�W�v" class="f">
  </td></form>
</tr>
</table>
<font size="-1">
EOM

	# ���O�ꗗ�̏ꍇ
	if ($in{'shukei'} ne "on") {

		# �y�[�W�J�z
		local($pg) = 0;
		foreach ( keys(%in) ) {
			if (/^pg(\d+)$/) {
				$pg = $1;
				last;
			}
		}

		print "<dl><dt>��<b>���O�ꗗ</b>\n";

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
				print "<input type=\"submit\" name=\"pg$back\" value=\"�O��$pageView��\">\n";
			}
			if ($next < $i) {
				print "<input type=\"submit\" name=\"pg$next\" value=\"����$pageView��\">\n";
			}
			print "</form>\n";
		}

	# ���O�W�v�̏ꍇ
	} else {
		print "<p>��<b>���O�W�v</b>\n";
		print "<p><table border=\"1\" cellspacing=\"0\" cellpadding=\"2\">\n";
		print "<tr><th class=\"l\"><font size=\"-1\">���[�UID</font></th>";
		print "<th class=\"l\"><font size=\"-1\">�A�N�Z�X��</font></th></tr>\n";

		# �f�[�^�W�v
		local(%count);
		open(IN,"$axsfile");
		while (<IN>) {
			local($id,$date,$host,$agent) = split(/<>/);

			$count{$id}++;
		}
		close(IN);

		# �z��
		local($key,$val,@key,@val);
		while ( ($key,$val) = each(%count) ) {

			push(@key,$key);
			push(@val,$val);
		}

		# �\�[�g
		@key = @key[sort {$val[$b] <=> $val[$a]} 0..$#val];

		# �Z���W�v�\��
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
#  �������
#---------------------------------------
sub enter {
	&header;
	print <<EOM;
<font size="-1">
<div align="center">
<b>�p�X���[�h����͂��Ă�������</b>
</font>
<form action="$admin" method="post">
<input type="password" name="pass" size="8">
<input type="submit" value="���O�C��">
</form>
</div>
</body>
</html>
EOM
	exit;
}

