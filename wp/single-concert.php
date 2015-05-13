<!-- サブ画像 -->
<div id="banner">
  <img alt="" src="<?php echo get_template_directory_uri(); ?>images/image3.jpg">
  <div class="slogan">
    <h2>最新の演奏会</h2>

    <h3>次回の定期演奏会のお知らせです。</h3>
  </div>
</div><!-- / サブ画像 -->

<div id="wrapper">
  <!-- コンテンツ -->

  <section id="main">
    <section class="content">
      <?php query_posts('category_name=recent-concert'); ?>
      <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
      <h3 class="heading"><?php the_title(); ?></h3>

      <article class="concert">
        <div class="row">
          <div class="col-sm-4 col-sm-push-8">
            <?php if( the_field("end_flag", $post->ID) ) : echo the_title()."は終了いたしました。ご来場ありがとうございました。"; ?>
            <img alt="" class="posterimg frame" src="<?php the_post_thumbnail($post->ID); ?>" width="240" height="320">
          </div>

          <div class="col-sm-8 col-sm-pull-4">
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
                      <td><?php the_field("曲目1", $post->ID); ?></td>

                      <td><?php the_field("作曲者1", $post->ID); ?></td>
                    </tr>

                    <tr>
                      <td><?php the_field("曲目2", $post->ID); ?></td>

                      <td><?php the_field("作曲者2", $post->ID); ?></td>
                    </tr>

                    <tr>
                      <td><?php the_field("曲目3", $post->ID); ?></td>

                      <td><?php the_field("作曲者3", $post->ID); ?></td>
                    </tr>
                  </tbody>
                </table>
              </dd>

              <dt>入場料<!--(チケット販売中 <a href="../ticket/ticket.html">オンラインチケット予約はこちら</a>)--></dt>

              <dd><?php the_field("入場料", $post->ID); ?></dd>

              <dt>
                プレイガイド
                <?php if( the_field("end_flag", $post->ID) ) :
                  echo " (販売は終了しました)";
                  else echo " (販売中)"; 
                ?>
              </dt> 

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
          </div>
        </div>
      </article>
      <?php endwhile; else: ?>
        <p><?php echo "お探しの記事、ページは見つかりませんでした。"; ?></p>
      <?php endif; ?>
      <?php wp_reset_query(); ?>
    </section>
  </section><!-- / コンテンツ -->
  <div id="page-up">
    <a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
  </div>
</div><!-- / WRAPPER -->