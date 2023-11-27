// Cuando el contenido de la página ha sido completamente cargado.
window.addEventListener('DOMContentLoaded', (event) => {
    // Seleccionar el cuerpo del documento.
    const body = document.querySelector('body');
    // Seleccionar el botón para cambiar de tema.
    const themeBtn = document.querySelector('#theme-btn');
    // Seleccionar el botón para cerrar sesión.
    const logoutButton = document.querySelector('#logout-button');

    // Recuperar el tema guardado en el almacenamiento local.
    // Si no hay tema guardado, establecer el tema por defecto a 'light'.
    let savedTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : 'light';

    // Escuchar evento de click en el botón de tema.
    themeBtn.addEventListener('click', () => {
        // Alternar entre temas light y dark.
        savedTheme = savedTheme === 'light' ? 'dark' : 'light';
        // Actualizar el tema de la página.
        updateTheme(savedTheme);
    });

    // Establecer el tema inicial de la página.
    updateTheme(savedTheme);
});

/**
 * Actualiza el tema del sitio web.
 *
 * @param {string} theme El tema para establecer. Puede ser 'light' o 'dark'.
 */
function updateTheme(theme) {
    // Seleccionar el cuerpo del documento.
    const body = document.querySelector('body');
    // Seleccionar el botón para cambiar de tema.
    const themeBtn = document.querySelector('#theme-btn');
    // Seleccionar el botón para cerrar sesión.
    const logoutButton = document.querySelector('#logout-button');

    // Si el tema es 'light'.
    if (theme === 'light') {
        // Agregar la clase 'light-mode' al cuerpo del documento.
        // Esto debería cambiar el aspecto del sitio web a luz.
        body.classList.add('light-mode');
        // Eliminar la clase 'dark-mode' en caso de que esté presente.
        body.classList.remove('dark-mode');
        // Cambiar el texto del botón de tema a '🌞'.
        themeBtn.textContent = '🌞';
        // Añadir las clases 'btn' y 'btn-primary' para el estilo de Bootstrap.
        logoutButton.classList.add('btn', 'btn-primary');
        // Eliminar la clase 'btn-dark' en caso de que esté presente.
        logoutButton.classList.remove('btn-dark');
    } else {
        // Si el tema no es 'light' (es decir, es 'dark').
        // Eliminar la clase 'light-mode' en caso de que esté presente.
        body.classList.remove('light-mode');
        // Agregar la clase 'dark-mode' al cuerpo del documento.
        // Esto debería cambiar el aspecto del sitio web a oscuro.
        body.classList.add('dark-mode');
        // Cambiar el texto del botón de tema a '🌚'.
        themeBtn.textContent = '🌚';
        // Añadir las clases 'btn' y 'btn-dark' para el estilo de Bootstrap.
        logoutButton.classList.add('btn', 'btn-dark');
        // Eliminar la clase 'btn-primary' en caso de que esté presente.
        logoutButton.classList.remove('btn-primary');
    }
    // Guardar el tema actual en el almacenamiento local para
    // preservar la preferencia del usuario entre las visitas al sitio.
    localStorage.setItem('theme', theme);
}