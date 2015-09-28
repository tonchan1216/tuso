#┌─────────────────────────────────
#│ ClipMail
#│ sendmail.pl - 2007/05/23
#│ copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────

#-------------------------------------------------
#  送信実行
#-------------------------------------------------
sub send_mail {
	# 時間取得
	my ($date1, $date2) = &get_time;

	# ブラウザ情報
	my $agent = $ENV{'HTTP_USER_AGENT'};
	$agent =~ s/<//g;
	$agent =~ s/>//g;
	$agent =~ s/"//g;
	$agent =~ s/&//g;
	$agent =~ s/'//g;

	# 本文テンプレ読み込み
	my $tbody;
	open(IN,"$tmpl_body");
	while (<IN>) {
		s/\r\n/\n/;
		s/\r/\n/g;

		$tbody .= $_;
	}
	close(IN);

	# テンプレ変数変換
	$tbody =~ s/\$date/$date1/g;
	$tbody =~ s/\$agent/$agent/g;
	$tbody =~ s/\$host/$host/g;
	&jcode::convert(\$tbody, 'jis');

	# 自動返信ありのとき
	my $resbody;
	if ($auto_res) {

		# テンプレ
		open(IN,"$tmpl_bres");
		while (<IN>) {
			s/\r\n/\n/;
			s/\r/\n/g;

			$resbody .= $_;
		}
		close(IN);

		# 変数変換
		$resbody =~ s/\$date/$date1/g;
		$resbody =~ s/\$agent/$agent/g;
		$resbody =~ s/\$host/$host/g;

		# コード変換
		&jcode::convert(\$resbody, 'jis');
	}

	# ログファイルオープン
	open(DAT,"+< $logfile");
	eval "flock(DAT, 2);";

	# 先頭行を分解
	my $top_log = <DAT>;
	my ($log_date, $log_ip, $log_data) = split(/<>/, $top_log, 3);

	# ハッシュ%logに各項目を代入
	my %log;
	foreach ( split(/<>/, $log_data) ) {
		my ($key,$val) = split(/=/, $_, 2);
		$log{$key} = $val;
	}

	# 本文のキーを展開
	my ($bef, $mbody, $log, $flg, @ext);
	foreach (@key) {
		# 本文に含めない部分を排除
		next if ($_ eq "mode");
		next if ($_ eq "need");
		next if ($_ eq "match");
		next if ($_ eq "subject");
		next if ($in{'match'} && $_ eq $match2);
		next if ($bef eq $_);

		# 添付
		my $upl;
		if (/^clip-(\d+)$/i) {
			my $no = $1;
			if ($in{"clip-$no"}) { push(@ext,$no); }

			# ログ蓄積
			my ($upl_file) = (split(/:/, $in{"clip-$no"}))[0];
			$log .= "$_=$upl_file<>";
			my $tmp = "添付$no = $upl_file\n";
			&jcode::convert(\$tmp, 'jis', 'sjis');
			$mbody .= $tmp;

			# 内容を二重送信チェック
			if ($upl_file ne $log{$_}) {
				$flg++;
			}
			next;
		}

		# 内容を二重送信チェック
		if ($in{$_} ne $log{$_}) {
			$flg++;
		}

		# エスケープ
		$in{$_} =~ s/\0/ /g;
		$in{$_} =~ s/\.\n/\. \n/g;

		# 添付ファイル風の文字列拒否
		$in{$_} =~ s/Content-Disposition:\s*attachment;.*//ig;
		$in{$_} =~ s/Content-Transfer-Encoding:.*//ig;
		$in{$_} =~ s/Content-Type:\s*multipart\/mixed;\s*boundary=.*//ig;

		# ログ蓄積
		$log .= "$_=$in{$_}<>";

		# 改行復元
		$in{$_} =~ s/\t/\n/g;

		# HTMLタグ変換
		if ($html_tag == 1) {
			$in{$_} =~ s/&lt;/</g;
			$in{$_} =~ s/&gt;/>/g;
			$in{$_} =~ s/&quot;/"/g;
			$in{$_} =~ s/&#39;/'/g;
			$in{$_} =~ s/&amp;/&/g;
		} else {
			$in{$_} =~ s/&lt;/＜/g;
			$in{$_} =~ s/&gt;/＞/g;
			$in{$_} =~ s/&quot;/”/g;
			$in{$_} =~ s/&#39;/’/g;
			$in{$_} =~ s/&amp;/＆/g;
		}

		# 本文内容
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
		&error("二重送信のため処理を中止しました");
	}

	# ログ保存
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

	# 本文テンプレ内の変数を置き換え
	$tbody =~ s/\$message/$mbody/;

	# 返信テンプレ内の変数を置き換え
	$resbody =~ s/\$message/$mbody/ if ($auto_res);

	# メールアドレスがない場合は送信先に置き換え
	my $email;
	if ($in{'email'} eq "") {
		$email = $mailto;
	} else {
		$email = $in{'email'};
	}

	# MIMEエンコード
	my $subject2 = &mimeencode($subject);
	if ($in{'name'}) {
		$in{'name'} =~ s/\n//g;
		$from = &mimeencode("\"$in{'name'}\" <$email>");
	} else {
		$from = $email;
	}

	# 区切り線
	my $cut = "------_" . time . "_MULTIPART_MIXED_";

	# --- 送信内容フォーマット開始
	# ヘッダー
	my $body = "To: $mailto\n";
	$body .= "From: $from\n";
	if ($cc_mail && $email) { $body .= "Cc: $email\n"; }
	$body .= "Subject: $subject\n";
	$body .= "MIME-Version: 1.0\n";
	$body .= "Date: $date2\n";

	# 添付ありのとき
	if (@ext > 0) {
		$body .= "Content-Type: multipart/mixed; boundary=\"$cut\"\n";
	} else {
		$body .= "Content-type: text/plain; charset=iso-2022-jp\n";
	}

	$body .= "Content-Transfer-Encoding: 7bit\n";
	$body .= "X-Mailer: $ver\n\n";

	# 本文
	if (@ext > 0) {
		$body .= "--$cut\n";
		$body .= "Content-type: text/plain; charset=iso-2022-jp\n";
		$body .= "Content-Transfer-Encoding: 7bit\n\n";
	}
	$body .= "$tbody\n";

	# 返信内容フォーマット
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

	# 添付あり
	if (@ext > 0) {
		foreach my $i (@ext) {

			# ファイル名と一時ファイル名に分割
			my ($fname, $tmpfile) = split(/:/, $in{"clip-$i"}, 2);

			# ファイル名汚染チェック
			next if ($tmpfile !~ /^\d+\-$i\.\w+$/);

			# 一時ファイル名が存在しないときはスキップ
			next if (! -f "$tmpdir/$tmpfile");

			$fname = &mimeencode($fname);

			# 添付ファイルを定義
			$body .= qq|--$cut\n|;
			$body .= qq|Content-Type: application/octet-stream; name="$fname"\n|;
			$body .= qq|Content-Disposition: attachment; filename="$fname"\n|;
			$body .= qq|Content-Transfer-Encoding: Base64\n\n|;

			# 一時ファイルをBase64変換
			open(IN,"$tmpdir/$tmpfile");
			binmode(IN);
			while (<IN>) {
				$body .= &bodyencode($_, "b64");
			}
			$body .= &benflush("b64");
			close(IN);

			# 一時ファイル削除
			unlink("$tmpdir/$tmpfile");
		}
		$body .= "--$cut--\n";
	}

	# IO:Socketモジュール送信の場合
	if ($send_type == 2) {
		require $io_socket;

		# 本文送信
		&sendmail($email, $mailto, $body);

		# 返信送信
		&sendmail($mailto, $email, $res_body) if ($auto_res);

	# sendmail送信の場合
	} else {

		# 本文送信
		open(MAIL,"| $sendmail -t -i") || &error("メール送信失敗");
		print MAIL "$body\n";
		close(MAIL);

		# 返信送信
		if ($auto_res) {
			open(MAIL,"| $sendmail -t -i") || &error("メール送信失敗");
			print MAIL "$res_body\n";
			close(MAIL);
		}
	}

	# リロード
	if ($reload) {
		if ($ENV{'PERLXS'} eq "PerlIS") {
			print "HTTP/1.0 302 Temporary Redirection\r\n";
			print "Content-type: text/html\n";
		}
		print "Location: $back\n\n";
		exit;

	# 完了メッセージ
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

