<!DOCTYPE html>

<html dir="ltr" lang="ja">
<head>
  <meta charset="UTF-8">
  <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
  <meta content="東北大学交響楽団" name="description">
  <meta content="東北,大学,学友会,交響楽,オケ,オーケストラ" name="keywords">

  <title>Tohoku University Symphony Orchestra</title>
  <link rel="shortcut icon" href="images/favicon.ico" >
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <link href="style.css" media="screen" rel="stylesheet" type="text/css">
  <!--[if lt IE 9]>
  <script src="js/html5.js"></script>
  <script src="js/css3-mediaqueries.js"></script>
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
            <a class="navbar-brand" href="index.html"><img class="logoImg" src="images/title.png"></a>
          </div>

          <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav navbar-right">
              <li>
                <a href="news.html">ニュース<br>
                  <span>News</span>
                </a>
              </li>

              <li class="dropdown">
                <a class="dropdown-toggle" data-toggle="dropdown" href="#">演奏会<br>
                  <span>Concert</span>
                </a>

                <ul class="dropdown-menu">
                  <li>
                    <a href="concert.html">最新の演奏会</a>
                  </li>

                  <li>
                    <a href="pastconcert.html">過去の演奏会</a>
                  </li>

                  <li>
                    <a href="special.html">特別演奏会</a>
                  </li>
                </ul>
              </li>

              <li class="dropdown">
                <a class="dropdown-toggle" data-toggle="dropdown" href="#">紹介<br>
                  <span>About</span>
                </a>

                <ul class="dropdown-menu">
                  <li>
                    <a href="join.html">団員募集</a>
                  </li>

                  <li>
                    <a href="about.html">当団について</a>
                  </li>
                </ul>
              </li>

              <li>
                <a href="contact.html">お問い合わせ<br>
                  <span>Contact</span>
                </a>
              </li>

              <li>
                <a href="link.html">リンク<br>
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
    <img alt="" src="images/image3.jpg">
    <div class="slogan">
      <h2>お問い合わせ</h2>

      <h3>下記のメールフォームにてご連絡ください</h3>
    </div>
  </div><!-- / サブ画像 -->

  <div id="wrapper">
    <!-- コンテンツ -->

    <section id="main">
      <section class="content">
        <h3 class="heading">お問い合わせ</h3>

        <article class="plain">
          <p>演奏会や、入団に関する疑問等、なんでもお気軽にお問い合わせ下さい。</p>
        </article>
      </section>

      <section>
        <article class="plain">
          <?php
          mb_language("ja");
          mb_internal_encoding("UTF-8");

          $to = "tohokuunivorchhomepage@gmail.com";
          $subject = "お問い合わせメール:" . $_POST['subject'];
          $message = "お名前：".$_POST['name']."\n"
          ."メールアドレス:".$_POST['mail']."\n"
          ."用件:".$_POST['subject']."\n\n"
          ."===メール本文＝＝＝\n".$_POST['contents'];
          $body = mb_convert_encoding($message,'ISO-2022-JP', "auto");
          $header = "MIME-Version: 1.0\r\n"
          . "Content-Transfer-Encoding: 7bit\r\n"
          . "Content-Type: text/plain; charset=ISO-2022-JP\r\n"
          . "Message-Id: <" . md5(uniqid(microtime())) . "@tohokuuniv-orch.com>\r\n"
          . "From:".mb_encode_mimeheader($_POST["name"])."<mail-form@tohokuuniv-orch.com>\r\n"
          . "Reply-To:".$_POST["mail"]."\r\n";

          ini_set("sendmail_from", $from);
          if(!mb_send_mail($to,$subject,$body,$header, "-f ".$_POST["mail"])){
            echo "Error....記入された内容をご確認の上、もう一度送信してください。";
          }else{
            echo "正常に送信されました。迅速に対応いたしますので、今しばらくお待ちください。";
          }
          ?>
        </article>
      </section>
    </section><!-- / コンテンツ -->
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
              <a href="index.html"><img class="logoImg" src="images/logo.png"><br>
                <span>東北大学学友会交響楽団</span>
              </a>
            </p><!-- / ロゴ -->
          </div>

          <div class="col-md-6">
            <ul class="list-inline text-a-c">
              <li>
                <a href="sitemap.html">サイトマップ</a>
              </li>

              <li>
                <a href="privacypolicy.html">プライバシーポリシー</a>
              </li>

              <li>
                <a href="idemnity.html">免責事項</a>
              </li>

              <li>
                <a href="memberonly/member.html">団員専用ページ</a>
              </li>
            </ul>
          </div>

          <div class="col-md-3 text-a-r">

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
  <script src="js/jquery-1.11.2.min.js"></script>
  <script src="js/bootstrap.min.js"></script> 
  <script src="js/script.js"></script> 
  <script src="js/jquery.cookie.js"></script>
</body>
</html>