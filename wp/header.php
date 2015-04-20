<!DOCTYPE html>

<html dir="ltr" lang="ja">
<head>
  <meta charset="UTF-8">
  <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
  <meta content="東北大学交響楽団" name="description">
  <meta content="東北,大学,学友会,交響楽,オケ,オーケストラ" name="keywords">

  <title>Tohoku University Symphony Orchestra</title>
  <link href="<?php echo get_template_directory_uri(); ?>/style.css" media="screen" rel="stylesheet" type="text/css">
  <link href="<?php echo get_template_directory_uri(); ?>/css/jquery.bxslider.css" rel="stylesheet" type="text/css"><!--[if lt IE 9]>
  <script src="<?php echo get_template_directory_uri(); ?>js/html5.js"></script>
  <script src="<?php echo get_template_directory_uri(); ?>js/css3-mediaqueries.js"></script>
  <![endif]-->
  <?php wp_footer(); ?>

</head>

<body>
  <!-- ヘッダー -->

  <div id="header">
    <div class="fullwrapper">

      <!-- ロゴ -->
      <div class="logo">
        <a href="<?php bloginfo('url'); ?>"><img class="logoImg" src="<?php echo get_template_directory_uri(); ?>/images/logo.png"><img src="<?php echo get_template_directory_uri(); ?>/images/title.png"></a>
      </div><!-- / ロゴ -->

      <!-- メインナビゲーション -->
      <nav id="mainNav">
        <a class="menu" id="menu"><span>MENU</span></a>

        <div class="panel">
          <ul>
            <li>
              <a href="<?php bloginfo('url'); ?>/news">ニュース<br>
              <span>News</span></a>
            </li>

            <li>
              <a href="<?php bloginfo('url'); ?>/concert">最新の演奏会<br>
              <span>Concert</span></a>
            </li>

            <li>
              <a href="<?php bloginfo('url'); ?>/pastconcert">過去の演奏会<br>
              <span>Past Concert</span></a>
            </li>

            <li>
              <a href="<?php bloginfo('url'); ?>/join">団員募集<br>
              <span>Joinus</span></a>
            </li>

            <li>
              <a href="<?php bloginfo('url'); ?>/about">当団について<br>
              <span>About</span></a>
            </li>

            <li>
              <a href="<?php bloginfo('url'); ?>/contact">お問い合わせ<br>
              <span>Contact</span></a>
            </li>

            <li>
              <a href="<?php bloginfo('url'); ?>/link">リンク<br>
              <span>Link</span></a>
            </li>
          </ul>
        </div>
      </nav><!-- メインナビゲーション -->
    </div>
  </div><!-- / ヘッダー -->
