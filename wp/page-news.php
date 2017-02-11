<?php get_header();?>

<!-- サブ画像 -->
<div id="banner">
	<img alt="" src="<?php echo get_template_directory_uri(); ?>/images/image3.jpg">
	<div class="slogan">
		<h2>ニュース</h2>

		<h3>最新のお知らせやトピックスです。</h3>
	</div>
</div><!-- / サブ画像 -->

<div id="wrapper">
	<!-- コンテンツ -->

	<section id="main">
		<section class="content">
			<h3 class="heading">ニュース一覧</h3>

			<article id="news-list" class="container">
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

				<?php pagination($the_query->max_num_pages);?>
			</article>
		</section>
	</section><!-- / コンテンツ -->
	<div id="page-up">
		<a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
	</div>
</div><!-- / WRAPPER -->

<?php get_footer();?>