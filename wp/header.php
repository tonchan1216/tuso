<!DOCTYPE html>

<html dir="ltr" lang="ja">
<head>
	<meta charset="UTF-8">
	<meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
	<meta content="<?php bloginfo('description'); ?>" name="description">
	<meta content="東北,大学,学友会,交響楽,オケ,オーケストラ" name="keywords">

	<title><?php bloginfo('name'); ?></title>
	<link rel="shortcut icon" href="<?php echo get_template_directory_uri(); ?>/images/logo-1.png" >
	<link href="<?php echo get_template_directory_uri(); ?>/css/bootstrap.min.css" rel="stylesheet">
	<link href="<?php echo get_template_directory_uri(); ?>/style.css" media="screen" rel="stylesheet" type="text/css">
	<!--[if lt IE 9]>
	<script src="<?php echo get_template_directory_uri(); ?>/js/html5.js"></script>
	<script src="<?php echo get_template_directory_uri(); ?>/js/css3-mediaqueries.js"></script>
	<![endif]-->

	<?php wp_head();?>
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
						<a class="navbar-brand" href="<?php echo home_url();?>"><img class="logoImg" src="<?php echo get_template_directory_uri(); ?>/images/title.png" alt="東北大学交響楽団"></a>
					</div>

					<div class="collapse navbar-collapse" id="myNavbar">
						<ul class="nav navbar-nav navbar-right">
							<li>
								<a href="<?php echo home_url('/news/');?>">ニュース<br>
									<span>News</span>
								</a>
							</li>

							<li class="dropdown">
								<a class="dropdown-toggle" data-toggle="dropdown" href="#">演奏会<br>
									<span>Concert</span>
								</a>

								<ul class="dropdown-menu">
									<li>
										<a href="<?php echo home_url('/concert/');?>">最新の演奏会</a>
									</li>

									<li>
										<a href="<?php echo home_url('/pastconcert/');?>">過去の演奏会</a>
									</li>

									<li>
										<a href="<?php echo home_url('/special/');?>">特別演奏会</a>
									</li>
								</ul>
							</li>

							<li class="dropdown">
								<a class="dropdown-toggle" data-toggle="dropdown" href="#">紹介<br>
									<span>About</span>
								</a>

								<ul class="dropdown-menu">
									<li>
										<a href="<?php echo home_url('/join/');?>">団員募集</a>
									</li>

									<li>
										<a href="<?php echo home_url('/about/');?>">当団について</a>
									</li>
								</ul>
							</li>

							<li>
								<a href="<?php echo home_url('/contact/');?>">お問い合わせ<br>
									<span>Contact</span>
								</a>
							</li>

							<li>
								<a href="<?php echo home_url('/link/');?>">リンク<br>
									<span>Link</span>
								</a>
							</li>
						</ul>
					</div>
				</div>
			</nav>
		</div>
	</div><!-- / ヘッダー -->