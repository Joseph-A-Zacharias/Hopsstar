// Wait for the window to load
window.onload = function() {
  // Define the time in milliseconds after which to hide the cover
  var hideDelay = 10; // 3000 milliseconds = 3 seconds

  // Function to hide the cover after a delay
  function hideCover() {
      var cover = document.getElementById('cover');
      cover.style.opacity = '0'; // Start fading out
      setTimeout(function() {
          cover.style.display = 'none'; // Hide cover after animation completes
      }, 1200); // Wait for the same duration as animation (1.2s)
  }

  // Hide the cover after the specified delay
  setTimeout(hideCover, hideDelay);
};

document.addEventListener('DOMContentLoaded', () => {
  const loader = document.getElementById('themainloader');
  const popupContainer = document.getElementById('popup-container');
  const loadingLoaders = document.querySelectorAll('.loadingloader');
  const openPopupLinks = document.querySelectorAll('#open-popup');

  // Hide the loader when the page is shown (e.g., using the back button)
  window.addEventListener('pageshow', () => {
    loader.style.display = 'none';
  });

  // Handle click events for elements with the 'loadingloader' class
  loadingLoaders.forEach(el => {
    el.addEventListener('click', event => {
      const form = event.target.closest('form');
      if (!form || form.checkValidity()) {
        loader.style.display = 'block';
      } else {
        event.preventDefault();
      }
    });
  });

  // Handle click events for elements with id 'open-popup'
  openPopupLinks.forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      popupContainer.style.display = popupContainer.style.display === 'flex' ? 'none' : 'flex';
      console.log("popup-toggle");
    });
  });

  // Close popup when clicking outside of it
  popupContainer.addEventListener('click', event => {
    if (event.target === popupContainer) {
      popupContainer.style.display = 'none';
      console.log("popup-hide");
    }
  });
});

function onSubmit(event) {
    event.preventDefault();
    grecaptcha.ready(function() {
      grecaptcha.execute(function(token) {
        var form = document.getElementById("submit-form");
        form.querySelector('input[name="g-recaptcha-response"]').value = token;
        form.submit();
      });
    });
  }
