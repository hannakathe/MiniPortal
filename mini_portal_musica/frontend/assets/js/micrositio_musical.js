document.addEventListener("DOMContentLoaded", async () => {

    const cardsContainer = document.getElementById("cards-container");
    const songId = new URLSearchParams(window.location.search).get("id");

    // === Chat flotante ===
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatBody = document.getElementById('chat-body');

    function initChat() {
        if (!chatForm) return;

        chatForm.addEventListener('submit', async e => {
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
                const response = await fetch('http://127.0.0.1:8000/api/recommendations/chat-recommendations', { method: 'POST', body: formData });
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
        if(chatHeader){
            chatHeader.addEventListener('click', () => {
                document.getElementById('chat-float').classList.toggle('minimized');
            });
        }
    }

    initChat();

    // === Cargar catálogo de canciones (solo si estamos en micrositio_musical.html) ===
    async function loadSongsCatalog() {
        if (!cardsContainer) return;

        try {
            const response = await fetch('http://127.0.0.1:8000/api/songs/');
            const songs = await response.json();

            if (!Array.isArray(songs)) return;

            songs.forEach(song => {
                const card = document.createElement('div');
                card.classList.add('card');

                card.innerHTML = `
                    <a href="song_detail.html?id=${song.id}" class="card-link">
                        <img src="${song.album_image || '../assets/img/coin_machine1.jpg'}" alt="${song.title}">
                        <h3>${song.title}</h3>
                    </a>
                `;
                cardsContainer.appendChild(card);
            });
        } catch (error) {
            console.error("Error cargando canciones:", error);
            cardsContainer.innerHTML = `<p style="color:red;">No se pudieron cargar las canciones.</p>`;
        }
    }

    // === Cargar detalle de canción (solo si estamos en song_detail.html) ===
    async function loadSongDetail(id) {
        if (!id) return;

        // Elementos del detalle
        const albumImage = document.getElementById("album-image");
        const songTitle = document.getElementById("song-title");
        const songArtist = document.getElementById("song-artist");
        const songGenre = document.getElementById("song-genre");
        const songDiscografic = document.getElementById("song-discografic");
        const songAlbum = document.getElementById("song-album");
        const songCountry = document.getElementById("song-country");
        const songReleaseDate = document.getElementById("song-release-date");
        const songDescription = document.getElementById("song-description");
        const videoContainer = document.getElementById("video-container");
        const btnLyrics = document.getElementById("btn-lyrics");
        const btnMap = document.getElementById("btn-map");
        const mapModal = document.getElementById("map-modal");
        const closeMap = document.getElementById("close-map");
        const songMapDiv = document.getElementById("song-map");

        let songMap;

        try {
            const response = await fetch(`http://127.0.0.1:8000/api/songs/${id}`);
            const song = await response.json();

            // Actualizar información
            if(albumImage) albumImage.src = song.album_image || '../assets/img/coin_machine1.jpg';
            if(albumImage) albumImage.alt = song.title || 'Álbum';
            if(songTitle) songTitle.textContent = song.title || 'Desconocido';
            if(songArtist) songArtist.textContent = song.artist || 'Desconocido';
            if(songGenre) songGenre.textContent = song.genre || 'Desconocido';
            if(songDiscografic) songDiscografic.textContent = song.discografic || 'Desconocido';
            if(songAlbum) songAlbum.textContent = song.album || 'Desconocido';
            if(songCountry) songCountry.textContent = song.country || 'Desconocido';
            if(songReleaseDate) songReleaseDate.textContent = song.release_date || 'Desconocida';
            if(songDescription) songDescription.textContent = song.description || '';

            // Video YouTube
            if (videoContainer) {
                if (song.url_video && song.url_video.trim().length === 11) {
                    videoContainer.innerHTML = `
                        <iframe src="https://www.youtube.com/embed/${song.url_video}" 
                            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                            allowfullscreen>
                        </iframe>`;
                } else {
                    videoContainer.innerHTML = `<p>Video no disponible</p>`;
                }
            }

            // Botón letras
            if (btnLyrics) {
                if (song.lyrics && song.lyrics.trim() !== '') {
                    btnLyrics.href = song.lyrics;
                } else {
                    btnLyrics.style.display = "none";
                }
            }

            // Botón mapa
            if (btnMap) {
                btnMap.addEventListener("click", () => {
                    if (song.country_latitude && song.country_longitude) {
                        if(mapModal) mapModal.style.display = "flex";

                        if (!songMap && songMapDiv) {
                            songMap = L.map(songMapDiv).setView([song.country_latitude, song.country_longitude], 4);
                            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                                attribution: '© OpenStreetMap contributors'
                            }).addTo(songMap);
                            L.marker([song.country_latitude, song.country_longitude])
                             .addTo(songMap)
                             .bindPopup(`<b>${song.title}</b><br>${song.artist}<br>${song.country}`)
                             .openPopup();
                        } else if(songMap) {
                            songMap.setView([song.country_latitude, song.country_longitude], 4);
                        }
                    } else {
                        alert("No hay coordenadas disponibles para esta canción.");
                    }
                });
            }

            if(closeMap && mapModal){
                closeMap.addEventListener("click", () => mapModal.style.display = "none");
                mapModal.addEventListener("click", (e) => { if(e.target === mapModal) mapModal.style.display = "none"; });
            }

        } catch (error) {
            console.error("Error cargando detalle de canción:", error);
        }
    }

    // === Inicializar según la página ===
    if(songId) {
        loadSongDetail(songId); // song_detail.html
    } else {
        loadSongsCatalog(); // micrositio_musical.html
    }

});
