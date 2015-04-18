$(function() {
  $("div.panel").hide();
  $(".menu").click(function() {
    $(this).toggleClass("menuOpen").next().slideToggle();
  });
  $(".slideList").hide();
  $(".readmore").click(function() {
  	$(".slideList").slideToggle(1000, "swing");
  });
})