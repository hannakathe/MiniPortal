document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("cards-container");
    const apiUrl = "http://127.0.0.1:8000/api/songs";

    async function fetchSongs() {
        try {
            const response = await fetch(apiUrl);
            const songs = await response.json();

            songs.forEach(song => {
                const card = document.createElement("div");
                card.className = "card";

                // Mostrar solo la portada
                card.innerHTML = `<img src="${song.album_image || '../assets/img/coin_machine1.jpg'}" alt="${song.title}">`;

                // Redirigir a song_detail.html pasando el id
                card.addEventListener("click", () => {
                    window.location.href = `song_detail.html?id=${song.id}`;
                });

                container.appendChild(card);
            });
        } catch (error) {
            console.error("Error al obtener canciones:", error);
            container.innerHTML = "<p>Error al cargar las canciones.</p>";
        }
    }
const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const chatBody = document.getElementById('chat-body');
const cardsContainer = document.querySelector('.cards-container'); // Contenedor de canciones

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const message = chatInput.value.trim();
  if (!message) return;

  // Mostrar mensaje del usuario en el chat
  const userMsg = document.createElement('p');
  userMsg.classList.add('user');
  userMsg.textContent = message;
  chatBody.appendChild(userMsg);
  chatBody.scrollTop = chatBody.scrollHeight;
  chatInput.value = '';

  try {
    // Enviar mensaje a la API
    const formData = new FormData();
    formData.append('message', message);

    const response = await fetch('http://127.0.0.1:8000/api/recommendations/chat-recommendations', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();

    // Mostrar respuesta en el chat
    const botMsg = document.createElement('p');
    botMsg.classList.add('bot');

    if (Array.isArray(data) && data.length > 0) {
      botMsg.innerHTML = data.map(s => `🎵 ${s.title}`).join('<br>');
      chatBody.appendChild(botMsg);
      chatBody.scrollTop = chatBody.scrollHeight;

      // Actualizar grid de canciones SOLO con las recomendaciones
      cardsContainer.innerHTML = ''; // Limpiar canciones actuales
      data.forEach(song => {
        const card = document.createElement('div');
        card.classList.add('card');

        // Solo imagen del álbum en la tarjeta
        const img = document.createElement('img');
        img.src = song.album_image || 'assets/img/default_album.png'; // Coloca un default si no hay imagen
        img.alt = song.title;

        // Al hacer click, ir a detalle de la canción
        card.addEventListener('click', () => {
          window.location.href = `song_detail.html?id=${song.id}`;
        });

        card.appendChild(img);
        cardsContainer.appendChild(card);
      });

    } else if (data.mensaje) {
      botMsg.textContent = data.mensaje;
      chatBody.appendChild(botMsg);
      chatBody.scrollTop = chatBody.scrollHeight;
    } else {
      botMsg.textContent = 'No se encontraron recomendaciones';
      chatBody.appendChild(botMsg);
      chatBody.scrollTop = chatBody.scrollHeight;
    }

  } catch (error) {
    const botMsg = document.createElement('p');
    botMsg.classList.add('bot');
    botMsg.textContent = 'Error conectando con la API';
    chatBody.appendChild(botMsg);
    chatBody.scrollTop = chatBody.scrollHeight;
    console.error(error);
  }
});

    fetchSongs();
});
