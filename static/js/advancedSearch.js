const checkBox = document.querySelector("#adv-search-check");
const label = document.querySelector(".adv-search-label span");
// document.body.style.overflowX = "hidden";

var cards = [];

var prev = "";

checkBox.addEventListener("click", () => {
  checkBox.checked
    ? (label.innerHTML = "Advanced Search")
    : (label.innerHTML = "Advanced Search");

  if (checkBox.checked == true) {
    query = "query=" + $("#adv-search-check").val();
    $.ajax({
      type: "GET",
      url: "/api/advancedSearch",
      data: query, // serializes the form's elements.
      success: function (data) {
        data = JSON.parse(data);
        cards = [];
        for (let i = 0; i < data.length; i++) {
          var card = ` <div class="card advanced">
                    <div class="image-container">
                      <div class="subject-name">
                        <h2>${data[i].title}</h2>
                        <h5>${data[i].subtitle}</h5>
                        <a href="{% url 'contentView' %}?id=${data[i].id}"><span class="read">READ NOW</span></a>
                      </div>
                      <div class="subject-short">${data[i].subject_code}</div>
                    </div>
                    <div class="author">
                      <p>
                        Author:
                        <span class="author-name">${data[i].author}</span> |
                        <span class="author-duration">size: ${data[i].file_size}</span>
                      </p>
                    </div>
                  </div>`;
          cards.push(card);
        }

        prev = $(".subject-container").html();
        $(".subject-container").html(cards);
      },
    });
  } else {
    $(".advanced").remove();
    $(".subject-container").html(prev);
  }
});
