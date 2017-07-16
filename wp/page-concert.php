<?php get_header();?>

	<!-- サブ画像 -->
	<div id="banner">
		<img alt="" src="<?php echo get_template_directory_uri(); ?>/images/image3.jpg">
		<div class="slogan">
			<h2>最新の演奏会</h2>

			<h3>次回の演奏会のお知らせです。</h3>
		</div>
	</div><!-- / サブ画像 -->

	<div id="wrapper">
		<!-- コンテンツ -->
		<?php $arg = array(
			'post_type' => 'concert',
			'posts_per_page' => 1,
			'tax_query' => array(
				array(
					'taxonomy' => 'concert-cat',
					'field' => 'slug',
					'terms' => array( 'new' ),
					)
		  ),
			);?> 
		<?php $the_query = new WP_Query( $arg );?>
		<?php if ( $the_query->have_posts() ) : while ( $the_query->have_posts() ) : $the_query->the_post(); ?>
			<?php remove_filter('the_content', 'wpautop');?>

			<section id="main">
				<section class="content">
					<h3 class="heading"><?php the_title();?></h3>

					<article id="concert">
						<div class="row">
							<div class="col-sm-4 col-sm-push-8">
								<?php if (get_post_thumbnail_id()):?>
								<img alt="" class="posterimg frame" src="<?php echo wp_get_attachment_image_src(get_post_thumbnail_id(), 'full')[0];?>" width="240" height="320">
								<?php endif;?>
							</div>

							<div class="col-sm-8 col-sm-pull-4">
								<?php if (get_field('is_fine')) :?>
									<p><?php the_title();?>は終了いたしました。ご来場ありがとうございました。</p>
								<?php endif;?>
								<dl>
									<dt>指揮</dt>

									<dd><?php the_field('conductor');?></dd>

									<?php the_field('solist');?>

									<dt>日時</dt>

									<dd><?php the_field('date');?></dd>

									<dt>曲目</dt>

									<dd>
										<?php the_content();?>
									</dd>

									<dt>会場</dt>

									<dd>
										<?php the_field('place');?>
									</dd>

									<dt>入場料</dt>

									<dd><?php the_field('fee');?></dd>

									<?php if (get_field('play_guide_status') != 'yet') :?>

										<dt>プレイガイド　<?php echo (get_field('play_guide_status') == 'fine') ? '（販売終了）' : '';?></dt>

										<dd>
											<?php the_field('play_guide');?>
										</dd>

									<?php endif;?>

									<dt>お問い合わせ</dt>

									<dd>
										実行委員長　<?php the_field('chairman');?><br>
										<a href="mailto:<?php echo get_field('e-mail');?>"><?php the_field('e-mail');?></a>
									</dd>
								</dl>
							</div>
						</div>
					</article>
				</section>
			</section><!-- / コンテンツ -->
			<?php add_filter('the_content', 'wpautop');?>
		<?php endwhile;	endif;?>
		<?php wp_reset_postdata();?>

    <div id="page-up">
    	<a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
    </div>
  </div><!-- / WRAPPER -->

<?php get_footer();?>
