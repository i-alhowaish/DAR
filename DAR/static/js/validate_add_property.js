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

  document.addEventListener('DOMContentLoaded', function() {

    let lt= document.getElementById('latInput');
    let lg = document.getElementById('lngInput');

    form.addEventListener('submit', function(event) {
        // Validate Phone Number
        const ltv = lt.value;
        const lgv = lg.value; // Starts with '05' and followed by exactly 8 digits

        if (ltv == ''||lgv=='') {
            // alert('رقم الجوال يجب أن يبدأ بـ05 ويتكون من 10 أرقام.');
            Swal.fire({
              icon: "error",
              title: "خطأ",
              text:'الرجاء اختيار موقع على الخارطة',
            });
            this.value = '';

            event.preventDefault(); // Stop form submission
            phoneNumberInput.focus(); // Focus on phone number input for correction
            return false;
        }

    }
    );
  });