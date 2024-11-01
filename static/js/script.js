window.onload = function() {
  var hideDelay = 10;
  function hideCover() {
    var cover = document.getElementById('cover');
    cover.style.opacity = '0';
    setTimeout(function() {
      cover.style.display = 'none';
    }, 1200);
  }
  setTimeout(hideCover, hideDelay);
};

document.addEventListener('DOMContentLoaded', () => {
  const loader = document.getElementById('themainloader');
  const popupContainer = document.getElementById('popup-container');
  const loadingLoaders = document.querySelectorAll('.loadingloader');
  const openPopupLinks = document.querySelectorAll('#open-popup');
  window.addEventListener('pageshow', () => {
    loader.style.display = 'none';
  });
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
  openPopupLinks.forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      popupContainer.style.display = popupContainer.style.display === 'flex' ? 'none' : 'flex';
      console.log("popup-toggle");
    });
  });
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

  function dropDownFaq(){
    const detailsElements = document.querySelectorAll(".faqcontanier2 .drop-down");

    detailsElements.forEach((details) => {
      details.addEventListener("click", () => {
        // Close all other open details elements
        detailsElements.forEach((otherDetails) => {
          if (otherDetails !== details) {
            otherDetails.open = false;
          }
        });
      });
    });
  }