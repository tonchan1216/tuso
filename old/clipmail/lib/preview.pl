#��������������������������������������������������������������������
#�� ClipMail
#�� preview.pl - 2007/06/30
#�� copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������

#-------------------------------------------------
#  �v���r���[
#-------------------------------------------------
sub preview {
	my ($cp_flg, $flg, $cell, $hidden, %file, %ext);
	my $time = time;

	# �Y�t����
	if ($upl_flg) {

		# �ꎞ�f�B���N�g����|��
		&clean_dir;

		foreach my $i ( sort{ $a <=> $b }keys(%uplno) ) {

			# �t�@�C����ނ�F��
			my $file;
			if ($fname{$i} =~ /([^\\\/\.]+)\.([^\\\/\.]+)$/) {
				$file{$i} = "$1.$2";
				$ext{$i}  = $2;
			} else {
				next;
			}

			# �A�b�v���[�h�t�@�C��
			my $upfile = "$tmpdir/$time-$i.$ext{$i}";

			# �}�b�N�o�C�i���΍�
			if ($macbin) {
				my $length = substr($upfile, 83, 4);
				$length = unpack("%N", $length);
				$upfile = substr($upfile, 128, $length);
			}

			# �Y�t�t�@�C����������
			open(UPL,"> $upfile");
			binmode(UPL);
			print UPL $in{"clip-$i"};
			close(UPL);
		}
	}

	# ��ʓW�J
	open(IN,"$tmpl_conf") || &error("Open Error: $tmpl_conf");
	print "Content-type: text/html\n\n";
	while (<IN>) {
		if (/<!-- cell_begin -->/) {
			$flg = 1;
			next;
		}
		if (/<!-- cell_end -->/) {
			$flg = 0;

			$hidden .= qq|<input type="hidden" name="mode" value="send" />\n|;

			my $bef;
			foreach my $key (@key) {
				next if ($bef eq $key);

				# �摜SUBMIT�{�^���͖���
				next if ($key eq "x");
				next if ($key eq "y");

				if ($key eq "need" || $key eq "match" || ($in{'match'} && $key eq $match2)) {
					next;

				} elsif ($key eq "subject") {
					$hidden .= qq|<input type="hidden" name="$key" value="$in{$key}" />\n|;
					next;
				}

				# �Y�t�̂Ƃ�
				if ($key =~ /^clip-(\d+)$/i) {

					my $no = $1;
					if (defined($file{$no})) {
						$hidden .= qq|<input type="hidden" name="$key" value="$file{$no}:$time-$no.$ext{$no}" />\n|;
					} else {
						$hidden .= qq|<input type="hidden" name="$key" value="" />\n|;
					}

					my $tmp = $cell;
					$tmp =~ s/\$left/�Y�t$no/;

					# �摜�̂Ƃ�
					if ($ext{$no} =~ /^(gif|jpe?g|png|bmp)$/i) {

						# �\���T�C�Y����
						my ($w, $h) = &resize("$tmpdir/$time-$no.$ext{$no}", $1);

						$tmp =~ s|\$right|<img src="$tmpurl/$time-$no.$ext{$no}" width="$w" height="$h" alt="$file{$no}" />|;

					# �摜�ȊO
					} else {
						$tmp =~ s/\$right/$file{$no}/;
					}
					print $tmp;

				# �e�L�X�g�i�Y�t�ȊO�j
				} else {

					$in{$key} =~ s/\0/ /g;
					$hidden .= qq|<input type="hidden" name="$key" value="$in{$key}" />\n|;

					# ���s�ϊ�
					$in{$key} =~ s/\t/<br>/g;

					my $tmp = $cell;
					$tmp =~ s/\$left/$key/;
					$tmp =~ s/\$right/$in{$key}/;
					print $tmp;
				}

				$bef = $key;
			}
			next;
		}
		if ($flg) {
			$cell .= $_;
			next;
		}

		s/\$script/$script/;
		s/<!-- hidden -->/$hidden/;

		if (/(<\/body([^>]*)>)/i) {
			$cp_flg = 1;
			my $tmp = $1;
			s/$tmp/$copy\n$tmp/;
		}

		print;
	}
	close(IN);

	if (!$cp_flg) {
		print "$copy\n";
		print "</body></html>\n";
	}

	exit;
}

#-------------------------------------------------
#  �ꎞ�f�B���N�g���|��
#-------------------------------------------------
sub clean_dir {
		# �ꎞ�f�B���N�g�����ǂݎ��
		opendir(DIR,"$tmpdir");
		my @dir = readdir(DIR);
		closedir(DIR);

		foreach (@dir) {
			# �ΏۊO�̓X�L�b�v
			next if ($_ eq '.');
			next if ($_ eq '..');
			next if ($_ eq 'index.html');

			# �t�@�C�����Ԏ擾
			my $mtime = (stat("$tmpdir/$_"))[9];

			# 3���Ԉȏ�o�߂��Ă���t�@�C���͍폜
			if (time - $mtime > 3*3600) {
				unlink("$tmpdir/$_");
			}
		}
}

#-------------------------------------------------
#  �摜���T�C�Y
#-------------------------------------------------
sub resize {
	my ($path, $ext) = @_;

	# �T�C�Y�擾
	if ($ext =~ /^gif$/i) {
		($w, $h) = &g_size($path);

	} elsif ($ext =~ /^jpe?g$/i) {
		($w, $h) = &j_size($path);

	} elsif ($ext =~ /^png$/i) {
		($w, $h) = &p_size($path);

	} elsif ($ext =~ /^bmp$/i) {
		($w, $h) = &b_size($path);
	}

	# ����
	if ($w > $img_max_w || $h > $img_max_h) {
		$w2 = $img_max_w / $w;
		$h2 = $img_max_h / $h;
		if ($w2 < $h2) {
			$key = $w2;
		} else {
			$key = $h2;
		}
		$w = int ($w * $key) || 1;
		$h = int ($h * $key) || 1;
	}
	($w, $h);
}

#-------------------------------------------------
#  JPEG�T�C�Y�F��
#-------------------------------------------------
sub j_size {
	my $image = shift;

	my ($w, $h, $t);
	open(IMG, "$image") || return (0,0);
	binmode(IMG);
	read(IMG, $t, 2);
	while (1) {
		read(IMG, $t, 4);
		my ($m, $c, $l) = unpack("a a n", $t);

		if ($m ne "\xFF") {
			$w = $h = 0;
			last;
		} elsif ((ord($c) >= 0xC0) && (ord($c) <= 0xC3)) {
			read(IMG, $t, 5);
			($h, $w) = unpack("xnn", $t);
			last;
		} else {
			read(IMG, $t, ($l - 2));
		}
	}
	close(IMG);

	($w, $h);
}

#-------------------------------------------------
#  GIF�T�C�Y�F��
#-------------------------------------------------
sub g_size {
	my $image = shift;

	my $data;
	open(IMG,"$image") || return (0,0);
	binmode(IMG);
	sysread(IMG, $data, 10);
	close(IMG);

	if ($data =~ /^GIF/) { $data = substr($data, -4); }
	my $w = unpack("v", substr($data, 0, 2));
	my $h = unpack("v", substr($data, 2, 2));

	($w, $h);
}

#-------------------------------------------------
#  PNG�T�C�Y�F��
#-------------------------------------------------
sub p_size {
	my $image = shift;

	my $data;
	open(IMG, "$image") || return (0,0);
	binmode(IMG);
	read(IMG, $data, 24);
	close(IMG);

	my $w = unpack("N", substr($data, 16, 20));
	my $h = unpack("N", substr($data, 20, 24));

	($w, $h);
}

#-------------------------------------------------
#  BMP�T�C�Y
#-------------------------------------------------
sub b_size {
	my $image = shift;

	my $data;
	open(IMG, "$image") || return (0,0);
	binmode(IMG);
	seek(IMG, 0, 0);
	read(IMG, $data, 6);
	seek(IMG, 12, 1);
	read(IMG, $data, 8);

	unpack("VV", $data);
}



1;

