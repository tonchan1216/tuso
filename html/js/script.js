$(function() {
 	$("div.panel").hide();
  $(".menu").click(function() {
    $(this).toggleClass("menuOpen").next().slideToggle();
  });

  $(".slideList").hide();
  $(".readmore").click(function() {
  	$(".slideList").slideToggle(1000, "swing");
  });

  $("#page-up").hide();
  $(window).scroll(function() {
  	if( $(this).scrollTop() > 60 ){
			$("#page-up").fadeIn();
		}else{
			$("#page-up").fadeOut();
		}
  })
  $("#page-up a").click(function() {
      $("body").animate({
        scrollTop:0
      },500);
      return false;
  })
})