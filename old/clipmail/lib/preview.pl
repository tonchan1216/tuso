#┌─────────────────────────────────
#│ ClipMail
#│ preview.pl - 2007/06/30
#│ copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────

#-------------------------------------------------
#  プレビュー
#-------------------------------------------------
sub preview {
	my ($cp_flg, $flg, $cell, $hidden, %file, %ext);
	my $time = time;

	# 添付あり
	if ($upl_flg) {

		# 一時ディレクトリを掃除
		&clean_dir;

		foreach my $i ( sort{ $a <=> $b }keys(%uplno) ) {

			# ファイル種類を認識
			my $file;
			if ($fname{$i} =~ /([^\\\/\.]+)\.([^\\\/\.]+)$/) {
				$file{$i} = "$1.$2";
				$ext{$i}  = $2;
			} else {
				next;
			}

			# アップロードファイル
			my $upfile = "$tmpdir/$time-$i.$ext{$i}";

			# マックバイナリ対策
			if ($macbin) {
				my $length = substr($upfile, 83, 4);
				$length = unpack("%N", $length);
				$upfile = substr($upfile, 128, $length);
			}

			# 添付ファイル書き込み
			open(UPL,"> $upfile");
			binmode(UPL);
			print UPL $in{"clip-$i"};
			close(UPL);
		}
	}

	# 画面展開
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

				# 画像SUBMITボタンは無視
				next if ($key eq "x");
				next if ($key eq "y");

				if ($key eq "need" || $key eq "match" || ($in{'match'} && $key eq $match2)) {
					next;

				} elsif ($key eq "subject") {
					$hidden .= qq|<input type="hidden" name="$key" value="$in{$key}" />\n|;
					next;
				}

				# 添付のとき
				if ($key =~ /^clip-(\d+)$/i) {

					my $no = $1;
					if (defined($file{$no})) {
						$hidden .= qq|<input type="hidden" name="$key" value="$file{$no}:$time-$no.$ext{$no}" />\n|;
					} else {
						$hidden .= qq|<input type="hidden" name="$key" value="" />\n|;
					}

					my $tmp = $cell;
					$tmp =~ s/\$left/添付$no/;

					# 画像のとき
					if ($ext{$no} =~ /^(gif|jpe?g|png|bmp)$/i) {

						# 表示サイズ調整
						my ($w, $h) = &resize("$tmpdir/$time-$no.$ext{$no}", $1);

						$tmp =~ s|\$right|<img src="$tmpurl/$time-$no.$ext{$no}" width="$w" height="$h" alt="$file{$no}" />|;

					# 画像以外
					} else {
						$tmp =~ s/\$right/$file{$no}/;
					}
					print $tmp;

				# テキスト（添付以外）
				} else {

					$in{$key} =~ s/\0/ /g;
					$hidden .= qq|<input type="hidden" name="$key" value="$in{$key}" />\n|;

					# 改行変換
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
#  一時ディレクトリ掃除
#-------------------------------------------------
sub clean_dir {
		# 一時ディレクトリ内読み取り
		opendir(DIR,"$tmpdir");
		my @dir = readdir(DIR);
		closedir(DIR);

		foreach (@dir) {
			# 対象外はスキップ
			next if ($_ eq '.');
			next if ($_ eq '..');
			next if ($_ eq 'index.html');

			# ファイル時間取得
			my $mtime = (stat("$tmpdir/$_"))[9];

			# 3時間以上経過しているファイルは削除
			if (time - $mtime > 3*3600) {
				unlink("$tmpdir/$_");
			}
		}
}

#-------------------------------------------------
#  画像リサイズ
#-------------------------------------------------
sub resize {
	my ($path, $ext) = @_;

	# サイズ取得
	if ($ext =~ /^gif$/i) {
		($w, $h) = &g_size($path);

	} elsif ($ext =~ /^jpe?g$/i) {
		($w, $h) = &j_size($path);

	} elsif ($ext =~ /^png$/i) {
		($w, $h) = &p_size($path);

	} elsif ($ext =~ /^bmp$/i) {
		($w, $h) = &b_size($path);
	}

	# 調整
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
#  JPEGサイズ認識
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
#  GIFサイズ認識
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
#  PNGサイズ認識
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
#  BMPサイズ
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

