function removeFavorite(element) {
  // Assuming the card to be removed is two levels up in the DOM hierarchy from the clicked "X" icon.
  element.closest('.col').remove();
}

// Initialize Bootstrap tooltips
$(function () {
  $('[data-bs-toggle="tooltip"]').tooltip();
});
