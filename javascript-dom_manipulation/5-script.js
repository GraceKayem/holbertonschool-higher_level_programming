const header = document.querySelector("header");
const div = document.querySelector("#update_header")

div.addEventListener("click", function () {
  header.textContent = "New Header!!!";
});
