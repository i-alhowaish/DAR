function getCurrentYear() {
  var currentYear = new Date().getFullYear();
  return currentYear;
}

document.addEventListener("DOMContentLoaded", function () {
  var yearSpan = document.getElementById("year");
  if (yearSpan) {
      yearSpan.textContent = getCurrentYear();
  }
});