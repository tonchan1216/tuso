#!/usr/bin/perl

#��������������������������������������������������
#�� PasswordManager v2
#�� pwlog.cgi (SSI�p) - 2006/02/26
#�� Copyright (c) KentWeb
#�� http://www.kent-web.com/
#��������������������������������������������������
# �y�g�����z���O�C�����HTML�y�[�W�Ɉȉ���SSI�^�O���L�q
#  <!--#exec cgi="/�t���p�X/pwlog.cgi"-->
#
# �y���p�����z
#  1. SSI�̗��p�ł���T�[�o
#  2. ���ϐ� $ENV{'REMOTE_USER'} �ɂă��[�U�[ID���擾�ł��邱��
#  �� 2. �ɂ��ẮA������ pwlog_test.cgi �ɂăe�X�g���邱��

# �O���t�@�C���捞
require './init.cgi';

# �z�X�g�����擾
&get_host;

# ���Ԏ擾
$date = &get_time;

# ���b�N�J�n
&lock if ($lockkey);

# ���O�t�@�C���̓ǂݍ���
open(IN,"$axsfile") || &error("Open Error: $axsfile");
@data = <IN>;
close(IN);

# �u���E�U���
$agent = $ENV{'HTTP_USER_AGENT'};
$agent =~ s/&/&amp;/g;
$agent =~ s/</&lt;/g;
$agent =~ s/>/&gt;/g;
$agent =~ s/"/&quot;/g;

# ���O����
while ($log_max <= @data) { pop(@data); }
unshift(@data,"$ENV{'REMOTE_USER'}<>$date<>$host<>$agent<>\n");

# �X�V
open(OUT,">$axsfile") || &error("Write Error: $axsfile");
print OUT @data;
close(OUT);

# ���b�N����
&unlock if ($lockkey);

#---------------------------------------
#  �G���[
#---------------------------------------
sub error {
	if ($lockflag) { &unlock; }

	die "$_[0] : $!";
}

__END__

# �_�~�[GIF�摜
@gif = (
	"47","49","46","38","39","61","02","00","02","00","80","00",
	"00","00","00","00","ff","ff","ff","21","f9","04","01","00",
	"00","01","00","2c","00","00","00","00","02","00","02","00",
	"00","02","02","8c","53","00","3b",
	);

# �_�~�[�摜��\��
print "Content-type: image/gif\n\n";
foreach (@gif) {
	print pack('C*', hex($_));
}

