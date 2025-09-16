// Escucha cualquier click en el documento
document.addEventListener("click", function(e) {
    // Comprueba si el elemento clicado está dentro de un carrusel
    if (e.target.closest('.carousel')) {
        // Obtiene el carrusel más cercano al elemento clicado
        const carousel = e.target.closest('.carousel');
        // Selecciona todos los ítems dentro del carrusel
        const items = carousel.querySelectorAll('.carousel-item');
        // Encuentra el índice del ítem que actualmente tiene la clase 'active'
        let current = Array.from(items).findIndex(item => item.classList.contains('active'));
        // Calcula el siguiente índice de manera cíclica (vuelve al inicio al final)
        current = (current + 1) % items.length;
        // Activa el ítem correspondiente y desactiva los demás
        items.forEach((item, i) => item.classList.toggle('active', i === current));
    }
});

// Auto-rotación de los carruseles usando setInterval cada 3000 ms (3 segundos)
setInterval(() => {
    // Selecciona todos los carruseles en la página
    document.querySelectorAll('.carousel').forEach(carousel => {
        // Selecciona todos los ítems dentro de este carrusel
        const items = carousel.querySelectorAll('.carousel-item');
        // Encuentra el índice del ítem que actualmente tiene la clase 'active'
        let current = Array.from(items).findIndex(item => item.classList.contains('active'));
        // Calcula el siguiente índice de manera cíclica
        current = (current + 1) % items.length;
        // Activa el ítem correspondiente y desactiva los demás
        items.forEach((item, i) => item.classList.toggle('active', i === current));
    });
}, 3000);
