const toggleCardText = (moreBranch, dotBranch) => {
  const dots = document.getElementById(dotBranch);
  const more = document.getElementById(moreBranch);

  if (more.style.display === "none") {
    more.style.display = "inline";
    dots.innerHTML = "less...";
  } else {
    more.style.display = "none";
    dots.innerHTML = "more...";
  }
};
