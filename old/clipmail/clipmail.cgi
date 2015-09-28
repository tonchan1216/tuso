#!/usr/bin/perl

#┌─────────────────────────────────
#│ Clip Mail
#│ clipmail.cgi - 2007/05/26
#│ copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────

# 外部ファイル取り込み
require './init.cgi';
require $jcodepl;

# フォームデコード
&parse_form || &error("不明な処理です");

# チェックモード
if ($in{'mode'} eq "check") {
	require $checkpl;
	&check;
}

# POSTチェック
if ($postonly && !$post_flg) { &error("不正なアクセスです"); }

# 件名汚染チェック
if ($in{'subject'}) { $subject = &sub_check; }

# 著作権表記（削除不可）
$copy = <<EOM;
<br />
<div align="center" style="font-size:10px; font-family:Verdana,Helvetica,Arial;">
- <a href="http://www.kent-web.com/" target="_top">ClipMail</a> -
</div>
EOM

# 禁止ワード
if ($no_wd) {
	my $flg;
	foreach (@key) {
		foreach my $nowd ( split(/,/, $no_wd) ) {
			if (index($in{$_},$nowd) >= 0) {
				$flg = 1;
				last;
			}
		}
		if ($flg) { &error("禁止ワードが含まれています"); }
	}
}

# ホスト取得＆チェック
&get_host;

# 必須入力チェック
if ($in{'need'}) {
	# needフィールドの値を必須配列に加える
	my @tmp = split(/\s+/, $in{'need'});
	push(@need,@tmp);

	# 必須配列の重複要素を排除する
	my (@uniq, %seen);
	foreach (@need) {
		push(@uniq,$_) unless $seen{$_}++;
	}

	# 必須項目の入力値をチェックする
	foreach (@uniq) {

		# フィールドの値が投げられてこないもの（ラジオボタン等）
		if (!defined($in{$_})) {
			$check++;
			push(@key,$_);
			push(@err,$_);

		# 入力なしの場合
		} elsif ($in{$_} eq "") {
			$check++;
			push(@err,$_);
		}
	}
}

# 入力内容マッチ
local($match1, $match2);
if ($in{'match'}) {
	($match1, $match2) = split(/\s+/, $in{'match'}, 2);

	if ($in{$match1} ne $in{$match2}) {
		&error("$match1と$match2の再入力内容が異なります");
	}
}

# 入力チェック確認画面
if ($check || $max_flg) {
	require $erchkpl;
	&err_check;
}

# E-mail書式チェック
if ($in{'email'} =~ /\,/) {
	&error("メールアドレスにコンマ ( , ) が含まれています");
}
if ($in{'email'} && $in{'email'} !~ /^[\w\.\-]+\@[\w\.\-]+\.[a-zA-Z]{2,6}$/) {
	&error("メールアドレスの書式が不正です");
}

# プレビュー
if ($in{'mode'} ne "send") {
	require $prevwpl;
	&preview;

# 送信実行
} else {
	require $sendmpl;
	require $mimewpl;
	&send_mail;
}

#-------------------------------------------------
#  エラー処理
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
#  時間取得
#-------------------------------------------------
sub get_time {
	$ENV{'TZ'} = "JST-9";
	my ($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(time);
	my @week  = qw|Sun Mon Tue Wed Thu Fri Sat|;
	my @month = qw|Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec|;

	# 日時のフォーマット
	my $date1 = sprintf("%04d/%02d/%02d(%s) %02d:%02d:%02d",
			$year+1900,$mon+1,$mday,$week[$wday],$hour,$min,$sec);
	my $date2 = sprintf("%s, %02d %s %04d %02d:%02d:%02d",
			$week[$wday],$mday,$month[$mon],$year+1900,$hour,$min,$sec) . " +0900";

	return ($date1, $date2);
}

#-------------------------------------------------
#  ホスト名取得
#-------------------------------------------------
sub get_host {
	# ホスト名取得
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};

	if ($gethostbyaddr && ($host eq "" || $host eq $addr)) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
	}
	if ($host eq "") { $host = $addr; }

	# チェック
	if ($denyhost) {
		my $flg;
		foreach ( split(/\s+/, $denyhost) ) {
			s/\./\\\./g;
			s/\*/\.\*/g;

			if ($host =~ /$_/i) { $flg = 1; last; }
		}
		if ($flg) { &error("アクセスを許可されていません"); }
	}
}

#-------------------------------------------------
#  件名汚染チェック
#-------------------------------------------------
sub sub_check {
	my $sub = $in{'subject'};
	&jcode::convert(\$sub, 'euc', 'sjis');

	$sub =~ s/\r//g;
	$sub =~ s/\n//g;
	$sub =~ s/\@/＠/g;
	$sub =~ s/\./．/g;
	$sub =~ s/\+/＋/g;
	$sub =~ s/\-/－/g;
	$sub =~ s/\:/：/g;
	$sub =~ s/\;/；/g;
	$sub =~ s/\|/｜/g;

	&jcode::convert(\$sub, 'sjis', 'euc');
	return $sub;
}

