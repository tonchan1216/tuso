<?php 
add_theme_support('post-thumbnails');

//ページャ
//Pagenation
function pagination($pages = '', $range = 2){
  $showitems = ($range * 2)+1;//表示するページ数（５ページを表示）

  global $paged;//現在のページ値
  if(empty($paged)) $paged = 1;//デフォルトのページ

  if($pages == ''){
    global $wp_query;
    $pages = $wp_query->max_num_pages;//全ページ数を取得
    
    //全ページ数が空の場合は、１とする
    if(!$pages){
      $pages = 1;
    }
  }

  //全ページが１でない場合はページネーションを表示する
  if(1 != $pages){
    echo "<div class=\"pagenation\">\n";
    echo "<ul>\n";
   	
   	//Prev：現在のページ値が１より大きい場合は表示
    if($paged > 1) echo "<li class=\"prev\"><a href='".get_pagenum_link($paged - 1)."'>Prev</a></li>\n";

    for ($i=1; $i <= $pages; $i++){
      if (1 != $pages &&( !($i >= $paged+$range+1 || $i <= $paged-$range-1) || $pages <= $showitems )){
        //三項演算子での条件分岐
        echo ($paged == $i)? "<li class=\"active\">".$i."</li>\n":"<li><a href='".get_pagenum_link($i)."'>".$i."</a></li>\n";
      }
    }
  //Next：総ページ数より現在のページ値が小さい場合は表示
    if ($paged < $pages) echo "<li class=\"next\"><a href=\"".get_pagenum_link($paged + 1)."\">Next</a></li>\n";
    echo "</ul>\n";
    echo "</div>\n";
  }
}

add_action( 'init', 'create_post_type' );
function create_post_type() {
  register_post_type( 'concert',
    array(
      'labels' => array(
        'name' => __( '演奏会' ),
        'singular_name' => __( '演奏会' )
        ),
      'public' => true,
      'exclude_from_search' => true,
      'show_in_nav_menus' => false,
      'menu_position' => 10,
      'has_archive' => false,
      'rewrite' => array( 'with_front' => false ),
      'supports' => array('title','editor','thumbnail') 
      )
    );
  register_taxonomy(
    'concert-cat', 
    'concert', 
    array(
      'hierarchical' => true, 
      'update_count_callback' => '_update_post_term_count',
      'label' => '演奏会の分類',
      'singular_label' => '演奏会の分類',
      'public' => true,
      'show_ui' => true
      )
    );
}

add_action( 'init', 'create_post_type_2' );
function create_post_type_2() {
  register_post_type( 'memberonly',
    array(
      'labels' => array(
        'name' => __( '団員専用' ),
        'singular_name' => __( '団員専用' )
        ),
      'public' => true,
      'exclude_from_search' => true,
      'show_in_nav_menus' => false,
      'menu_position' => 10,
      'has_archive' => false,
      'supports' => array('title') 
      )
    );
  register_taxonomy(
    'member-cat', 
    'memberonly', 
    array(
      'hierarchical' => true, 
      'update_count_callback' => '_update_post_term_count',
      'label' => 'カテゴリ',
      'singular_label' => 'カテゴリ',
      'public' => true,
      'show_ui' => true
      )
    );
}