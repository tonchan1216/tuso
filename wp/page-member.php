<?php if ( !is_user_logged_in()) auth_redirect();?>
<?php 	
	add_action( 'wp_enqueue_scripts', 'add_files' );
	add_action('wp_print_scripts', 'add_scripts');
	?>
<?php get_header();?>

<!-- サブ画像 -->
<div id="banner">
	<img alt="" src="<?php echo get_template_directory_uri(); ?>/images/image3.jpg">
	<div class="slogan">
		<h2>団員専用ページ</h2>

		<h3>各種資料やスケジュールを提供しています</h3>
	</div>
</div><!-- / サブ画像 -->

<div id="wrapper">
	<!-- コンテンツ -->

	<div id="member" class="container-fluid">
		<div class="row">

			<div class="col-md-3">
				<h3>団員専用メニュー</h3>
				<ul id="tab-menu" class="nav nav-pills">
					<li class="active">
						<a data-toggle="tab" href="#tab-top">各種リンク</a>
					</li>

					<li>
						<a data-toggle="tab" href="#tab-file">ファイル</a>
					</li>

					<li>
						<a data-toggle="tab" href="#tab-rec">録音</a>
					</li>

					<li>
						<a data-toggle="tab" href="#tab-gal">ギャラリー</a>
					</li>

					<li>
						<a data-toggle="tab" href="#tab-other">その他</a>
					</li>
				</ul>
			</div>

			<div class="col-md-9">
				<article class="content">
					<div id="tab-top" class="tabbox tab-pane fade in active">

						<article class="container-fluid">
							<h3>各種リンク</h3>
<!-- 								<dl>
									<dt>
										指定席購入ページ
									</dt>
									<dd>
										<a href="hagi-ticket.html">第165回定期演奏会　チケット申し込み</a>
									</dd>
								</dl>	 -->							

								<dl>
									<?php $arg = array(
										'post_type' => 'memberonly',
										'tax_query' => array(
											array('taxonomy' => 'member-cat', 'field' => 'slug', 'terms' => 'link')
											)
											);?> 
									<?php $the_query = new WP_Query( $arg );?>
									<?php if ( $the_query->have_posts() ) : while ( $the_query->have_posts() ) : $the_query->the_post(); ?>
										<dt><?php the_title();?></dt>
										<dd>
											<a href="<?php echo get_field('link');?>"><?php the_field('link_title');?></a>
										</dd>
									<?php endwhile;	endif;?>
									<?php wp_reset_postdata();?>
								</dl>
							</article>
						</div>

						<div id="tab-file" class="tabbox tab-pane fade">

							<article class="container-fluid">
								<h3>ファイルダウンロード</h3>

								<dl>
									<?php $arg = array(
										'post_type' => 'memberonly',
										'tax_query' => array(
											array('taxonomy' => 'member-cat', 'field' => 'slug', 'terms' => 'file')
											)
											);?> 
									<?php $the_query = new WP_Query( $arg );?>
									<?php if ( $the_query->have_posts() ) : while ( $the_query->have_posts() ) : $the_query->the_post(); ?>
										<dt><?php the_date('Y/m/d');?></dt>
										<dd>
											<a href="<?php echo get_field('file');?>"><?php the_title();?></a>
										</dd>
									<?php endwhile;	endif;?>
									<?php wp_reset_postdata();?>
								</dl>

							</article>
						</div>

						<div id="tab-rec" class="tabbox tab-pane fade">

							<article class="container-fluid">
								<h3>録音</h3>
								<h4 id="play-title">Playボタンから再生できます</h4>
								<audio id="audio-player" href="" controls>このブラウザはオーディオ未対応です。</audio>
								<ul id="music-library">           
									<li>
										<span>2015/06/19</span>
										<button class="play" href="#">Play</button>
										<a href="#">0619B0.mp3</a>
									</li>
									<li>
										<span>2015/06/19</span>
										<button class="play" href="#">Play</button>
										<a href="#">0619B1.mp3</a>
									</li>
									<li>
										<span>2015/06/19</span>
										<button class="play" href="#">Play</button>
										<a href="#">0619H.mp3</a>
									</li>
								</ul>
							</article>
						</div>

						<div id="tab-gal" class="tabbox tab-pane fade">
							<section class="content container-fluid">
								<h3>ギャラリー</h3>
								<div class="row">
									<?php $arg = array(
										'post_type' => 'memberonly',
										'tax_query' => array(
											array('taxonomy' => 'member-cat', 'field' => 'slug', 'terms' => 'gallery')
											)
											);?> 
									<?php $the_query = new WP_Query( $arg );?>
									<?php if ( $the_query->have_posts() ) : while ( $the_query->have_posts() ) : $the_query->the_post(); ?>
										<dd>
											<a class="col-sm-3 col-xs-6" href="<?php echo get_field('image');?>" data-lightbox="gall" data-title="<?php echo get_the_title();?>"><img src="<?php echo get_field('image');?>" /></a>
										</dd>
									<?php endwhile;	endif;?>
									<?php wp_reset_postdata();?>
								</div>

							</section>
						</div>

						<div id="tab-other" class="tabbox tab-pane fade">
							<article class="container-fluid">
								<?php $arg = array(
									'post_type' => 'memberonly',
									'tax_query' => array(
										array('taxonomy' => 'member-cat', 'field' => 'slug', 'terms' => 'other')
										)
										);?> 
								<?php $the_query = new WP_Query( $arg );?>
								<?php if ( $the_query->have_posts() ) : while ( $the_query->have_posts() ) : $the_query->the_post(); ?>
									<section class="content">
										<h3><?php the_title();?></h3>
										<?php the_field('contents');?>
									</section>
								<?php endwhile;	endif;?>
								<?php wp_reset_postdata();?>
							</article>
						</div>
					</article>
				</div>

			</div>
		</div><!-- / コンテンツ -->

		<div id="page-up">
			<a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
		</div>
	</div><!-- / WRAPPER -->

	<?php get_footer();?>