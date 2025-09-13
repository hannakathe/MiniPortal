document.addEventListener("DOMContentLoaded", async () => {
    const container = document.getElementById("song-detail");
    const cardsContainer = document.getElementById("cards-container");
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatBody = document.getElementById('chat-body');

    const params = new URLSearchParams(window.location.search);
    const songId = params.get("id");

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

            console.log("Datos de la canción recibidos:", song); // Para depuración
            console.log("Valor de url_video:", song.url_video); // Para depuración
            console.log("Tipo de url_video:", typeof song.url_video); // Para depuración

            let videoEmbed = '';
            // Verificamos si url_video existe y no está vacío (incluyendo null, undefined o string vacío)
            if (song.url_video != null && song.url_video !== undefined && song.url_video.toString().trim() !== '') {
                const videoID = song.url_video.toString().trim();
                console.log("ID de video extraído:", videoID); // Para depuración
                
                // Verificamos que el ID tenga la longitud correcta (11 caracteres)
                if (videoID.length === 11) {
                    videoEmbed = `
                        <div class="video-container">
                            <p><strong>Video:</strong></p>
                            <iframe width="100%" height="400" 
                                src="https://www.youtube.com/embed/${videoID}" 
                                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                allowfullscreen>
                            </iframe>
                        </div>`;
                } else {
                    videoEmbed = `
                        <div class="video-container">
                            <p><strong>Video:</strong></p>
                            <p>Formato de ID no válido: "${videoID}"</p>
                            <p>El ID de YouTube debe tener 11 caracteres, pero tiene ${videoID.length}.</p>
                        </div>`;
                    console.error("ID de YouTube con longitud incorrecta:", videoID, "Longitud:", videoID.length);
                }
            } else {
                videoEmbed = `<p>Video no disponible - No se proporcionó un ID de video válido</p>`;
                console.warn("No hay ID de video disponible para esta canción");
            }

            // Crear el botón/enlace para las letras
            let lyricsButton = '';
            if (song.lyrics && song.lyrics.trim() !== '') {
                lyricsButton = `
                    <div style="margin: 15px 0;">
                        <a href="${song.lyrics}" target="_blank" class="lyrics-button" style="text-decoration: none; color: white;">
                            📝 Ver letra completa 📝
                        </a>
                    </div>`;
            } else {
                lyricsButton = `<p>Letra no disponible</p>`;
            }

            // Resto del código para renderizar la canción...
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
                ${lyricsButton}
                ${videoEmbed}
                <button id="btn-map" style="margin-top: 15px;">🌎 Ver ubicación 🌎</button>
                
                <!-- Modal para el mapa -->
                <div id="map-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; 
                    background:rgba(0,0,0,0.7); justify-content:center; align-items:center; z-index:9999;">
                    <div style="position:relative; width:80%; max-width:800px; background:#fff; border-radius:10px; padding:10px;">
                        <span id="close-map" style="position:absolute; top:5px; right:10px; cursor:pointer; font-size:20px;">✖</span>
                        <div id="song-map" style="height:500px; width:100%; border-radius:10px;"></div>
                    </div>
                </div>
            `;

            // === Inicializar mapa en modal ===
            const btnMap = document.getElementById("btn-map");
            const mapModal = document.getElementById("map-modal");
            const closeMap = document.getElementById("close-map");
            let songMap;

            if (btnMap && mapModal && closeMap && song.country_latitude && song.country_longitude) {
                btnMap.addEventListener("click", () => {
                    mapModal.style.display = "flex";

                    const zoomLevel = 4;

                    if (songMap) {
                        songMap.setView([song.country_latitude, song.country_longitude], zoomLevel);
                    } else {
                        songMap = L.map("song-map").setView([song.country_latitude, song.country_longitude], zoomLevel);

                        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                            attribution: '© OpenStreetMap contributors'
                        }).addTo(songMap);

                        L.marker([song.country_latitude, song.country_longitude])
                            .addTo(songMap)
                            .bindPopup(`<b>${song.title}</b><br>${song.artist}<br>${song.country}`)
                            .openPopup();
                    }
                });

                closeMap.addEventListener("click", () => {
                    mapModal.style.display = "none";
                });

                mapModal.addEventListener("click", (e) => {
                    if (e.target === mapModal) {
                        mapModal.style.display = "none";
                    }
                });
            } else if (btnMap) {
                btnMap.addEventListener("click", () => {
                    alert("No hay coordenadas disponibles para esta canción.");
                });
            }

        } catch (error) {
            console.error("Error al cargar la canción:", error);
            container.innerHTML = "<p>Error al cargar la canción.</p>";
        }
    }

    // Resto del código sin cambios...
    // === Función genérica para renderizar canciones en tarjetas ===
    function renderSongs(songs) {
        if (!cardsContainer) return;
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
    }

    // === Función para cargar todas las canciones en el catálogo ===
    async function loadAllSongs() {
        if (!cardsContainer) return;
        const apiUrl = `http://127.0.0.1:8000/api/songs/`;

        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const songs = await response.json();
            renderSongs(songs);
        } catch (error) {
            console.error("Error al cargar canciones:", error);
            if (cardsContainer) cardsContainer.innerHTML = "<p>Error al cargar canciones.</p>";
        }
    }

    // === Función para manejar chat flotante y recomendaciones IA ===
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
                    renderSongs(data);
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