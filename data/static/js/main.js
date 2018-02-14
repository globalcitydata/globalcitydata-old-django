$(function () {
  $('.lazy').lazy();
});

$(".hiddenbtn").click(function() {
  var lable = $(".hiddenbtn").text().trim();
  var hidden = $(".hiddenText").text().trim();
  if (lable == "Request dataset access") {
    $(".hiddenbtn").text(hidden)
  } else {
    $(".hiddenbtn").text("Request dataset access")
  }
});