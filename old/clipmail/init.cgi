#┌─────────────────────────────────
#│ Clip MAIL v1.0
#│ init.cgi - 2007/07/26
#│ copyright (c) KentWeb
#│ webmaster@kent-web.com
#│ http://www.kent-web.com/
#└─────────────────────────────────
$ver = 'Clip MAIL v1.0';
#┌─────────────────────────────────
#│ [注意事項]
#│ 1. このスクリプトはフリーソフトです。このスクリプトを使用した
#│    いかなる損害に対して作者は一切の責任を負いません。
#│ 2. 送信フォームのHTMLページの作成に関しては、HTML文法の範疇
#│    となるため、サポート対象外となります。
#│ 3. 設置に関する質問はサポート掲示板にお願いいたします。
#│    直接メールによる質問はお受けいたしておりません。
#└─────────────────────────────────
#
# [ 送信フォーム (HTML) の記述例 ]
#
# ・タグの記述例 (1)
#   おなまえ <input type="text" name="name" size="25">
#   → このフォームに「山田太郎」と入力して送信すると、
#      「name = 山田太郎」という形式で受信します
#
# ・タグの記述例 (2)
#   お好きな色 <input type="radio" name="color" value="青">
#   → このラジオボックスにチェックして送信すると、
#      「color = 青」という形式で受信します
#
# ・タグの記述例 (3)
#   E-mail <input type="text" name="email" size="25">
#   → name値に「email」という文字を使うとこれはメールアドレス
#      と認識し、アドレスの書式を簡易チェックします
#   → (○) abc@xxx.co.jp
#   → (×) abc.xxx.co.jp → 入力エラーとなります
#
# ・タグの記述例 (4)
#   E-mail <input type="text" name="_email" size="25">
#   → name値の先頭に「アンダーバー 」を付けると、その入力値は
#     「入力必須」となります。
#      上記の例では、「メールアドレスは入力必須」となります。
#
# ・name値への「全角文字」の使用は可能です
#  (例) <input type="radio" name="年齢" value="20歳代">
#  → 上記のラジオボックスにチェックを入れて送信すると、
#     「年齢 = 20歳代」という書式で受け取ることができます。
#
# ・name値を「name」とするとこれを「送信者名」と認識して送信元の
#   メールアドレスを「送信者 <メールアドレス>」というフォーマットに
#   自動変換します。
#  (フォーム記述例)  <input type="text" name="name">
#  (送信元アドレス)  太郎 <taro@email.xx.jp>
#
# ・タグの記述例 (5)
#   ＜添付メール許可の場合＞
#   <input type="file" name="clip-1" size="40">
#   → name値を「clip-」+「数字」にしてください。
#   → 「数字」を変えることで、参照用フィールドを複数用意することが
#      できます。
#
# ・コマンドタグ (1)
#   → 入力必須項目を強制指定する（半角スペースで複数指定可）
#   → ラジオボタン、チェックボックス対策
#   → name値を「need」、value値を「必須項目1 + 半角スペース +必須項目2 + 半角スペース ...」
#   (例) <input type="hidden" name="need" value="名前 メールアドレス 性別">
#
# ・コマンドタグ (2)
#   → 2つの入力内容が同一かをチェックする
#   → name値を「match」、value値を「項目1 + 半角スペース + 項目2」
#   (例) <input type="hidden" name="match" value="email email2">
#
# ・コマンドタグ (3)
#   → メール件名を指定する
#   → この場合、設定で指定する $subject より優先されます。
#   (例) <input type="hidden" name="subject" value="メールタイトル○○">
#
#  [ 簡易チェック ]
#   http://～～/clipmail.cgi?mode=check
#
#  [ 設置例 ]
#
#  public_html / index.html (トップページ等）
#       |
#       +-- postmail / clipmail.cgi   [705]
#             |        admin.cgi      [705] ... 管理画面
#             |        init.cgi       [604] ... 設定ファイル
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
#  ▼基本設定
#===========================================================

# 外部ファイル
$jcodepl = './lib/jcode.pl';
$mimewpl = './lib/mimew.pl';
$checkpl = './lib/check.pl';
$prevwpl = './lib/preview.pl';
$sendmpl = './lib/sendmail.pl';
$erchkpl = './lib/errcheck.pl';

# 送信先メールアドレス
$mailto = 'tohokuuniv@tohokuuniv-orch.com';

# 添付メールを許可する
# 0 : no
# 1 : yes
$attach = 0;

# 添付メール許可のとき添付ファイルの「拡張子」を指定する場合
# → 例 (ドットなしで記述) : @pmt_ext = ('gif', 'jpg', 'jpeg', 'png');
# → すべての拡張子をOKにするときは、@pmt_ext = (); とします
@pmt_ext = ('gif', 'jpg', 'jpeg', 'png', 'bmp');

