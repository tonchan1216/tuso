<?php get_header();?>

<!-- サブ画像 -->
<div id="banner">
	<img alt="" src="<?php echo get_template_directory_uri(); ?>/images/image3.jpg">
	<div class="slogan">
		<h2>過去の演奏会</h2>

		<h3>過去の定期演奏会の情報です。</h3>
	</div>
</div><!-- / サブ画像 -->

<div id="wrapper">
	<!-- コンテンツ -->

	<section id="main">
		<section class="content container-fluid">
			<h3 class="heading">過去の演奏会一覧</h3>
			<div id="gallery" class="row">
				<?php $arg = array(
					'post_type' => 'concert',
					'posts_per_page' => 16,
					'tax_query' => array(
						array('taxonomy' => 'concert-cat', 'field' => 'slug', 'terms' => 'past')
						)
						);?> 
				<?php $the_query = new WP_Query( $arg );?>
				<?php if ( $the_query->have_posts() ) : while ( $the_query->have_posts() ) : $the_query->the_post(); ?>
					<div class="elem col-md-3 col-sm-4 col-xs-6">
						<a href="<?php echo get_the_permalink();?>" title="<?php echo get_the_title();?>">
							<img alt="" src="<?php echo wp_get_attachment_image_src(get_post_thumbnail_id(), 'full')[0];?>"><br>
							<?php the_title();?>
						</a>
					</div>
				<?php endwhile;	endif;?>
				<?php wp_reset_postdata();?>
			</div>

		</section>

		<section class="content">
			<h3 class="heading">定期演奏会記録</h3>

			<p>それ以前の演奏会は<a class="readmore">こちらから</a></p>
			<div class="slideList">
				<table id="concertRecord" class="table table-striped table-condensed" summary="過去の演奏会" width="100%">

					<?php $arg = array(
						'post_type' => 'concert',
						'nopaging' => true,
						'tax_query' => array(
							array('taxonomy' => 'concert-cat', 'field' => 'slug', 'terms' => 'past')
							)
							);?> 
					<?php $the_query = new WP_Query( $arg );?>
					<?php if ( $the_query->have_posts() ) : while ( $the_query->have_posts() ) : $the_query->the_post(); ?>
						<tr data-href="<?php echo get_the_permalink();?>">
							<?php the_field('excert_text');?>
						</tr>
					<?php endwhile;	endif;?>
					<?php wp_reset_postdata();?>
					
					<tr><th>138回</th><td>2002年6月29日</td><td>ブラームス 交響曲第1番 他</td><td>ローマン・コフマン</td></tr>
					<tr><th>137回</th><td>2001年12月1日</td><td>ラフマニノフ 交響曲第2番 他</td><td>石川善美</td></tr>
					<tr><th>136回</th><td>2001年6月16日</td><td>ブルックナー 交響曲第4番「ロマンティック」他</td><td>ヨルダン・ダフォフ</td></tr>
					<tr><th>135回</th><td>2000年11月25日</td><td>シューベルト 交響曲第9番「ザ・グレート」他</td><td>石川善美</td></tr>
					<tr><th>134回</th><td>2000年6月24日</td><td>チャイコフスキー 交響曲第6番「悲愴」他</td><td>高宮誠</td></tr>
					<tr><th>133回</th><td>1999年11月27日</td><td>ベートヴェン 交響曲第5番 他</td><td>石川善美</td></tr>
					<tr><th>132回</th><td>1999年6月19日</td><td>シベリウス 交響曲第1番 他</td><td>渡邊康雄</td></tr>
					<tr><th>131回</th><td>1998年11月28日</td><td>ドヴォルザーク 交響曲9番「新世界より」他</td><td>ローマン・コフマン</td></tr>
					<tr><th>130回</th><td>1998年6月20日</td><td>ベートーヴェン 交響曲第9番「合唱」他</td><td>石川善美</td></tr>
					<tr><th>129回</th><td>1997年11月29日</td><td>ブラームス 交響曲第4番 他</td><td>アイダール・トリバエフ</td></tr>
					<tr><th>128回</th><td>1997年6月7日</td><td>チャイコフスキー 交響曲4番 他</td><td>高宮誠</td></tr>
					<tr><th>127回</th><td>1996年11月30日</td><td>ドヴォルザーク 交響曲第8番 他</td><td>ジョセフ・シルヴァースタイン</td></tr>
					<tr><th>126回</th><td>1996年6月8日</td><td>マーラー 交響曲第5番 他</td><td>ゴードン・ライト</td></tr>
					<tr><th>125回</th><td>1995年11月18日</td><td>ブラームス 交響曲第1番 他</td><td>江藤俊哉</td></tr>
					<tr><th>124回</th><td>1995年6月24日</td><td>チャイコフスキー 交響曲第5番 他</td><td>黒岩英臣</td></tr>
					<tr><th>123回</th><td>1994年12月3日</td><td>ブラームス 交響曲第2番 他</td><td>石川善美</td></tr>
					<tr><th>122回</th><td>1994年6月18日</td><td>ラフマニノフ 交響曲第2番 他</td><td>ゴードン・ライト</td></tr>
					<tr><th>121回</th><td>1993年11月20日</td><td>ベートーヴェン 交響曲第1番 他</td><td>ヴォフガング・ポドゥシュカ</td></tr>
					<tr><th>120回</th><td>1993年6月19日</td><td>ベートーヴェン 交響曲第9番「合唱」他</td><td>石川善美</td></tr>
					<tr><th>119回</th><td>1992年12月19日</td><td>ドヴォルザーク 交響曲第9番「新世界より」他</td><td>ヴォフガング・ポドゥシュカ</td></tr>
					<tr><th>118回</th><td>1992年6月13日</td><td>シベリウス 交響曲第2番 他</td><td>渡邊康雄</td></tr>
					<tr><th>117回</th><td>1991年11月23日</td><td>ブラームス 交響曲第4番 他</td><td>ヴォフガング・ポドゥシュカ</td></tr>
					<tr><th>116回</th><td>1991年6月15日</td><td>ベルリオーズ 幻想交響曲 他</td><td>ジョセフ・シルヴァースタイン</td></tr>
					<tr><th>115回</th><td>1990年12月22日</td><td>ブルックナー 交響曲7番 他</td><td>大町陽一郎</td></tr>
					<tr><th>114回</th><td>1990年6月16日</td><td>ショスタコーヴィチ 交響曲10番 他</td><td>井上道義</td></tr>
					<tr><th>113回</th><td>1989年11月28日</td><td>ブラームス 交響曲第1番 他</td><td>田中良和</td></tr>
					<tr><th>112回</th><td>1989年6月17日</td><td>ドヴォルザーク　チェロ協奏曲他</td><td>菊地俊一<br />チェロ：レイヌ・フラショ</td></tr>
					<tr><th>111回</th><td>1988年11月28日</td><td>チャイコフスキー 交響曲6番「悲愴」他</td><td>江藤俊哉</td></tr>
					<tr><th>110回</th><td>1988年6月11日</td><td>ベートーヴェン 交響曲第9番「合唱」他</td><td>菊地俊一</td></tr>
					<tr><th>109回</th><td>1987年12月29日</td><td>ブラームス 交響曲第2番 他</td><td>外山雄三</td></tr>
					<tr><th>108回</th><td>1987年6月6日</td><td>ベートーヴェン 交響曲第7番 他</td><td>山田一雄</td></tr>
					<tr><th>107回</th><td>1986年11月29日</td><td>シベリウス 交響曲第2番 他</td><td>井上道義</td></tr>
					<tr><th>106回</th><td>1986年6月14日</td><td>チャイコフスキー 交響曲第5番 他</td><td>ヴィクター・フェルドブリル</td></tr>
					<tr><th>105回</th><td>1985年11月30日</td><td>ブラームス 交響曲第4番 他</td><td>ヴィクター・フェルドブリル</td></tr>
					<tr><th>104回</th><td>1985年6月15日</td><td>ドヴォルザーク 交響曲第7番 他</td><td>田中一嘉</td></tr>
					<tr><th>103回</th><td>1984年12月1日</td><td>ベートーヴェン 交響曲第5番「運命」他</td><td>大町陽一郎</td></tr>
					<tr><th>102回</th><td>1984年6月2日</td><td>プロコフィエフ　交響曲第7番「青春」他</td><td>井上道義</td></tr>
					<tr><th>101回</th><td>1983年11月26日</td><td>ブラームス 交響曲第1番 他</td><td>山田一雄</td></tr>
					<tr><th>100回</th><td>1983年6月18日</td><td>ベートーヴェン 交響曲第9番「合唱」他</td><td>高宮誠</td></tr>
					<tr><th>99回</th><td>1982年12月11日</td><td>ドヴォルザーク 交響曲第8番 他</td><td>菊地俊一</td></tr>
					<tr><th>98回</th><td>1982年6月17日</td><td>ブラームス 交響曲第三番 他</td><td>山田一雄</td></tr>
					<tr><th>97回</th><td>1981年12月5日</td><td>シューマン 交響曲第3番「ライン」他</td><td>大町陽一郎</td></tr>
					<tr><th>96回</th><td>1981年7月11日</td><td>ショーソン 交響曲 他</td><td>ズデニェク・コシュラー</td></tr>
					<tr><th>95回</th><td>1980年12月6日</td><td>チャイコフスキー 交響曲第6番「悲愴」他</td><td>高宮誠<br/>ヴァイオリン:江藤俊哉</td></tr>
					<tr><th>94回</th><td>1980年6月21日</td><td>ベートーヴェン 交響曲第7番 他</td><td>大町陽一郎</td></tr>
					<tr><th>93回</th><td>1979年12月15日</td><td>ブラームス 交響曲第2番 他</td><td>高宮誠</td></tr>
					<tr><th>92回</th><td>1979年6月2日</td><td>ベルリオーズ 幻想交響曲 他</td><td>小林研一郎</td></tr>
					<tr><th>91回</th><td>1978年12月16日</td><td>シベリウス 交響曲第2番 他</td><td>佐藤功太郎</td></tr>
					<tr><th>90回</th><td>1978年6月26日</td><td>ベートーヴェン 交響曲第9番「合唱」他</td><td>山田一雄</td></tr>
					<tr><th>89回</th><td>1977年11月28日</td><td>サンサーンス チェロ協奏曲他</td><td>小泉和裕<br />チェロ：レイヌ・フラショ</td></tr>
					<tr><th>88回</th><td>1977年6月25日</td><td>ブルックナー 交響曲第4番「ロマンティック」他</td><td>デイヴィット・ハウエル</td></tr>
					<tr><th>87回</th><td>1976年12月6日</td><td>チャイコフスキー 交響曲第6番「悲愴」他</td><td>山田一雄<br/>ヴァイオリン:外山滋</td></tr>
					<tr><th>86回</th><td>1976年6月24日</td><td>ドヴォルザーク 交響曲第8番 他</td><td>小泉和裕</td></tr>
					<tr><th>85回</th><td>1975年12月6日</td><td>ベートーヴェン 交響曲第3番「英雄」他</td><td>高宮誠</td></tr>
					<tr><th>84回</th><td>1975年6月28日</td><td>ブラームス 交響曲第1番 他</td><td>ペーター・シュヴァルツ</td></tr>
					<tr><th>83回</th><td>1974年12月14日</td><td>ブラームス 交響曲第3番他</td><td>ペーター・シュヴァルツ</td></tr>
					<tr><th>82回</th><td>1974年6月15日</td><td>ドヴォルザーク チェロ協奏曲</td><td>高宮誠<br/>チェロ：レイヌ・フラショ</td></tr>
					<tr><th>81回</th><td>1973年12月8日</td><td>チャイコフスキー 交響曲第5番 他</td><td>尾高忠明</td></tr>
					<tr><th>80回</th><td>1973年6月23日</td><td>ベートーヴェン 交響曲第9番「合唱」他</td><td>高宮誠</td></tr>
					<tr><th>79回</th><td>1972年12月9日</td><td>ブラームス 交響曲第2番 他</td><td>山田一雄</td></tr>
					<tr><th>78回</th><td>1972年6月24日</td><td>モーツァルト 交響曲第35番「ハフナー」他</td><td>伴有雄</td></tr>
					<tr><th>77回</th><td>1971年11月26日</td><td>ドヴォルザーク 交響曲第9番「新世界より」</td><td>高宮誠</td></tr>
					<tr><th>76回</th><td>1971年6月13日</td><td>ブラームス 交響曲第4番 他</td><td>久山恵子</td></tr>
					<tr><th>75回</th><td>1970年12月5日</td><td>ベートーヴェン 交響曲第4番 他</td><td>山田一雄</td></tr>
					<tr><th>74回</th><td>1970年6月13日</td><td>ベートーヴェン 交響曲第3番「英雄」他</td><td>高宮誠<br/>ヴァイオリン:外山滋</td></tr>
					<tr><th>73回</th><td>1969年11月22日</td><td>ブラームス 交響曲第1番 他</td><td>高宮誠</td></tr>
					<tr><th>72回</th><td>1969年6月14日</td><td>ドヴォルザーク 交響曲第8番 他</td><td>高宮誠<br>オーボエ：鈴木清三</td></tr>
					<tr><th>71回</th><td>1968年11月30日</td><td>ベートーヴェン 交響曲第6番「田園」他</td><td>熊田為宏</td></tr>
					<tr><th>70回</th><td>1968年6月15日</td><td>ベートーヴェン 交響曲第9番「合唱」他</td><td>山田和男</td></tr>
					<tr><th>69回</th><td>1967年11月11日</td><td>ベートーヴェン 交響曲第5番「運命」他</td><td>奥田道昭<br>ホルン:バリー・タックウェル</td></tr>
					<tr><th>68回</th><td>1967年6月17日</td><td>チャイコフスキー 交響曲第5番 他</td><td>浜田徳昭</td></tr>
					<tr><th>67回</th><td>1966年11月26日</td><td>ベートーヴェン 交響曲第7番 他</td><td>遠藤雅古</td></tr>
					<tr><th>66回</th><td>1966年6月18日</td><td>芥川也寸志 交響管弦楽のための音楽 他</td><td>山田和男</td></tr>
					<tr><th>65回</th><td>1965年11月27日</td><td>チャイコフスキー 交響曲第6番「悲愴」他</td><td>奥田道昭</td></tr>
					<tr><th>64回</th><td>1965年6月12日</td><td>モーツァルト 交響曲第41番 他</td><td>上田仁</td></tr>
					<tr><th>63回</th><td>1964年12月5日</td><td>ブラームス 交響曲第1番 他</td><td>山田和男</td></tr>
					<tr><th>62回</th><td>1964年6月13日</td><td>シベリウス 交響曲第2番 他</td><td>奥田道昭</td></tr>
					<tr><th>61回</th><td>1963年11月16日</td><td>ベートーヴェン　交響曲第3番「英雄」他</td><td>熊田為宏</td></tr>
					<tr><th>60回</th><td>1963年6月8日</td><td>ベートーヴェン 交響曲第9番「合唱」他</td><td>金子登</td></tr>
					<tr><th>59回</th><td>1962年11月29日</td><td>ベートーヴェン 交響曲第5番「運命」他</td><td>久山恵子</td></tr>
					<tr><th>58回</th><td>1962年6月16日</td><td>ベートーヴェン 交響曲第2番 他</td><td>奥田道昭</td></tr>
					<tr><th>57回</th><td>1961年11月28日</td><td>ブラームス 交響曲第4番 他</td><td>浜田徳昭</td></tr>
					<tr><th>56回</th><td>1961年6月17日</td><td>スメタナ「わが祖国」よりモルダウ 他</td><td>奥田道昭</td></tr>
					<tr><th>55回</th><td>1960年11月19日</td><td>ベートーヴェン 交響曲第3番「英雄」他</td><td>マンフレート・グルリット</td></tr>
					<tr><th>54回</th><td>1960年6月18日</td><td>ドヴォルザーク 交響曲第9番「新世界より」他</td><td>若杉弘</td></tr>
					<tr><th>53回</th><td>1959年11月28日</td><td>チャイコフスキー 交響曲第5番 他</td><td>久山恵子</td></tr>
					<tr><th>52回</th><td>1959年6月13日</td><td>ブラームス 交響曲第1番 他</td><td>山本直純</td></tr>
					<tr><th>51回</th><td>1958年11月29日</td><td>ベートーヴェン 交響曲第1番 他</td><td>山本直純</td></tr>
					<tr><th>50回</th><td>1958年6月28日</td><td>ベートーヴェン 交響曲第9番「合唱」 他</td><td>金子登</td></tr>
					<tr><th>49回</th><td>1957年11月30日</td><td>ドビュッシー 小組曲 他</td><td>熊田為宏</td></tr>
					<tr><th>48回</th><td>1957年6月29日</td><td>ベートーヴェン 交響曲第7番 他</td><td>白根六郎</td></tr>
					<tr><th>47回</th><td>1956年12月1日</td><td>モーツァルト レクイエム 他</td><td>熊田為宏</td></tr>
					<tr><th>46回</th><td>1956年6月30日</td><td>ベートーヴェン 交響曲第4番 他</td><td>小川卓郎</td></tr>
					<tr><th>45回</th><td>1955年11月26日</td><td>ドヴォルザーク 交響曲第9番「新世界より」他</td><td>白根六郎</td></tr>
					<tr><th>44回</th><td>1955年6月25日</td><td>ベートーヴェン 交響曲第5番「運命」他</td><td>白根六郎</td></tr>
					<tr><th>43回</th><td>1954年12月4日</td><td>ベートーヴェン 交響曲第9番「合唱」 他</td><td>熊田為宏</td></tr>
					<tr><th>42回</th><td>1954年6月12日</td><td>シューベルト 交響曲第4番 他</td><td>白根六郎</td></tr>
					<tr><th>41回</th><td>1953年10月31日</td><td>モーツァルト 交響曲第41番 他</td><td>白根六郎</td></tr>
					<tr><th>40回</th><td>1953年7月4日</td><td>ベートーヴェン 交響曲第8番 他</td><td>白根六郎</td></tr>
					<tr><th>39回</th><td>1952年11月15日</td><td>ベートーヴェン 交響曲第3番「英雄」他</td><td>金子登</td></tr>
					<tr><th>38回</th><td>1952年6月1日</td><td>ハイドン 交響曲第100番「軍隊」他</td><td>白根六郎</td></tr>
					<tr><th>37回</th><td>1951年11月17日</td><td>ベートーヴェン ピアノ協奏曲第5番「皇帝」他</td><td>白根六郎</td></tr>
					<tr><th>36回</th><td>1951年6月24日</td><td>メンデルスゾーン 交響曲第4番「イタリア」他</td><td>白根六郎</td></tr>
					<tr><th>35回</th><td>1950年11月25日</td><td>ベートーヴェン 交響曲第7番 他</td><td>白根六郎</td></tr>
					<tr><th>34回</th><td>1950年6月11日</td><td>シューベルト 交響曲第5番 他</td><td>白根六郎</td></tr>
					<tr><th>33回</th><td>1949年11月20日</td><td>ベートーヴェン 交響曲第9番「合唱」</td><td>金子登</td></tr>
					<tr><th>32回</th><td>1949年6月28日</td><td>ベートーヴェン 交響曲第9番「合唱」より第1楽章 他</td><td>白根六郎</td></tr>
					<tr><th>31回</th><td>1948年11月7日</td><td>バッハ 管弦楽組曲第2番 他</td><td>白根六郎</td></tr>
					<tr><th>30回</th><td>1948年6月26日</td><td>ベートーヴェン ピアノ協奏曲第1番 他</td><td>白根六郎</td></tr>
					<tr><th>29回</th><td>1947年11月22日</td><td>ベートーヴェン 交響曲第1番 他</td><td>白根六郎</td></tr>
					<tr><th>28回</th><td>1943年11月14日</td><td>ベートーヴェン 交響曲第5番「運命」他</td><td>白根六郎</td></tr>
					<tr><th>27回</th><td>1943年5月28日</td><td>シューベルト 交響曲第8番「未完成」他</td><td>斉藤弘</td></tr>
					<tr><th>25回</th><td>1942年6月21日</td><td>モーツァルト ピアノ協奏曲第20番 他</td><td>白根六郎</td></tr>
					<tr><th>24回</th><td>1941年10月30日</td><td>ハイドン 交響曲第94番「驚愕」他</td><td>白根六郎</td></tr>
					<tr><th>23回</th><td>1941年6月19日</td><td>ハイドン 交響曲第13番 他</td><td>白根六郎</td></tr>
					<tr><th>22回</th><td>1940年11月10日</td><td>ハイドン チェロ協奏曲 第2番 他</td><td>金子登</td></tr>
					<tr><th>21回</th><td>1940年6月16日</td><td>シューベルト 交響曲第8番「未完成」他</td><td>石川正生</td></tr>
					<tr><th>20回</th><td>1939年11月19日</td><td>ベートーヴェン 交響曲1番 他</td><td>金子登</td></tr>
					<tr><th>19回</th><td>1939年6月22日</td><td>ラロ チェロ協奏曲 他</td><td>米地秀三</td></tr>
					<tr><th>18回</th><td>1938年11月15日</td><td>ベートーヴェン 交響曲第5番「運命」他</td><td>斉藤弘</td></tr>
					<tr><th>17回</th><td>1937年11月27日</td><td>近衛秀麿編曲 雅楽「越天楽」他</td><td>高橋功</td></tr>
					<tr><th>16回</th><td>1937年6月20日</td><td>ベートーヴェン 交響曲2番 他</td><td>斉藤弘</td></tr>
					<tr><th>15回</th><td>1936年11月1日</td><td>モーツァルト 交響曲40番 他</td><td>木村弦三</td></tr>
					<tr><th>14回</th><td>1936年6月7日</td><td>ベートーヴェン　交響曲1番他</td><td>斉藤弘</td></tr>
					<tr><th>13回</th><td>1935年10月27日</td><td>ビゼー 「カルメン」組曲 他</td><td>斉藤弘</td></tr>
					<tr><th>12回</th><td>1934年11月4日</td><td>グリーグ 「ペール・ギュント」第2組曲 他</td><td>斉藤弘</td></tr>
					<tr><th>11回</th><td>1934年6月9日</td><td>モーツァルト 交響曲第39番 他</td><td>斉藤弘</td></tr>
					<tr><th>10回</th><td>1933年10月28日</td><td>グリーグ 「ペール・ギュント」第1組曲 他</td><td>斉藤弘</td></tr>
					<tr><th>9回</th><td>1933年6月11日</td><td>ハイドン　交響曲104番「ロンドン」他</td><td>斉藤弘</td></tr>
					<tr><th>8回</th><td>1932年10月29日</td><td>ハイドン 交響曲13番 他</td><td>斉藤弘</td></tr>
					<tr><th>7回</th><td>1931年11月5日</td><td>ベートーヴェン 交響曲第8番 他</td><td>斉藤弘</td></tr>
					<tr><th>6回</th><td>1930年10月25日</td><td>ベートーヴェン 交響曲第1番 他</td><td>斉藤弘</td></tr>
					<tr><th>5回</th><td>1929年10月3日</td><td>メンデルスゾーン 結婚行進曲他</td><td>斉藤弘</td></tr>
					<tr><th>4回</th><td>1928年11月8日</td><td>シューベルト 交響曲第8番「未完成」他</td><td>斉藤弘</td></tr>
					<tr><th>3回</th><td>1928年3月3日</td><td>ボイエルデュー 「バグダッドの大守」序曲 他</td><td>斉藤弘</td></tr>
					<tr><th>2回</th><td>1927年6月16日</td><td>モーツァルト 「魔笛」序曲他</td><td>斉藤弘</td></tr>
					<tr><th>1回</th><td>1926年2月6日</td><td>ハイドン 交響曲第100番「軍隊」より第3楽章 他</td><td>斉藤弘</td></tr>
				</table>
			</div>

		</section>
	</section><!-- / コンテンツ -->
	<div id="page-up">
		<a href="#" class="btn btn-info btn-lg"><span class="glyphicon glyphicon-arrow-up"></span></a>
	</div>
</div><!-- / WRAPPER -->

<?php get_footer();?>