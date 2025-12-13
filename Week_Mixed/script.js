// TASK 5, SEMANA 3: Agregar interactividad básica
document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Mostrar un mensaje de bienvenida en la consola
    console.log("¡El script.js ha cargado exitosamente! Listo para la interactividad.");

    // 2. Cambiar el texto de un párrafo al hacer clic en un botón
    const changeTextBtn = document.getElementById('change-text-btn');
    const welcomeText = document.getElementById('welcome-text');

    if (changeTextBtn) {
        changeTextBtn.addEventListener('click', () => {
            if (welcomeText.textContent === "¡Bienvenido! Soy un desarrollador enfocado en el aprendizaje continuo de tecnologías web modernas.") {
                welcomeText.textContent = "¡Gracias por visitar! Ahora estoy demostrando manipulación del DOM con JavaScript.";
            } else {
                 welcomeText.textContent = "¡Bienvenido! Soy un desarrollador enfocado en el aprendizaje continuo de tecnologías web modernas.";
            }
        });
    }

    // 3. Mostrar/Ocultar contenido con un botón (efecto dinámico)
    const toggleInfoBtn = document.getElementById('toggle-info-btn');
    const extraInfoDiv = document.getElementById('extra-info');

    if (toggleInfoBtn) {
        toggleInfoBtn.addEventListener('click', () => {
            // Verifica si el div está oculto ('none') y lo cambia a visible ('block')
            if (extraInfoDiv.style.display === 'none') {
                extraInfoDiv.style.display = 'block';
                toggleInfoBtn.textContent = 'Ocultar Info Extra';
            } else {
                extraInfoDiv.style.display = 'none';
                toggleInfoBtn.textContent = 'Mostrar/Ocultar Info Extra';
            }
        });
    }
});
