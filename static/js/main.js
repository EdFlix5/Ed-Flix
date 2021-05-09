$(function () {
  $("a.page-scroll").bind("click", function (event) {
    var $anchor = $(this);
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: $($anchor.attr("href")).offset().top,
        },
        1500,
        "easeInOutExpo"
      );
    event.preventDefault();
  });
});

// Highlight the top nav as scrolling occurs
$("body").scrollspy({
  target: ".navbar-fixed-top",
});

// Closes the Responsive Menu on Menu Item Click
$(".navbar-collapse ul li a").click(function () {
  $(".navbar-toggle:visible").click();
});

function viewModal() {
  $(".auth").toggle();
}

$(document).mouseup(function (e) {
  var container = $(".wrap");

  // if the target of the click isn't the container nor a descendant of the container
  if (!container.is(e.target) && container.has(e.target).length === 0) {
    $(".auth").hide();
  }
});

const btnAnimated = document.querySelector(".btn--animated");
const featureSection = document.querySelector("#features");

btnAnimated.addEventListener("click", (e) => {
  e.preventDefault();
  featureSection.scrollIntoView({ behavior: "smooth" });
});
