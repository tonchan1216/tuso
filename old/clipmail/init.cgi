#��������������������������������������������������������������������
#�� Clip MAIL v1.0
#�� init.cgi - 2007/07/26
#�� copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������
$ver = 'Clip MAIL v1.0';
#��������������������������������������������������������������������
#�� [���ӎ���]
#�� 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����
#��    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B
#�� 2. ���M�t�H�[����HTML�y�[�W�̍쐬�Ɋւ��ẮAHTML���@�̔��e
#��    �ƂȂ邽�߁A�T�|�[�g�ΏۊO�ƂȂ�܂��B
#�� 3. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B
#��    ���ڃ��[���ɂ�鎿��͂��󂯂������Ă���܂���B
#��������������������������������������������������������������������
#
# [ ���M�t�H�[�� (HTML) �̋L�q�� ]
#
# �E�^�O�̋L�q�� (1)
#   ���Ȃ܂� <input type="text" name="name" size="25">
#   �� ���̃t�H�[���Ɂu�R�c���Y�v�Ɠ��͂��đ��M����ƁA
#      �uname = �R�c���Y�v�Ƃ����`���Ŏ�M���܂�
#
# �E�^�O�̋L�q�� (2)
#   ���D���ȐF <input type="radio" name="color" value="��">
#   �� ���̃��W�I�{�b�N�X�Ƀ`�F�b�N���đ��M����ƁA
#      �ucolor = �v�Ƃ����`���Ŏ�M���܂�
#
# �E�^�O�̋L�q�� (3)
#   E-mail <input type="text" name="email" size="25">
#   �� name�l�Ɂuemail�v�Ƃ����������g���Ƃ���̓��[���A�h���X
#      �ƔF�����A�A�h���X�̏������ȈՃ`�F�b�N���܂�
#   �� (��) abc@xxx.co.jp
#   �� (�~) abc.xxx.co.jp �� ���̓G���[�ƂȂ�܂�
#
# �E�^�O�̋L�q�� (4)
#   E-mail <input type="text" name="_email" size="25">
#   �� name�l�̐擪�Ɂu�A���_�[�o�[ �v��t����ƁA���̓��͒l��
#     �u���͕K�{�v�ƂȂ�܂��B
#      ��L�̗�ł́A�u���[���A�h���X�͓��͕K�{�v�ƂȂ�܂��B
#
# �Ename�l�ւ́u�S�p�����v�̎g�p�͉\�ł�
#  (��) <input type="radio" name="�N��" value="20�Α�">
#  �� ��L�̃��W�I�{�b�N�X�Ƀ`�F�b�N�����đ��M����ƁA
#     �u�N�� = 20�Α�v�Ƃ��������Ŏ󂯎�邱�Ƃ��ł��܂��B
#
# �Ename�l���uname�v�Ƃ���Ƃ�����u���M�Җ��v�ƔF�����đ��M����
#   ���[���A�h���X���u���M�� <���[���A�h���X>�v�Ƃ����t�H�[�}�b�g��
#   �����ϊ����܂��B
#  (�t�H�[���L�q��)  <input type="text" name="name">
#  (���M���A�h���X)  ���Y <taro@email.xx.jp>
#
# �E�^�O�̋L�q�� (5)
#   ���Y�t���[�����̏ꍇ��
#   <input type="file" name="clip-1" size="40">
#   �� name�l���uclip-�v+�u�����v�ɂ��Ă��������B
#   �� �u�����v��ς��邱�ƂŁA�Q�Ɨp�t�B�[���h�𕡐��p�ӂ��邱�Ƃ�
#      �ł��܂��B
#
# �E�R�}���h�^�O (1)
#   �� ���͕K�{���ڂ������w�肷��i���p�X�y�[�X�ŕ����w��j
#   �� ���W�I�{�^���A�`�F�b�N�{�b�N�X�΍�
#   �� name�l���uneed�v�Avalue�l���u�K�{����1 + ���p�X�y�[�X +�K�{����2 + ���p�X�y�[�X ...�v
#   (��) <input type="hidden" name="need" value="���O ���[���A�h���X ����">
#
# �E�R�}���h�^�O (2)
#   �� 2�̓��͓��e�����ꂩ���`�F�b�N����
#   �� name�l���umatch�v�Avalue�l���u����1 + ���p�X�y�[�X + ����2�v
#   (��) <input type="hidden" name="match" value="email email2">
#
# �E�R�}���h�^�O (3)
#   �� ���[���������w�肷��
#   �� ���̏ꍇ�A�ݒ�Ŏw�肷�� $subject ���D�悳��܂��B
#   (��) <input type="hidden" name="subject" value="���[���^�C�g������">
#
#  [ �ȈՃ`�F�b�N ]
#   http://�`�`/clipmail.cgi?mode=check
#
#  [ �ݒu�� ]
#
#  public_html / index.html (�g�b�v�y�[�W���j
#       |
#       +-- postmail / clipmail.cgi   [705]
#             |        admin.cgi      [705] ... �Ǘ����
#             |        init.cgi       [604] ... �ݒ�t�@�C��
#             |
#             +-- lib / jcode.pl      [604]
#             |         mimew.pl      [604]
#             |         io-socket.pl  [604]
#             |         check.pl      [604]
#             |         preview.pl    [604]
#             |         sendmail.pl   [604]
#             |         errcheck.pl   [604]
#             |
#             +-- data / pwd.cgi      [606]
#             |          log.cgi      [606]
#             |
#             +-- temp [707] /
#             |
#             +-- tmpl / body.txt
#                        body_res.txt
#                        conf.html
#                        err1.html
#                        err2.html
#                        thx.html

