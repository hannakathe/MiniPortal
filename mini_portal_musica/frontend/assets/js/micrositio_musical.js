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

    fetchSongs();
});
