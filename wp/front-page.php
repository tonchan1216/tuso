<?php get_header();?>

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
			<img src="<?php echo get_field('image1');?>" class="img-responsive">
			<div class="carousel-caption">
			</div>
		</div>

		<div class="item">
			<img src="<?php echo get_field('image2');?>" class="img-responsive">
			<div class="carousel-caption">
			</div>
		</div>

		<div class="item">
			<img src="<?php echo get_field('image3');?>" class="img-responsive">
			<div class="carousel-caption">
			</div>
		</div>

		<div class="item">
			<img src="<?php echo get_field('image4');?>" class="img-responsive">
			<div class="carousel-caption">
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

<!-- / WRAPPER -->
<div id="wrapper" class="container">
	<section class="content">
		<h3 class="heading">ようこそ東北大学交響楽団へ</h3>

		<div class="row">
			<div class="col-md-4">
				<img alt="" class="frame img-responsive" src="<?php echo get_template_directory_uri(); ?>/images/image5.jpg" width="320">
			</div>

			<div class="col-md-8">
				<div class="plain">
					<?php while ( have_posts() ) : the_post(); ?>
						<?php the_content();?>
					<?php endwhile; ?>
				</div>
			</div>
		</div>
	</section>

	<section class="content">
		<div class="row">
			<div class="col-md-8">
				<h3 class="heading">Contents！</h3>
				<article class="container-fluid">
					<div id="contents-link" class="row">
						<div class="col-sm-4">
							<a href="<?php echo home_url('/concert/');?>">
								<img src="<?php echo get_template_directory_uri(); ?>/images/top_image2.jpg" alt="">
								<p id="link-c">演奏会にお越しの方</p>
							</a>
						</div>
						<div class="col-sm-4">
							<a href="<?php echo home_url('/join/');?>">
								<img src="<?php echo get_template_directory_uri(); ?>/images/top_image3.jpg" alt="">
								<p id="link-j">入団希望の方</p>
							</a>
						</div>
						<div class="col-sm-4">
							<a href="<?php echo home_url('/member/');?>">
								<img src="<?php echo get_template_directory_uri(); ?>/images/top_image1.jpg" alt="">
								<p id="link-m">団員の方</p>
							</a>
						</div>
					</div>
				</article>

				<h3 class="heading">News　Post！</h3>
				<article id="news-list" class="container-fluid">
					<!-- ニュース -->
					<ul>
						<?php $arg = array(
							'post_type'=> array('post','concert'),
							'paged' => get_query_var('page'),
							'posts_per_page' => 10,
							'date_query' => array(
								array('after' => array('year' => 2014))
								)
							);?>
						<?php $the_query = new WP_Query($arg);?>
						<?php if ( $the_query->have_posts() ) : while ( $the_query->have_posts() ) : $the_query->the_post(); ?>
							<li>
								<span><?php the_time('Y/m/d');?></span>
								<?php if ($post->post_type == 'concert') :?>
									<a href="<?php echo get_the_permalink();?>"><?php the_title();?>の情報を掲載しました。</a>
								<?php else:?>
									<a href="<?php echo get_the_permalink();?>"><?php the_title();?></a>
								<?php endif;?>
							</li>
						<?php endwhile;	endif;?>
						<?php wp_reset_postdata();?>				
					</ul>
					<!--  -->
				</article>
			</div>

			<div class="col-md-4">
				<div id="tw">
					<a class="twitter-timeline" href="https://twitter.com/UnivTohoku_orch" data-widget-id="642200772520730624" data-chrome="noscrollbar nofooter" data-tweet-limit="4">@UnivTohoku_orchさんのツイート</a>
				</div>
			</div>
		</div>
	</section>

	<div id="page-up">
		<a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
	</div>
</div><!-- / WRAPPER -->

<?php get_footer();?>