#===========================================================
#  ����{�ݒ�
#===========================================================

# �O���t�@�C��
$jcodepl = './lib/jcode.pl';
$mimewpl = './lib/mimew.pl';
$checkpl = './lib/check.pl';
$prevwpl = './lib/preview.pl';
$sendmpl = './lib/sendmail.pl';
$erchkpl = './lib/errcheck.pl';

# ���M�惁�[���A�h���X
$mailto = 'tohokuuniv@tohokuuniv-orch.com';

# �Y�t���[����������
# 0 : no
# 1 : yes
$attach = 0;

# �Y�t���[�����̂Ƃ��Y�t�t�@�C���́u�g���q�v���w�肷��ꍇ
# �� �� (�h�b�g�Ȃ��ŋL�q) : @pmt_ext = ('gif', 'jpg', 'jpeg', 'png');
# �� ���ׂĂ̊g���q��OK�ɂ���Ƃ��́A@pmt_ext = (); �Ƃ��܂�
@pmt_ext = ('gif', 'jpg', 'jpeg', 'png', 'bmp');

# �摜�v���r���[�̎��̕\���T�C�Y
# �� �摜��GIF/JPEG/PNG/BMP�̂�
# �� ���ɉ����A�c��
$img_max_w = 200;
$img_max_h = 150;

# ���̓t�B�[���h������̍ő�e�ʁi�o�C�g�j
# ���Q�l : �S�p1���� = 2�o�C�g
$max_field = 300;

# �ő��M�T�C�Y
# �� �� : 102400 = 100KB
$maxdata = 1024000;

# �����ԐM
# 0 : no
# 1 : yes
$auto_res = 0;

# ���O�~�ς̍ő�ۑ���
# �� 0 �ɂ���Ƌ@�\����
$keep_log = 200;

# HTML�^�O�̏���
# �� < > " & ' �̏���
# 1 : ���S����
# 2 : �S�p�ɕϊ��i�Z�L�����e�B�エ�����߁j
$html_tag = 2;

# ���[���^�C�g��
$subject = 'Web����̂��₢���킹';

# �{�̃v���O�����yURL�p�X�z
$script = './clipmail.cgi';

# �Ǘ��v���O�����yURL�p�X�z
$admincgi = './admin.cgi';

# ���O�t�@�C���y�T�[�o�p�X�z
$logfile = './data/log.cgi';

# �p�X���[�h�t�@�C���y�T�[�o�p�X�z
$pwdfile = './data/pwd.cgi';

# �ꎞ�f�B���N�g���yURL�p�X�z
$tmpurl = './temp';

# �ꎞ�f�B���N�g���y�T�[�o�p�X�z
$tmpdir = './temp';

# �m�F��ʃe���v���[�g�y�T�[�o�p�X�z
$tmpl_conf = './tmpl/conf.html';

# ��ʃG���[��ʃe���v���[�g�y�T�[�o�p�X�z
$tmpl_err1 = './tmpl/err1.html';

# ���̓G���[��ʃe���v���[�g�y�T�[�o�p�X�z
$tmpl_err2 = './tmpl/err2.html';

# ���M���ʃe���v���[�g�y�T�[�o�p�X�z
$tmpl_thx = './tmpl/thx.html';

# ���M�p���b�Z�[�W�e���v���[�g�y�T�[�o�p�X�z
$tmpl_body = './tmpl/body.txt';

# �ԐM�p���b�Z�[�W�e���v���[�g�y�T�[�o�p�X�z
$tmpl_bres = './tmpl/body_res.txt';

# ���M��̌`��
# 0 : �������b�Z�[�W���o��.
# 1 : �߂�� ($back) �֎����W�����v������.
$reload = 0;

# ���M��̖߂��yURL�p�X�z
# �� http://����L�q����
$back = 'http://www.tohokuuniv-orch.com/clipmail/clipmail.html';

