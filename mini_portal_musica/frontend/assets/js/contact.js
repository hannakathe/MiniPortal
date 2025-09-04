document.addEventListener("DOMContentLoaded", () => {
  // Como las secciones se cargan dinámicamente,
  // esperamos a que el contenedor de contacto exista
  const observer = new MutationObserver(() => {
    const form = document.getElementById("contactForm");
    if (form) {
      observer.disconnect();

      form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        let messageBox = form.querySelector(".message");
        if (messageBox) messageBox.remove();

        messageBox = document.createElement("p");
        messageBox.classList.add("message");
        form.appendChild(messageBox);

        try {
          const response = await fetch("http://127.0.0.1:8000/api/contact/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(data),
});


          if (response.ok) {
            messageBox.textContent = "✅ Mensaje enviado con éxito";
            messageBox.classList.remove("error");
            messageBox.classList.add("success");
            form.reset();
          } else {
            messageBox.textContent = "❌ Error al enviar el mensaje";
            messageBox.classList.remove("success");
            messageBox.classList.add("error");
          }
        } catch (error) {
          messageBox.textContent = "⚠️ No se pudo conectar con el servidor";
          messageBox.classList.remove("success");
          messageBox.classList.add("error");
        }
      });
    }
  });

  observer.observe(document.getElementById("contact-container"), { childList: true });
});
