const singleCardWidth = document.querySelector(".card").offsetWidth;

const recommendCardNumber = document.querySelectorAll(".card-recommend").length;
const recommendTotalWidth = (recommendCardNumber + 1) * singleCardWidth;
document.querySelector(".recommend").style.width = `${recommendTotalWidth}px`;

const mostViewedCardNumber = document.querySelectorAll(".card-mostvisited")
  .length;
const mostViewedTotalWidth = (mostViewedCardNumber + 1) * singleCardWidth;
document.querySelector(
  ".most-viewed"
).style.width = `${mostViewedTotalWidth}px`;

// Card slider
const cardsRecommend = document.querySelectorAll(".card-recommend");
const cardsMostVisited = document.querySelectorAll(".card-mostvisited");
const rightArrow1 = document.querySelector(".right-arrow1");
const leftArrow1 = document.querySelector(".left-arrow1");
const rightArrow2 = document.querySelector(".right-arrow2");
const leftArrow2 = document.querySelector(".left-arrow2");
let oldPositionRecommend = 0;
let oldPositionMostViewed = 0;

// When recommended cards are empty
if (recommendCardNumber < 1) {
  document.querySelector(".no-card").style.display = "block";
}

// Hide Arrow when card is less than 4
if (recommendCardNumber <= 4) {
  rightArrow1.style.display = "none";
  leftArrow1.style.display = "none";
}

// console.log(recommendCardNumber, mostViewedCardNumber);

if (mostViewedCardNumber <= 4) {
  rightArrow2.style.display = "none";
  leftArrow2.style.display = "none";
}

const onRightClick1 = function () {
  if (Math.abs((oldPositionRecommend * 614) / 40 - 1228) < recommendTotalWidth)
    oldPositionRecommend -= 40;
  cardsRecommend.forEach((c, i) => {
    c.style.transform = `translateX(${oldPositionRecommend}vw)`;
  });
  /*
  console.log(
    "clickedRight",
    (oldPositionRecommend * 614) / 40 - 1228,
    recommendTotalWidth
  );
  */
};

const onRightClick2 = function () {
  if (
    Math.abs((oldPositionMostViewed * 614) / 40 - 1228) < mostViewedTotalWidth
  )
    oldPositionMostViewed -= 40;
  cardsMostVisited.forEach((c, i) => {
    c.style.transform = `translateX(${oldPositionMostViewed}vw)`;
  });
  /*
  console.log(
    "clickedRight",
    (oldPositionMostViewed * 614) / 40 - 1228,
    mostViewedTotalWidth
  );
  */
};

const onLeftClick1 = function () {
  if (oldPositionRecommend < 0) {
    oldPositionRecommend += 40;
  }
  cardsRecommend.forEach((c, i) => {
    c.style.transform = `translateX(${oldPositionRecommend}vw)`;
  });
  // console.log("clickedLeft", oldPositionRecommend);
};

const onLeftClick2 = function () {
  if (oldPositionMostViewed < 0) {
    oldPositionMostViewed += 40;
  }
  cardsMostVisited.forEach((c, i) => {
    c.style.transform = `translateX(${oldPositionMostViewed}vw)`;
  });
  // console.log("clickedLeft", oldPositionMostViewed);
};

rightArrow1.addEventListener("click", onRightClick1);
leftArrow1.addEventListener("click", onLeftClick1);
rightArrow2.addEventListener("click", onRightClick2);
leftArrow2.addEventListener("click", onLeftClick2);
