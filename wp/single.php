<?php get_header(); ?>

<?php
$post = $wp_query->post;
if ( in_category('concert') ) {
	get_template_part( 'single-concert' );
} elseif ( in_category('news') ) {
  get_template_part( 'single-news' );
} else {
	get_template_part( 'single-news' );
}
?>

<?php get_footer(); ?>