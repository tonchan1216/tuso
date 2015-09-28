#��������������������������������������������������������������������
#�� ClipMail
#�� sendmail.pl - 2007/05/23
#�� copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������

#-------------------------------------------------
#  ���M���s
#-------------------------------------------------
sub send_mail {
	# ���Ԏ擾
	my ($date1, $date2) = &get_time;

	# �u���E�U���
	my $agent = $ENV{'HTTP_USER_AGENT'};
	$agent =~ s/<//g;
	$agent =~ s/>//g;
	$agent =~ s/"//g;
	$agent =~ s/&//g;
	$agent =~ s/'//g;

	# �{���e���v���ǂݍ���
	my $tbody;
	open(IN,"$tmpl_body");
	while (<IN>) {
		s/\r\n/\n/;
		s/\r/\n/g;

		$tbody .= $_;
	}
	close(IN);

	# �e���v���ϐ��ϊ�
	$tbody =~ s/\$date/$date1/g;
	$tbody =~ s/\$agent/$agent/g;
	$tbody =~ s/\$host/$host/g;
	&jcode::convert(\$tbody, 'jis');

	# �����ԐM����̂Ƃ�
	my $resbody;
	if ($auto_res) {

		# �e���v��
		open(IN,"$tmpl_bres");
		while (<IN>) {
			s/\r\n/\n/;
			s/\r/\n/g;

			$resbody .= $_;
		}
		close(IN);

		# �ϐ��ϊ�
		$resbody =~ s/\$date/$date1/g;
		$resbody =~ s/\$agent/$agent/g;
		$resbody =~ s/\$host/$host/g;

		# �R�[�h�ϊ�
		&jcode::convert(\$resbody, 'jis');
	}

	# ���O�t�@�C���I�[�v��
	open(DAT,"+< $logfile");
	eval "flock(DAT, 2);";

	# �擪�s�𕪉�
	my $top_log = <DAT>;
	my ($log_date, $log_ip, $log_data) = split(/<>/, $top_log, 3);

	# �n�b�V��%log�Ɋe���ڂ���
	my %log;
	foreach ( split(/<>/, $log_data) ) {
		my ($key,$val) = split(/=/, $_, 2);
		$log{$key} = $val;
	}

	# �{���̃L�[��W�J
	my ($bef, $mbody, $log, $flg, @ext);
	foreach (@key) {
		# �{���Ɋ܂߂Ȃ�������r��
		next if ($_ eq "mode");
		next if ($_ eq "need");
		next if ($_ eq "match");
		next if ($_ eq "subject");
		next if ($in{'match'} && $_ eq $match2);
		next if ($bef eq $_);

		# �Y�t
		my $upl;
		if (/^clip-(\d+)$/i) {
			my $no = $1;
			if ($in{"clip-$no"}) { push(@ext,$no); }

			# ���O�~��
			my ($upl_file) = (split(/:/, $in{"clip-$no"}))[0];
			$log .= "$_=$upl_file<>";
			my $tmp = "�Y�t$no = $upl_file\n";
			&jcode::convert(\$tmp, 'jis', 'sjis');
			$mbody .= $tmp;

			# ���e���d���M�`�F�b�N
			if ($upl_file ne $log{$_}) {
				$flg++;
			}
			next;
		}

		# ���e���d���M�`�F�b�N
		if ($in{$_} ne $log{$_}) {
			$flg++;
		}

		# �G�X�P�[�v
		$in{$_} =~ s/\0/ /g;
		$in{$_} =~ s/\.\n/\. \n/g;

		# �Y�t�t�@�C�����̕����񋑔�
		$in{$_} =~ s/Content-Disposition:\s*attachment;.*//ig;
		$in{$_} =~ s/Content-Transfer-Encoding:.*//ig;
		$in{$_} =~ s/Content-Type:\s*multipart\/mixed;\s*boundary=.*//ig;

		# ���O�~��
		$log .= "$_=$in{$_}<>";

		# ���s����
		$in{$_} =~ s/\t/\n/g;

		# HTML�^�O�ϊ�
		if ($html_tag == 1) {
			$in{$_} =~ s/&lt;/</g;
			$in{$_} =~ s/&gt;/>/g;
			$in{$_} =~ s/&quot;/"/g;
			$in{$_} =~ s/&#39;/'/g;
			$in{$_} =~ s/&amp;/&/g;
		} else {
			$in{$_} =~ s/&lt;/��/g;
			$in{$_} =~ s/&gt;/��/g;
			$in{$_} =~ s/&quot;/�h/g;
			$in{$_} =~ s/&#39;/�f/g;
			$in{$_} =~ s/&amp;/��/g;
		}

		# �{�����e
		my $tmp;
		if ($in{$_} =~ /\n/) {
			$tmp = "$_ = \n$in{$_}\n";
		} else {
			$tmp = "$_ = $in{$_}\n";
		}
		&jcode::convert(\$tmp, 'jis', 'sjis');
		$mbody .= $tmp;

		$bef = $_;
	}

	if (!$flg) {
		close(DAT);
		&error("��d���M�̂��ߏ����𒆎~���܂���");
	}

	# ���O�ۑ�
	my @log;
	if ($keep_log > 0) {
		my $i = 0;
		seek(DAT, 0, 0);
		while(<DAT>) {
			push(@log,$_);

			$i++;
			last if ($i >= $keep_log-1);
		}
	}
	seek(DAT, 0, 0);
	print DAT "date=$date1<>ip=$addr<>$log\n";
	print DAT @log if (@log > 0);
	truncate(DAT, tell(DAT));
	close(DAT);

	# �{���e���v�����̕ϐ���u������
	$tbody =~ s/\$message/$mbody/;

	# �ԐM�e���v�����̕ϐ���u������
	$resbody =~ s/\$message/$mbody/ if ($auto_res);

	# ���[���A�h���X���Ȃ��ꍇ�͑��M��ɒu������
	my $email;
	if ($in{'email'} eq "") {
		$email = $mailto;
	} else {
		$email = $in{'email'};
	}

	# MIME�G���R�[�h
	my $subject2 = &mimeencode($subject);
	if ($in{'name'}) {
		$in{'name'} =~ s/\n//g;
		$from = &mimeencode("\"$in{'name'}\" <$email>");
	} else {
		$from = $email;
	}

	# ��؂��
	my $cut = "------_" . time . "_MULTIPART_MIXED_";

	# --- ���M���e�t�H�[�}�b�g�J�n
	# �w�b�_�[
	my $body = "To: $mailto\n";
	$body .= "From: $from\n";
	if ($cc_mail && $email) { $body .= "Cc: $email\n"; }
	$body .= "Subject: $subject\n";
	$body .= "MIME-Version: 1.0\n";
	$body .= "Date: $date2\n";

	# �Y�t����̂Ƃ�
	if (@ext > 0) {
		$body .= "Content-Type: multipart/mixed; boundary=\"$cut\"\n";
	} else {
		$body .= "Content-type: text/plain; charset=iso-2022-jp\n";
	}

	$body .= "Content-Transfer-Encoding: 7bit\n";
	$body .= "X-Mailer: $ver\n\n";

	# �{��
	if (@ext > 0) {
		$body .= "--$cut\n";
		$body .= "Content-type: text/plain; charset=iso-2022-jp\n";
		$body .= "Content-Transfer-Encoding: 7bit\n\n";
	}
	$body .= "$tbody\n";

	# �ԐM���e�t�H�[�}�b�g
	my $res_body;
	if ($auto_res) {
		$res_body .= "To: $email\n";
		$res_body .= "From: $mailto\n";
		$res_body .= "Subject: $subject2\n";
		$res_body .= "MIME-Version: 1.0\n";
		$res_body .= "Content-type: text/plain; charset=iso-2022-jp\n";
		$res_body .= "Content-Transfer-Encoding: 7bit\n";
		$res_body .= "Date: $date2\n";
		$res_body .= "X-Mailer: $ver\n\n";
		$res_body .= "$resbody\n";
	}

	# �Y�t����
	if (@ext > 0) {
		foreach my $i (@ext) {

			# �t�@�C�����ƈꎞ�t�@�C�����ɕ���
			my ($fname, $tmpfile) = split(/:/, $in{"clip-$i"}, 2);

			# �t�@�C���������`�F�b�N
			next if ($tmpfile !~ /^\d+\-$i\.\w+$/);

			# �ꎞ�t�@�C���������݂��Ȃ��Ƃ��̓X�L�b�v
			next if (! -f "$tmpdir/$tmpfile");

			$fname = &mimeencode($fname);

			# �Y�t�t�@�C�����`
			$body .= qq|--$cut\n|;
			$body .= qq|Content-Type: application/octet-stream; name="$fname"\n|;
			$body .= qq|Content-Disposition: attachment; filename="$fname"\n|;
			$body .= qq|Content-Transfer-Encoding: Base64\n\n|;

			# �ꎞ�t�@�C����Base64�ϊ�
			open(IN,"$tmpdir/$tmpfile");
			binmode(IN);
			while (<IN>) {
				$body .= &bodyencode($_, "b64");
			}
			$body .= &benflush("b64");
			close(IN);

			# �ꎞ�t�@�C���폜
			unlink("$tmpdir/$tmpfile");
		}
		$body .= "--$cut--\n";
	}

	# IO:Socket���W���[�����M�̏ꍇ
	if ($send_type == 2) {
		require $io_socket;

		# �{�����M
		&sendmail($email, $mailto, $body);

		# �ԐM���M
		&sendmail($mailto, $email, $res_body) if ($auto_res);

	# sendmail���M�̏ꍇ
	} else {

		# �{�����M
		open(MAIL,"| $sendmail -t -i") || &error("���[�����M���s");
		print MAIL "$body\n";
		close(MAIL);

		# �ԐM���M
		if ($auto_res) {
			open(MAIL,"| $sendmail -t -i") || &error("���[�����M���s");
			print MAIL "$res_body\n";
			close(MAIL);
		}
	}

	# �����[�h
	if ($reload) {
		if ($ENV{'PERLXS'} eq "PerlIS") {
			print "HTTP/1.0 302 Temporary Redirection\r\n";
			print "Content-type: text/html\n";
		}
		print "Location: $back\n\n";
		exit;

	# �������b�Z�[�W
	} else {
		my $cp_flg;
		open(IN,"$tmpl_thx") || &error("Open Error: $tmpl_thx");
		print "Content-type: text/html\n\n";
		while (<IN>) {
			s/\$back/$back/;

			if (/(<\/body([^>]*)>)/i) {
				$cp_flg = 1;
				my $tmp = $1;
				s/$tmp/$copy\n$tmp/;
			}

			print;
		}
		close(IN);

		if (!$cp_flg) {
			print "$copy\n</body></html>\n";
		}
		exit;
	}
}


1;

