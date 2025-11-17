document.addEventListener("DOMContentLoaded", function () {
  const div = document.querySelector("#hello");
  
  fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
  .then(response => response.json())
  .then(data => {
      div.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error:', error)
    });
});
