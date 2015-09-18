$(function() {
  //page-up
  $("#page-up").hide();
  $(window).scroll(function() {
  	if( $(this).scrollTop() > 60 ){
     $("#page-up").fadeIn();
   }else{
     $("#page-up").fadeOut();
   }
 });
  $("#page-up a").click(function() {
    $("body").animate({
      scrollTop:0
    },500);
    return false;
  });

  //contets-link
  $(".contents-link").children("div").hover(
    function(){
      /* mouse enter の処理 */
      $(this).find("p").stop().animate({"top": "6px"}, 800);
    }, 
    function(){
      /* mouse leave の処理 */
      $(this).find("p").stop().animate({"top": "60px"}, 800);
    });

  //audio player
  $('#music-library').find('a').each(function(){
    $(this).attr('href',"https://dl.dropboxusercontent.com/u/10141433/"+$(this).text()+"?dl=1");
  });
  $(".play").click(function() {
    var audio = $("#audio-player")[0];
    //audio.src = $(this).next().attr('href');
    audio.src = "https://dl.dropboxusercontent.com/u/10141433/" + $(this).next().text();
    $('#play-title').text($(this).next().text() + "再生中");
    audio.load();
    audio.play();
    return false;
  })

  //slide on off
  $(".slideList").hide();
  $(".readmore").click(function(){
    $(".slideList").slideToggle(1000,"swing");
  })

  //view-port toggle
  switch ($.cookie("style")){ 
    case "sp":
      $('#sp').addClass("active");
      $('#pc').removeClass("active");
      $('meta[name=viewport]').attr("content","width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no");
      break;
    case "pc":
      $('#sp').removeClass("active");
      $('#pc').addClass("active");
      $('meta[name=viewport]').attr("content","width=1200");
      break;
  }

  $("#view-toggle input[type=radio]").change(function(){
    status =  $(this).val();
    $.cookie("style",status, {expires:30});
    //vp_switch(status);
    location.reload();
    return false;
  })
});

