const goBack = document.querySelector(".link_404");

goBack.addEventListener("click", (event) => {
    event.preventDefault();
    // Regresa al usuario a la página anterior
    window.history.back();
})