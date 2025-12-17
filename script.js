// ==========================================
// JAVASCRIPT PARA MENÚS DESPLEGABLES
// ==========================================

// Esperamos a que el DOM esté cargado
document.addEventListener("DOMContentLoaded", () => {
  // 1. MENÚ MÓVIL - Toggle principal
  const menuToggle = document.getElementById("menuToggle")
  const navMenu = document.getElementById("navMenu")

  menuToggle.addEventListener("click", () => {
    // Alternamos la clase 'active' en ambos elementos
    menuToggle.classList.toggle("active")
    navMenu.classList.toggle("active")
  })

  // 2. DROPDOWNS - Menús desplegables
  const dropdowns = document.querySelectorAll(".dropdown")

  // Para cada dropdown en la página
  dropdowns.forEach((dropdown) => {
    const toggle = dropdown.querySelector(".dropdown-toggle")

    // Cuando hacemos click en el botón
    toggle.addEventListener("click", () => {
      // Cerramos todos los otros dropdowns
      dropdowns.forEach((otherDropdown) => {
        if (otherDropdown !== dropdown) {
          otherDropdown.classList.remove("active")
          const otherToggle = otherDropdown.querySelector(".dropdown-toggle")
          otherToggle.setAttribute("aria-expanded", "false")
        }
      })

      // Alternamos el dropdown actual
      dropdown.classList.toggle("active")

      // Actualizamos el atributo aria-expanded para accesibilidad
      const isExpanded = dropdown.classList.contains("active")
      toggle.setAttribute("aria-expanded", isExpanded)
    })
  })

  // 3. CERRAR MENÚ AL HACER CLICK FUERA
  document.addEventListener("click", (event) => {
    // Si el click no fue en el menú ni en el botón toggle
    const isClickInsideMenu = navMenu.contains(event.target)
    const isClickOnToggle = menuToggle.contains(event.target)

    if (!isClickInsideMenu && !isClickOnToggle && navMenu.classList.contains("active")) {
      // Cerramos el menú móvil
      menuToggle.classList.remove("active")
      navMenu.classList.remove("active")
    }

    // Cerrar dropdowns si hacemos click fuera
    const isClickInsideDropdown = event.target.closest(".dropdown")
    if (!isClickInsideDropdown) {
      dropdowns.forEach((dropdown) => {
        dropdown.classList.remove("active")
        const toggle = dropdown.querySelector(".dropdown-toggle")
        toggle.setAttribute("aria-expanded", "false")
      })
    }
  })

  // 4. ACCESIBILIDAD - Navegación con teclado
  // Escape para cerrar menús
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      // Cerrar menú móvil
      if (navMenu.classList.contains("active")) {
        menuToggle.classList.remove("active")
        navMenu.classList.remove("active")
        menuToggle.focus() // Devolvemos el foco al botón
      }

      // Cerrar dropdowns
      dropdowns.forEach((dropdown) => {
        if (dropdown.classList.contains("active")) {
          dropdown.classList.remove("active")
          const toggle = dropdown.querySelector(".dropdown-toggle")
          toggle.setAttribute("aria-expanded", "false")
          toggle.focus() // Devolvemos el foco al botón
        }
      })
    }
  })
})
