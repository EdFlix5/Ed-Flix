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
