document.addEventListener('DOMContentLoaded', function () {
  var signUpLink = document.querySelector('.sign-up-link');

  signUpLink.addEventListener('click', function () {
      // Get the URL dynamically from Django template
      var registerUrl = 'login';
      
      // Redirect to the dynamically obtained URL
      window.location.href = registerUrl;
  });
});
document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('.form-dar');
  const phoneNumberInput = document.getElementById('phone_number');
  const emailInput = document.querySelector('input[type="email"]');

  form.addEventListener('submit', function(event) {
      // Validate Phone Number
      const phoneNumber = phoneNumberInput.value;
      const phoneRegex = /^05\d{8}$/; // Starts with '05' and followed by exactly 8 digits

      if (!phoneRegex.test(phoneNumber)) {
          // alert('رقم الجوال يجب أن يبدأ بـ05 ويتكون من 10 أرقام.');
          Swal.fire({
            icon: "error",
            title: "خطأ",
            text:'رقم الجوال يجب أن يبدأ بـ05 ويتكون من 10 أرقام.',
          });
          this.value = '';
      }
          event.preventDefault(); // Stop form submission
          phoneNumberInput.focus(); // Focus on phone number input for correction
          return false;
      }

      
  );
});
