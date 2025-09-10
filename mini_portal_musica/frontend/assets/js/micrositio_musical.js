document.addEventListener("DOMContentLoaded", async () => {

    const container = document.getElementById("song-detail");
    const cardsContainer = document.getElementById("cards-container");
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatBody = document.getElementById('chat-body');

    const params = new URLSearchParams(window.location.search);
    const songId = params.get("id");

    // === Función para extraer el ID de YouTube de cualquier URL tipo watch?v= ===
    function extractYouTubeID(url) {
        if (!url) return null;
        url = url.trim();
        const regExp = /(?:\?v=|&v=|youtu\.be\/|\/embed\/)([a-zA-Z0-9_-]{11})/;
        const match = url.match(regExp);
        return match ? match[1] : null;
    }

    // === Función para mostrar los detalles de una canción ===
    async function loadSongDetail(id) {
        if (!id) {
            container.innerHTML = "<p>No se especificó ninguna canción.</p>";
            return;
        }
        const apiUrl = `http://127.0.0.1:8000/api/songs/${id}`;

        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const song = await response.json();

            let videoEmbed = '';
            if (song.url_video) {
                const videoID = extractYouTubeID(song.url_video);
                if (videoID) {
                    videoEmbed = `
                        <p><strong>Video:</strong></p>
                        <iframe width="50%" height="315" 
                            src="https://www.youtube.com/embed/${videoID}" 
                            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                            allowfullscreen>
                        </iframe>
                        <p><a href="${song.url_video}" target="_blank">Ver en YouTube</a></p>`;
                } else {
                    videoEmbed = `<p>Video no disponible</p>`;
                }
            }

            container.innerHTML = `
                <h1>${song.title || 'Desconocido'}</h1>
                <img src="${song.album_image || '../assets/img/coin_machine1.jpg'}" alt="${song.title}" style="width:300px; height:auto; border-radius:10px;">
                <p><strong>Artista:</strong> ${song.artist || 'Desconocido'}</p>
                <p><strong>Género:</strong> ${song.genre || 'Desconocido'}</p>
                <p><strong>Disquera:</strong> ${song.discografic || 'Desconocido'}</p>
                <p><strong>Álbum:</strong> ${song.album || 'Desconocido'}</p>
                <p><strong>País:</strong> ${song.country || 'Desconocido'}</p>
                <p><strong>Fecha de lanzamiento:</strong> ${song.release_date || 'Desconocida'}</p>
                <p><strong>Descripción:</strong> ${song.description || ''}</p>
                <p><strong>Letras:</strong></p>
                <pre style="white-space: pre-wrap;">${song.lyrics || 'No disponible'}</pre>
                ${videoEmbed}
            `;
        } catch (error) {
            console.error("Error al cargar la canción:", error);
            container.innerHTML = "<p>Error al cargar la canción.</p>";
        }
    }

    // === Función para cargar todas las canciones en el catálogo ===
    async function loadAllSongs() {
        if (!cardsContainer) return;
        const apiUrl = `http://127.0.0.1:8000/api/songs/`;

        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const songs = await response.json();

            cardsContainer.innerHTML = '';
            songs.forEach(song => {
                const card = document.createElement('div');
                card.classList.add('card');

                const img = document.createElement('img');
                img.src = song.album_image || '../assets/img/default_album.png';
                img.alt = song.title;

                const title = document.createElement('h3');
                title.textContent = song.title || 'Sin título';

                card.appendChild(img);
                card.appendChild(title);

                card.addEventListener('click', () => {
                    window.location.href = `song_detail.html?id=${song.id}`;
                });

                cardsContainer.appendChild(card);
            });

        } catch (error) {
            console.error("Error al cargar canciones:", error);
            if (cardsContainer) cardsContainer.innerHTML = "<p>Error al cargar canciones.</p>";
        }
    }

    // === Función para manejar chat flotante ===
    function initChat() {
        if (!chatForm) return;

        chatForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const message = chatInput.value.trim();
            if (!message) return;

            const userMsg = document.createElement('p');
            userMsg.classList.add('user');
            userMsg.textContent = message;
            chatBody.appendChild(userMsg);
            chatBody.scrollTop = chatBody.scrollHeight;
            chatInput.value = '';

            try {
                const formData = new FormData();
                formData.append('message', message);

                const response = await fetch('http://127.0.0.1:8000/api/recommendations/chat-recommendations', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();

                const botMsg = document.createElement('p');
                botMsg.classList.add('bot');

                if (Array.isArray(data) && data.length > 0) {
                    botMsg.innerHTML = data.map(s => `🎵 ${s.title}`).join('<br>');
                } else if (data.mensaje) {
                    botMsg.textContent = data.mensaje;
                } else {
                    botMsg.textContent = 'No se encontraron recomendaciones';
                }

                chatBody.appendChild(botMsg);
                chatBody.scrollTop = chatBody.scrollHeight;

            } catch (error) {
                const botMsg = document.createElement('p');
                botMsg.classList.add('bot');
                botMsg.textContent = 'Error conectando con la API';
                chatBody.appendChild(botMsg);
                chatBody.scrollTop = chatBody.scrollHeight;
                console.error(error);
            }
        });

        const chatHeader = document.getElementById('chat-header');
        if (chatHeader) {
            chatHeader.addEventListener('click', () => {
                document.getElementById('chat-float').classList.toggle('minimized');
            });
        }
    }

    if (container) loadSongDetail(songId);
    if (cardsContainer) loadAllSongs();
    initChat();
});
