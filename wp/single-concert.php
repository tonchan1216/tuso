<!-- サブ画像 -->
<div class="subImg" id="mainBanner">
  <img alt="" src="<?php echo get_template_directory_uri(); ?>/images/image02.jpg" width="100%">

  <div class="slogan">
    <h2>タイトルが入ります。</h2>

    <h3>テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。</h3>
  </div>
</div><!-- / サブ画像 -->

<div id="wrapper">
  <!-- コンテンツ -->

  <section id="main">
    <section class="content">
      <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
      <h3 class="heading"><?php the_title(); ?></h3>

      <article class="concert">
        <?php echo "<p>".the_title()."は終了いたしました。ご来場ありがとうございました。</p>" ?>
        <img alt="" class="posterimg frame" src="<?php the_post_thumbnail($post->ID); ?>" width="240" height="320">
        <dl>
          <dt>指揮</dt>

          <dd><?php the_field("指揮", $post->ID); ?></dd>

          <dt>日時</dt>

          <dd><?php the_field("日時", $post->ID); ?></dd>

          <dt></dt>

          <dt>会場</dt>

          <dd>
            <?php the_field("会場", $post->ID); ?><br>
            会場へのアクセスは<a href="<?php the_field("アクセスリンク", $post->ID); ?>">こちら</a>
          </dd>

          <dt>曲目</dt>

          <dd>
            <table summary="musiclist">
              <tbody>
                <tr>
                  <td>序曲「ローマの謝肉祭」作品9</td>

                  <td>ベルリオーズ<br>
                  H.Berlioz</td>
                </tr>

                <tr>
                  <td>交響曲第1番 ハ長調 作品21</td>

                  <td>ベートーヴェン<br>
                  L.v.Beethoven</td>
                </tr>

                <tr>
                  <td>交響曲第4番 ホ短調 作品98</td>

                  <td>ブラームス<br>
                  J.Brahms</td>
                </tr>
              </tbody>
            </table>
          </dd>

          <dt>入場料<!--(チケット販売中 <a href="../ticket/ticket.html">オンラインチケット予約はこちら</a>)--></dt>

          <dd><?php the_field("入場料", $post->ID); ?></dd>

          <dt>プレイガイド　（販売中）</dt> 

          <dd>
            (株)ヤマハミュージックリテイリング仙台店、東北大学生協川内店、藤崎、(株)仙台三越、
            <br>カワイミュージックショップ仙台、東京エレクトロンホール宮城(宮城県民会館)
          </dd>

          <dt>お問い合わせ</dt>

          <dd>
            実行委員長　<?php the_field("実行委員長", $post->ID); ?><br>
            <a href="mailto:<?php the_field("gmail", $post->ID); ?>"><?php the_field("gmail", $post->ID); ?></a>
          </dd>
        </dl>
      </article>
      <?php endwhile; else: ?>
        <p><?php echo "お探しの記事、ページは見つかりませんでした。"; ?></p>
      <?php endif; ?>
      <?php wp_reset_query(); ?>
    </section>
  </section><!-- / コンテンツ -->
</div><!-- / WRAPPER -->