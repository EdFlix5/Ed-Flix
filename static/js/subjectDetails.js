// Not needed
// if ($(window).innerHeight() > $(".footer").offset().top) {
//   var offset = $(window).innerHeight() - $(".footer").outerHeight();
//   $(".footer").css(
//     "margin-top",
//     parseInt($(".footer").css("marginTop"), 10) +
//       offset -
//       $(".footer ").offset().top
//   );
// }

const links = document.querySelectorAll(".navbar-list a");
links.forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    const id = this.getAttribute("href");
    id.scrollIntoView({ behavior: "smooth" });
  });
});
