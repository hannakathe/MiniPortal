document.addEventListener('DOMContentLoaded', () => {
    const sections = [
        {id: 'home-container', file: 'assets/pages/home.html'},
        {id: 'about-container', file: 'assets/pages/about_me.html'},
        {id: 'projects-container', file: 'assets/pages/projects.html'},
        {id: 'skills-container', file: 'assets/pages/skills.html'},
        {id: 'contact-container', file: 'assets/pages/contact.html'}
    ];

    sections.forEach(section => {
        fetch(section.file)
            .then(res => res.text())
            .then(html => {
                document.getElementById(section.id).innerHTML = html;
            })
            .catch(err => console.error(`Error cargando ${section.file}:`, err));
    });
});
