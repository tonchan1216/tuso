#┌─────────────────────────────────
#│ ClipMail
#│ errcheck.pl - 2007/07/26
#│ copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────

#-------------------------------------------------
#  入力エラー表示
#-------------------------------------------------
sub err_check {
	my ($err, $cp_flg, $flg, $cell);

	open(IN,"$tmpl_err2") || &error("Open Error: $tmpl_err2");
	print "Content-type: text/html\n\n";
	while (<IN>) {
		if (/<!-- cell_begin -->/) {
			$flg = 1;
		}
		if (/<!-- cell_end -->/) {
			$flg = 0;

			my $bef;
			foreach my $key (@key) {
				next if ($key eq "need");
				next if ($key eq "subject");
				next if ($key eq "match");
				next if ($in{'match'} && $key eq $match2);
				next if ($_ eq "match");
				next if ($bef eq $key);

				# 画像SUBMITボタンは無視
				next if ($key eq "x");
				next if ($key eq "y");

				my $key_name = $key;
				my $tmp = $cell;
				if ($key =~ /^clip-(\d+)$/i) {
					$key_name = "添付$1";
				}
				$tmp =~ s/\$left/$key_name/;

				my $erflg;
				foreach my $err (@err) {
					if ($err eq $key) {
						$erflg++;
						last;
					}
				}
				# 入力なし
				if ($erflg) {
					$tmp =~ s|\$right|<span style="color:$alm_col">$key_nameは入力必須です.</span>|;

				# 入力オーバー
				} elsif (defined($err{$key})) {
					$tmp =~ s|\$right|<span style="color:$alm_col">$key_nameの入力内容が大きすぎます.</span>|;

				# 正常
				} else {

					# 添付のとき
					if ($key =~ /^clip-\d+$/i) {
						$tmp =~ s/\$right/$fname{$1}/;

					# テキスト（添付以外）
					} else {

						$in{$key} =~ s/\t/<br>/g;
						$in{$key} =~ s/\0/ /g;
						$tmp =~ s/\$right/$in{$key}/;
					}
				}
				print $tmp;

				$bef = $key;
			}
		}
		if ($flg) {
			$cell .= $_;
			next;
		}

		if (/(<\/body([^>]*)>)/i) {
			$cp_flg = 1;
			$tmp = $1;
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


1;

