window.addEventListener('load', () => {
    // if there is an erorr -- > show modal
    if (document.querySelector(".invalid-feedback")) {
      document.querySelector('button[data-bs-target="#updateForm"]').click();
    }
})