# ���M�� method=POST ���� (0=no 1=yes)
# �� �Z�L�����e�B�΍�
$postonly = 1;

# �A���[���F
$alm_col = "#dd0000";

# �z�X�g�擾���@
# 0 : gethostbyaddr�֐����g��Ȃ�
# 1 : gethostbyaddr�֐����g��
$gethostbyaddr = 0;

# �A�N�Z�X�����i��������Δ��p�X�y�[�X�ŋ�؂�A�A�X�^���X�N�j
# �� ���ۃz�X�g������IP�A�h���X�̋L�q��
#   �i�O����v�͐擪�� ^ ������j�y��z^210.12.345.*
#   �i�����v�͖����� $ ������j�y��z*.anonymizer.com$
$denyhost = '';

# �֎~���[�h
# �� ���e���֎~���郏�[�h���R���}�ŋ�؂�
$no_wd = '';

# ���[�����M�`��
# 1 : sendmail���M�isendmail�����p�\�ȃT�[�o�j
# 2 : IO:Socket���W���[�����M�i�\�P�b�g�֘A�̃��W���[�������p�\�ȃT�[�o�j
$send_type = 1;

## sendmail���M�̂Ƃ� ##
# sendmail�̃p�X
$sendmail = '/usr/sbin/sendmail';

##�y���zsendmail���M�̕��͐ݒ�͂����܂łŏI���B�����艺�͐ݒ�s�v�ł��B

## IO:Socket���W���[�����M�̂Ƃ� ##
# io-socket.pl�̃p�X
$io_socket = './lib/io-socket.pl';

# SMTP�T�[�o
$server = "mail.server.xx.jp";

# SMTP�|�[�g�ԍ��i�ʏ��25�j
$port = 25;

# POP before SMTP���g�p����
# 0 : no
# 1 : yes
$pop_bef_smtp = 0;

# POP3�T�[�o�yPOP before SMTP�̂Ƃ��z
$pop3sv = 'mail.server.xx.jp';

# POP3�|�[�g�ԍ��i�ʏ��110�j�yPOP before SMTP�̂Ƃ��z
$pop3port = 110;

# �ڑ�ID�yPOP before SMTP�̂Ƃ��z
$user = 'user_id';

# �ڑ��p�X���[�h�yPOP before SMTP�̂Ƃ��z
$pass = 'password';

## ��SMTP�T�[�o�ւ̐ڑ���񂱂��܂�

#===========================================================
#  ���ݒ芮��
#===========================================================

