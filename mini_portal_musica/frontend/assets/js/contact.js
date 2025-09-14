// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", () => {
  // Como el formulario se carga dinámicamente, usamos un MutationObserver
  // para detectar cuando el contenedor de contacto recibe elementos hijos
  const observer = new MutationObserver(() => {
    // Busca el formulario de contacto dentro del contenedor
    const form = document.getElementById("contactForm");
    if (form) {
      // Si el formulario ya existe, dejamos de observar cambios
      observer.disconnect();

      // Agrega un listener al evento submit del formulario
      form.addEventListener("submit", async function (e) {
        // Evita que el formulario se envíe de forma tradicional
        e.preventDefault();

        // Obtiene los datos del formulario como un objeto
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        // Busca un mensaje previo dentro del formulario y lo elimina
        let messageBox = form.querySelector(".message");
        if (messageBox) messageBox.remove();

        // Crea un nuevo párrafo para mostrar mensajes
        messageBox = document.createElement("p");
        messageBox.classList.add("message");
        form.appendChild(messageBox);

        try {
          // Envía los datos del formulario al servidor usando fetch
          const response = await fetch("http://127.0.0.1:8000/api/contact/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
          });

          // Si la respuesta es exitosa
          if (response.ok) {
            messageBox.textContent = "✅ Mensaje enviado con éxito";
            messageBox.classList.remove("error");
            messageBox.classList.add("success");
            form.reset(); // Limpia los campos del formulario
          } else {
            // Si hubo un error en la respuesta
            messageBox.textContent = "❌ Error al enviar el mensaje";
            messageBox.classList.remove("success");
            messageBox.classList.add("error");
          }
        } catch (error) {
          // Si ocurre un error de conexión
          messageBox.textContent = "⚠️ No se pudo conectar con el servidor";
          messageBox.classList.remove("success");
          messageBox.classList.add("error");
        }
      });
    }
  });

  // Comienza a observar cambios en los hijos del contenedor de contacto
  observer.observe(document.getElementById("contact-container"), { childList: true });
});
