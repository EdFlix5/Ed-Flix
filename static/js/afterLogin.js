const singleCardWidth = document.querySelector(".card").offsetWidth;

const recommendCardNumber = document.querySelector(".recommend")
  .childElementCount;
const recommendTotalWidth = (recommendCardNumber + 1) * singleCardWidth;
document.querySelector(".recommend").style.width = `${recommendTotalWidth}px`;

const mostViewedCardNumber = document.querySelector(".most-viewed")
  .childElementCount;
const mostViewedTotalWidth = (mostViewedCardNumber + 1) * singleCardWidth;
document.querySelector(
  ".most-viewed"
).style.width = `${mostViewedTotalWidth}px`;

const cardsRecommend = document.querySelectorAll(".card-recommend");
const cardsMostVisited = document.querySelectorAll(".card-mostvisited");
const rightArrow1 = document.querySelector(".right-arrow1");
const leftArrow1 = document.querySelector(".left-arrow1");
const rightArrow2 = document.querySelector(".right-arrow2");
const leftArrow2 = document.querySelector(".left-arrow2");
const onLeftClick = function (cardType) {
  cardType.forEach((c, i) => {
    c.style.transform = `translateX(0)`;
  });
};
const onRightClick = function (cardType) {
  cardType.forEach((c, i) => {
    c.style.transform = `translateX(-85vw)`;
  });
};
rightArrow1.addEventListener("click", () => onRightClick(cardsRecommend));
leftArrow1.addEventListener("click", () => onLeftClick(cardsRecommend));
rightArrow2.addEventListener("click", () => onRightClick(cardsMostVisited));
leftArrow2.addEventListener("click", () => onLeftClick(cardsMostVisited));
