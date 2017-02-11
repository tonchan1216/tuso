<?php get_header();?>

<!-- サブ画像 -->
<div id="banner">
	<img alt="" src="<?php echo get_template_directory_uri(); ?>/images/image3.jpg">
	<div class="slogan">
		<h2>過去の特別演奏会・演奏旅行</h2>

		<h3>過去の演奏旅行やジョイントコンサートなどの情報です。</h3>
	</div>
</div><!-- / サブ画像 -->

<div id="wrapper">
	<!-- コンテンツ -->

	<section id="main">
		<section class="content">
			<h3 class="heading">特別演奏会の記録</h3>
			<div class="">
				<table id="concertRecord" class="table table-striped table-condensed" summary="過去の特別演奏" width="100%">

					<?php $arg = array(
						'post_type' => 'concert',
						'tax_query' => array(
							array('taxonomy' => 'concert-cat', 'field' => 'slug', 'terms' => 'special')
							)
							);?> 
					<?php $the_query = new WP_Query( $arg );?>
					<?php if ( $the_query->have_posts() ) : while ( $the_query->have_posts() ) : $the_query->the_post(); ?>
						<tr data-href="<?php echo get_the_permalink();?>">
							<th><?php the_field('special_category');?></th>
							<td><?php the_time('Y年m月d日');?></td>
							<td><?php the_title();?></td>
						</tr>
					<?php endwhile;	endif;?>
					<?php wp_reset_postdata();?>
				</table>
			</div>

		</section>
	</section><!-- / コンテンツ -->
	<div id="page-up">
		<a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
	</div>
</div><!-- / WRAPPER -->

<?php get_footer();?>