<?php get_header(); ?>

<?php
$post = $wp_query->post;
if ( in_category('news') ) {
	get_template_part( 'single-news' );
} elseif ( in_category('concert') ) {
  get_template_part( 'single-concert' );
} else {
	get_template_part( 'index' );
}
?>

<?php get_footer(); ?>