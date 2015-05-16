<?php get_header(); ?>

<!-- カルーセル -->
<div id="carousel" class="carousel slide carousel-fade" data-ride="carousel">

  <ol class="carousel-indicators">
    <li data-target="#carousel" data-slide-to="0" class="active"></li>
    <li data-target="#carousel" data-slide-to="1"></li>
    <li data-target="#carousel" data-slide-to="2"></li>
    <li data-target="#carousel" data-slide-to="3"></li>
  </ol>

  <div class="carousel-inner">
    <div class="item active">
      <img src="<?php echo get_template_directory_uri(); ?>/images/image6.jpg" alt="サンプル画像１" class="img-responsive">
      <div class="carousel-caption">
        <h2>タイトルが入ります</h2>
        <h3>テキストが入りますテキストが入りますテキストが入ります</h3>
      </div>
    </div>    

    <div class="item">
      <img src="<?php echo get_template_directory_uri(); ?>/images/image2.jpg" alt="サンプル画像２" class="img-responsive">
        <div class="carousel-caption">
        <h2>タイトルが入ります</h2>
        <h3>テキストが入りますテキストが入りますテキストが入ります</h3>
      </div>
    </div>     

    <div class="item">
      <img src="<?php echo get_template_directory_uri(); ?>/images/image3.jpg" alt="サンプル画像２" class="img-responsive">
        <div class="carousel-caption">
        <h2>タイトルが入ります</h2>
        <h3>テキストが入りますテキストが入りますテキストが入ります</h3>
      </div>
    </div>   

    <div class="item">
      <img src="<?php echo get_template_directory_uri(); ?>/images/image5.jpg" alt="サンプル画像２" class="img-responsive">
        <div class="carousel-caption">
        <h2>タイトルが入ります</h2>
        <h3>テキストが入りますテキストが入りますテキストが入ります</h3>
      </div>
    </div>
  </div>

  <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left"></span>
  </a>
  <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right"></span>
  </a>
</div><!-- / カルーセル -->

<div id="wrapper" class="container">
  <section class="content">
    <h3 class="heading">新着情報</h3>

      <article class="news container-fluid">
        <?php query_posts('category_name=news,concert&showpost=5'); if (have_posts()) : while (have_posts()) : the_post(); ?>

          <dl>
            <dt>
              <a href="<?php the_permalink(); ?>"><?php the_time('Y/m/d'); ?></a>
            </dt>

            <dd>
              <a href="<?php the_permalink(); ?>"><?php the_title();?></a>
            </dd>
          </dl>

        <?php endwhile; endif; ?>
        <?php wp_reset_query(); ?>

      </article>
  </section>

  <section class="content">
    <h3 class="heading">タイトルが入ります。</h3>

    <div class="row">
      <div class="col-md-4">
        <img alt="" class="frame img-responsive" src="<?php echo get_template_directory_uri(); ?>/images/image5.jpg" width="320">
      </div>
      
      <div class="col-md-8">
        <p>テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。</p>

        <p>テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。</p>

        <p>テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。</p>

        <p>テキストが入ります。テキストが入ります。テキストが入ります。</p>
      </div>
    </div>
  </section>


<?php get_footer(); ?>