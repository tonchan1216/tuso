<?php
function is_tree( $pid ) {      // $pid = 指定したページの ID
    global $post;         // $post に現在の固定ページの情報をロード

    if ( is_page($pid) )
        return true;            // その固定ページまたはサブページの場合

    $anc = get_post_ancestors( $post->ID );
    foreach ( $anc as $ancestor ) {
        if( is_page() && $ancestor == $pid ) {
            return true;
        }
    }

    return false;  // その固定ページではない、または親ページではない場合
}

remove_filter ( 'the_content', 'wpautop' );
remove_filter ( 'the_excerpt', 'wpautop' );

add_theme_support('post-thumbnails');

?>