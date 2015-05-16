<?php get_header(); ?>

<?php while ( have_posts() ) : the_post(); ?>
  <!-- サブ画像 -->
  <div id="banner">
    <img alt="" src="images/image3.jpg">
    <div class="slogan">
      <h2>タイトルが入ります。</h2>

      <h3>テキストが入ります。テキストが入ります。テキストが入ります。テキストが入ります。</h3>
    </div>
  </div><!-- / サブ画像 -->

	<div id="wrapper">

	<?php the_content(); ?>
	
<?php endwhile; ?>

<?php get_footer(); ?>