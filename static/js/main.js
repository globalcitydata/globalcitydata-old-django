// $(function () {
//   $('.lazy').lazy();
// });

$(".hiddenbtn").click(function() {
  var lable = $(".hiddenbtn").text().trim();
  var hidden = $(".hiddenText").text().trim();
  if (lable == "Request access") {
    $(".hiddenbtn").text(hidden)
  } else {
    $(".hiddenbtn").text("Request access")
  }
});

// Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });