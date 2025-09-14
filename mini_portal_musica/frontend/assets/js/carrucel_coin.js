document.addEventListener("click", function(e) {
    if (e.target.closest('.carousel')) {
        const carousel = e.target.closest('.carousel');
        const items = carousel.querySelectorAll('.carousel-item');
        let current = Array.from(items).findIndex(item => item.classList.contains('active'));
        current = (current + 1) % items.length;
        items.forEach((item, i) => item.classList.toggle('active', i === current));
    }
});

// Auto-rotación con setInterval
setInterval(() => {
    document.querySelectorAll('.carousel').forEach(carousel => {
        const items = carousel.querySelectorAll('.carousel-item');
        let current = Array.from(items).findIndex(item => item.classList.contains('active'));
        current = (current + 1) % items.length;
        items.forEach((item, i) => item.classList.toggle('active', i === current));
    });
}, 3000);
