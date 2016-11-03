<?php get_header();?>

<!-- カルーセル -->
<div id="carousel" class="carousel slide carousel-fade" data-ride="carousel">

	<ol class="carousel-indicators">
		<li data-target="#carousel" data-slide-to="0" class="active"></li>
		<li data-target="#carousel" data-slide-to="1"></li>
		<li data-target="#carousel" data-slide-to="2"></li>
		<li data-target="#carousel" data-slide-to="3"></li>
	</ol>

	<div class="carousel-inner">
		<div class="item active">
			<img src="images/image6.jpg" alt="サンプル画像１" class="img-responsive">
			<div class="carousel-caption">
			</div>
		</div>

		<div class="item">
			<img src="images/image03.jpg" alt="サンプル画像２" class="img-responsive">
			<div class="carousel-caption">
			</div>
		</div>

		<div class="item">
			<img src="images/image3.jpg" alt="サンプル画像２" class="img-responsive">
			<div class="carousel-caption">
			</div>
		</div>

		<div class="item">
			<img src="images/image5.jpg" alt="サンプル画像２" class="img-responsive">
			<div class="carousel-caption">
			</div>
		</div>
	</div>

	<a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
		<span class="glyphicon glyphicon-chevron-left"></span>
	</a>
	<a class="right carousel-control" href="#carousel" role="button" data-slide="next">
		<span class="glyphicon glyphicon-chevron-right"></span>
	</a>
</div><!-- / カルーセル -->

<!-- / WRAPPER -->
<div id="wrapper" class="container">
	<section class="content">
		<h3 class="heading">ようこそ東北大学交響楽団へ</h3>

		<div class="row">
			<div class="col-md-4">
				<img alt="" class="frame img-responsive" src="<?php echo get_template_directory_uri(); ?>/images/image5.jpg" width="320">
			</div>

			<div class="col-md-8">
				<div class="plain">
					<p>東北大学交響楽団は、東北大学学友会の学生オーケストラとして活動している団体です。</p>

					<p>我々は年２回の定期演奏会に加え、技術力向上のための合宿や大学行事での演奏など、様々な活動を行っています。</p>

					<p>定期演奏会での皆様のご来場を、団員一同こころからお待ちしております。</p>
				</div>
			</div>
		</div>
	</section>

	<section class="content">
		<div class="row">
			<div class="col-md-8">
				<h3 class="heading">Contents！</h3>
				<article class="container-fluid">
					<div id="contents-link" class="row">
						<div class="col-sm-4">
						<a href="concert.html"><img src="<?php echo get_template_directory_uri(); ?>/images/top_image2.jpg" alt=""><p id="link-c">演奏会にお越しの方</p></a>
						</div>
						<div class="col-sm-4">
							<a href="join.html"><img src="<?php echo get_template_directory_uri(); ?>/images/top_image3.jpg" alt=""><p id="link-j">入団希望の方</p></a>
						</div>
						<div class="col-sm-4">
							<a href="memberonly/member.html"><img src="<?php echo get_template_directory_uri(); ?>/images/top_image1.jpg" alt=""><p id="link-m">団員の方</p></a>
						</div>
					</div>
				</article>

				<h3 class="heading">News　Post！</h3>
				<article id="news-list" class="container-fluid">
					<!-- ニュース -->
					<ul>
						<li>
							<span>2016/10/02</span>
							<a href="concert.html">第167回定期演奏会の情報を掲載しました。</a>
						</li>
						<li>
							<span>2016/04/06</span>
							<a href="news/2016-04-06.html">平成28年度新歓行事を掲載しました。</a>
						</li>
						<li>
							<span>2015/12/17</span>
							<a href="concert.html">第166回定期演奏会の情報を掲載しました。</a>
						</li>
						<li>
							<span>2015/12/17</span>
							<a href="news/2015-12-17.html">ホームページをリニューアルしました。</a>
						</li>
						<li>
							<span>2015/12/05</span>
							<a href="past/165.html">第165回定期演奏会を行いました。ご来場ありがとうございました。</a>
						</li>
						<li>
							<span>2015/09/25</span>
							<a href="">第165回定期演奏会の情報を掲載しました。</a>
						</li>
					</ul>
					<!--  -->
				</article>
			</div>

			<div class="col-md-4">
				<div id="tw">
					<a class="twitter-timeline" href="https://twitter.com/UnivTohoku_orch" data-widget-id="642200772520730624" data-chrome="noscrollbar nofooter" data-tweet-limit="4">@UnivTohoku_orchさんのツイート</a>
				</div>
			</div>
		</div>
	</section>

	<div id="page-up">
		<a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
	</div>
</div><!-- / WRAPPER -->

<?php get_footer();?>
