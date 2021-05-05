const checkBox = document.querySelector("#adv-search-check");
const label = document.querySelector(".adv-search-label span");

checkBox.addEventListener("click", () => {
  checkBox.checked
    ? (label.innerHTML = "Disable Advanced Search")
    : (label.innerHTML = "Enable Advanced Search");
});