# 画像プレビューの時の表示サイズ
# → 画像はGIF/JPEG/PNG/BMPのみ
# → 順に横幅、縦幅
$img_max_w = 200;
$img_max_h = 150;

# 入力フィールドあたりの最大容量（バイト）
# ＊参考 : 全角1文字 = 2バイト
$max_field = 300;

# 最大受信サイズ
# → 例 : 102400 = 100KB
$maxdata = 1024000;

# 自動返信
# 0 : no
# 1 : yes
$auto_res = 0;

# ログ蓄積の最大保存数
# → 0 にすると機能無効
$keep_log = 200;

# HTMLタグの処理
# → < > " & ' の処理
# 1 : 完全復元
# 2 : 全角に変換（セキュリティ上おすすめ）
$html_tag = 2;

# メールタイトル
$subject = 'Webからのお問い合わせ';

# 本体プログラム【URLパス】
$script = './clipmail.cgi';

# 管理プログラム【URLパス】
$admincgi = './admin.cgi';

# ログファイル【サーバパス】
$logfile = './data/log.cgi';

# パスワードファイル【サーバパス】
$pwdfile = './data/pwd.cgi';

# 一時ディレクトリ【URLパス】
$tmpurl = './temp';

# 一時ディレクトリ【サーバパス】
$tmpdir = './temp';

# 確認画面テンプレート【サーバパス】
$tmpl_conf = './tmpl/conf.html';

# 一般エラー画面テンプレート【サーバパス】
$tmpl_err1 = './tmpl/err1.html';

# 入力エラー画面テンプレート【サーバパス】
$tmpl_err2 = './tmpl/err2.html';

# 送信後画面テンプレート【サーバパス】
$tmpl_thx = './tmpl/thx.html';

# 送信用メッセージテンプレート【サーバパス】
$tmpl_body = './tmpl/body.txt';

# 返信用メッセージテンプレート【サーバパス】
$tmpl_bres = './tmpl/body_res.txt';

# 送信後の形態
# 0 : 完了メッセージを出す.
# 1 : 戻り先 ($back) へ自動ジャンプさせる.
$reload = 0;

# 送信後の戻り先【URLパス】
# → http://から記述する
$back = 'http://www.tohokuuniv-orch.com/clipmail/clipmail.html';

# 送信は method=POST 限定 (0=no 1=yes)
# → セキュリティ対策
$postonly = 1;

# アラーム色
$alm_col = "#dd0000";

# ホスト取得方法
# 0 : gethostbyaddr関数を使わない
# 1 : gethostbyaddr関数を使う
$gethostbyaddr = 0;

# アクセス制限（複数あれば半角スペースで区切る、アスタリスク可）
# → 拒否ホスト名又はIPアドレスの記述例
#   （前方一致は先頭に ^ をつける）【例】^210.12.345.*
#   （後方一致は末尾に $ をつける）【例】*.anonymizer.com$
$denyhost = '';

# 禁止ワード
# → 投稿時禁止するワードをコンマで区切る
$no_wd = '';

# メール送信形式
# 1 : sendmail送信（sendmailが利用可能なサーバ）
# 2 : IO:Socketモジュール送信（ソケット関連のモジュールが利用可能なサーバ）
$send_type = 1;

## sendmail送信のとき ##
# sendmailのパス
$sendmail = '/usr/sbin/sendmail';

##【注】sendmail送信の方は設定はここまでで終了。これより下は設定不要です。

## IO:Socketモジュール送信のとき ##
# io-socket.plのパス
$io_socket = './lib/io-socket.pl';

# SMTPサーバ
$server = "mail.server.xx.jp";

# SMTPポート番号（通常は25）
$port = 25;

# POP before SMTPを使用する
# 0 : no
# 1 : yes
$pop_bef_smtp = 0;

# POP3サーバ【POP before SMTPのとき】
$pop3sv = 'mail.server.xx.jp';

# POP3ポート番号（通常は110）【POP before SMTPのとき】
$pop3port = 110;

# 接続ID【POP before SMTPのとき】
$user = 'user_id';

# 接続パスワード【POP before SMTPのとき】
$pass = 'password';

## ↑SMTPサーバへの接続情報ここまで

#===========================================================
#  ▲設定完了
#===========================================================

