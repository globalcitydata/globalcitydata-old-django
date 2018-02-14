$(function () {
  $('.lazy').lazy();
});

$(".btn").click(function() {
  var lable = $(".btn").text().trim();
  var hidden = $(".hiddenText").text().trim();
  if (lable == "Request dataset access") {
    $(".btn").text(hidden)
  } else {
    $(".btn").text("Request dataset access")
  }
});