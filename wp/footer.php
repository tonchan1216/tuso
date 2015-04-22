  <!-- フッター -->

  <div id="footer">
    <div class="inner">
      <!-- 3カラム -->

      <section class="gridWrapper">
        <article class="grid">
          <!-- ロゴ -->
          <p class="logo">
            <a href="<?php bloginfo('url'); ?>"><img class="logoImg" src="<?php echo get_template_directory_uri(); ?>/images/logo.png"><br>
            <span>東北大学学友会交響楽団</span></a>
          </p><!-- / ロゴ -->
        </article>

        <article class="grid">
          <ul class="list-inline text-a-c">
            <li>
              <a href="<?php bloginfo('url'); ?>/sitemap.html">サイトマップ</a>
            </li>

            <li>
              <a href="<?php bloginfo('url'); ?>/privacypolicy.html">プライバシーポリシー</a>
            </li>

            <li>
              <a href="<?php bloginfo('url'); ?>/idemnity.html">免責事項</a>
            </li>

            <li>
              <a href="<?php bloginfo('url'); ?>/member.html">団員専用ページへ</a>
            </li>
          </ul>
        </article>

        <article class="grid f-right text-a-r">
          <!-- 電話番号+受付時間 -->

          <p class="mail">E-mail: <strong>abcde@ABC.com</strong></p>

          <p><a href="http://validator.w3.org/check?uri=referer"><img alt="Valid XHTML 1.0 Transitional" height="31" src="http://www.w3.org/Icons/valid-xhtml10" width="88"></a> <a href="http://jigsaw.w3.org/css-validator/"><img alt="Valid CSS!" src="http://jigsaw.w3.org/css-validator/images/vcss" style="border:0;width:88px;height:31px"></a></p>

          <p><!-- FC2カウンター ここから --><script language="JavaScript" src="http://counter1.fc2.com/counter.php?id=2160762" type="text/javascript"></script> <noscript><img alt="counter" src="http://counter1.fc2.com/counter_img.php?id=2160762"><br>
          <strong><a href="http://flowerfan.com/">ギフト</a></strong></noscript> <!-- FC2カウンター ここまで --></p>
        </article>
      </section><!-- / 3カラム -->
    </div>

    <div class="copyright">
      (C) Copyright 東北大学交響楽団／東北大学学友会交響楽部　2015 All rights reserved.
    </div>
  </div><!-- / フッター -->

  <script src="<?php echo get_template_directory_uri(); ?>/js/jquery1.7.2.min.js"></script> 
  <script src="<?php echo get_template_directory_uri(); ?>/js/script.js"></script> 
  <script src="<?php echo get_template_directory_uri(); ?>/js/jquery.bxslider.js"></script>
  <?php echo <<< EOM 
    <script>
      $(function(){
        $('.bxslider').bxSlider({
          auto: true,
          mode: 'fade'
        });
      });
    </script>
    EOM; 
  ?>
  <?php wp_footer(); ?>
</body>
</html>