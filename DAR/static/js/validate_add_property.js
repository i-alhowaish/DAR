document.addEventListener("DOMContentLoaded", function() {
  function validatePositiveDecimal(inputId) {
      var inputElement = document.getElementById(inputId);
      if (inputElement) {
          inputElement.addEventListener("input", function() {
              var value = parseFloat(this.value);
              if (value < 0) {
                Swal.fire({
                    icon: "error",
                    title: "خطأ",
                    text: "الخانة لا يمكن ان تكون بالسالب",
                  });
                  this.value = '';
              }
          });
      }
  }

  // Validate fields
  validatePositiveDecimal("priceInput");
  validatePositiveDecimal("lengthInput");
  validatePositiveDecimal("widthInput");
  // Assuming "totalLengthInput" is the ID for total length field
  validatePositiveDecimal("totalLengthInput");
  validatePositiveDecimal("yearBuilt");
  validatePositiveDecimal("sidesInput");
  validatePositiveDecimal("bathroomsInput");
  validatePositiveDecimal("bedroomInput");
});



// Example validation for the number of sides
document.getElementById('sidesInput').addEventListener('input', function() {
    var value = parseInt(this.value, 10);
    if (value < 1 || value > 4) {
        Swal.fire({
            icon: "error",
            title: "خطأ",
            text: "عدد الواجهات يكون بين 1 الى 4",
          });
      this.value = ''; // Reset the input
    }
  });

  