#-------------------------------------------------
#  フォームデコード
#-------------------------------------------------
sub parse_form {
	# 各変数初期化
	undef(%in);
	undef(%fname);
	undef(%uplno);
	undef(%ctype);
	undef(%err);
	undef(@key);
	undef(@need);
	undef(@err);
	($macbin, $post_flg, $upl_flg, $max_flg, $check) = (0, 0, 0, 0, 0);

	# 最大容量チェック
	my $conlen = $ENV{'CONTENT_LENGTH'};
	if ($conlen > $maxdata) {
		my $maxd = int( $maxdata / 1024 ) . "KB";
		&error("容量サイズオーバーです : $maxdまで");
	}

	# マルチパートフォームのとき
	if ($ENV{'CONTENT_TYPE'} =~ m|multipart/form-data|i) {
		$post_flg = 1;

		# 変数初期化
		my ($key, $val, $uplno);

		# 標準入力をバイナリモード宣言
		binmode(STDIN);

		# 先頭のboundaryを認識
		my $bound = <STDIN>;
		$bound =~ s/\r\n//;

		# 標準入力を展開
		while (<STDIN>) {

			# マックバイナリ認識
			if (m|application/x-macbinary|i) { $macbin = 1; }

			# Content-Disposition認識
			if (/^Content-Disposition:/i) {
				$flg = 1;
			}

			# name属性認識
			if ($flg == 1 && /\s+name="([^";]+)"/i) {
				$key = $1;

				if ($key =~ /^_?clip-(\d+)$/i) {
					$upl_flg++;
					$uplno = $1;
					$uplno{$uplno} = $uplno;
				}
			}

			# filename属性認識（ファイルアップ）
			if ($uplno && /\s+filename="([^";]+)"/i) {

				# 添付拒否のとき
				if (!$attach) { &error("添付メールは許可されていません"); }

				my $fnam = $1;
				&jcode::convert(\$fnam, 'sjis');
				$fname{$uplno} = $fnam;

				# 拡張子チェック
				if (@pmt_ext > 0) {
					my $flg;
					foreach my $ext (@pmt_ext) {
						if ($fname{$uplno} =~ /\.$ext$/i) { $flg++; last; }
					}
					if (!$flg) {
						&error("許可されていない添付ファイルです : $fname{$uplno}");
					}
				}
			}

			# Content-Type認識（ファイルアップ）
			if ($uplno && /Content-Type:\s*([^";]+)/i) {
				my $ctype = $1;
				$ctype =~ s/\r//g;
				$ctype =~ s/\n//g;

				$ctype{$uplno} = $ctype;
			}

			# ヘッダ → 本文
			if ($flg == 1 && /^\r\n/) {
				$flg = 2;
				next;
			}
			# 本文認識
			if ($flg == 2) {

				# boundary検出 → フィールド終了
				if (/^$bound/) {

					# 末尾の改行をカット
					$val =~ s/\r\n$//;

					# テキスト系処理
					if (!$uplno) {

						# S-JISコード変換
						&jcode::convert(\$key, 'sjis');
						&jcode::convert(\$val, 'sjis');

						# エスケープ
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

						# 各項目サイズをチェック
						if (length($key) > $max_field || length($val) > $max_field) {
							$max_flg = 1;
							$err{$key} = $val;
						}
					}

					# 必須入力項目を認識＆チェック
					if ($key =~ /^_(.+)/) {
						$key = $1;
						push(@need,$key);

						if ($val eq "") { $check++; push(@err,$key); }
					}

					# %in定義
					$in{$key} .= "\0" if (defined($in{$key}));
					$in{$key} .= $val;

					# キーは配列化しておく
					push(@key,$key);

					# フラグを初期化
					$flg = $uplno = $key = $val = '';
					next;
				}
				# boundary検出まで本文を覚えておく
				$val .= $_;
			}
		}
		# 返り値
		$conlen;

	# マルチパートフォーム以外のとき
	} else {

		# データ受取
		my $buf;
		if ($ENV{'REQUEST_METHOD'} eq "POST") {
			$post_flg = 1;
			read(STDIN, $buf, $ENV{'CONTENT_LENGTH'});
		} else {
			$buf = $ENV{'QUERY_STRING'};
		}

		# URLデコード
		foreach ( split(/&/, $buf) ) {
			my ($key, $val) = split(/=/);
			$key =~ tr/+/ /;
			$key =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;
			$val =~ tr/+/ /;
			$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;

			# S-JISコード変換
			&jcode::convert(\$key, 'sjis');
			&jcode::convert(\$val, 'sjis');

			# エスケープ
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

			# 各項目サイズをチェック
			if (length($key) > $max_field || length($val) > $max_field) {
				$max_flg = 1;
				$err{$key} = $val;
			}

			# 必須入力項目を認識＆チェック
			if ($key =~ /^_(.+)/) {
				$key = $1;
				push(@need,$key);

				if ($val eq "") { $check++; push(@err,$key); }
			}

			# %in定義
			$in{$key} .= "\0" if (defined($in{$key}));
			$in{$key} .= $val;

			# キーは配列化しておく
			push(@key,$key);
		}
		# 返り値
		if ($buf) { return 1; } else { return 0; }
	}
}


1;

