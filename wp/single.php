<?php get_header();?>

<!-- サブ画像 -->
<div id="banner">
	<img alt="" src="<?php echo get_template_directory_uri(); ?>/images/image3.jpg">
	<div class="slogan">
		<h2><?php the_title();?></h2>

		<h3><?php the_field('introduction');?></h3>
	</div>
</div><!-- / サブ画像 -->

<div id="wrapper">
	<!-- コンテンツ -->

	<section id="main">
		<section id="news" class="content container-fluid">
			<h4 class="news-data"><?php the_time('Y/m/d');?></h4>

			<h3 class="news-title"><?php the_title();?></h3>

			<article class="news-content">
				<?php while ( have_posts() ) : the_post(); ?>
					<?php remove_filter('the_content', 'wpautop');
					the_content();
					add_filter('the_content', 'wpautop');
					?>
				<?php endwhile; ?>
			</article>
		</section>
	</section><!-- / コンテンツ -->
</div><!-- / WRAPPER -->

<?php get_footer();?>