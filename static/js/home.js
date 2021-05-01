$(".sidebar-dropdown > a").click(function () {
  $(".sidebar-submenu").slideUp(200);
  if ($(this).parent().hasClass("active")) {
    $(".sidebar-dropdown").removeClass("active");
    $(this).parent().removeClass("active");
  } else {
    $(".sidebar-dropdown").removeClass("active");
    $(this).next(".sidebar-submenu").slideDown(200);
    $(this).parent().addClass("active");
  }
});

$("#close-sidebar").click(function () {
  $(".page-wrapper").removeClass("toggled");
});
$("#show-sidebar").click(function () {
  $(".page-wrapper").addClass("toggled");
});

// After Login
/*
const singleCardWidth = document.querySelector(".card").offsetWidth;

const recommendCardNumber = document.querySelector(".recommend")
  .childElementCount;
const recommendTotalWidth = (recommendCardNumber + 2) * singleCardWidth;
document.querySelector(".recommend").style.width = `${recommendTotalWidth}px`;

const mostViewedCardNumber = document.querySelector(".most-viewed")
  .childElementCount;
const mostViewedTotalWidth = (mostViewedCardNumber + 2) * singleCardWidth;
document.querySelector(
  ".most-viewed"
).style.width = `${mostViewedTotalWidth}px`;
*/
