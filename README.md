# 🌐 Micrositio Web par Musica con API REST

## 🎯 Objetivo del Proyecto
El objetivo de este proyecto es que los estudiantes, aplicando los conocimientos adquiridos durante el curso, sean capaces de diseñar y desarrollar un **micrositio web completo** que combine tanto el **backend basado en servicios API REST**, como un **frontend funcional y bien estructurado**.  

El estudiante deberá crear su propia API para gestionar datos y consumirla desde el frontend mediante **JavaScript**, siguiendo buenas prácticas de desarrollo web moderno.  
Este proyecto les permitirá entender la conexión real entre capas **frontend y backend**, además de fortalecer la habilidad para construir **interfaces dinámicas, integradas y con diseño profesional**.  

### IMPORTANTE EJECUTAR ENTORNO VIRTUAL: 

``` source venv/Scripts/activate** ```

### RELOAD SERVER:

```uvicorn app.main:app --reload```

### ACTUALIZAR requirements.txt: 
```pip freeze > requirements.txt```


---

## 📂 Caso de Uso
Cada micrositio personal deberá estar dividido en **5 secciones principales**:

1. **Home**  
   - Presentación del estudiante tipo hoja de vida:  
     - Foto  
     - Descripción  
     - Contacto  
     - Proyectos realizados  
     - Skills técnicos  

2. **Catálogo de una entidad personalizada**  
   - El estudiante elegirá la entidad que desea mostrar (ejemplo: películas, juegos, libros, recetas, etc.).  
   - Se desarrollará un catálogo dinámico con datos provenientes de su **API propia**.  

3. **Detalle de entidad**  
   - Cada ítem del catálogo podrá ser consultado en detalle.  
   - Incluirá: imagen, descripción extendida y un video embebido.  

4. **Formulario de contacto**  
   - Página con validación en **frontend**.  
   - Envío de datos hacia un endpoint en el **backend**.  

5. **Sección con mapa**  
   - Integración de un mapa con datos geográficos del proyecto, del estudiante o de la entidad mostrada.  

6. **Sección Inteligente (IA)**  
   - Desarrollo de una funcionalidad usando un **modelo de Inteligencia Artificial**.  

---

## Estructura del proyecto
```
MiniPortal
├─ mini_portal_musica
│  ├─ 📂backend
│  │  ├─ 📂app
│  │  │  ├─ crud.py
│  │  │  ├─ database.py
│  │  │  ├─ database_contact.py
│  │  │  ├─ main.py
│  │  │  ├─ models.py
│  │  │  ├─ models_contact.py
│  │  │  ├─ 📂routers
│  │  │  │  ├─ contact.py
│  │  │  │  ├─ recommendations.py
│  │  │  │  ├─ songs.py
│  │  │  │  └─ __pycache__
│  │  │  │     ├─ contact.cpython-312.pyc
│  │  │  │     ├─ recommendations.cpython-312.pyc
│  │  │  │     └─ songs.cpython-312.pyc
│  │  │  ├─ 📂schemas.py
│  │  │  ├─ 📂seed.py
│  │  │  ├─ 📂utils
│  │  │  │  └─ recommender.py
│  │  │  └─ __pycache__
│  │  │     ├─ database.cpython-312.pyc
│  │  │     ├─ database_contact.cpython-312.pyc
│  │  │     ├─ main.cpython-312.pyc
│  │  │     ├─ models.cpython-312.pyc
│  │  │     ├─ models_contact.cpython-312.pyc
│  │  │     └─ schemas.cpython-312.pyc
│  │  ├─ contact.db
│  │  └─ README.md
│  ├─ 📂docs
│  │  └─ Proyecto-corte1_Micrositio_API_REST.pdf
│  ├─ 📂frontend
│  │  ├─ 📂assets
│  │  │  ├─ 📂css
│  │  │  │  ├─ about_me.css
│  │  │  │  ├─ contact.css
│  │  │  │  ├─ content_skills.css
│  │  │  │  ├─ home.css
│  │  │  │  ├─ micrositio_musical.css
│  │  │  │  ├─ projects.css
│  │  │  │  ├─ skills.css
│  │  │  │  ├─ song_detail.css
│  │  │  │  └─ style.css
│  │  │  ├─ 📂icons
│  │  │  │  ├─ github_96.png
│  │  │  │  ├─ gmail_96.png
│  │  │  │  └─ linkedin_96.png
│  │  │  ├─ 📂img
│  │  │  │  ├─ A Night at the Opera.png
│  │  │  │  ├─ blue_mind1.png
│  │  │  │  ├─ coin_machine1.jpg
│  │  │  │  ├─ foto_perfil.jpg
│  │  │  │  ├─ img1.jpg
│  │  │  │  ├─ img2.jpg
│  │  │  │  ├─ img3.jpg
│  │  │  │  ├─ img4.jpg
│  │  │  │  ├─ img5.jpg
│  │  │  │  ├─ img6.jpg
│  │  │  │  └─ music_site1.png
│  │  │  ├─ 📂js
│  │  │  │  ├─ app.js
│  │  │  │  ├─ carousel.js
│  │  │  │  ├─ contact.js
│  │  │  │  ├─ loadSections.js
│  │  │  │  └─ micrositio_musical.js
│  │  │  └─ 📂pages
│  │  │     ├─ about_me.html
│  │  │     ├─ contact.html
│  │  │     ├─ content_skills.html
│  │  │     ├─ home.html
│  │  │     ├─ projects_intro.html
│  │  │     └─ skills.html
│  │  ├─ index.html
│  │  ├─ 📂projects
│  │  │  ├─ blue_mind.html
│  │  │  ├─ coin_machine.html
│  │  │  ├─ micrositio_musical.html
│  │  │  └─ song_detail.html
│  │  └─ README.md
│  ├─ requirements.txt
│  └─ 📂venv
├─ .gitignore
└─ README.md

```

---

## 🛠️ Tecnologías Utilizadas
- **Frontend:** HTML5, CSS3, JavaScript (fetch API)  
- **Backend:** Node.js con Express / u otro framework equivalente  
- **API REST:** Endpoints propios para CRUD de la entidad elegida  
- **Base de Datos:** JSON / MongoDB / MySQL (dependiendo de la implementación del estudiante)  
- **Extras:**  
  - Integración de mapas (ej: Leaflet, Google Maps API)  
  - Embebido de videos (YouTube, Vimeo)  
  - IA (modelo básico de predicción, clasificación o recomendación)  

---

## 📑 Documento del Proyecto
`Proyecto-corte1_Micrositio_API_REST.pdf`  

## 🚀 Ejecución del Proyecto

1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/usuario/proyecto-micrositio.git
   cd proyecto-micrositio

