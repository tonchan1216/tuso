<?php get_header();?>
<?php while ( have_posts() ) : the_post(); ?>

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

		<?php remove_filter('the_content', 'wpautop');
		the_content();
		add_filter('the_content', 'wpautop');
		?>

	<div id="page-up">
		<a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
	</div>
</div><!-- / WRAPPER -->
<?php endwhile; ?>

<?php get_footer(); ?>