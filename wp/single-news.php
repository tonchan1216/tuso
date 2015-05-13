<!-- サブ画像 -->
<div id="banner">
  <img alt="" src="<?php echo get_template_directory_uri(); ?>/images/image3.jpg">
  <div class="slogan">
    <h2>タイトルが入ります。</h2>

    <h3>テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。</h3>
  </div>
</div><!-- / サブ画像 -->

<div id="wrapper">
  <!-- コンテンツ -->

  <section id="main">
    <section class="content container-fluid">
      <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
      <h4 class="news-data"><?php the_date('Y/m/d'); ?></h4>

      <h3 class="news-title"><?php the_title();?></h3>

      <article class="news-content">
        <?php the_content(); ?>
      </article>

      <?php endwhile; else: ?>
        <p><?php echo "お探しの記事、ページは見つかりませんでした。"; ?></p>
      <?php endif; ?>
      <?php wp_reset_query(); ?>

    </section>
  </section><!-- / コンテンツ -->
</div><!-- / WRAPPER -->