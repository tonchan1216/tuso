#!/usr/local/bin/perl

#��������������������������������������������������
#�� PasswordManager v2
#�� pwlog_test.cgi (SSI�p) - 2005/08/19
#�� Copyright (c) KentWeb
#�� http://www.kent-web.com/
#��������������������������������������������������
# �y�g�����z���O�C�����HTML�y�[�W�Ɉȉ���SSI�^�O���L�q
#  <!--#exec cgi="/�t���p�X/pwlog_test.cgi"-->
#
# �y���p�����z
#  1. SSI�̗��p�ł���T�[�o
#  2. ���ϐ� $ENV{'REMOTE_USER'} �ɂă��[�U�[ID���擾�ł��邱��

print "Content-type: text/plain\n\n";
print "���[�U�[ID�\\���e�X�g �� $ENV{'REMOTE_USER'}\n";