#-------------------------------------------------
#  �t�H�[���f�R�[�h
#-------------------------------------------------
sub parse_form {
	# �e�ϐ�������
	undef(%in);
	undef(%fname);
	undef(%uplno);
	undef(%ctype);
	undef(%err);
	undef(@key);
	undef(@need);
	undef(@err);
	($macbin, $post_flg, $upl_flg, $max_flg, $check) = (0, 0, 0, 0, 0);

	# �ő�e�ʃ`�F�b�N
	my $conlen = $ENV{'CONTENT_LENGTH'};
	if ($conlen > $maxdata) {
		my $maxd = int( $maxdata / 1024 ) . "KB";
		&error("�e�ʃT�C�Y�I�[�o�[�ł� : $maxd�܂�");
	}

	# �}���`�p�[�g�t�H�[���̂Ƃ�
	if ($ENV{'CONTENT_TYPE'} =~ m|multipart/form-data|i) {
		$post_flg = 1;

		# �ϐ�������
		my ($key, $val, $uplno);

		# �W�����͂��o�C�i�����[�h�錾
		binmode(STDIN);

		# �擪��boundary��F��
		my $bound = <STDIN>;
		$bound =~ s/\r\n//;

		# �W�����͂�W�J
		while (<STDIN>) {

			# �}�b�N�o�C�i���F��
			if (m|application/x-macbinary|i) { $macbin = 1; }

			# Content-Disposition�F��
			if (/^Content-Disposition:/i) {
				$flg = 1;
			}

			# name�����F��
			if ($flg == 1 && /\s+name="([^";]+)"/i) {
				$key = $1;

				if ($key =~ /^_?clip-(\d+)$/i) {
					$upl_flg++;
					$uplno = $1;
					$uplno{$uplno} = $uplno;
				}
			}

			# filename�����F���i�t�@�C���A�b�v�j
			if ($uplno && /\s+filename="([^";]+)"/i) {

				# �Y�t���ۂ̂Ƃ�
				if (!$attach) { &error("�Y�t���[���͋�����Ă��܂���"); }

				my $fnam = $1;
				&jcode::convert(\$fnam, 'sjis');
				$fname{$uplno} = $fnam;

				# �g���q�`�F�b�N
				if (@pmt_ext > 0) {
					my $flg;
					foreach my $ext (@pmt_ext) {
						if ($fname{$uplno} =~ /\.$ext$/i) { $flg++; last; }
					}
					if (!$flg) {
						&error("������Ă��Ȃ��Y�t�t�@�C���ł� : $fname{$uplno}");
					}
				}
			}

			# Content-Type�F���i�t�@�C���A�b�v�j
			if ($uplno && /Content-Type:\s*([^";]+)/i) {
				my $ctype = $1;
				$ctype =~ s/\r//g;
				$ctype =~ s/\n//g;

				$ctype{$uplno} = $ctype;
			}

			# �w�b�_ �� �{��
			if ($flg == 1 && /^\r\n/) {
				$flg = 2;
				next;
			}
			# �{���F��
			if ($flg == 2) {

				# boundary���o �� �t�B�[���h�I��
				if (/^$bound/) {

					# �����̉��s���J�b�g
					$val =~ s/\r\n$//;

					# �e�L�X�g�n����
					if (!$uplno) {

						# S-JIS�R�[�h�ϊ�
						&jcode::convert(\$key, 'sjis');
						&jcode::convert(\$val, 'sjis');

						# �G�X�P�[�v
						$key =~ s/&//g;
						$key =~ s/"//g;
						$key =~ s/<//g;
						$key =~ s/>//g;
						$key =~ s/'//g;
						$key =~ s/\r//g;
						$key =~ s/\n//g;
						$val =~ s/&/&amp;/g;
						$val =~ s/"/&quot;/g;
						$val =~ s/</&lt;/g;
						$val =~ s/>/&gt;/g;
						$val =~ s/\r\n/\t/g;
						$val =~ s/\r/\t/g;
						$val =~ s/\n/\t/g;

						# �e���ڃT�C�Y���`�F�b�N
						if (length($key) > $max_field || length($val) > $max_field) {
							$max_flg = 1;
							$err{$key} = $val;
						}
					}

					# �K�{���͍��ڂ�F�����`�F�b�N
					if ($key =~ /^_(.+)/) {
						$key = $1;
						push(@need,$key);

						if ($val eq "") { $check++; push(@err,$key); }
					}

					# %in��`
					$in{$key} .= "\0" if (defined($in{$key}));
					$in{$key} .= $val;

					# �L�[�͔z�񉻂��Ă���
					push(@key,$key);

					# �t���O��������
					$flg = $uplno = $key = $val = '';
					next;
				}
				# boundary���o�܂Ŗ{�����o���Ă���
				$val .= $_;
			}
		}
		# �Ԃ�l
		$conlen;

	# �}���`�p�[�g�t�H�[���ȊO�̂Ƃ�
	} else {

		# �f�[�^���
		my $buf;
		if ($ENV{'REQUEST_METHOD'} eq "POST") {
			$post_flg = 1;
			read(STDIN, $buf, $ENV{'CONTENT_LENGTH'});
		} else {
			$buf = $ENV{'QUERY_STRING'};
		}

		# URL�f�R�[�h
		foreach ( split(/&/, $buf) ) {
			my ($key, $val) = split(/=/);
			$key =~ tr/+/ /;
			$key =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;
			$val =~ tr/+/ /;
			$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;

			# S-JIS�R�[�h�ϊ�
			&jcode::convert(\$key, 'sjis');
			&jcode::convert(\$val, 'sjis');

			# �G�X�P�[�v
			$key =~ s/&//g;
			$key =~ s/"//g;
			$key =~ s/<//g;
			$key =~ s/>//g;
			$key =~ s/'//g;
			$key =~ s/\r//g;
			$key =~ s/\n//g;
			$val =~ s/&/&amp;/g;
			$val =~ s/"/&quot;/g;
			$val =~ s/</&lt;/g;
			$val =~ s/>/&gt;/g;
			$val =~ s/\r\n/\t/g;
			$val =~ s/\r/\t/g;
			$val =~ s/\n/\t/g;

			# �e���ڃT�C�Y���`�F�b�N
			if (length($key) > $max_field || length($val) > $max_field) {
				$max_flg = 1;
				$err{$key} = $val;
			}

			# �K�{���͍��ڂ�F�����`�F�b�N
			if ($key =~ /^_(.+)/) {
				$key = $1;
				push(@need,$key);

				if ($val eq "") { $check++; push(@err,$key); }
			}

			# %in��`
			$in{$key} .= "\0" if (defined($in{$key}));
			$in{$key} .= $val;

			# �L�[�͔z�񉻂��Ă���
			push(@key,$key);
		}
		# �Ԃ�l
		if ($buf) { return 1; } else { return 0; }
	}
}


1;

