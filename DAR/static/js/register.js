document.addEventListener('DOMContentLoaded', function () {
  var signUpLink = document.querySelector('.sign-up-link');

  signUpLink.addEventListener('click', function () {
      // Get the URL dynamically from Django template
      var registerUrl = 'login';
      
      // Redirect to the dynamically obtained URL
      window.location.href = registerUrl;
  });
});
