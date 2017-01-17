<?php if ( !is_user_logged_in()) auth_redirect();?>

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
						<a data-toggle="tab" href="#tab-cal">スケジュール</a>
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
									<dt>
										2016/09/12
									</dt>
									<dd>
										<a href="asset/166-anser_sheet.xlsx">第166回定期演奏会　アンケート集計結果</a>
									</dd>
								</dl>

								<dl>
									<dt>
										2016/08/22
									</dt>
									<dd>
										<a href="asset/H28kawauchi-bus.xlsx">H28年度川内合宿　バス割り</a>
									</dd>									
									<dd>
										<a href="asset/H28kawauchi-kakari.xlsx">H28年度川内合宿　係一覧</a>
									</dd>
									<dd>
										<a href="asset/H28kawauchi-notice.docx">H28年度川内合宿　諸連絡</a>
									</dd>
									<dd>
										<a href="asset/H28kawauchi-time_table.xlsx">H28年度川内合宿　タイムテーブル</a>
									</dd>
									<dd>
										<a href="asset/H28kawauchi-notes.docx">H28年度川内合宿　注意事項</a>
									</dd>
									<dd>
										<a href="asset/H28kawauchi-cover.docx">H28年度川内合宿　しおり表紙</a>
									</dd>
									<dd>
										<a href="asset/H28kawauchi-room.xlsx">H28年度川内合宿　部屋割り</a>
									</dd>
								</dl>								

								<dl>
									<dt>
										2016/08/07
									</dt>
									<dd>
										<a href="asset/H28kawauchi-budget.pdf">H28年度川内合宿予算</a>
									</dd>									
									<dd>
										<a href="asset/H28kawauchi-inquiry.pdf">H28年度川内合宿アンケート集計</a>
									</dd>
								</dl>

								<dl>
									<dt>
										2016/06/28
									</dt>
									<dd>
										<a href="asset/images.pdf" target="_blank">楽譜　仮面舞踏会(pdf版)</a>
									</dd>									
									<dd>
										<a href="asset/1467119593193.jpg" target="_blank">楽譜　仮面舞踏会(画像1)</a>
									</dd>
									<dd>
										<a href="asset/1467119594969.jpg" target="_blank">楽譜　仮面舞踏会(画像2)</a>
									</dd>
									<dd>
										<a href="asset/1467119596448.jpg" target="_blank">楽譜　仮面舞踏会(画像3)</a>
									</dd>
									<dd>
										<a href="asset/1467119597872.jpg" target="_blank">楽譜　仮面舞踏会(画像4)</a>
									</dd>
									<dd>
										<a href="asset/1467119600975.jpg" target="_blank">楽譜　仮面舞踏会(画像5)</a>
									</dd>
									<dd>
										<a href="asset/1467119602388.jpg" target="_blank">楽譜　仮面舞踏会(画像6)</a>
									</dd>
									<dd>
										<a href="asset/1467119604046.jpg" target="_blank">楽譜　仮面舞踏会(画像7)</a>
									</dd>
									<dd>
										<a href="asset/1467119605484.jpg" target="_blank">楽譜　仮面舞踏会(画像8)</a>
									</dd>
									<dd>
										<a href="asset/1467119611058.jpg" target="_blank">楽譜　仮面舞踏会(画像9)</a>
									</dd>
									<dd>
										<a href="asset/1467119612542.jpg" target="_blank">楽譜　仮面舞踏会(画像10)</a>
									</dd>
									<dd>
										<a href="asset/1467119613919.jpg" target="_blank">楽譜　仮面舞踏会(画像11)</a>
									</dd>
									<dd>
										<a href="asset/1467119615155.jpg" target="_blank">楽譜　仮面舞踏会(画像12)</a>
									</dd>
									<dd>
										<a href="asset/1467119617211.jpg" target="_blank">楽譜　仮面舞踏会(画像13)</a>
									</dd>
									<dd>
										<a href="asset/1467119619333.jpg" target="_blank">楽譜　仮面舞踏会(画像14)</a>
									</dd>
									<dd>
										<a href="asset/1467119620569.jpg" target="_blank">楽譜　仮面舞踏会(画像15)</a>
									</dd>
									<dd>
										<a href="asset/1467119621700.jpg" target="_blank">楽譜　仮面舞踏会(画像16)</a>
									</dd>
									<dd>
										<a href="asset/1467119623889.jpg" target="_blank">楽譜　仮面舞踏会(画像17)</a>
									</dd>
								</dl>								

								<dl>
									<dt>
										2016/01/21
									</dt>
									<dd>
										<a href="asset/165-impression.docx">印象に残った理由(docx)</a>
									</dd>
								</dl>

								<dl>
									<dt>
										2016/01/21
									</dt>
									<dd>
										<a href="asset/165-opinion.docx">ご意見・ご感想・聞きたい曲(docx)</a>
									</dd>
								</dl>

								<dl>
									<dt>
										2016/01/21
									</dt>
									<dd>
										<a href="asset/165-anser_sheet.xlsx">165アンケート集計表(xlsx)</a>
									</dd>
								</dl>

								<dl>
									<dt>
										2015/9/25
									</dt>
									<dd>
										<a href="asset/ininjyo_2013.pdf">委任状</a>
									</dd>
								</dl>

								<dl>
									<dt>
										2015/9/25
									</dt>
									<dd>
										<a href="asset/164kessan.pdf">第164回定期演奏会決算（最終版）</a>
									</dd>
								</dl>

								<dl>
									<dt>
										2015/9/25
									</dt>
									<dd>
										<a href="asset/twitter_kisoku.pdf">団twitter運用規則</a>
									</dd>
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

						<div id="tab-cal" class="tabbox tab-pane fade">
							<div class="cal_wrapper">
								<div class="googlecal">
									<iframe src="https://www.google.com/calendar/embed?showTitle=0&amp;showPrint=0&amp;showTabs=0&amp;showCalendars=0&amp;showTz=0&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=tohokuunivorchhomepage%40gmail.com&amp;color=%23AB8B00&amp;ctz=Asia%2FTokyo" style=" border-width:0 " height="600" frameborder="0" scrolling="no"></iframe>
								</div>
							</div>
						</div>

						<div id="tab-gal" class="tabbox tab-pane fade">
							<section class="content container-fluid">
								<h3>ギャラリー</h3>
								<div class="row">
									<a class="col-sm-3 col-xs-6" href="../images/image1.jpg" data-lightbox="gall" data-title="ここに説明文を入れる"><img src="../images/image1.jpg" /></a>
									<a class="col-sm-3 col-xs-6" href="../images/image2.jpg" data-lightbox="gall" data-title="ここに説明文を入れる"><img src="../images/image2.jpg" /></a>
									<a class="col-sm-3 col-xs-6" href="../images/image3.jpg" data-lightbox="gall" data-title="ここに説明文を入れる"><img src="../images/image3.jpg" /></a>
									<a class="col-sm-3 col-xs-6" href="../images/image4.jpg" data-lightbox="gall" data-title="ここに説明文を入れる"><img src="../images/image4.jpg" /></a>
									<a class="col-sm-3 col-xs-6" href="../images/image5.jpg" data-lightbox="gall" data-title="ここに説明文を入れる"><img src="../images/image5.jpg" /></a>
									<a class="col-sm-3 col-xs-6" href="../images/image6.jpg" data-lightbox="gall" data-title="ここに説明文を入れる"><img src="../images/image6.jpg" /></a>
									<a class="col-sm-3 col-xs-6" href="../images/image7.jpg" data-lightbox="gall" data-title="ここに説明文を入れる"><img src="../images/image7.jpg" /></a>
									<a class="col-sm-3 col-xs-6" href="../images/image8.jpg" data-lightbox="gall" data-title="ここに説明文を入れる"><img src="../images/image8.jpg" /></a>
									<a class="col-sm-3 col-xs-6" href="../images/image9.jpg" data-lightbox="gall" data-title="ここに説明文を入れる"><img src="../images/image9.jpg" /></a>

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