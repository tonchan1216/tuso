#!/usr/bin/perl

#��������������������������������������������������������������������
#�� Clip Mail
#�� clipmail.cgi - 2007/05/26
#�� copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������

# �O���t�@�C����荞��
require './init.cgi';
require $jcodepl;

# �t�H�[���f�R�[�h
&parse_form || &error("�s���ȏ����ł�");

# �`�F�b�N���[�h
if ($in{'mode'} eq "check") {
	require $checkpl;
	&check;
}

# POST�`�F�b�N
if ($postonly && !$post_flg) { &error("�s���ȃA�N�Z�X�ł�"); }

# ���������`�F�b�N
if ($in{'subject'}) { $subject = &sub_check; }

# ���쌠�\�L�i�폜�s�j
$copy = <<EOM;
<br />
<div align="center" style="font-size:10px; font-family:Verdana,Helvetica,Arial;">
- <a href="http://www.kent-web.com/" target="_top">ClipMail</a> -
</div>
EOM

# �֎~���[�h
if ($no_wd) {
	my $flg;
	foreach (@key) {
		foreach my $nowd ( split(/,/, $no_wd) ) {
			if (index($in{$_},$nowd) >= 0) {
				$flg = 1;
				last;
			}
		}
		if ($flg) { &error("�֎~���[�h���܂܂�Ă��܂�"); }
	}
}

# �z�X�g�擾���`�F�b�N
&get_host;

# �K�{���̓`�F�b�N
if ($in{'need'}) {
	# need�t�B�[���h�̒l��K�{�z��ɉ�����
	my @tmp = split(/\s+/, $in{'need'});
	push(@need,@tmp);

	# �K�{�z��̏d���v�f��r������
	my (@uniq, %seen);
	foreach (@need) {
		push(@uniq,$_) unless $seen{$_}++;
	}

	# �K�{���ڂ̓��͒l���`�F�b�N����
	foreach (@uniq) {

		# �t�B�[���h�̒l���������Ă��Ȃ����́i���W�I�{�^�����j
		if (!defined($in{$_})) {
			$check++;
			push(@key,$_);
			push(@err,$_);

		# ���͂Ȃ��̏ꍇ
		} elsif ($in{$_} eq "") {
			$check++;
			push(@err,$_);
		}
	}
}

# ���͓��e�}�b�`
local($match1, $match2);
if ($in{'match'}) {
	($match1, $match2) = split(/\s+/, $in{'match'}, 2);

	if ($in{$match1} ne $in{$match2}) {
		&error("$match1��$match2�̍ē��͓��e���قȂ�܂�");
	}
}

# ���̓`�F�b�N�m�F���
if ($check || $max_flg) {
	require $erchkpl;
	&err_check;
}

# E-mail�����`�F�b�N
if ($in{'email'} =~ /\,/) {
	&error("���[���A�h���X�ɃR���} ( , ) ���܂܂�Ă��܂�");
}
if ($in{'email'} && $in{'email'} !~ /^[\w\.\-]+\@[\w\.\-]+\.[a-zA-Z]{2,6}$/) {
	&error("���[���A�h���X�̏������s���ł�");
}

# �v���r���[
if ($in{'mode'} ne "send") {
	require $prevwpl;
	&preview;

# ���M���s
} else {
	require $sendmpl;
	require $mimewpl;
	&send_mail;
}

#-------------------------------------------------
#  �G���[����
#-------------------------------------------------
sub error {
	my $err = shift;

	print "Content-type: text/html\n\n";
	open(IN,"$tmpl_err1");
	while (<IN>) {
		s/\$error/$err/;

		print;
	}
	close(IN);

	exit;
}

#-------------------------------------------------
#  ���Ԏ擾
#-------------------------------------------------
sub get_time {
	$ENV{'TZ'} = "JST-9";
	my ($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(time);
	my @week  = qw|Sun Mon Tue Wed Thu Fri Sat|;
	my @month = qw|Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec|;

	# �����̃t�H�[�}�b�g
	my $date1 = sprintf("%04d/%02d/%02d(%s) %02d:%02d:%02d",
			$year+1900,$mon+1,$mday,$week[$wday],$hour,$min,$sec);
	my $date2 = sprintf("%s, %02d %s %04d %02d:%02d:%02d",
			$week[$wday],$mday,$month[$mon],$year+1900,$hour,$min,$sec) . " +0900";

	return ($date1, $date2);
}

#-------------------------------------------------
#  �z�X�g���擾
#-------------------------------------------------
sub get_host {
	# �z�X�g���擾
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};

	if ($gethostbyaddr && ($host eq "" || $host eq $addr)) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
	}
	if ($host eq "") { $host = $addr; }

	# �`�F�b�N
	if ($denyhost) {
		my $flg;
		foreach ( split(/\s+/, $denyhost) ) {
			s/\./\\\./g;
			s/\*/\.\*/g;

			if ($host =~ /$_/i) { $flg = 1; last; }
		}
		if ($flg) { &error("�A�N�Z�X��������Ă��܂���"); }
	}
}

#-------------------------------------------------
#  ���������`�F�b�N
#-------------------------------------------------
sub sub_check {
	my $sub = $in{'subject'};
	&jcode::convert(\$sub, 'euc', 'sjis');

	$sub =~ s/\r//g;
	$sub =~ s/\n//g;
	$sub =~ s/\@/��/g;
	$sub =~ s/\./�D/g;
	$sub =~ s/\+/�{/g;
	$sub =~ s/\-/�|/g;
	$sub =~ s/\:/�F/g;
	$sub =~ s/\;/�G/g;
	$sub =~ s/\|/�b/g;

	&jcode::convert(\$sub, 'sjis', 'euc');
	return $sub;
}

