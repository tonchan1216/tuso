	<!-- フッター -->
	<div id="footer">
		<div class="inner container">
			<!-- 3カラム -->

			<section id="footer-grid">
				<div class="row">
					<div class="col-md-3">
						<!-- ロゴ -->
						<p class="logo">
							<a href="index.html"><img class="logoImg" src="<?php echo get_template_directory_uri(); ?>/images/logo.png"><br>
								<span>東北大学交響楽団</span>
							</a>
						</p><!-- / ロゴ -->
					</div>

					<div class="col-md-6">
						<ul class="list-inline text-a-c">
							<li>
								<a href="<?php echo home_url('/sitemap/');?>">サイトマップ</a>
							</li>

							<li>
								<a href="<?php echo home_url('/privacypolicy/');?>">プライバシーポリシー</a>
							</li>

							<li>
								<a href="<?php echo home_url('/idemnity/');?>">免責事項</a>
							</li>

							<li>
								<a href="<?php echo home_url('/member/');?>">団員専用ページ</a>
							</li>
						</ul>
					</div>

					<div class="col-md-3 text-a-r">

						<p><a href="http://validator.w3.org/check?uri=referer"><img alt="Valid XHTML 1.0 Transitional" height="31" src="http://www.w3.org/Icons/valid-xhtml10" width="88"></a> <a href="http://jigsaw.w3.org/css-validator/"><img alt="Valid CSS!" src="http://jigsaw.w3.org/css-validator/images/vcss" style="border:0;width:88px;height:31px"></a></p>

						<p></p>
					</div>
				</div>
			</section><!-- / 3カラム -->
		</div>

		<div class="copyright">
			(C) Copyright 東北大学交響楽団／東北大学学友会交響楽部　<?php echo date('Y'); ?> All rights reserved.
		</div>
	</div><!-- / フッター -->
	<script src="<?php echo get_template_directory_uri(); ?>/js/jquery-1.11.2.min.js"></script>
	<script src="<?php echo get_template_directory_uri(); ?>/js/bootstrap.min.js"></script>
	<script src="<?php echo get_template_directory_uri(); ?>/js/script.js"></script>
	<script src="<?php echo get_template_directory_uri(); ?>/js/jquery.cookie.js"></script>

	<?php if (is_front_page()) :?>
		<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");
		</script>
	<?php endif;?>

	<?php wp_footer();?>

	<?php if (is_page(array('pastconcert','special')) ) :?>
		<script>
			jQuery( function($) {
				$('tbody tr[data-href]').addClass('clickable').click( function() {
					window.location = $(this).attr('data-href');
				}).find('a').hover( function() {
					$(this).parents('tr').unbind('click');
				}, function() {
					$(this).parents('tr').click( function() {
						window.location = $(this).attr('data-href');
					});
				});
			});
		</script>
	<?php endif;?>
</body>
</html>