#!/usr/bin/perl

#┌────────────────────────
#│ PasswordManager v2
#│ pwlog.cgi (SSI用) - 2006/02/26
#│ Copyright (c) KentWeb
#│ http://www.kent-web.com/
#└────────────────────────
# 【使い方】ログイン後のHTMLページに以下のSSIタグを記述
#  <!--#exec cgi="/フルパス/pwlog.cgi"-->
#
# 【利用条件】
#  1. SSIの利用できるサーバ
#  2. 環境変数 $ENV{'REMOTE_USER'} にてユーザーIDが取得できること
#  ※ 2. については、同梱の pwlog_test.cgi にてテストすること

# 外部ファイル取込
require './init.cgi';

# ホスト名を取得
&get_host;

# 時間取得
$date = &get_time;

# ロック開始
&lock if ($lockkey);

# ログファイルの読み込み
open(IN,"$axsfile") || &error("Open Error: $axsfile");
@data = <IN>;
close(IN);

# ブラウザ情報
$agent = $ENV{'HTTP_USER_AGENT'};
$agent =~ s/&/&amp;/g;
$agent =~ s/</&lt;/g;
$agent =~ s/>/&gt;/g;
$agent =~ s/"/&quot;/g;

# ログ調整
while ($log_max <= @data) { pop(@data); }
unshift(@data,"$ENV{'REMOTE_USER'}<>$date<>$host<>$agent<>\n");

# 更新
open(OUT,">$axsfile") || &error("Write Error: $axsfile");
print OUT @data;
close(OUT);

# ロック解除
&unlock if ($lockkey);

#---------------------------------------
#  エラー
#---------------------------------------
sub error {
	if ($lockflag) { &unlock; }

	die "$_[0] : $!";
}

__END__

# ダミーGIF画像
@gif = (
	"47","49","46","38","39","61","02","00","02","00","80","00",
	"00","00","00","00","ff","ff","ff","21","f9","04","01","00",
	"00","01","00","2c","00","00","00","00","02","00","02","00",
	"00","02","02","8c","53","00","3b",
	);

# ダミー画像を表示
print "Content-type: image/gif\n\n";
foreach (@gif) {
	print pack('C*', hex($_));
}

