<?php $pass = "166kasugai";?>
<!DOCTYPE html>

<html dir="ltr" lang="ja">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no">
	<meta content="東北大学交響楽団" name="description">
	<meta content="東北,大学,学友会,交響楽,オケ,オーケストラ" name="keywords">

	<title>Tohoku University Symphony Orchestra</title>
	<link rel="shortcut icon" href="images/favicon.ico" >
	<link href="../css/bootstrap.min.css" rel="stylesheet">
	<link href="../style.css" media="screen" rel="stylesheet" type="text/css">
	<link href="../css/lightbox.css" media="screen" rel="stylesheet" type="text/css">
	<!--[if lt IE 9]>
	<script src="../js/html5.js"></script>
	<script src="../js/css3-mediaqueries.js"></script>
	<script type="text/javascript" src="http://api.html5media.info/1.1.4/html5media.min.js"></script>
	<![endif]-->
</head>

<body>
	<!-- ヘッダー -->
	<div id="header">
		<div class="fullwrapper">

			<!-- / メインナビゲーション -->
			<nav id="mainNav" class="navbar navbar-fixed-top navbar-default">
				<div class="container-fluid">

					<div class="navbar-header">
						<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span> 
						</button>
						<a class="navbar-brand" href="../index.html"><img class="logoImg" src="../images/title.png"></a>
					</div>

					<div class="collapse navbar-collapse" id="myNavbar">
						<ul class="nav navbar-nav navbar-right">
							<li>
								<a href="../news.html">ニュース<br>
									<span>News</span>
								</a>
							</li>

							<li class="dropdown">
								<a class="dropdown-toggle" data-toggle="dropdown" href="../#">演奏会<br>
									<span>Concert</span>
								</a>

								<ul class="dropdown-menu">
									<li>
										<a href="../concert.html">最新の演奏会</a>
									</li>

									<li>
										<a href="../pastconcert.html">過去の演奏会</a>
									</li>

									<li>
										<a href="../special.html">特別演奏会</a>
									</li>
								</ul>
							</li>

							<li class="dropdown">
								<a class="dropdown-toggle" data-toggle="dropdown" href="../#">紹介<br>
									<span>About</span>
								</a>

								<ul class="dropdown-menu">
									<li>
										<a href="../join.html">団員募集</a>
									</li>

									<li>
										<a href="../about.html">当団について</a>
									</li>
								</ul>
							</li>

							<li>
								<a href="../contact.html">お問い合わせ<br>
									<span>Contact</span>
								</a>
							</li>

							<li>
								<a href="../link.html">リンク<br>
									<span>Link</span>
								</a>
							</li> 
						</ul>
					</div>
				</div>
			</nav>
		</div>
	</div><!-- / ヘッダー -->

	<!-- サブ画像 -->
	<div id="banner">
		<img alt="" src="../images/image3.jpg">
		<div class="slogan">
			<h2>団員専用指定席申請ページ</h2>

			<h3>定期演奏会の指定席券を申請いただけます</h3>
		</div>
	</div><!-- / サブ画像 -->

	<div id="wrapper">
		<!-- コンテンツ -->

		<div id="member" class="container-fluid">
			<div class="row">

				<div class="col-md-3">
					<h3>指定席申し込みの流れ</h3>
					<ul id="tab-menu" class="nav nav-pills">
						<li>
							<a data-toggle="tab" href="#ticket-block">座席ブロック指定</a>
						</li>

						<li>
							<a data-toggle="tab" href="#ticket-seat">座席番号指定</a>
						</li>

						<li>
							<a data-toggle="tab" href="#ticket-confirm">確認</a>
						</li>						

						<li>
							<a data-toggle="tab" href="#ticket-form">情報入力</a>
						</li>

						<li class="active">
							<a data-toggle="tab" href="#tab-complete">申し込み完了</a>
						</li>
					</ul>
				</div>

				<div class="col-md-9">
					<article class="content">

						<div id="ticket-complete" class="tabbox tab-pane fade in active">
							<article class="container-fluid">
								<?php
								function read_csv(){
									if (($handle = fopen("asset/ticket.csv", "r")) !== false) {
										while (($line = fgetcsv($handle, 1000, ",")) !== false) {
											$records[] = $line; 
										} 
										fclose($handle);
										return $records;						
									}else{
										return false;
									}
								}

								function check_reserved($selected_seat,$records){
									foreach ($selected_seat as $selected_value) {
										$data = explode('-',$selected_value);
										foreach ($records as $record_value) {
											if ($data[0] == $record_value[0] && $data[1] == $record_value[1]) {
												$booking_error[] = $data[0].'-'.$data[1];
												break;
											}
										}
									}
									return ($booking_error) ? $booking_error : false;
								}

								function write_csv($selected_seat){
									if (($handle = fopen("asset/ticket.csv", "a")) !== false) {
										foreach ($selected_seat as $fields) {
											$data = explode('-',$fields);
											if(!fwrite($handle, $data[0].",".$data[1].",1\n")) $write_error = "Write data error";
										}
										fclose($handle); 
									}else{
										$write_error = "Open file error";
									}
									return ($write_error) ? $write_error : false;
								}

								function send_email($data){
									mb_language("ja");
									mb_internal_encoding("UTF-8");

									$to = "cleartone1216@gmail.com";
									$subject = "指定席予約メール:".$data['name'];
									$message = "お名前：".$data['name']."様\n"
									."学年:".$data['grade']."\n"
									."パート:".$data['part']."\n"
									."メールアドレス:".$data['mail']."\n\n"
									."＝＝＝指定席予約フォーム＝＝＝\n指定席の予約が完了いたしました。\nお申し込みいただいた指定席は以下の通りです。\n\n";
									$message .= "【".$data['number']."】\n";
									foreach ($data['seat'] as $value) {
										$message .= $value . "\n";
									}
									$message .= "\n以上の".strval(count($data['seat']))."枚(".strval(count($data['seat'])*1500)."円)になります。\n\n";
									$message .= "本メールの内容に心当たりのない方は、tohokuunivorchhomepage@gmail.comまでご連絡ください。\n";

									$body = mb_convert_encoding($message,'ISO-2022-JP', "auto");
									$header = "MIME-Version: 1.0\r\n"
									. "Content-Transfer-Encoding: 7bit\r\n"
									. "Content-Type: text/plain; charset=ISO-2022-JP\r\n"
									. "Message-Id: <" . md5(uniqid(microtime())) . "@tohokuuniv-orch.com>\r\n"
									. "From:".mb_encode_mimeheader($data["name"])."<ticket-form@tohokuuniv-orch.com>\r\n"
									. "Cc:".mb_encode_mimeheader($data["name"])."<".$data["mail"].">\r\n"
									. "Reply-To:".$data["mail"]."\r\n";

									ini_set("sendmail_from", $from);
									return mb_send_mail($to,$subject,$body,$header, "-f ".$data["mail"]);
								}
								?>

								<?php if (htmlspecialchars($_POST['password']) == $pass):?>

									<?php 
									//実行フェーズ
									$mail_error = false;
									$records = read_csv();
									if(!$records){
										$application_error['read'] = "Can't read File";
									} else {
										$booking_error = check_reserved($_POST['seat'], $records);

										if ($booking_error) {
											$application_error['check'] = "選択いただいた座席の中に，既に他の方が予約したものがあります。<br>該当する座席番号：";
											foreach ($booking_error as $value) {
												$application_error['check'] .= "「".$value."」";
											}
										} else {
											$write_error = write_csv($_POST['seat']);

											if ($write_error) {
												$application_error['write'] = "Can't write File";
											} else {
												$mail_error = send_email($_POST);
											//$mail_error = true;
												if (!$mail_error) {
													$application_error['mail'] = "Can't send Email";
												}
											}
										}
									}
									?>

									<?php if($application_error):?>
										<h3>お申し込みエラー</h3>
										<div>
											指定席のお申し込み中にエラーが発生いたしました。<br>
											お手数をおかけしますが、下記リンクより再度アクセスして申請を行ってください。<br>
											※何度もこのエラーが表示される場合は，表示されるエラーメッセージと共に担当者へご報告願います。
											<ul class="error_messages">
												<?php foreach ($application_error as $key => $value) {
													echo "<li>";
													echo "<p class='application_error'>" . $key . " Error!!" . "</p>";
													echo $value;
													echo "</li>";
												}?>
											</ul>
										</div>
									<?php else:?>
										<h3>お申し込み完了</h3>
										<div>
											指定席のお申し込みが完了いたしました。<br>
											入力いただいたアドレスに完了メールを送信いたしましたのでご確認ください。<br>
											※届いていない場合は迷惑メールに分類されている可能性がございますので、そちらもご確認ください。
										</div>
									<?php endif;?>

								<?php else:?>
									<h3>お申し込みエラー</h3>
									<div>
										パスワードの認証に失敗しました。再度ご確認の上、お申込みください。
									</div>
								<?php endif;?>
								<div>
									<ul class="link-buttons">
										<li><a class="btn btn-info" href="member.html" title="">団員専用ページトップ</a></li>
									</ul>
								</div>

							</article>
						</div>
					</article>
				</div>

			</div>
		</div><!-- / コンテンツ -->

		<div id="page-up">
			<a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
		</div>
	</div><!-- / WRAPPER -->

	<!-- フッター -->
	<div id="footer">
		<div class="inner">
			<!-- 3カラム -->

			<section id="footer-grid">
				<div class="row">
					<div class="col-md-3">
						<!-- ロゴ -->
						<p class="logo">
							<a href="../index.html"><img class="logoImg" src="../images/logo.png"><br>
								<span>東北大学交響楽団</span>
							</a>
						</p><!-- / ロゴ -->
					</div>

					<div class="col-md-6">
						<ul class="list-inline text-a-c">
							<li>
								<a href="../sitemap.html">サイトマップ</a>
							</li>

							<li>
								<a href="../privacypolicy.html">プライバシーポリシー</a>
							</li>

							<li>
								<a href="../idemnity.html">免責事項</a>
							</li>

							<li>
								<a href="member.html">団員専用ページ</a>
							</li>
						</ul>
					</div>

					<div class="col-md-3 text-a-r">
						<!-- 電話番号+受付時間 -->

						<p><a href="http://validator.w3.org/check?uri=referer"><img alt="Valid XHTML 1.0 Transitional" height="31" src="http://www.w3.org/Icons/valid-xhtml10" width="88"></a> <a href="http://jigsaw.w3.org/css-validator/"><img alt="Valid CSS!" src="http://jigsaw.w3.org/css-validator/images/vcss" style="border:0;width:88px;height:31px"></a></p>

						<p></p>
					</div>
				</div>
			</section><!-- / 3カラム -->
		</div>

		<div class="copyright">
			(C) Copyright 東北大学交響楽団／東北大学学友会交響楽部　2015 All rights reserved.
		</div>
	</div><!-- / フッター -->
	<script src="../js/jquery-1.11.2.min.js"></script>
	<script src="../js/bootstrap.min.js"></script> 
	<script src="../js/script.js"></script> 
	<script src="../js/jquery.cookie.js"></script>
	<script src="../js/lightbox.js"></script>
</body>
</html>