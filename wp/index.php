<?php get_header(); ?>

<?php while ( have_posts() ) : the_post(); ?>
	<?php remove_filter('the_content', 'wpautop');
		the_content();
		add_filter('the_content', 'wpautop');
	?>
<?php endwhile; ?>

<?php get_footer(); ?>