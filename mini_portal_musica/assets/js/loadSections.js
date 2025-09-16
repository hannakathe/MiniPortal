// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {
    // Define las secciones de la página y el archivo HTML que se cargará en cada una
    const sections = [
        {id: 'home-container', file: 'assets/pages/home.html'},
        {id: 'about-container', file: 'assets/pages/about_me.html'},
        {id: 'projects-container', file: 'assets/pages/projects_intro.html'},
        {id: 'skills-container', file: 'assets/pages/skills.html'},
        {id: 'contact-container', file: 'assets/pages/contact.html'}
    ];

    // Itera sobre cada sección para cargar su contenido
    sections.forEach(section => {
        // Realiza una petición fetch al archivo HTML correspondiente
        fetch(section.file)
            .then(res => res.text()) // Convierte la respuesta en texto (HTML)
            .then(html => {
                // Inserta el HTML cargado dentro del contenedor correspondiente
                document.getElementById(section.id).innerHTML = html;
            })
            .catch(err => console.error(`Error cargando ${section.file}:`, err)); // Maneja errores de carga
    });
});
