# 🌐 Micrositio Web par Musica con API REST

## 🎯 Objetivo del Proyecto
El objetivo de este proyecto es que los estudiantes, aplicando los conocimientos adquiridos durante el curso, sean capaces de diseñar y desarrollar un **micrositio web completo** que combine tanto el **backend basado en servicios API REST**, como un **frontend funcional y bien estructurado**.  

El estudiante deberá crear su propia API para gestionar datos y consumirla desde el frontend mediante **JavaScript**, siguiendo buenas prácticas de desarrollo web moderno.  
Este proyecto les permitirá entender la conexión real entre capas **frontend y backend**, además de fortalecer la habilidad para construir **interfaces dinámicas, integradas y con diseño profesional**.  

**IMPORTANTE EJECUTAR ENTORNO VIRTUAL: source .venv/bin/activate**
**RELOAD SERVER: uvicorn backend.app.main:app --reload**

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
mini_portal_musica
├── .gitignore
├── 📂backend
│   ├── 📜README.md
│   ├── 📂app
│   │   ├── __pycache__
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── 📂routers
│   │   │   ├── __pycache__
│   │   │   ├── contact.py
│   │   │   ├── profile.py
│   │   │   ├── recommendations.py
│   │   │   └── songs.py
│   │   ├── schemas.py
│   │   ├── seed.py
│   │   └── 📂utils
│   │       ├── __pycache__
│   │       └── recommender.py
│   └── songs.db
├── 📂docs
│   ├── Proyecto-corte1_Micrositio_API_REST.pdf
│   └── 📂screenshots
📂frontend/
├── README.md
├── 📂assets/
│   ├── 📂css/
│   │   └── style.css          # Estilos globales
│   ├── 📂img/                   # Fotos, logos, screenshots de proyectos
│   │   ├── perfil.png
│   │   ├── micrositio.png
│   │   └── otros_proyectos.png
│   └── 📂js/
│       ├── app.js             # Funciones globales
│       ├── portfolio.js       # Funciones de home y proyectos
│       ├── catalog.js         # Funciones específicas del catálogo musical
│       └── detail.js          # Funciones de detalle de canción
├── index.html                 # Home / Portafolio
├── 📂projects/
│   ├── micrositio.html        # Página del micrositio musical
│   └── otros_proyectos.html   # Página con descripción de otros proyectos
├── 📂skills/
│   └── index.html             # Página de skills técnicos
├── contact.html               # Formulario de contacto
├── catalog.html               # Catálogo de canciones del proyecto musical
└── detail.html                # Detalle de canción
├── requirements.txt
├── 📜README.md
└── 📂venv
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
