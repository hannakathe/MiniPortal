# 🌐 Micrositio Web par Musica con API REST

## 🎯 Objetivo del Proyecto
El objetivo de este proyecto es que los estudiantes, aplicando los conocimientos adquiridos durante el curso, sean capaces de diseñar y desarrollar un **micrositio web completo** que combine tanto el **backend basado en servicios API REST**, como un **frontend funcional y bien estructurado**.  

El estudiante deberá crear su propia API para gestionar datos y consumirla desde el frontend mediante **JavaScript**, siguiendo buenas prácticas de desarrollo web moderno.  
Este proyecto les permitirá entender la conexión real entre capas **frontend y backend**, además de fortalecer la habilidad para construir **interfaces dinámicas, integradas y con diseño profesional**.  

**IMPORTANTE EJECUTAR ENTORNO VIRTUAL: source venv/Scripts/activate**
**RELOAD SERVER: uvicorn app.main:app --reload**

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

```
MiniPortal
├─ mini_portal_musica
│  ├─ backend
│  │  ├─ app
│  │  │  ├─ crud.py
│  │  │  ├─ database.py
│  │  │  ├─ database_contact.py
│  │  │  ├─ main.py
│  │  │  ├─ models.py
│  │  │  ├─ models_contact.py
│  │  │  ├─ routers
│  │  │  │  ├─ contact.py
│  │  │  │  ├─ recommendations.py
│  │  │  │  ├─ songs.py
│  │  │  │  └─ __pycache__
│  │  │  │     ├─ contact.cpython-312.pyc
│  │  │  │     ├─ recommendations.cpython-312.pyc
│  │  │  │     └─ songs.cpython-312.pyc
│  │  │  ├─ schemas.py
│  │  │  ├─ seed.py
│  │  │  ├─ utils
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
│  ├─ docs
│  │  └─ Proyecto-corte1_Micrositio_API_REST.pdf
│  ├─ frontend
│  │  ├─ assets
│  │  │  ├─ css
│  │  │  │  ├─ about_me.css
│  │  │  │  ├─ contact.css
│  │  │  │  ├─ content_skills.css
│  │  │  │  ├─ home.css
│  │  │  │  ├─ micrositio_musical.css
│  │  │  │  ├─ projects.css
│  │  │  │  ├─ skills.css
│  │  │  │  ├─ song_detail.css
│  │  │  │  └─ style.css
│  │  │  ├─ icons
│  │  │  │  ├─ github_96.png
│  │  │  │  ├─ gmail_96.png
│  │  │  │  └─ linkedin_96.png
│  │  │  ├─ img
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
│  │  │  ├─ js
│  │  │  │  ├─ app.js
│  │  │  │  ├─ carousel.js
│  │  │  │  ├─ contact.js
│  │  │  │  ├─ loadSections.js
│  │  │  │  └─ micrositio_musical.js
│  │  │  └─ pages
│  │  │     ├─ about_me.html
│  │  │     ├─ contact.html
│  │  │     ├─ content_skills.html
│  │  │     ├─ home.html
│  │  │     ├─ projects_intro.html
│  │  │     └─ skills.html
│  │  ├─ index.html
│  │  ├─ projects
│  │  │  ├─ blue_mind.html
│  │  │  ├─ coin_machine.html
│  │  │  ├─ micrositio_musical.html
│  │  │  └─ song_detail.html
│  │  └─ README.md
│  ├─ requirements.txt
│  └─ venv
│     ├─ Include
│     │  └─ site
│     │     └─ python3.12
│     │        └─ greenlet
│     │           └─ greenlet.h
│     ├─ Lib
│     │  └─ site-packages
│     │     ├─ annotated_types
│     │     │  ├─ py.typed
│     │     │  ├─ test_cases.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ test_cases.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ annotated_types-0.7.0.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ anyio
│     │     │  ├─ abc
│     │     │  │  ├─ _eventloop.py
│     │     │  │  ├─ _resources.py
│     │     │  │  ├─ _sockets.py
│     │     │  │  ├─ _streams.py
│     │     │  │  ├─ _subprocesses.py
│     │     │  │  ├─ _tasks.py
│     │     │  │  ├─ _testing.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ _eventloop.cpython-312.pyc
│     │     │  │     ├─ _resources.cpython-312.pyc
│     │     │  │     ├─ _sockets.cpython-312.pyc
│     │     │  │     ├─ _streams.cpython-312.pyc
│     │     │  │     ├─ _subprocesses.cpython-312.pyc
│     │     │  │     ├─ _tasks.cpython-312.pyc
│     │     │  │     ├─ _testing.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ from_thread.py
│     │     │  ├─ lowlevel.py
│     │     │  ├─ py.typed
│     │     │  ├─ pytest_plugin.py
│     │     │  ├─ streams
│     │     │  │  ├─ buffered.py
│     │     │  │  ├─ file.py
│     │     │  │  ├─ memory.py
│     │     │  │  ├─ stapled.py
│     │     │  │  ├─ text.py
│     │     │  │  ├─ tls.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ buffered.cpython-312.pyc
│     │     │  │     ├─ file.cpython-312.pyc
│     │     │  │     ├─ memory.cpython-312.pyc
│     │     │  │     ├─ stapled.cpython-312.pyc
│     │     │  │     ├─ text.cpython-312.pyc
│     │     │  │     ├─ tls.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ to_interpreter.py
│     │     │  ├─ to_process.py
│     │     │  ├─ to_thread.py
│     │     │  ├─ _backends
│     │     │  │  ├─ _asyncio.py
│     │     │  │  ├─ _trio.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ _asyncio.cpython-312.pyc
│     │     │  │     ├─ _trio.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _core
│     │     │  │  ├─ _asyncio_selector_thread.py
│     │     │  │  ├─ _contextmanagers.py
│     │     │  │  ├─ _eventloop.py
│     │     │  │  ├─ _exceptions.py
│     │     │  │  ├─ _fileio.py
│     │     │  │  ├─ _resources.py
│     │     │  │  ├─ _signals.py
│     │     │  │  ├─ _sockets.py
│     │     │  │  ├─ _streams.py
│     │     │  │  ├─ _subprocesses.py
│     │     │  │  ├─ _synchronization.py
│     │     │  │  ├─ _tasks.py
│     │     │  │  ├─ _tempfile.py
│     │     │  │  ├─ _testing.py
│     │     │  │  ├─ _typedattr.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ _asyncio_selector_thread.cpython-312.pyc
│     │     │  │     ├─ _contextmanagers.cpython-312.pyc
│     │     │  │     ├─ _eventloop.cpython-312.pyc
│     │     │  │     ├─ _exceptions.cpython-312.pyc
│     │     │  │     ├─ _fileio.cpython-312.pyc
│     │     │  │     ├─ _resources.cpython-312.pyc
│     │     │  │     ├─ _signals.cpython-312.pyc
│     │     │  │     ├─ _sockets.cpython-312.pyc
│     │     │  │     ├─ _streams.cpython-312.pyc
│     │     │  │     ├─ _subprocesses.cpython-312.pyc
│     │     │  │     ├─ _synchronization.cpython-312.pyc
│     │     │  │     ├─ _tasks.cpython-312.pyc
│     │     │  │     ├─ _tempfile.cpython-312.pyc
│     │     │  │     ├─ _testing.cpython-312.pyc
│     │     │  │     ├─ _typedattr.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ from_thread.cpython-312.pyc
│     │     │     ├─ lowlevel.cpython-312.pyc
│     │     │     ├─ pytest_plugin.cpython-312.pyc
│     │     │     ├─ to_interpreter.cpython-312.pyc
│     │     │     ├─ to_process.cpython-312.pyc
│     │     │     ├─ to_thread.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ anyio-4.10.0.dist-info
│     │     │  ├─ entry_points.txt
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ certifi
│     │     │  ├─ cacert.pem
│     │     │  ├─ core.py
│     │     │  ├─ py.typed
│     │     │  ├─ __init__.py
│     │     │  ├─ __main__.py
│     │     │  └─ __pycache__
│     │     │     ├─ core.cpython-312.pyc
│     │     │     ├─ __init__.cpython-312.pyc
│     │     │     └─ __main__.cpython-312.pyc
│     │     ├─ certifi-2025.8.3.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ click
│     │     │  ├─ core.py
│     │     │  ├─ decorators.py
│     │     │  ├─ exceptions.py
│     │     │  ├─ formatting.py
│     │     │  ├─ globals.py
│     │     │  ├─ parser.py
│     │     │  ├─ py.typed
│     │     │  ├─ shell_completion.py
│     │     │  ├─ termui.py
│     │     │  ├─ testing.py
│     │     │  ├─ types.py
│     │     │  ├─ utils.py
│     │     │  ├─ _compat.py
│     │     │  ├─ _termui_impl.py
│     │     │  ├─ _textwrap.py
│     │     │  ├─ _winconsole.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ core.cpython-312.pyc
│     │     │     ├─ decorators.cpython-312.pyc
│     │     │     ├─ exceptions.cpython-312.pyc
│     │     │     ├─ formatting.cpython-312.pyc
│     │     │     ├─ globals.cpython-312.pyc
│     │     │     ├─ parser.cpython-312.pyc
│     │     │     ├─ shell_completion.cpython-312.pyc
│     │     │     ├─ termui.cpython-312.pyc
│     │     │     ├─ testing.cpython-312.pyc
│     │     │     ├─ types.cpython-312.pyc
│     │     │     ├─ utils.cpython-312.pyc
│     │     │     ├─ _compat.cpython-312.pyc
│     │     │     ├─ _termui_impl.cpython-312.pyc
│     │     │     ├─ _textwrap.cpython-312.pyc
│     │     │     ├─ _winconsole.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ click-8.2.1.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE.txt
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ colorama
│     │     │  ├─ ansi.py
│     │     │  ├─ ansitowin32.py
│     │     │  ├─ initialise.py
│     │     │  ├─ tests
│     │     │  │  ├─ ansitowin32_test.py
│     │     │  │  ├─ ansi_test.py
│     │     │  │  ├─ initialise_test.py
│     │     │  │  ├─ isatty_test.py
│     │     │  │  ├─ utils.py
│     │     │  │  ├─ winterm_test.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ ansitowin32_test.cpython-312.pyc
│     │     │  │     ├─ ansi_test.cpython-312.pyc
│     │     │  │     ├─ initialise_test.cpython-312.pyc
│     │     │  │     ├─ isatty_test.cpython-312.pyc
│     │     │  │     ├─ utils.cpython-312.pyc
│     │     │  │     ├─ winterm_test.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ win32.py
│     │     │  ├─ winterm.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ ansi.cpython-312.pyc
│     │     │     ├─ ansitowin32.cpython-312.pyc
│     │     │     ├─ initialise.cpython-312.pyc
│     │     │     ├─ win32.cpython-312.pyc
│     │     │     ├─ winterm.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ colorama-0.4.6.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE.txt
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ distro
│     │     │  ├─ distro.py
│     │     │  ├─ py.typed
│     │     │  ├─ __init__.py
│     │     │  ├─ __main__.py
│     │     │  └─ __pycache__
│     │     │     ├─ distro.cpython-312.pyc
│     │     │     ├─ __init__.cpython-312.pyc
│     │     │     └─ __main__.cpython-312.pyc
│     │     ├─ distro-1.9.0.dist-info
│     │     │  ├─ entry_points.txt
│     │     │  ├─ INSTALLER
│     │     │  ├─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ dns
│     │     │  ├─ asyncbackend.py
│     │     │  ├─ asyncquery.py
│     │     │  ├─ asyncresolver.py
│     │     │  ├─ btree.py
│     │     │  ├─ btreezone.py
│     │     │  ├─ dnssec.py
│     │     │  ├─ dnssecalgs
│     │     │  │  ├─ base.py
│     │     │  │  ├─ cryptography.py
│     │     │  │  ├─ dsa.py
│     │     │  │  ├─ ecdsa.py
│     │     │  │  ├─ eddsa.py
│     │     │  │  ├─ rsa.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ cryptography.cpython-312.pyc
│     │     │  │     ├─ dsa.cpython-312.pyc
│     │     │  │     ├─ ecdsa.cpython-312.pyc
│     │     │  │     ├─ eddsa.cpython-312.pyc
│     │     │  │     ├─ rsa.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ dnssectypes.py
│     │     │  ├─ e164.py
│     │     │  ├─ edns.py
│     │     │  ├─ entropy.py
│     │     │  ├─ enum.py
│     │     │  ├─ exception.py
│     │     │  ├─ flags.py
│     │     │  ├─ grange.py
│     │     │  ├─ immutable.py
│     │     │  ├─ inet.py
│     │     │  ├─ ipv4.py
│     │     │  ├─ ipv6.py
│     │     │  ├─ message.py
│     │     │  ├─ name.py
│     │     │  ├─ namedict.py
│     │     │  ├─ nameserver.py
│     │     │  ├─ node.py
│     │     │  ├─ opcode.py
│     │     │  ├─ py.typed
│     │     │  ├─ query.py
│     │     │  ├─ quic
│     │     │  │  ├─ _asyncio.py
│     │     │  │  ├─ _common.py
│     │     │  │  ├─ _sync.py
│     │     │  │  ├─ _trio.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ _asyncio.cpython-312.pyc
│     │     │  │     ├─ _common.cpython-312.pyc
│     │     │  │     ├─ _sync.cpython-312.pyc
│     │     │  │     ├─ _trio.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ rcode.py
│     │     │  ├─ rdata.py
│     │     │  ├─ rdataclass.py
│     │     │  ├─ rdataset.py
│     │     │  ├─ rdatatype.py
│     │     │  ├─ rdtypes
│     │     │  │  ├─ ANY
│     │     │  │  │  ├─ AFSDB.py
│     │     │  │  │  ├─ AMTRELAY.py
│     │     │  │  │  ├─ AVC.py
│     │     │  │  │  ├─ CAA.py
│     │     │  │  │  ├─ CDNSKEY.py
│     │     │  │  │  ├─ CDS.py
│     │     │  │  │  ├─ CERT.py
│     │     │  │  │  ├─ CNAME.py
│     │     │  │  │  ├─ CSYNC.py
│     │     │  │  │  ├─ DLV.py
│     │     │  │  │  ├─ DNAME.py
│     │     │  │  │  ├─ DNSKEY.py
│     │     │  │  │  ├─ DS.py
│     │     │  │  │  ├─ DSYNC.py
│     │     │  │  │  ├─ EUI48.py
│     │     │  │  │  ├─ EUI64.py
│     │     │  │  │  ├─ GPOS.py
│     │     │  │  │  ├─ HINFO.py
│     │     │  │  │  ├─ HIP.py
│     │     │  │  │  ├─ ISDN.py
│     │     │  │  │  ├─ L32.py
│     │     │  │  │  ├─ L64.py
│     │     │  │  │  ├─ LOC.py
│     │     │  │  │  ├─ LP.py
│     │     │  │  │  ├─ MX.py
│     │     │  │  │  ├─ NID.py
│     │     │  │  │  ├─ NINFO.py
│     │     │  │  │  ├─ NS.py
│     │     │  │  │  ├─ NSEC.py
│     │     │  │  │  ├─ NSEC3.py
│     │     │  │  │  ├─ NSEC3PARAM.py
│     │     │  │  │  ├─ OPENPGPKEY.py
│     │     │  │  │  ├─ OPT.py
│     │     │  │  │  ├─ PTR.py
│     │     │  │  │  ├─ RESINFO.py
│     │     │  │  │  ├─ RP.py
│     │     │  │  │  ├─ RRSIG.py
│     │     │  │  │  ├─ RT.py
│     │     │  │  │  ├─ SMIMEA.py
│     │     │  │  │  ├─ SOA.py
│     │     │  │  │  ├─ SPF.py
│     │     │  │  │  ├─ SSHFP.py
│     │     │  │  │  ├─ TKEY.py
│     │     │  │  │  ├─ TLSA.py
│     │     │  │  │  ├─ TSIG.py
│     │     │  │  │  ├─ TXT.py
│     │     │  │  │  ├─ URI.py
│     │     │  │  │  ├─ WALLET.py
│     │     │  │  │  ├─ X25.py
│     │     │  │  │  ├─ ZONEMD.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ AFSDB.cpython-312.pyc
│     │     │  │  │     ├─ AMTRELAY.cpython-312.pyc
│     │     │  │  │     ├─ AVC.cpython-312.pyc
│     │     │  │  │     ├─ CAA.cpython-312.pyc
│     │     │  │  │     ├─ CDNSKEY.cpython-312.pyc
│     │     │  │  │     ├─ CDS.cpython-312.pyc
│     │     │  │  │     ├─ CERT.cpython-312.pyc
│     │     │  │  │     ├─ CNAME.cpython-312.pyc
│     │     │  │  │     ├─ CSYNC.cpython-312.pyc
│     │     │  │  │     ├─ DLV.cpython-312.pyc
│     │     │  │  │     ├─ DNAME.cpython-312.pyc
│     │     │  │  │     ├─ DNSKEY.cpython-312.pyc
│     │     │  │  │     ├─ DS.cpython-312.pyc
│     │     │  │  │     ├─ DSYNC.cpython-312.pyc
│     │     │  │  │     ├─ EUI48.cpython-312.pyc
│     │     │  │  │     ├─ EUI64.cpython-312.pyc
│     │     │  │  │     ├─ GPOS.cpython-312.pyc
│     │     │  │  │     ├─ HINFO.cpython-312.pyc
│     │     │  │  │     ├─ HIP.cpython-312.pyc
│     │     │  │  │     ├─ ISDN.cpython-312.pyc
│     │     │  │  │     ├─ L32.cpython-312.pyc
│     │     │  │  │     ├─ L64.cpython-312.pyc
│     │     │  │  │     ├─ LOC.cpython-312.pyc
│     │     │  │  │     ├─ LP.cpython-312.pyc
│     │     │  │  │     ├─ MX.cpython-312.pyc
│     │     │  │  │     ├─ NID.cpython-312.pyc
│     │     │  │  │     ├─ NINFO.cpython-312.pyc
│     │     │  │  │     ├─ NS.cpython-312.pyc
│     │     │  │  │     ├─ NSEC.cpython-312.pyc
│     │     │  │  │     ├─ NSEC3.cpython-312.pyc
│     │     │  │  │     ├─ NSEC3PARAM.cpython-312.pyc
│     │     │  │  │     ├─ OPENPGPKEY.cpython-312.pyc
│     │     │  │  │     ├─ OPT.cpython-312.pyc
│     │     │  │  │     ├─ PTR.cpython-312.pyc
│     │     │  │  │     ├─ RESINFO.cpython-312.pyc
│     │     │  │  │     ├─ RP.cpython-312.pyc
│     │     │  │  │     ├─ RRSIG.cpython-312.pyc
│     │     │  │  │     ├─ RT.cpython-312.pyc
│     │     │  │  │     ├─ SMIMEA.cpython-312.pyc
│     │     │  │  │     ├─ SOA.cpython-312.pyc
│     │     │  │  │     ├─ SPF.cpython-312.pyc
│     │     │  │  │     ├─ SSHFP.cpython-312.pyc
│     │     │  │  │     ├─ TKEY.cpython-312.pyc
│     │     │  │  │     ├─ TLSA.cpython-312.pyc
│     │     │  │  │     ├─ TSIG.cpython-312.pyc
│     │     │  │  │     ├─ TXT.cpython-312.pyc
│     │     │  │  │     ├─ URI.cpython-312.pyc
│     │     │  │  │     ├─ WALLET.cpython-312.pyc
│     │     │  │  │     ├─ X25.cpython-312.pyc
│     │     │  │  │     ├─ ZONEMD.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ CH
│     │     │  │  │  ├─ A.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ A.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ dnskeybase.py
│     │     │  │  ├─ dsbase.py
│     │     │  │  ├─ euibase.py
│     │     │  │  ├─ IN
│     │     │  │  │  ├─ A.py
│     │     │  │  │  ├─ AAAA.py
│     │     │  │  │  ├─ APL.py
│     │     │  │  │  ├─ DHCID.py
│     │     │  │  │  ├─ HTTPS.py
│     │     │  │  │  ├─ IPSECKEY.py
│     │     │  │  │  ├─ KX.py
│     │     │  │  │  ├─ NAPTR.py
│     │     │  │  │  ├─ NSAP.py
│     │     │  │  │  ├─ NSAP_PTR.py
│     │     │  │  │  ├─ PX.py
│     │     │  │  │  ├─ SRV.py
│     │     │  │  │  ├─ SVCB.py
│     │     │  │  │  ├─ WKS.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ A.cpython-312.pyc
│     │     │  │  │     ├─ AAAA.cpython-312.pyc
│     │     │  │  │     ├─ APL.cpython-312.pyc
│     │     │  │  │     ├─ DHCID.cpython-312.pyc
│     │     │  │  │     ├─ HTTPS.cpython-312.pyc
│     │     │  │  │     ├─ IPSECKEY.cpython-312.pyc
│     │     │  │  │     ├─ KX.cpython-312.pyc
│     │     │  │  │     ├─ NAPTR.cpython-312.pyc
│     │     │  │  │     ├─ NSAP.cpython-312.pyc
│     │     │  │  │     ├─ NSAP_PTR.cpython-312.pyc
│     │     │  │  │     ├─ PX.cpython-312.pyc
│     │     │  │  │     ├─ SRV.cpython-312.pyc
│     │     │  │  │     ├─ SVCB.cpython-312.pyc
│     │     │  │  │     ├─ WKS.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ mxbase.py
│     │     │  │  ├─ nsbase.py
│     │     │  │  ├─ svcbbase.py
│     │     │  │  ├─ tlsabase.py
│     │     │  │  ├─ txtbase.py
│     │     │  │  ├─ util.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ dnskeybase.cpython-312.pyc
│     │     │  │     ├─ dsbase.cpython-312.pyc
│     │     │  │     ├─ euibase.cpython-312.pyc
│     │     │  │     ├─ mxbase.cpython-312.pyc
│     │     │  │     ├─ nsbase.cpython-312.pyc
│     │     │  │     ├─ svcbbase.cpython-312.pyc
│     │     │  │     ├─ tlsabase.cpython-312.pyc
│     │     │  │     ├─ txtbase.cpython-312.pyc
│     │     │  │     ├─ util.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ renderer.py
│     │     │  ├─ resolver.py
│     │     │  ├─ reversename.py
│     │     │  ├─ rrset.py
│     │     │  ├─ serial.py
│     │     │  ├─ set.py
│     │     │  ├─ tokenizer.py
│     │     │  ├─ transaction.py
│     │     │  ├─ tsig.py
│     │     │  ├─ tsigkeyring.py
│     │     │  ├─ ttl.py
│     │     │  ├─ update.py
│     │     │  ├─ version.py
│     │     │  ├─ versioned.py
│     │     │  ├─ win32util.py
│     │     │  ├─ wire.py
│     │     │  ├─ xfr.py
│     │     │  ├─ zone.py
│     │     │  ├─ zonefile.py
│     │     │  ├─ zonetypes.py
│     │     │  ├─ _asyncbackend.py
│     │     │  ├─ _asyncio_backend.py
│     │     │  ├─ _ddr.py
│     │     │  ├─ _features.py
│     │     │  ├─ _immutable_ctx.py
│     │     │  ├─ _no_ssl.py
│     │     │  ├─ _tls_util.py
│     │     │  ├─ _trio_backend.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ asyncbackend.cpython-312.pyc
│     │     │     ├─ asyncquery.cpython-312.pyc
│     │     │     ├─ asyncresolver.cpython-312.pyc
│     │     │     ├─ btree.cpython-312.pyc
│     │     │     ├─ btreezone.cpython-312.pyc
│     │     │     ├─ dnssec.cpython-312.pyc
│     │     │     ├─ dnssectypes.cpython-312.pyc
│     │     │     ├─ e164.cpython-312.pyc
│     │     │     ├─ edns.cpython-312.pyc
│     │     │     ├─ entropy.cpython-312.pyc
│     │     │     ├─ enum.cpython-312.pyc
│     │     │     ├─ exception.cpython-312.pyc
│     │     │     ├─ flags.cpython-312.pyc
│     │     │     ├─ grange.cpython-312.pyc
│     │     │     ├─ immutable.cpython-312.pyc
│     │     │     ├─ inet.cpython-312.pyc
│     │     │     ├─ ipv4.cpython-312.pyc
│     │     │     ├─ ipv6.cpython-312.pyc
│     │     │     ├─ message.cpython-312.pyc
│     │     │     ├─ name.cpython-312.pyc
│     │     │     ├─ namedict.cpython-312.pyc
│     │     │     ├─ nameserver.cpython-312.pyc
│     │     │     ├─ node.cpython-312.pyc
│     │     │     ├─ opcode.cpython-312.pyc
│     │     │     ├─ query.cpython-312.pyc
│     │     │     ├─ rcode.cpython-312.pyc
│     │     │     ├─ rdata.cpython-312.pyc
│     │     │     ├─ rdataclass.cpython-312.pyc
│     │     │     ├─ rdataset.cpython-312.pyc
│     │     │     ├─ rdatatype.cpython-312.pyc
│     │     │     ├─ renderer.cpython-312.pyc
│     │     │     ├─ resolver.cpython-312.pyc
│     │     │     ├─ reversename.cpython-312.pyc
│     │     │     ├─ rrset.cpython-312.pyc
│     │     │     ├─ serial.cpython-312.pyc
│     │     │     ├─ set.cpython-312.pyc
│     │     │     ├─ tokenizer.cpython-312.pyc
│     │     │     ├─ transaction.cpython-312.pyc
│     │     │     ├─ tsig.cpython-312.pyc
│     │     │     ├─ tsigkeyring.cpython-312.pyc
│     │     │     ├─ ttl.cpython-312.pyc
│     │     │     ├─ update.cpython-312.pyc
│     │     │     ├─ version.cpython-312.pyc
│     │     │     ├─ versioned.cpython-312.pyc
│     │     │     ├─ win32util.cpython-312.pyc
│     │     │     ├─ wire.cpython-312.pyc
│     │     │     ├─ xfr.cpython-312.pyc
│     │     │     ├─ zone.cpython-312.pyc
│     │     │     ├─ zonefile.cpython-312.pyc
│     │     │     ├─ zonetypes.cpython-312.pyc
│     │     │     ├─ _asyncbackend.cpython-312.pyc
│     │     │     ├─ _asyncio_backend.cpython-312.pyc
│     │     │     ├─ _ddr.cpython-312.pyc
│     │     │     ├─ _features.cpython-312.pyc
│     │     │     ├─ _immutable_ctx.cpython-312.pyc
│     │     │     ├─ _no_ssl.cpython-312.pyc
│     │     │     ├─ _tls_util.cpython-312.pyc
│     │     │     ├─ _trio_backend.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ dnspython-2.8.0.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  └─ WHEEL
│     │     ├─ email_validator
│     │     │  ├─ deliverability.py
│     │     │  ├─ exceptions.py
│     │     │  ├─ py.typed
│     │     │  ├─ rfc_constants.py
│     │     │  ├─ syntax.py
│     │     │  ├─ types.py
│     │     │  ├─ validate_email.py
│     │     │  ├─ version.py
│     │     │  ├─ __init__.py
│     │     │  ├─ __main__.py
│     │     │  └─ __pycache__
│     │     │     ├─ deliverability.cpython-312.pyc
│     │     │     ├─ exceptions.cpython-312.pyc
│     │     │     ├─ rfc_constants.cpython-312.pyc
│     │     │     ├─ syntax.cpython-312.pyc
│     │     │     ├─ types.cpython-312.pyc
│     │     │     ├─ validate_email.cpython-312.pyc
│     │     │     ├─ version.cpython-312.pyc
│     │     │     ├─ __init__.cpython-312.pyc
│     │     │     └─ __main__.cpython-312.pyc
│     │     ├─ email_validator-2.3.0.dist-info
│     │     │  ├─ entry_points.txt
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ fastapi
│     │     │  ├─ applications.py
│     │     │  ├─ background.py
│     │     │  ├─ cli.py
│     │     │  ├─ concurrency.py
│     │     │  ├─ datastructures.py
│     │     │  ├─ dependencies
│     │     │  │  ├─ models.py
│     │     │  │  ├─ utils.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ models.cpython-312.pyc
│     │     │  │     ├─ utils.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ encoders.py
│     │     │  ├─ exceptions.py
│     │     │  ├─ exception_handlers.py
│     │     │  ├─ logger.py
│     │     │  ├─ middleware
│     │     │  │  ├─ cors.py
│     │     │  │  ├─ gzip.py
│     │     │  │  ├─ httpsredirect.py
│     │     │  │  ├─ trustedhost.py
│     │     │  │  ├─ wsgi.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ cors.cpython-312.pyc
│     │     │  │     ├─ gzip.cpython-312.pyc
│     │     │  │     ├─ httpsredirect.cpython-312.pyc
│     │     │  │     ├─ trustedhost.cpython-312.pyc
│     │     │  │     ├─ wsgi.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ openapi
│     │     │  │  ├─ constants.py
│     │     │  │  ├─ docs.py
│     │     │  │  ├─ models.py
│     │     │  │  ├─ utils.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ constants.cpython-312.pyc
│     │     │  │     ├─ docs.cpython-312.pyc
│     │     │  │     ├─ models.cpython-312.pyc
│     │     │  │     ├─ utils.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ params.py
│     │     │  ├─ param_functions.py
│     │     │  ├─ py.typed
│     │     │  ├─ requests.py
│     │     │  ├─ responses.py
│     │     │  ├─ routing.py
│     │     │  ├─ security
│     │     │  │  ├─ api_key.py
│     │     │  │  ├─ base.py
│     │     │  │  ├─ http.py
│     │     │  │  ├─ oauth2.py
│     │     │  │  ├─ open_id_connect_url.py
│     │     │  │  ├─ utils.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ api_key.cpython-312.pyc
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ http.cpython-312.pyc
│     │     │  │     ├─ oauth2.cpython-312.pyc
│     │     │  │     ├─ open_id_connect_url.cpython-312.pyc
│     │     │  │     ├─ utils.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ staticfiles.py
│     │     │  ├─ templating.py
│     │     │  ├─ testclient.py
│     │     │  ├─ types.py
│     │     │  ├─ utils.py
│     │     │  ├─ websockets.py
│     │     │  ├─ _compat.py
│     │     │  ├─ __init__.py
│     │     │  ├─ __main__.py
│     │     │  └─ __pycache__
│     │     │     ├─ applications.cpython-312.pyc
│     │     │     ├─ background.cpython-312.pyc
│     │     │     ├─ cli.cpython-312.pyc
│     │     │     ├─ concurrency.cpython-312.pyc
│     │     │     ├─ datastructures.cpython-312.pyc
│     │     │     ├─ encoders.cpython-312.pyc
│     │     │     ├─ exceptions.cpython-312.pyc
│     │     │     ├─ exception_handlers.cpython-312.pyc
│     │     │     ├─ logger.cpython-312.pyc
│     │     │     ├─ params.cpython-312.pyc
│     │     │     ├─ param_functions.cpython-312.pyc
│     │     │     ├─ requests.cpython-312.pyc
│     │     │     ├─ responses.cpython-312.pyc
│     │     │     ├─ routing.cpython-312.pyc
│     │     │     ├─ staticfiles.cpython-312.pyc
│     │     │     ├─ templating.cpython-312.pyc
│     │     │     ├─ testclient.cpython-312.pyc
│     │     │     ├─ types.cpython-312.pyc
│     │     │     ├─ utils.cpython-312.pyc
│     │     │     ├─ websockets.cpython-312.pyc
│     │     │     ├─ _compat.cpython-312.pyc
│     │     │     ├─ __init__.cpython-312.pyc
│     │     │     └─ __main__.cpython-312.pyc
│     │     ├─ fastapi-0.116.1.dist-info
│     │     │  ├─ entry_points.txt
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ greenlet
│     │     │  ├─ CObjects.cpp
│     │     │  ├─ greenlet.cpp
│     │     │  ├─ greenlet.h
│     │     │  ├─ greenlet_allocator.hpp
│     │     │  ├─ greenlet_compiler_compat.hpp
│     │     │  ├─ greenlet_cpython_compat.hpp
│     │     │  ├─ greenlet_exceptions.hpp
│     │     │  ├─ greenlet_internal.hpp
│     │     │  ├─ greenlet_msvc_compat.hpp
│     │     │  ├─ greenlet_refs.hpp
│     │     │  ├─ greenlet_slp_switch.hpp
│     │     │  ├─ greenlet_thread_support.hpp
│     │     │  ├─ platform
│     │     │  │  ├─ setup_switch_x64_masm.cmd
│     │     │  │  ├─ switch_aarch64_gcc.h
│     │     │  │  ├─ switch_alpha_unix.h
│     │     │  │  ├─ switch_amd64_unix.h
│     │     │  │  ├─ switch_arm32_gcc.h
│     │     │  │  ├─ switch_arm32_ios.h
│     │     │  │  ├─ switch_arm64_masm.asm
│     │     │  │  ├─ switch_arm64_masm.obj
│     │     │  │  ├─ switch_arm64_msvc.h
│     │     │  │  ├─ switch_csky_gcc.h
│     │     │  │  ├─ switch_loongarch64_linux.h
│     │     │  │  ├─ switch_m68k_gcc.h
│     │     │  │  ├─ switch_mips_unix.h
│     │     │  │  ├─ switch_ppc64_aix.h
│     │     │  │  ├─ switch_ppc64_linux.h
│     │     │  │  ├─ switch_ppc_aix.h
│     │     │  │  ├─ switch_ppc_linux.h
│     │     │  │  ├─ switch_ppc_macosx.h
│     │     │  │  ├─ switch_ppc_unix.h
│     │     │  │  ├─ switch_riscv_unix.h
│     │     │  │  ├─ switch_s390_unix.h
│     │     │  │  ├─ switch_sh_gcc.h
│     │     │  │  ├─ switch_sparc_sun_gcc.h
│     │     │  │  ├─ switch_x32_unix.h
│     │     │  │  ├─ switch_x64_masm.asm
│     │     │  │  ├─ switch_x64_masm.obj
│     │     │  │  ├─ switch_x64_msvc.h
│     │     │  │  ├─ switch_x86_msvc.h
│     │     │  │  ├─ switch_x86_unix.h
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ PyGreenlet.cpp
│     │     │  ├─ PyGreenlet.hpp
│     │     │  ├─ PyGreenletUnswitchable.cpp
│     │     │  ├─ PyModule.cpp
│     │     │  ├─ slp_platformselect.h
│     │     │  ├─ TBrokenGreenlet.cpp
│     │     │  ├─ tests
│     │     │  │  ├─ fail_clearing_run_switches.py
│     │     │  │  ├─ fail_cpp_exception.py
│     │     │  │  ├─ fail_initialstub_already_started.py
│     │     │  │  ├─ fail_slp_switch.py
│     │     │  │  ├─ fail_switch_three_greenlets.py
│     │     │  │  ├─ fail_switch_three_greenlets2.py
│     │     │  │  ├─ fail_switch_two_greenlets.py
│     │     │  │  ├─ leakcheck.py
│     │     │  │  ├─ test_contextvars.py
│     │     │  │  ├─ test_cpp.py
│     │     │  │  ├─ test_extension_interface.py
│     │     │  │  ├─ test_gc.py
│     │     │  │  ├─ test_generator.py
│     │     │  │  ├─ test_generator_nested.py
│     │     │  │  ├─ test_greenlet.py
│     │     │  │  ├─ test_greenlet_trash.py
│     │     │  │  ├─ test_leaks.py
│     │     │  │  ├─ test_stack_saved.py
│     │     │  │  ├─ test_throw.py
│     │     │  │  ├─ test_tracing.py
│     │     │  │  ├─ test_version.py
│     │     │  │  ├─ test_weakref.py
│     │     │  │  ├─ _test_extension.c
│     │     │  │  ├─ _test_extension.cp312-win_amd64.pyd
│     │     │  │  ├─ _test_extension_cpp.cp312-win_amd64.pyd
│     │     │  │  ├─ _test_extension_cpp.cpp
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ fail_clearing_run_switches.cpython-312.pyc
│     │     │  │     ├─ fail_cpp_exception.cpython-312.pyc
│     │     │  │     ├─ fail_initialstub_already_started.cpython-312.pyc
│     │     │  │     ├─ fail_slp_switch.cpython-312.pyc
│     │     │  │     ├─ fail_switch_three_greenlets.cpython-312.pyc
│     │     │  │     ├─ fail_switch_three_greenlets2.cpython-312.pyc
│     │     │  │     ├─ fail_switch_two_greenlets.cpython-312.pyc
│     │     │  │     ├─ leakcheck.cpython-312.pyc
│     │     │  │     ├─ test_contextvars.cpython-312.pyc
│     │     │  │     ├─ test_cpp.cpython-312.pyc
│     │     │  │     ├─ test_extension_interface.cpython-312.pyc
│     │     │  │     ├─ test_gc.cpython-312.pyc
│     │     │  │     ├─ test_generator.cpython-312.pyc
│     │     │  │     ├─ test_generator_nested.cpython-312.pyc
│     │     │  │     ├─ test_greenlet.cpython-312.pyc
│     │     │  │     ├─ test_greenlet_trash.cpython-312.pyc
│     │     │  │     ├─ test_leaks.cpython-312.pyc
│     │     │  │     ├─ test_stack_saved.cpython-312.pyc
│     │     │  │     ├─ test_throw.cpython-312.pyc
│     │     │  │     ├─ test_tracing.cpython-312.pyc
│     │     │  │     ├─ test_version.cpython-312.pyc
│     │     │  │     ├─ test_weakref.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ TExceptionState.cpp
│     │     │  ├─ TGreenlet.cpp
│     │     │  ├─ TGreenlet.hpp
│     │     │  ├─ TGreenletGlobals.cpp
│     │     │  ├─ TMainGreenlet.cpp
│     │     │  ├─ TPythonState.cpp
│     │     │  ├─ TStackState.cpp
│     │     │  ├─ TThreadState.hpp
│     │     │  ├─ TThreadStateCreator.hpp
│     │     │  ├─ TThreadStateDestroy.cpp
│     │     │  ├─ TUserGreenlet.cpp
│     │     │  ├─ _greenlet.cp312-win_amd64.pyd
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ greenlet-3.2.4.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  ├─ LICENSE
│     │     │  │  └─ LICENSE.PSF
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ h11
│     │     │  ├─ py.typed
│     │     │  ├─ _abnf.py
│     │     │  ├─ _connection.py
│     │     │  ├─ _events.py
│     │     │  ├─ _headers.py
│     │     │  ├─ _readers.py
│     │     │  ├─ _receivebuffer.py
│     │     │  ├─ _state.py
│     │     │  ├─ _util.py
│     │     │  ├─ _version.py
│     │     │  ├─ _writers.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ _abnf.cpython-312.pyc
│     │     │     ├─ _connection.cpython-312.pyc
│     │     │     ├─ _events.cpython-312.pyc
│     │     │     ├─ _headers.cpython-312.pyc
│     │     │     ├─ _readers.cpython-312.pyc
│     │     │     ├─ _receivebuffer.cpython-312.pyc
│     │     │     ├─ _state.cpython-312.pyc
│     │     │     ├─ _util.cpython-312.pyc
│     │     │     ├─ _version.cpython-312.pyc
│     │     │     ├─ _writers.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ h11-0.16.0.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE.txt
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ httpcore
│     │     │  ├─ py.typed
│     │     │  ├─ _api.py
│     │     │  ├─ _async
│     │     │  │  ├─ connection.py
│     │     │  │  ├─ connection_pool.py
│     │     │  │  ├─ http11.py
│     │     │  │  ├─ http2.py
│     │     │  │  ├─ http_proxy.py
│     │     │  │  ├─ interfaces.py
│     │     │  │  ├─ socks_proxy.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ connection.cpython-312.pyc
│     │     │  │     ├─ connection_pool.cpython-312.pyc
│     │     │  │     ├─ http11.cpython-312.pyc
│     │     │  │     ├─ http2.cpython-312.pyc
│     │     │  │     ├─ http_proxy.cpython-312.pyc
│     │     │  │     ├─ interfaces.cpython-312.pyc
│     │     │  │     ├─ socks_proxy.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _backends
│     │     │  │  ├─ anyio.py
│     │     │  │  ├─ auto.py
│     │     │  │  ├─ base.py
│     │     │  │  ├─ mock.py
│     │     │  │  ├─ sync.py
│     │     │  │  ├─ trio.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ anyio.cpython-312.pyc
│     │     │  │     ├─ auto.cpython-312.pyc
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ mock.cpython-312.pyc
│     │     │  │     ├─ sync.cpython-312.pyc
│     │     │  │     ├─ trio.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _exceptions.py
│     │     │  ├─ _models.py
│     │     │  ├─ _ssl.py
│     │     │  ├─ _sync
│     │     │  │  ├─ connection.py
│     │     │  │  ├─ connection_pool.py
│     │     │  │  ├─ http11.py
│     │     │  │  ├─ http2.py
│     │     │  │  ├─ http_proxy.py
│     │     │  │  ├─ interfaces.py
│     │     │  │  ├─ socks_proxy.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ connection.cpython-312.pyc
│     │     │  │     ├─ connection_pool.cpython-312.pyc
│     │     │  │     ├─ http11.cpython-312.pyc
│     │     │  │     ├─ http2.cpython-312.pyc
│     │     │  │     ├─ http_proxy.cpython-312.pyc
│     │     │  │     ├─ interfaces.cpython-312.pyc
│     │     │  │     ├─ socks_proxy.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _synchronization.py
│     │     │  ├─ _trace.py
│     │     │  ├─ _utils.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ _api.cpython-312.pyc
│     │     │     ├─ _exceptions.cpython-312.pyc
│     │     │     ├─ _models.cpython-312.pyc
│     │     │     ├─ _ssl.cpython-312.pyc
│     │     │     ├─ _synchronization.cpython-312.pyc
│     │     │     ├─ _trace.cpython-312.pyc
│     │     │     ├─ _utils.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ httpcore-1.0.9.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE.md
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  └─ WHEEL
│     │     ├─ httpx
│     │     │  ├─ py.typed
│     │     │  ├─ _api.py
│     │     │  ├─ _auth.py
│     │     │  ├─ _client.py
│     │     │  ├─ _config.py
│     │     │  ├─ _content.py
│     │     │  ├─ _decoders.py
│     │     │  ├─ _exceptions.py
│     │     │  ├─ _main.py
│     │     │  ├─ _models.py
│     │     │  ├─ _multipart.py
│     │     │  ├─ _status_codes.py
│     │     │  ├─ _transports
│     │     │  │  ├─ asgi.py
│     │     │  │  ├─ base.py
│     │     │  │  ├─ default.py
│     │     │  │  ├─ mock.py
│     │     │  │  ├─ wsgi.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ asgi.cpython-312.pyc
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ default.cpython-312.pyc
│     │     │  │     ├─ mock.cpython-312.pyc
│     │     │  │     ├─ wsgi.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _types.py
│     │     │  ├─ _urlparse.py
│     │     │  ├─ _urls.py
│     │     │  ├─ _utils.py
│     │     │  ├─ __init__.py
│     │     │  ├─ __pycache__
│     │     │  │  ├─ _api.cpython-312.pyc
│     │     │  │  ├─ _auth.cpython-312.pyc
│     │     │  │  ├─ _client.cpython-312.pyc
│     │     │  │  ├─ _config.cpython-312.pyc
│     │     │  │  ├─ _content.cpython-312.pyc
│     │     │  │  ├─ _decoders.cpython-312.pyc
│     │     │  │  ├─ _exceptions.cpython-312.pyc
│     │     │  │  ├─ _main.cpython-312.pyc
│     │     │  │  ├─ _models.cpython-312.pyc
│     │     │  │  ├─ _multipart.cpython-312.pyc
│     │     │  │  ├─ _status_codes.cpython-312.pyc
│     │     │  │  ├─ _types.cpython-312.pyc
│     │     │  │  ├─ _urlparse.cpython-312.pyc
│     │     │  │  ├─ _urls.cpython-312.pyc
│     │     │  │  ├─ _utils.cpython-312.pyc
│     │     │  │  ├─ __init__.cpython-312.pyc
│     │     │  │  └─ __version__.cpython-312.pyc
│     │     │  └─ __version__.py
│     │     ├─ httpx-0.28.1.dist-info
│     │     │  ├─ entry_points.txt
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE.md
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  └─ WHEEL
│     │     ├─ idna
│     │     │  ├─ codec.py
│     │     │  ├─ compat.py
│     │     │  ├─ core.py
│     │     │  ├─ idnadata.py
│     │     │  ├─ intranges.py
│     │     │  ├─ package_data.py
│     │     │  ├─ py.typed
│     │     │  ├─ uts46data.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ codec.cpython-312.pyc
│     │     │     ├─ compat.cpython-312.pyc
│     │     │     ├─ core.cpython-312.pyc
│     │     │     ├─ idnadata.cpython-312.pyc
│     │     │     ├─ intranges.cpython-312.pyc
│     │     │     ├─ package_data.cpython-312.pyc
│     │     │     ├─ uts46data.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ idna-3.10.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ LICENSE.md
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ jiter
│     │     │  ├─ jiter.cp312-win_amd64.pyd
│     │     │  ├─ py.typed
│     │     │  ├─ __init__.py
│     │     │  ├─ __init__.pyi
│     │     │  └─ __pycache__
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ jiter-0.10.0.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  └─ WHEEL
│     │     ├─ multipart
│     │     │  ├─ decoders.py
│     │     │  ├─ exceptions.py
│     │     │  ├─ multipart.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ decoders.cpython-312.pyc
│     │     │     ├─ exceptions.cpython-312.pyc
│     │     │     ├─ multipart.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ openai
│     │     │  ├─ cli
│     │     │  │  ├─ _api
│     │     │  │  │  ├─ audio.py
│     │     │  │  │  ├─ chat
│     │     │  │  │  │  ├─ completions.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ completions.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ completions.py
│     │     │  │  │  ├─ files.py
│     │     │  │  │  ├─ fine_tuning
│     │     │  │  │  │  ├─ jobs.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ jobs.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ image.py
│     │     │  │  │  ├─ models.py
│     │     │  │  │  ├─ _main.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ audio.cpython-312.pyc
│     │     │  │  │     ├─ completions.cpython-312.pyc
│     │     │  │  │     ├─ files.cpython-312.pyc
│     │     │  │  │     ├─ image.cpython-312.pyc
│     │     │  │  │     ├─ models.cpython-312.pyc
│     │     │  │  │     ├─ _main.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ _cli.py
│     │     │  │  ├─ _errors.py
│     │     │  │  ├─ _models.py
│     │     │  │  ├─ _progress.py
│     │     │  │  ├─ _tools
│     │     │  │  │  ├─ fine_tunes.py
│     │     │  │  │  ├─ migrate.py
│     │     │  │  │  ├─ _main.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ fine_tunes.cpython-312.pyc
│     │     │  │  │     ├─ migrate.cpython-312.pyc
│     │     │  │  │     ├─ _main.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ _utils.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ _cli.cpython-312.pyc
│     │     │  │     ├─ _errors.cpython-312.pyc
│     │     │  │     ├─ _models.cpython-312.pyc
│     │     │  │     ├─ _progress.cpython-312.pyc
│     │     │  │     ├─ _utils.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ helpers
│     │     │  │  ├─ local_audio_player.py
│     │     │  │  ├─ microphone.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ local_audio_player.cpython-312.pyc
│     │     │  │     ├─ microphone.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ lib
│     │     │  │  ├─ .keep
│     │     │  │  ├─ azure.py
│     │     │  │  ├─ streaming
│     │     │  │  │  ├─ chat
│     │     │  │  │  │  ├─ _completions.py
│     │     │  │  │  │  ├─ _events.py
│     │     │  │  │  │  ├─ _types.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ _completions.cpython-312.pyc
│     │     │  │  │  │     ├─ _events.cpython-312.pyc
│     │     │  │  │  │     ├─ _types.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ responses
│     │     │  │  │  │  ├─ _events.py
│     │     │  │  │  │  ├─ _responses.py
│     │     │  │  │  │  ├─ _types.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ _events.cpython-312.pyc
│     │     │  │  │  │     ├─ _responses.cpython-312.pyc
│     │     │  │  │  │     ├─ _types.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ _assistants.py
│     │     │  │  │  ├─ _deltas.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ _assistants.cpython-312.pyc
│     │     │  │  │     ├─ _deltas.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ _old_api.py
│     │     │  │  ├─ _parsing
│     │     │  │  │  ├─ _completions.py
│     │     │  │  │  ├─ _responses.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ _completions.cpython-312.pyc
│     │     │  │  │     ├─ _responses.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ _pydantic.py
│     │     │  │  ├─ _tools.py
│     │     │  │  ├─ _validators.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ azure.cpython-312.pyc
│     │     │  │     ├─ _old_api.cpython-312.pyc
│     │     │  │     ├─ _pydantic.cpython-312.pyc
│     │     │  │     ├─ _tools.cpython-312.pyc
│     │     │  │     ├─ _validators.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ pagination.py
│     │     │  ├─ py.typed
│     │     │  ├─ resources
│     │     │  │  ├─ audio
│     │     │  │  │  ├─ audio.py
│     │     │  │  │  ├─ speech.py
│     │     │  │  │  ├─ transcriptions.py
│     │     │  │  │  ├─ translations.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ audio.cpython-312.pyc
│     │     │  │  │     ├─ speech.cpython-312.pyc
│     │     │  │  │     ├─ transcriptions.cpython-312.pyc
│     │     │  │  │     ├─ translations.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ batches.py
│     │     │  │  ├─ beta
│     │     │  │  │  ├─ assistants.py
│     │     │  │  │  ├─ beta.py
│     │     │  │  │  ├─ realtime
│     │     │  │  │  │  ├─ realtime.py
│     │     │  │  │  │  ├─ sessions.py
│     │     │  │  │  │  ├─ transcription_sessions.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ realtime.cpython-312.pyc
│     │     │  │  │  │     ├─ sessions.cpython-312.pyc
│     │     │  │  │  │     ├─ transcription_sessions.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ threads
│     │     │  │  │  │  ├─ messages.py
│     │     │  │  │  │  ├─ runs
│     │     │  │  │  │  │  ├─ runs.py
│     │     │  │  │  │  │  ├─ steps.py
│     │     │  │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  │  └─ __pycache__
│     │     │  │  │  │  │     ├─ runs.cpython-312.pyc
│     │     │  │  │  │  │     ├─ steps.cpython-312.pyc
│     │     │  │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  │  ├─ threads.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ messages.cpython-312.pyc
│     │     │  │  │  │     ├─ threads.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ assistants.cpython-312.pyc
│     │     │  │  │     ├─ beta.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ chat
│     │     │  │  │  ├─ chat.py
│     │     │  │  │  ├─ completions
│     │     │  │  │  │  ├─ completions.py
│     │     │  │  │  │  ├─ messages.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ completions.cpython-312.pyc
│     │     │  │  │  │     ├─ messages.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ chat.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ completions.py
│     │     │  │  ├─ containers
│     │     │  │  │  ├─ containers.py
│     │     │  │  │  ├─ files
│     │     │  │  │  │  ├─ content.py
│     │     │  │  │  │  ├─ files.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ content.cpython-312.pyc
│     │     │  │  │  │     ├─ files.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ containers.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ conversations
│     │     │  │  │  ├─ conversations.py
│     │     │  │  │  ├─ items.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ conversations.cpython-312.pyc
│     │     │  │  │     ├─ items.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ embeddings.py
│     │     │  │  ├─ evals
│     │     │  │  │  ├─ evals.py
│     │     │  │  │  ├─ runs
│     │     │  │  │  │  ├─ output_items.py
│     │     │  │  │  │  ├─ runs.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ output_items.cpython-312.pyc
│     │     │  │  │  │     ├─ runs.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ evals.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ files.py
│     │     │  │  ├─ fine_tuning
│     │     │  │  │  ├─ alpha
│     │     │  │  │  │  ├─ alpha.py
│     │     │  │  │  │  ├─ graders.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ alpha.cpython-312.pyc
│     │     │  │  │  │     ├─ graders.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ checkpoints
│     │     │  │  │  │  ├─ checkpoints.py
│     │     │  │  │  │  ├─ permissions.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ checkpoints.cpython-312.pyc
│     │     │  │  │  │     ├─ permissions.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ fine_tuning.py
│     │     │  │  │  ├─ jobs
│     │     │  │  │  │  ├─ checkpoints.py
│     │     │  │  │  │  ├─ jobs.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ checkpoints.cpython-312.pyc
│     │     │  │  │  │     ├─ jobs.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ fine_tuning.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ images.py
│     │     │  │  ├─ models.py
│     │     │  │  ├─ moderations.py
│     │     │  │  ├─ realtime
│     │     │  │  │  ├─ client_secrets.py
│     │     │  │  │  ├─ realtime.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ client_secrets.cpython-312.pyc
│     │     │  │  │     ├─ realtime.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ responses
│     │     │  │  │  ├─ input_items.py
│     │     │  │  │  ├─ responses.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ input_items.cpython-312.pyc
│     │     │  │  │     ├─ responses.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ uploads
│     │     │  │  │  ├─ parts.py
│     │     │  │  │  ├─ uploads.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ parts.cpython-312.pyc
│     │     │  │  │     ├─ uploads.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ vector_stores
│     │     │  │  │  ├─ files.py
│     │     │  │  │  ├─ file_batches.py
│     │     │  │  │  ├─ vector_stores.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ files.cpython-312.pyc
│     │     │  │  │     ├─ file_batches.cpython-312.pyc
│     │     │  │  │     ├─ vector_stores.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ webhooks.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ batches.cpython-312.pyc
│     │     │  │     ├─ completions.cpython-312.pyc
│     │     │  │     ├─ embeddings.cpython-312.pyc
│     │     │  │     ├─ files.cpython-312.pyc
│     │     │  │     ├─ images.cpython-312.pyc
│     │     │  │     ├─ models.cpython-312.pyc
│     │     │  │     ├─ moderations.cpython-312.pyc
│     │     │  │     ├─ webhooks.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ types
│     │     │  │  ├─ audio
│     │     │  │  │  ├─ speech_create_params.py
│     │     │  │  │  ├─ speech_model.py
│     │     │  │  │  ├─ transcription.py
│     │     │  │  │  ├─ transcription_create_params.py
│     │     │  │  │  ├─ transcription_create_response.py
│     │     │  │  │  ├─ transcription_include.py
│     │     │  │  │  ├─ transcription_segment.py
│     │     │  │  │  ├─ transcription_stream_event.py
│     │     │  │  │  ├─ transcription_text_delta_event.py
│     │     │  │  │  ├─ transcription_text_done_event.py
│     │     │  │  │  ├─ transcription_verbose.py
│     │     │  │  │  ├─ transcription_word.py
│     │     │  │  │  ├─ translation.py
│     │     │  │  │  ├─ translation_create_params.py
│     │     │  │  │  ├─ translation_create_response.py
│     │     │  │  │  ├─ translation_verbose.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ speech_create_params.cpython-312.pyc
│     │     │  │  │     ├─ speech_model.cpython-312.pyc
│     │     │  │  │     ├─ transcription.cpython-312.pyc
│     │     │  │  │     ├─ transcription_create_params.cpython-312.pyc
│     │     │  │  │     ├─ transcription_create_response.cpython-312.pyc
│     │     │  │  │     ├─ transcription_include.cpython-312.pyc
│     │     │  │  │     ├─ transcription_segment.cpython-312.pyc
│     │     │  │  │     ├─ transcription_stream_event.cpython-312.pyc
│     │     │  │  │     ├─ transcription_text_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ transcription_text_done_event.cpython-312.pyc
│     │     │  │  │     ├─ transcription_verbose.cpython-312.pyc
│     │     │  │  │     ├─ transcription_word.cpython-312.pyc
│     │     │  │  │     ├─ translation.cpython-312.pyc
│     │     │  │  │     ├─ translation_create_params.cpython-312.pyc
│     │     │  │  │     ├─ translation_create_response.cpython-312.pyc
│     │     │  │  │     ├─ translation_verbose.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ audio_model.py
│     │     │  │  ├─ audio_response_format.py
│     │     │  │  ├─ auto_file_chunking_strategy_param.py
│     │     │  │  ├─ batch.py
│     │     │  │  ├─ batch_create_params.py
│     │     │  │  ├─ batch_error.py
│     │     │  │  ├─ batch_list_params.py
│     │     │  │  ├─ batch_request_counts.py
│     │     │  │  ├─ beta
│     │     │  │  │  ├─ assistant.py
│     │     │  │  │  ├─ assistant_create_params.py
│     │     │  │  │  ├─ assistant_deleted.py
│     │     │  │  │  ├─ assistant_list_params.py
│     │     │  │  │  ├─ assistant_response_format_option.py
│     │     │  │  │  ├─ assistant_response_format_option_param.py
│     │     │  │  │  ├─ assistant_stream_event.py
│     │     │  │  │  ├─ assistant_tool.py
│     │     │  │  │  ├─ assistant_tool_choice.py
│     │     │  │  │  ├─ assistant_tool_choice_function.py
│     │     │  │  │  ├─ assistant_tool_choice_function_param.py
│     │     │  │  │  ├─ assistant_tool_choice_option.py
│     │     │  │  │  ├─ assistant_tool_choice_option_param.py
│     │     │  │  │  ├─ assistant_tool_choice_param.py
│     │     │  │  │  ├─ assistant_tool_param.py
│     │     │  │  │  ├─ assistant_update_params.py
│     │     │  │  │  ├─ chat
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ code_interpreter_tool.py
│     │     │  │  │  ├─ code_interpreter_tool_param.py
│     │     │  │  │  ├─ file_search_tool.py
│     │     │  │  │  ├─ file_search_tool_param.py
│     │     │  │  │  ├─ function_tool.py
│     │     │  │  │  ├─ function_tool_param.py
│     │     │  │  │  ├─ realtime
│     │     │  │  │  │  ├─ conversation_created_event.py
│     │     │  │  │  │  ├─ conversation_item.py
│     │     │  │  │  │  ├─ conversation_item_content.py
│     │     │  │  │  │  ├─ conversation_item_content_param.py
│     │     │  │  │  │  ├─ conversation_item_created_event.py
│     │     │  │  │  │  ├─ conversation_item_create_event.py
│     │     │  │  │  │  ├─ conversation_item_create_event_param.py
│     │     │  │  │  │  ├─ conversation_item_deleted_event.py
│     │     │  │  │  │  ├─ conversation_item_delete_event.py
│     │     │  │  │  │  ├─ conversation_item_delete_event_param.py
│     │     │  │  │  │  ├─ conversation_item_input_audio_transcription_completed_event.py
│     │     │  │  │  │  ├─ conversation_item_input_audio_transcription_delta_event.py
│     │     │  │  │  │  ├─ conversation_item_input_audio_transcription_failed_event.py
│     │     │  │  │  │  ├─ conversation_item_param.py
│     │     │  │  │  │  ├─ conversation_item_retrieve_event.py
│     │     │  │  │  │  ├─ conversation_item_retrieve_event_param.py
│     │     │  │  │  │  ├─ conversation_item_truncated_event.py
│     │     │  │  │  │  ├─ conversation_item_truncate_event.py
│     │     │  │  │  │  ├─ conversation_item_truncate_event_param.py
│     │     │  │  │  │  ├─ conversation_item_with_reference.py
│     │     │  │  │  │  ├─ conversation_item_with_reference_param.py
│     │     │  │  │  │  ├─ error_event.py
│     │     │  │  │  │  ├─ input_audio_buffer_append_event.py
│     │     │  │  │  │  ├─ input_audio_buffer_append_event_param.py
│     │     │  │  │  │  ├─ input_audio_buffer_cleared_event.py
│     │     │  │  │  │  ├─ input_audio_buffer_clear_event.py
│     │     │  │  │  │  ├─ input_audio_buffer_clear_event_param.py
│     │     │  │  │  │  ├─ input_audio_buffer_committed_event.py
│     │     │  │  │  │  ├─ input_audio_buffer_commit_event.py
│     │     │  │  │  │  ├─ input_audio_buffer_commit_event_param.py
│     │     │  │  │  │  ├─ input_audio_buffer_speech_started_event.py
│     │     │  │  │  │  ├─ input_audio_buffer_speech_stopped_event.py
│     │     │  │  │  │  ├─ rate_limits_updated_event.py
│     │     │  │  │  │  ├─ realtime_client_event.py
│     │     │  │  │  │  ├─ realtime_client_event_param.py
│     │     │  │  │  │  ├─ realtime_connect_params.py
│     │     │  │  │  │  ├─ realtime_response.py
│     │     │  │  │  │  ├─ realtime_response_status.py
│     │     │  │  │  │  ├─ realtime_response_usage.py
│     │     │  │  │  │  ├─ realtime_server_event.py
│     │     │  │  │  │  ├─ response_audio_delta_event.py
│     │     │  │  │  │  ├─ response_audio_done_event.py
│     │     │  │  │  │  ├─ response_audio_transcript_delta_event.py
│     │     │  │  │  │  ├─ response_audio_transcript_done_event.py
│     │     │  │  │  │  ├─ response_cancel_event.py
│     │     │  │  │  │  ├─ response_cancel_event_param.py
│     │     │  │  │  │  ├─ response_content_part_added_event.py
│     │     │  │  │  │  ├─ response_content_part_done_event.py
│     │     │  │  │  │  ├─ response_created_event.py
│     │     │  │  │  │  ├─ response_create_event.py
│     │     │  │  │  │  ├─ response_create_event_param.py
│     │     │  │  │  │  ├─ response_done_event.py
│     │     │  │  │  │  ├─ response_function_call_arguments_delta_event.py
│     │     │  │  │  │  ├─ response_function_call_arguments_done_event.py
│     │     │  │  │  │  ├─ response_output_item_added_event.py
│     │     │  │  │  │  ├─ response_output_item_done_event.py
│     │     │  │  │  │  ├─ response_text_delta_event.py
│     │     │  │  │  │  ├─ response_text_done_event.py
│     │     │  │  │  │  ├─ session.py
│     │     │  │  │  │  ├─ session_created_event.py
│     │     │  │  │  │  ├─ session_create_params.py
│     │     │  │  │  │  ├─ session_create_response.py
│     │     │  │  │  │  ├─ session_updated_event.py
│     │     │  │  │  │  ├─ session_update_event.py
│     │     │  │  │  │  ├─ session_update_event_param.py
│     │     │  │  │  │  ├─ transcription_session.py
│     │     │  │  │  │  ├─ transcription_session_create_params.py
│     │     │  │  │  │  ├─ transcription_session_update.py
│     │     │  │  │  │  ├─ transcription_session_updated_event.py
│     │     │  │  │  │  ├─ transcription_session_update_param.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ conversation_created_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_content.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_content_param.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_created_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_create_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_create_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_deleted_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_delete_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_delete_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_input_audio_transcription_completed_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_input_audio_transcription_delta_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_input_audio_transcription_failed_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_param.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_retrieve_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_retrieve_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_truncated_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_truncate_event.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_truncate_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_with_reference.cpython-312.pyc
│     │     │  │  │  │     ├─ conversation_item_with_reference_param.cpython-312.pyc
│     │     │  │  │  │     ├─ error_event.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_append_event.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_append_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_cleared_event.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_clear_event.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_clear_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_committed_event.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_commit_event.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_commit_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_speech_started_event.cpython-312.pyc
│     │     │  │  │  │     ├─ input_audio_buffer_speech_stopped_event.cpython-312.pyc
│     │     │  │  │  │     ├─ rate_limits_updated_event.cpython-312.pyc
│     │     │  │  │  │     ├─ realtime_client_event.cpython-312.pyc
│     │     │  │  │  │     ├─ realtime_client_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ realtime_connect_params.cpython-312.pyc
│     │     │  │  │  │     ├─ realtime_response.cpython-312.pyc
│     │     │  │  │  │     ├─ realtime_response_status.cpython-312.pyc
│     │     │  │  │  │     ├─ realtime_response_usage.cpython-312.pyc
│     │     │  │  │  │     ├─ realtime_server_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_audio_delta_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_audio_done_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_audio_transcript_delta_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_audio_transcript_done_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_cancel_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_cancel_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ response_content_part_added_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_content_part_done_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_created_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_create_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_create_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ response_done_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_function_call_arguments_delta_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_function_call_arguments_done_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_output_item_added_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_output_item_done_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_text_delta_event.cpython-312.pyc
│     │     │  │  │  │     ├─ response_text_done_event.cpython-312.pyc
│     │     │  │  │  │     ├─ session.cpython-312.pyc
│     │     │  │  │  │     ├─ session_created_event.cpython-312.pyc
│     │     │  │  │  │     ├─ session_create_params.cpython-312.pyc
│     │     │  │  │  │     ├─ session_create_response.cpython-312.pyc
│     │     │  │  │  │     ├─ session_updated_event.cpython-312.pyc
│     │     │  │  │  │     ├─ session_update_event.cpython-312.pyc
│     │     │  │  │  │     ├─ session_update_event_param.cpython-312.pyc
│     │     │  │  │  │     ├─ transcription_session.cpython-312.pyc
│     │     │  │  │  │     ├─ transcription_session_create_params.cpython-312.pyc
│     │     │  │  │  │     ├─ transcription_session_update.cpython-312.pyc
│     │     │  │  │  │     ├─ transcription_session_updated_event.cpython-312.pyc
│     │     │  │  │  │     ├─ transcription_session_update_param.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ thread.py
│     │     │  │  │  ├─ threads
│     │     │  │  │  │  ├─ annotation.py
│     │     │  │  │  │  ├─ annotation_delta.py
│     │     │  │  │  │  ├─ file_citation_annotation.py
│     │     │  │  │  │  ├─ file_citation_delta_annotation.py
│     │     │  │  │  │  ├─ file_path_annotation.py
│     │     │  │  │  │  ├─ file_path_delta_annotation.py
│     │     │  │  │  │  ├─ image_file.py
│     │     │  │  │  │  ├─ image_file_content_block.py
│     │     │  │  │  │  ├─ image_file_content_block_param.py
│     │     │  │  │  │  ├─ image_file_delta.py
│     │     │  │  │  │  ├─ image_file_delta_block.py
│     │     │  │  │  │  ├─ image_file_param.py
│     │     │  │  │  │  ├─ image_url.py
│     │     │  │  │  │  ├─ image_url_content_block.py
│     │     │  │  │  │  ├─ image_url_content_block_param.py
│     │     │  │  │  │  ├─ image_url_delta.py
│     │     │  │  │  │  ├─ image_url_delta_block.py
│     │     │  │  │  │  ├─ image_url_param.py
│     │     │  │  │  │  ├─ message.py
│     │     │  │  │  │  ├─ message_content.py
│     │     │  │  │  │  ├─ message_content_delta.py
│     │     │  │  │  │  ├─ message_content_part_param.py
│     │     │  │  │  │  ├─ message_create_params.py
│     │     │  │  │  │  ├─ message_deleted.py
│     │     │  │  │  │  ├─ message_delta.py
│     │     │  │  │  │  ├─ message_delta_event.py
│     │     │  │  │  │  ├─ message_list_params.py
│     │     │  │  │  │  ├─ message_update_params.py
│     │     │  │  │  │  ├─ refusal_content_block.py
│     │     │  │  │  │  ├─ refusal_delta_block.py
│     │     │  │  │  │  ├─ required_action_function_tool_call.py
│     │     │  │  │  │  ├─ run.py
│     │     │  │  │  │  ├─ runs
│     │     │  │  │  │  │  ├─ code_interpreter_logs.py
│     │     │  │  │  │  │  ├─ code_interpreter_output_image.py
│     │     │  │  │  │  │  ├─ code_interpreter_tool_call.py
│     │     │  │  │  │  │  ├─ code_interpreter_tool_call_delta.py
│     │     │  │  │  │  │  ├─ file_search_tool_call.py
│     │     │  │  │  │  │  ├─ file_search_tool_call_delta.py
│     │     │  │  │  │  │  ├─ function_tool_call.py
│     │     │  │  │  │  │  ├─ function_tool_call_delta.py
│     │     │  │  │  │  │  ├─ message_creation_step_details.py
│     │     │  │  │  │  │  ├─ run_step.py
│     │     │  │  │  │  │  ├─ run_step_delta.py
│     │     │  │  │  │  │  ├─ run_step_delta_event.py
│     │     │  │  │  │  │  ├─ run_step_delta_message_delta.py
│     │     │  │  │  │  │  ├─ run_step_include.py
│     │     │  │  │  │  │  ├─ step_list_params.py
│     │     │  │  │  │  │  ├─ step_retrieve_params.py
│     │     │  │  │  │  │  ├─ tool_call.py
│     │     │  │  │  │  │  ├─ tool_calls_step_details.py
│     │     │  │  │  │  │  ├─ tool_call_delta.py
│     │     │  │  │  │  │  ├─ tool_call_delta_object.py
│     │     │  │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  │  └─ __pycache__
│     │     │  │  │  │  │     ├─ code_interpreter_logs.cpython-312.pyc
│     │     │  │  │  │  │     ├─ code_interpreter_output_image.cpython-312.pyc
│     │     │  │  │  │  │     ├─ code_interpreter_tool_call.cpython-312.pyc
│     │     │  │  │  │  │     ├─ code_interpreter_tool_call_delta.cpython-312.pyc
│     │     │  │  │  │  │     ├─ file_search_tool_call.cpython-312.pyc
│     │     │  │  │  │  │     ├─ file_search_tool_call_delta.cpython-312.pyc
│     │     │  │  │  │  │     ├─ function_tool_call.cpython-312.pyc
│     │     │  │  │  │  │     ├─ function_tool_call_delta.cpython-312.pyc
│     │     │  │  │  │  │     ├─ message_creation_step_details.cpython-312.pyc
│     │     │  │  │  │  │     ├─ run_step.cpython-312.pyc
│     │     │  │  │  │  │     ├─ run_step_delta.cpython-312.pyc
│     │     │  │  │  │  │     ├─ run_step_delta_event.cpython-312.pyc
│     │     │  │  │  │  │     ├─ run_step_delta_message_delta.cpython-312.pyc
│     │     │  │  │  │  │     ├─ run_step_include.cpython-312.pyc
│     │     │  │  │  │  │     ├─ step_list_params.cpython-312.pyc
│     │     │  │  │  │  │     ├─ step_retrieve_params.cpython-312.pyc
│     │     │  │  │  │  │     ├─ tool_call.cpython-312.pyc
│     │     │  │  │  │  │     ├─ tool_calls_step_details.cpython-312.pyc
│     │     │  │  │  │  │     ├─ tool_call_delta.cpython-312.pyc
│     │     │  │  │  │  │     ├─ tool_call_delta_object.cpython-312.pyc
│     │     │  │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  │  ├─ run_create_params.py
│     │     │  │  │  │  ├─ run_list_params.py
│     │     │  │  │  │  ├─ run_status.py
│     │     │  │  │  │  ├─ run_submit_tool_outputs_params.py
│     │     │  │  │  │  ├─ run_update_params.py
│     │     │  │  │  │  ├─ text.py
│     │     │  │  │  │  ├─ text_content_block.py
│     │     │  │  │  │  ├─ text_content_block_param.py
│     │     │  │  │  │  ├─ text_delta.py
│     │     │  │  │  │  ├─ text_delta_block.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ annotation.cpython-312.pyc
│     │     │  │  │  │     ├─ annotation_delta.cpython-312.pyc
│     │     │  │  │  │     ├─ file_citation_annotation.cpython-312.pyc
│     │     │  │  │  │     ├─ file_citation_delta_annotation.cpython-312.pyc
│     │     │  │  │  │     ├─ file_path_annotation.cpython-312.pyc
│     │     │  │  │  │     ├─ file_path_delta_annotation.cpython-312.pyc
│     │     │  │  │  │     ├─ image_file.cpython-312.pyc
│     │     │  │  │  │     ├─ image_file_content_block.cpython-312.pyc
│     │     │  │  │  │     ├─ image_file_content_block_param.cpython-312.pyc
│     │     │  │  │  │     ├─ image_file_delta.cpython-312.pyc
│     │     │  │  │  │     ├─ image_file_delta_block.cpython-312.pyc
│     │     │  │  │  │     ├─ image_file_param.cpython-312.pyc
│     │     │  │  │  │     ├─ image_url.cpython-312.pyc
│     │     │  │  │  │     ├─ image_url_content_block.cpython-312.pyc
│     │     │  │  │  │     ├─ image_url_content_block_param.cpython-312.pyc
│     │     │  │  │  │     ├─ image_url_delta.cpython-312.pyc
│     │     │  │  │  │     ├─ image_url_delta_block.cpython-312.pyc
│     │     │  │  │  │     ├─ image_url_param.cpython-312.pyc
│     │     │  │  │  │     ├─ message.cpython-312.pyc
│     │     │  │  │  │     ├─ message_content.cpython-312.pyc
│     │     │  │  │  │     ├─ message_content_delta.cpython-312.pyc
│     │     │  │  │  │     ├─ message_content_part_param.cpython-312.pyc
│     │     │  │  │  │     ├─ message_create_params.cpython-312.pyc
│     │     │  │  │  │     ├─ message_deleted.cpython-312.pyc
│     │     │  │  │  │     ├─ message_delta.cpython-312.pyc
│     │     │  │  │  │     ├─ message_delta_event.cpython-312.pyc
│     │     │  │  │  │     ├─ message_list_params.cpython-312.pyc
│     │     │  │  │  │     ├─ message_update_params.cpython-312.pyc
│     │     │  │  │  │     ├─ refusal_content_block.cpython-312.pyc
│     │     │  │  │  │     ├─ refusal_delta_block.cpython-312.pyc
│     │     │  │  │  │     ├─ required_action_function_tool_call.cpython-312.pyc
│     │     │  │  │  │     ├─ run.cpython-312.pyc
│     │     │  │  │  │     ├─ run_create_params.cpython-312.pyc
│     │     │  │  │  │     ├─ run_list_params.cpython-312.pyc
│     │     │  │  │  │     ├─ run_status.cpython-312.pyc
│     │     │  │  │  │     ├─ run_submit_tool_outputs_params.cpython-312.pyc
│     │     │  │  │  │     ├─ run_update_params.cpython-312.pyc
│     │     │  │  │  │     ├─ text.cpython-312.pyc
│     │     │  │  │  │     ├─ text_content_block.cpython-312.pyc
│     │     │  │  │  │     ├─ text_content_block_param.cpython-312.pyc
│     │     │  │  │  │     ├─ text_delta.cpython-312.pyc
│     │     │  │  │  │     ├─ text_delta_block.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ thread_create_and_run_params.py
│     │     │  │  │  ├─ thread_create_params.py
│     │     │  │  │  ├─ thread_deleted.py
│     │     │  │  │  ├─ thread_update_params.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ assistant.cpython-312.pyc
│     │     │  │  │     ├─ assistant_create_params.cpython-312.pyc
│     │     │  │  │     ├─ assistant_deleted.cpython-312.pyc
│     │     │  │  │     ├─ assistant_list_params.cpython-312.pyc
│     │     │  │  │     ├─ assistant_response_format_option.cpython-312.pyc
│     │     │  │  │     ├─ assistant_response_format_option_param.cpython-312.pyc
│     │     │  │  │     ├─ assistant_stream_event.cpython-312.pyc
│     │     │  │  │     ├─ assistant_tool.cpython-312.pyc
│     │     │  │  │     ├─ assistant_tool_choice.cpython-312.pyc
│     │     │  │  │     ├─ assistant_tool_choice_function.cpython-312.pyc
│     │     │  │  │     ├─ assistant_tool_choice_function_param.cpython-312.pyc
│     │     │  │  │     ├─ assistant_tool_choice_option.cpython-312.pyc
│     │     │  │  │     ├─ assistant_tool_choice_option_param.cpython-312.pyc
│     │     │  │  │     ├─ assistant_tool_choice_param.cpython-312.pyc
│     │     │  │  │     ├─ assistant_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ assistant_update_params.cpython-312.pyc
│     │     │  │  │     ├─ code_interpreter_tool.cpython-312.pyc
│     │     │  │  │     ├─ code_interpreter_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ file_search_tool.cpython-312.pyc
│     │     │  │  │     ├─ file_search_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ function_tool.cpython-312.pyc
│     │     │  │  │     ├─ function_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ thread.cpython-312.pyc
│     │     │  │  │     ├─ thread_create_and_run_params.cpython-312.pyc
│     │     │  │  │     ├─ thread_create_params.cpython-312.pyc
│     │     │  │  │     ├─ thread_deleted.cpython-312.pyc
│     │     │  │  │     ├─ thread_update_params.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ chat
│     │     │  │  │  ├─ chat_completion.py
│     │     │  │  │  ├─ chat_completion_allowed_tools_param.py
│     │     │  │  │  ├─ chat_completion_allowed_tool_choice_param.py
│     │     │  │  │  ├─ chat_completion_assistant_message_param.py
│     │     │  │  │  ├─ chat_completion_audio.py
│     │     │  │  │  ├─ chat_completion_audio_param.py
│     │     │  │  │  ├─ chat_completion_chunk.py
│     │     │  │  │  ├─ chat_completion_content_part_image.py
│     │     │  │  │  ├─ chat_completion_content_part_image_param.py
│     │     │  │  │  ├─ chat_completion_content_part_input_audio_param.py
│     │     │  │  │  ├─ chat_completion_content_part_param.py
│     │     │  │  │  ├─ chat_completion_content_part_refusal_param.py
│     │     │  │  │  ├─ chat_completion_content_part_text.py
│     │     │  │  │  ├─ chat_completion_content_part_text_param.py
│     │     │  │  │  ├─ chat_completion_custom_tool_param.py
│     │     │  │  │  ├─ chat_completion_deleted.py
│     │     │  │  │  ├─ chat_completion_developer_message_param.py
│     │     │  │  │  ├─ chat_completion_function_call_option_param.py
│     │     │  │  │  ├─ chat_completion_function_message_param.py
│     │     │  │  │  ├─ chat_completion_function_tool.py
│     │     │  │  │  ├─ chat_completion_function_tool_param.py
│     │     │  │  │  ├─ chat_completion_message.py
│     │     │  │  │  ├─ chat_completion_message_custom_tool_call.py
│     │     │  │  │  ├─ chat_completion_message_custom_tool_call_param.py
│     │     │  │  │  ├─ chat_completion_message_function_tool_call.py
│     │     │  │  │  ├─ chat_completion_message_function_tool_call_param.py
│     │     │  │  │  ├─ chat_completion_message_param.py
│     │     │  │  │  ├─ chat_completion_message_tool_call.py
│     │     │  │  │  ├─ chat_completion_message_tool_call_param.py
│     │     │  │  │  ├─ chat_completion_message_tool_call_union_param.py
│     │     │  │  │  ├─ chat_completion_modality.py
│     │     │  │  │  ├─ chat_completion_named_tool_choice_custom_param.py
│     │     │  │  │  ├─ chat_completion_named_tool_choice_param.py
│     │     │  │  │  ├─ chat_completion_prediction_content_param.py
│     │     │  │  │  ├─ chat_completion_reasoning_effort.py
│     │     │  │  │  ├─ chat_completion_role.py
│     │     │  │  │  ├─ chat_completion_store_message.py
│     │     │  │  │  ├─ chat_completion_stream_options_param.py
│     │     │  │  │  ├─ chat_completion_system_message_param.py
│     │     │  │  │  ├─ chat_completion_token_logprob.py
│     │     │  │  │  ├─ chat_completion_tool_choice_option_param.py
│     │     │  │  │  ├─ chat_completion_tool_message_param.py
│     │     │  │  │  ├─ chat_completion_tool_param.py
│     │     │  │  │  ├─ chat_completion_tool_union_param.py
│     │     │  │  │  ├─ chat_completion_user_message_param.py
│     │     │  │  │  ├─ completions
│     │     │  │  │  │  ├─ message_list_params.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ message_list_params.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ completion_create_params.py
│     │     │  │  │  ├─ completion_list_params.py
│     │     │  │  │  ├─ completion_update_params.py
│     │     │  │  │  ├─ parsed_chat_completion.py
│     │     │  │  │  ├─ parsed_function_tool_call.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ chat_completion.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_allowed_tools_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_allowed_tool_choice_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_assistant_message_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_audio.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_audio_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_chunk.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_content_part_image.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_content_part_image_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_content_part_input_audio_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_content_part_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_content_part_refusal_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_content_part_text.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_content_part_text_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_custom_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_deleted.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_developer_message_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_function_call_option_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_function_message_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_function_tool.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_function_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_message.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_message_custom_tool_call.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_message_custom_tool_call_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_message_function_tool_call.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_message_function_tool_call_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_message_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_message_tool_call.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_message_tool_call_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_message_tool_call_union_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_modality.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_named_tool_choice_custom_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_named_tool_choice_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_prediction_content_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_reasoning_effort.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_role.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_store_message.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_stream_options_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_system_message_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_token_logprob.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_tool_choice_option_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_tool_message_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_tool_union_param.cpython-312.pyc
│     │     │  │  │     ├─ chat_completion_user_message_param.cpython-312.pyc
│     │     │  │  │     ├─ completion_create_params.cpython-312.pyc
│     │     │  │  │     ├─ completion_list_params.cpython-312.pyc
│     │     │  │  │     ├─ completion_update_params.cpython-312.pyc
│     │     │  │  │     ├─ parsed_chat_completion.cpython-312.pyc
│     │     │  │  │     ├─ parsed_function_tool_call.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ chat_model.py
│     │     │  │  ├─ completion.py
│     │     │  │  ├─ completion_choice.py
│     │     │  │  ├─ completion_create_params.py
│     │     │  │  ├─ completion_usage.py
│     │     │  │  ├─ containers
│     │     │  │  │  ├─ files
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ file_create_params.py
│     │     │  │  │  ├─ file_create_response.py
│     │     │  │  │  ├─ file_list_params.py
│     │     │  │  │  ├─ file_list_response.py
│     │     │  │  │  ├─ file_retrieve_response.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ file_create_params.cpython-312.pyc
│     │     │  │  │     ├─ file_create_response.cpython-312.pyc
│     │     │  │  │     ├─ file_list_params.cpython-312.pyc
│     │     │  │  │     ├─ file_list_response.cpython-312.pyc
│     │     │  │  │     ├─ file_retrieve_response.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ container_create_params.py
│     │     │  │  ├─ container_create_response.py
│     │     │  │  ├─ container_list_params.py
│     │     │  │  ├─ container_list_response.py
│     │     │  │  ├─ container_retrieve_response.py
│     │     │  │  ├─ conversations
│     │     │  │  │  ├─ computer_screenshot_content.py
│     │     │  │  │  ├─ container_file_citation_body.py
│     │     │  │  │  ├─ conversation.py
│     │     │  │  │  ├─ conversation_create_params.py
│     │     │  │  │  ├─ conversation_deleted_resource.py
│     │     │  │  │  ├─ conversation_item.py
│     │     │  │  │  ├─ conversation_item_list.py
│     │     │  │  │  ├─ conversation_update_params.py
│     │     │  │  │  ├─ file_citation_body.py
│     │     │  │  │  ├─ input_file_content.py
│     │     │  │  │  ├─ input_image_content.py
│     │     │  │  │  ├─ input_text_content.py
│     │     │  │  │  ├─ item_create_params.py
│     │     │  │  │  ├─ item_list_params.py
│     │     │  │  │  ├─ item_retrieve_params.py
│     │     │  │  │  ├─ lob_prob.py
│     │     │  │  │  ├─ message.py
│     │     │  │  │  ├─ output_text_content.py
│     │     │  │  │  ├─ refusal_content.py
│     │     │  │  │  ├─ summary_text_content.py
│     │     │  │  │  ├─ text_content.py
│     │     │  │  │  ├─ top_log_prob.py
│     │     │  │  │  ├─ url_citation_body.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ computer_screenshot_content.cpython-312.pyc
│     │     │  │  │     ├─ container_file_citation_body.cpython-312.pyc
│     │     │  │  │     ├─ conversation.cpython-312.pyc
│     │     │  │  │     ├─ conversation_create_params.cpython-312.pyc
│     │     │  │  │     ├─ conversation_deleted_resource.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_list.cpython-312.pyc
│     │     │  │  │     ├─ conversation_update_params.cpython-312.pyc
│     │     │  │  │     ├─ file_citation_body.cpython-312.pyc
│     │     │  │  │     ├─ input_file_content.cpython-312.pyc
│     │     │  │  │     ├─ input_image_content.cpython-312.pyc
│     │     │  │  │     ├─ input_text_content.cpython-312.pyc
│     │     │  │  │     ├─ item_create_params.cpython-312.pyc
│     │     │  │  │     ├─ item_list_params.cpython-312.pyc
│     │     │  │  │     ├─ item_retrieve_params.cpython-312.pyc
│     │     │  │  │     ├─ lob_prob.cpython-312.pyc
│     │     │  │  │     ├─ message.cpython-312.pyc
│     │     │  │  │     ├─ output_text_content.cpython-312.pyc
│     │     │  │  │     ├─ refusal_content.cpython-312.pyc
│     │     │  │  │     ├─ summary_text_content.cpython-312.pyc
│     │     │  │  │     ├─ text_content.cpython-312.pyc
│     │     │  │  │     ├─ top_log_prob.cpython-312.pyc
│     │     │  │  │     ├─ url_citation_body.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ create_embedding_response.py
│     │     │  │  ├─ embedding.py
│     │     │  │  ├─ embedding_create_params.py
│     │     │  │  ├─ embedding_model.py
│     │     │  │  ├─ evals
│     │     │  │  │  ├─ create_eval_completions_run_data_source.py
│     │     │  │  │  ├─ create_eval_completions_run_data_source_param.py
│     │     │  │  │  ├─ create_eval_jsonl_run_data_source.py
│     │     │  │  │  ├─ create_eval_jsonl_run_data_source_param.py
│     │     │  │  │  ├─ eval_api_error.py
│     │     │  │  │  ├─ runs
│     │     │  │  │  │  ├─ output_item_list_params.py
│     │     │  │  │  │  ├─ output_item_list_response.py
│     │     │  │  │  │  ├─ output_item_retrieve_response.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ output_item_list_params.cpython-312.pyc
│     │     │  │  │  │     ├─ output_item_list_response.cpython-312.pyc
│     │     │  │  │  │     ├─ output_item_retrieve_response.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ run_cancel_response.py
│     │     │  │  │  ├─ run_create_params.py
│     │     │  │  │  ├─ run_create_response.py
│     │     │  │  │  ├─ run_delete_response.py
│     │     │  │  │  ├─ run_list_params.py
│     │     │  │  │  ├─ run_list_response.py
│     │     │  │  │  ├─ run_retrieve_response.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ create_eval_completions_run_data_source.cpython-312.pyc
│     │     │  │  │     ├─ create_eval_completions_run_data_source_param.cpython-312.pyc
│     │     │  │  │     ├─ create_eval_jsonl_run_data_source.cpython-312.pyc
│     │     │  │  │     ├─ create_eval_jsonl_run_data_source_param.cpython-312.pyc
│     │     │  │  │     ├─ eval_api_error.cpython-312.pyc
│     │     │  │  │     ├─ run_cancel_response.cpython-312.pyc
│     │     │  │  │     ├─ run_create_params.cpython-312.pyc
│     │     │  │  │     ├─ run_create_response.cpython-312.pyc
│     │     │  │  │     ├─ run_delete_response.cpython-312.pyc
│     │     │  │  │     ├─ run_list_params.cpython-312.pyc
│     │     │  │  │     ├─ run_list_response.cpython-312.pyc
│     │     │  │  │     ├─ run_retrieve_response.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ eval_create_params.py
│     │     │  │  ├─ eval_create_response.py
│     │     │  │  ├─ eval_custom_data_source_config.py
│     │     │  │  ├─ eval_delete_response.py
│     │     │  │  ├─ eval_list_params.py
│     │     │  │  ├─ eval_list_response.py
│     │     │  │  ├─ eval_retrieve_response.py
│     │     │  │  ├─ eval_stored_completions_data_source_config.py
│     │     │  │  ├─ eval_update_params.py
│     │     │  │  ├─ eval_update_response.py
│     │     │  │  ├─ file_chunking_strategy.py
│     │     │  │  ├─ file_chunking_strategy_param.py
│     │     │  │  ├─ file_content.py
│     │     │  │  ├─ file_create_params.py
│     │     │  │  ├─ file_deleted.py
│     │     │  │  ├─ file_list_params.py
│     │     │  │  ├─ file_object.py
│     │     │  │  ├─ file_purpose.py
│     │     │  │  ├─ fine_tuning
│     │     │  │  │  ├─ alpha
│     │     │  │  │  │  ├─ grader_run_params.py
│     │     │  │  │  │  ├─ grader_run_response.py
│     │     │  │  │  │  ├─ grader_validate_params.py
│     │     │  │  │  │  ├─ grader_validate_response.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ grader_run_params.cpython-312.pyc
│     │     │  │  │  │     ├─ grader_run_response.cpython-312.pyc
│     │     │  │  │  │     ├─ grader_validate_params.cpython-312.pyc
│     │     │  │  │  │     ├─ grader_validate_response.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ checkpoints
│     │     │  │  │  │  ├─ permission_create_params.py
│     │     │  │  │  │  ├─ permission_create_response.py
│     │     │  │  │  │  ├─ permission_delete_response.py
│     │     │  │  │  │  ├─ permission_retrieve_params.py
│     │     │  │  │  │  ├─ permission_retrieve_response.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ permission_create_params.cpython-312.pyc
│     │     │  │  │  │     ├─ permission_create_response.cpython-312.pyc
│     │     │  │  │  │     ├─ permission_delete_response.cpython-312.pyc
│     │     │  │  │  │     ├─ permission_retrieve_params.cpython-312.pyc
│     │     │  │  │  │     ├─ permission_retrieve_response.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ dpo_hyperparameters.py
│     │     │  │  │  ├─ dpo_hyperparameters_param.py
│     │     │  │  │  ├─ dpo_method.py
│     │     │  │  │  ├─ dpo_method_param.py
│     │     │  │  │  ├─ fine_tuning_job.py
│     │     │  │  │  ├─ fine_tuning_job_event.py
│     │     │  │  │  ├─ fine_tuning_job_integration.py
│     │     │  │  │  ├─ fine_tuning_job_wandb_integration.py
│     │     │  │  │  ├─ fine_tuning_job_wandb_integration_object.py
│     │     │  │  │  ├─ jobs
│     │     │  │  │  │  ├─ checkpoint_list_params.py
│     │     │  │  │  │  ├─ fine_tuning_job_checkpoint.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ checkpoint_list_params.cpython-312.pyc
│     │     │  │  │  │     ├─ fine_tuning_job_checkpoint.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ job_create_params.py
│     │     │  │  │  ├─ job_list_events_params.py
│     │     │  │  │  ├─ job_list_params.py
│     │     │  │  │  ├─ reinforcement_hyperparameters.py
│     │     │  │  │  ├─ reinforcement_hyperparameters_param.py
│     │     │  │  │  ├─ reinforcement_method.py
│     │     │  │  │  ├─ reinforcement_method_param.py
│     │     │  │  │  ├─ supervised_hyperparameters.py
│     │     │  │  │  ├─ supervised_hyperparameters_param.py
│     │     │  │  │  ├─ supervised_method.py
│     │     │  │  │  ├─ supervised_method_param.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ dpo_hyperparameters.cpython-312.pyc
│     │     │  │  │     ├─ dpo_hyperparameters_param.cpython-312.pyc
│     │     │  │  │     ├─ dpo_method.cpython-312.pyc
│     │     │  │  │     ├─ dpo_method_param.cpython-312.pyc
│     │     │  │  │     ├─ fine_tuning_job.cpython-312.pyc
│     │     │  │  │     ├─ fine_tuning_job_event.cpython-312.pyc
│     │     │  │  │     ├─ fine_tuning_job_integration.cpython-312.pyc
│     │     │  │  │     ├─ fine_tuning_job_wandb_integration.cpython-312.pyc
│     │     │  │  │     ├─ fine_tuning_job_wandb_integration_object.cpython-312.pyc
│     │     │  │  │     ├─ job_create_params.cpython-312.pyc
│     │     │  │  │     ├─ job_list_events_params.cpython-312.pyc
│     │     │  │  │     ├─ job_list_params.cpython-312.pyc
│     │     │  │  │     ├─ reinforcement_hyperparameters.cpython-312.pyc
│     │     │  │  │     ├─ reinforcement_hyperparameters_param.cpython-312.pyc
│     │     │  │  │     ├─ reinforcement_method.cpython-312.pyc
│     │     │  │  │     ├─ reinforcement_method_param.cpython-312.pyc
│     │     │  │  │     ├─ supervised_hyperparameters.cpython-312.pyc
│     │     │  │  │     ├─ supervised_hyperparameters_param.cpython-312.pyc
│     │     │  │  │     ├─ supervised_method.cpython-312.pyc
│     │     │  │  │     ├─ supervised_method_param.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ graders
│     │     │  │  │  ├─ label_model_grader.py
│     │     │  │  │  ├─ label_model_grader_param.py
│     │     │  │  │  ├─ multi_grader.py
│     │     │  │  │  ├─ multi_grader_param.py
│     │     │  │  │  ├─ python_grader.py
│     │     │  │  │  ├─ python_grader_param.py
│     │     │  │  │  ├─ score_model_grader.py
│     │     │  │  │  ├─ score_model_grader_param.py
│     │     │  │  │  ├─ string_check_grader.py
│     │     │  │  │  ├─ string_check_grader_param.py
│     │     │  │  │  ├─ text_similarity_grader.py
│     │     │  │  │  ├─ text_similarity_grader_param.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ label_model_grader.cpython-312.pyc
│     │     │  │  │     ├─ label_model_grader_param.cpython-312.pyc
│     │     │  │  │     ├─ multi_grader.cpython-312.pyc
│     │     │  │  │     ├─ multi_grader_param.cpython-312.pyc
│     │     │  │  │     ├─ python_grader.cpython-312.pyc
│     │     │  │  │     ├─ python_grader_param.cpython-312.pyc
│     │     │  │  │     ├─ score_model_grader.cpython-312.pyc
│     │     │  │  │     ├─ score_model_grader_param.cpython-312.pyc
│     │     │  │  │     ├─ string_check_grader.cpython-312.pyc
│     │     │  │  │     ├─ string_check_grader_param.cpython-312.pyc
│     │     │  │  │     ├─ text_similarity_grader.cpython-312.pyc
│     │     │  │  │     ├─ text_similarity_grader_param.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ image.py
│     │     │  │  ├─ images_response.py
│     │     │  │  ├─ image_create_variation_params.py
│     │     │  │  ├─ image_edit_completed_event.py
│     │     │  │  ├─ image_edit_params.py
│     │     │  │  ├─ image_edit_partial_image_event.py
│     │     │  │  ├─ image_edit_stream_event.py
│     │     │  │  ├─ image_generate_params.py
│     │     │  │  ├─ image_gen_completed_event.py
│     │     │  │  ├─ image_gen_partial_image_event.py
│     │     │  │  ├─ image_gen_stream_event.py
│     │     │  │  ├─ image_model.py
│     │     │  │  ├─ model.py
│     │     │  │  ├─ model_deleted.py
│     │     │  │  ├─ moderation.py
│     │     │  │  ├─ moderation_create_params.py
│     │     │  │  ├─ moderation_create_response.py
│     │     │  │  ├─ moderation_image_url_input_param.py
│     │     │  │  ├─ moderation_model.py
│     │     │  │  ├─ moderation_multi_modal_input_param.py
│     │     │  │  ├─ moderation_text_input_param.py
│     │     │  │  ├─ other_file_chunking_strategy_object.py
│     │     │  │  ├─ realtime
│     │     │  │  │  ├─ audio_transcription.py
│     │     │  │  │  ├─ audio_transcription_param.py
│     │     │  │  │  ├─ client_secret_create_params.py
│     │     │  │  │  ├─ client_secret_create_response.py
│     │     │  │  │  ├─ conversation_created_event.py
│     │     │  │  │  ├─ conversation_item.py
│     │     │  │  │  ├─ conversation_item_added.py
│     │     │  │  │  ├─ conversation_item_created_event.py
│     │     │  │  │  ├─ conversation_item_create_event.py
│     │     │  │  │  ├─ conversation_item_create_event_param.py
│     │     │  │  │  ├─ conversation_item_deleted_event.py
│     │     │  │  │  ├─ conversation_item_delete_event.py
│     │     │  │  │  ├─ conversation_item_delete_event_param.py
│     │     │  │  │  ├─ conversation_item_done.py
│     │     │  │  │  ├─ conversation_item_input_audio_transcription_completed_event.py
│     │     │  │  │  ├─ conversation_item_input_audio_transcription_delta_event.py
│     │     │  │  │  ├─ conversation_item_input_audio_transcription_failed_event.py
│     │     │  │  │  ├─ conversation_item_input_audio_transcription_segment.py
│     │     │  │  │  ├─ conversation_item_param.py
│     │     │  │  │  ├─ conversation_item_retrieve_event.py
│     │     │  │  │  ├─ conversation_item_retrieve_event_param.py
│     │     │  │  │  ├─ conversation_item_truncated_event.py
│     │     │  │  │  ├─ conversation_item_truncate_event.py
│     │     │  │  │  ├─ conversation_item_truncate_event_param.py
│     │     │  │  │  ├─ input_audio_buffer_append_event.py
│     │     │  │  │  ├─ input_audio_buffer_append_event_param.py
│     │     │  │  │  ├─ input_audio_buffer_cleared_event.py
│     │     │  │  │  ├─ input_audio_buffer_clear_event.py
│     │     │  │  │  ├─ input_audio_buffer_clear_event_param.py
│     │     │  │  │  ├─ input_audio_buffer_committed_event.py
│     │     │  │  │  ├─ input_audio_buffer_commit_event.py
│     │     │  │  │  ├─ input_audio_buffer_commit_event_param.py
│     │     │  │  │  ├─ input_audio_buffer_speech_started_event.py
│     │     │  │  │  ├─ input_audio_buffer_speech_stopped_event.py
│     │     │  │  │  ├─ input_audio_buffer_timeout_triggered.py
│     │     │  │  │  ├─ log_prob_properties.py
│     │     │  │  │  ├─ mcp_list_tools_completed.py
│     │     │  │  │  ├─ mcp_list_tools_failed.py
│     │     │  │  │  ├─ mcp_list_tools_in_progress.py
│     │     │  │  │  ├─ noise_reduction_type.py
│     │     │  │  │  ├─ output_audio_buffer_clear_event.py
│     │     │  │  │  ├─ output_audio_buffer_clear_event_param.py
│     │     │  │  │  ├─ rate_limits_updated_event.py
│     │     │  │  │  ├─ realtime_audio_config.py
│     │     │  │  │  ├─ realtime_audio_config_input.py
│     │     │  │  │  ├─ realtime_audio_config_input_param.py
│     │     │  │  │  ├─ realtime_audio_config_output.py
│     │     │  │  │  ├─ realtime_audio_config_output_param.py
│     │     │  │  │  ├─ realtime_audio_config_param.py
│     │     │  │  │  ├─ realtime_audio_formats.py
│     │     │  │  │  ├─ realtime_audio_formats_param.py
│     │     │  │  │  ├─ realtime_audio_input_turn_detection.py
│     │     │  │  │  ├─ realtime_audio_input_turn_detection_param.py
│     │     │  │  │  ├─ realtime_client_event.py
│     │     │  │  │  ├─ realtime_client_event_param.py
│     │     │  │  │  ├─ realtime_connect_params.py
│     │     │  │  │  ├─ realtime_conversation_item_assistant_message.py
│     │     │  │  │  ├─ realtime_conversation_item_assistant_message_param.py
│     │     │  │  │  ├─ realtime_conversation_item_function_call.py
│     │     │  │  │  ├─ realtime_conversation_item_function_call_output.py
│     │     │  │  │  ├─ realtime_conversation_item_function_call_output_param.py
│     │     │  │  │  ├─ realtime_conversation_item_function_call_param.py
│     │     │  │  │  ├─ realtime_conversation_item_system_message.py
│     │     │  │  │  ├─ realtime_conversation_item_system_message_param.py
│     │     │  │  │  ├─ realtime_conversation_item_user_message.py
│     │     │  │  │  ├─ realtime_conversation_item_user_message_param.py
│     │     │  │  │  ├─ realtime_error.py
│     │     │  │  │  ├─ realtime_error_event.py
│     │     │  │  │  ├─ realtime_function_tool.py
│     │     │  │  │  ├─ realtime_function_tool_param.py
│     │     │  │  │  ├─ realtime_mcphttp_error.py
│     │     │  │  │  ├─ realtime_mcphttp_error_param.py
│     │     │  │  │  ├─ realtime_mcp_approval_request.py
│     │     │  │  │  ├─ realtime_mcp_approval_request_param.py
│     │     │  │  │  ├─ realtime_mcp_approval_response.py
│     │     │  │  │  ├─ realtime_mcp_approval_response_param.py
│     │     │  │  │  ├─ realtime_mcp_list_tools.py
│     │     │  │  │  ├─ realtime_mcp_list_tools_param.py
│     │     │  │  │  ├─ realtime_mcp_protocol_error.py
│     │     │  │  │  ├─ realtime_mcp_protocol_error_param.py
│     │     │  │  │  ├─ realtime_mcp_tool_call.py
│     │     │  │  │  ├─ realtime_mcp_tool_call_param.py
│     │     │  │  │  ├─ realtime_mcp_tool_execution_error.py
│     │     │  │  │  ├─ realtime_mcp_tool_execution_error_param.py
│     │     │  │  │  ├─ realtime_response.py
│     │     │  │  │  ├─ realtime_response_create_audio_output.py
│     │     │  │  │  ├─ realtime_response_create_audio_output_param.py
│     │     │  │  │  ├─ realtime_response_create_mcp_tool.py
│     │     │  │  │  ├─ realtime_response_create_mcp_tool_param.py
│     │     │  │  │  ├─ realtime_response_create_params.py
│     │     │  │  │  ├─ realtime_response_create_params_param.py
│     │     │  │  │  ├─ realtime_response_status.py
│     │     │  │  │  ├─ realtime_response_usage.py
│     │     │  │  │  ├─ realtime_response_usage_input_token_details.py
│     │     │  │  │  ├─ realtime_response_usage_output_token_details.py
│     │     │  │  │  ├─ realtime_server_event.py
│     │     │  │  │  ├─ realtime_session_client_secret.py
│     │     │  │  │  ├─ realtime_session_create_request.py
│     │     │  │  │  ├─ realtime_session_create_request_param.py
│     │     │  │  │  ├─ realtime_session_create_response.py
│     │     │  │  │  ├─ realtime_tools_config.py
│     │     │  │  │  ├─ realtime_tools_config_param.py
│     │     │  │  │  ├─ realtime_tools_config_union.py
│     │     │  │  │  ├─ realtime_tools_config_union_param.py
│     │     │  │  │  ├─ realtime_tool_choice_config.py
│     │     │  │  │  ├─ realtime_tool_choice_config_param.py
│     │     │  │  │  ├─ realtime_tracing_config.py
│     │     │  │  │  ├─ realtime_tracing_config_param.py
│     │     │  │  │  ├─ realtime_transcription_session_audio.py
│     │     │  │  │  ├─ realtime_transcription_session_audio_input.py
│     │     │  │  │  ├─ realtime_transcription_session_audio_input_param.py
│     │     │  │  │  ├─ realtime_transcription_session_audio_input_turn_detection.py
│     │     │  │  │  ├─ realtime_transcription_session_audio_input_turn_detection_param.py
│     │     │  │  │  ├─ realtime_transcription_session_audio_param.py
│     │     │  │  │  ├─ realtime_transcription_session_create_request.py
│     │     │  │  │  ├─ realtime_transcription_session_create_request_param.py
│     │     │  │  │  ├─ realtime_transcription_session_create_response.py
│     │     │  │  │  ├─ realtime_transcription_session_turn_detection.py
│     │     │  │  │  ├─ realtime_truncation.py
│     │     │  │  │  ├─ realtime_truncation_param.py
│     │     │  │  │  ├─ realtime_truncation_retention_ratio.py
│     │     │  │  │  ├─ realtime_truncation_retention_ratio_param.py
│     │     │  │  │  ├─ response_audio_delta_event.py
│     │     │  │  │  ├─ response_audio_done_event.py
│     │     │  │  │  ├─ response_audio_transcript_delta_event.py
│     │     │  │  │  ├─ response_audio_transcript_done_event.py
│     │     │  │  │  ├─ response_cancel_event.py
│     │     │  │  │  ├─ response_cancel_event_param.py
│     │     │  │  │  ├─ response_content_part_added_event.py
│     │     │  │  │  ├─ response_content_part_done_event.py
│     │     │  │  │  ├─ response_created_event.py
│     │     │  │  │  ├─ response_create_event.py
│     │     │  │  │  ├─ response_create_event_param.py
│     │     │  │  │  ├─ response_done_event.py
│     │     │  │  │  ├─ response_function_call_arguments_delta_event.py
│     │     │  │  │  ├─ response_function_call_arguments_done_event.py
│     │     │  │  │  ├─ response_mcp_call_arguments_delta.py
│     │     │  │  │  ├─ response_mcp_call_arguments_done.py
│     │     │  │  │  ├─ response_mcp_call_completed.py
│     │     │  │  │  ├─ response_mcp_call_failed.py
│     │     │  │  │  ├─ response_mcp_call_in_progress.py
│     │     │  │  │  ├─ response_output_item_added_event.py
│     │     │  │  │  ├─ response_output_item_done_event.py
│     │     │  │  │  ├─ response_text_delta_event.py
│     │     │  │  │  ├─ response_text_done_event.py
│     │     │  │  │  ├─ session_created_event.py
│     │     │  │  │  ├─ session_updated_event.py
│     │     │  │  │  ├─ session_update_event.py
│     │     │  │  │  ├─ session_update_event_param.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ audio_transcription.cpython-312.pyc
│     │     │  │  │     ├─ audio_transcription_param.cpython-312.pyc
│     │     │  │  │     ├─ client_secret_create_params.cpython-312.pyc
│     │     │  │  │     ├─ client_secret_create_response.cpython-312.pyc
│     │     │  │  │     ├─ conversation_created_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_added.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_created_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_create_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_create_event_param.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_deleted_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_delete_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_delete_event_param.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_done.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_input_audio_transcription_completed_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_input_audio_transcription_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_input_audio_transcription_failed_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_input_audio_transcription_segment.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_param.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_retrieve_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_retrieve_event_param.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_truncated_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_truncate_event.cpython-312.pyc
│     │     │  │  │     ├─ conversation_item_truncate_event_param.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_append_event.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_append_event_param.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_cleared_event.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_clear_event.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_clear_event_param.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_committed_event.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_commit_event.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_commit_event_param.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_speech_started_event.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_speech_stopped_event.cpython-312.pyc
│     │     │  │  │     ├─ input_audio_buffer_timeout_triggered.cpython-312.pyc
│     │     │  │  │     ├─ log_prob_properties.cpython-312.pyc
│     │     │  │  │     ├─ mcp_list_tools_completed.cpython-312.pyc
│     │     │  │  │     ├─ mcp_list_tools_failed.cpython-312.pyc
│     │     │  │  │     ├─ mcp_list_tools_in_progress.cpython-312.pyc
│     │     │  │  │     ├─ noise_reduction_type.cpython-312.pyc
│     │     │  │  │     ├─ output_audio_buffer_clear_event.cpython-312.pyc
│     │     │  │  │     ├─ output_audio_buffer_clear_event_param.cpython-312.pyc
│     │     │  │  │     ├─ rate_limits_updated_event.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_config.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_config_input.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_config_input_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_config_output.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_config_output_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_config_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_formats.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_formats_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_input_turn_detection.cpython-312.pyc
│     │     │  │  │     ├─ realtime_audio_input_turn_detection_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_client_event.cpython-312.pyc
│     │     │  │  │     ├─ realtime_client_event_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_connect_params.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_assistant_message.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_assistant_message_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_function_call.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_function_call_output.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_function_call_output_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_function_call_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_system_message.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_system_message_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_user_message.cpython-312.pyc
│     │     │  │  │     ├─ realtime_conversation_item_user_message_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_error.cpython-312.pyc
│     │     │  │  │     ├─ realtime_error_event.cpython-312.pyc
│     │     │  │  │     ├─ realtime_function_tool.cpython-312.pyc
│     │     │  │  │     ├─ realtime_function_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcphttp_error.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcphttp_error_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_approval_request.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_approval_request_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_approval_response.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_approval_response_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_list_tools.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_list_tools_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_protocol_error.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_protocol_error_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_tool_call.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_tool_call_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_tool_execution_error.cpython-312.pyc
│     │     │  │  │     ├─ realtime_mcp_tool_execution_error_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_create_audio_output.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_create_audio_output_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_create_mcp_tool.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_create_mcp_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_create_params.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_create_params_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_status.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_usage.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_usage_input_token_details.cpython-312.pyc
│     │     │  │  │     ├─ realtime_response_usage_output_token_details.cpython-312.pyc
│     │     │  │  │     ├─ realtime_server_event.cpython-312.pyc
│     │     │  │  │     ├─ realtime_session_client_secret.cpython-312.pyc
│     │     │  │  │     ├─ realtime_session_create_request.cpython-312.pyc
│     │     │  │  │     ├─ realtime_session_create_request_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_session_create_response.cpython-312.pyc
│     │     │  │  │     ├─ realtime_tools_config.cpython-312.pyc
│     │     │  │  │     ├─ realtime_tools_config_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_tools_config_union.cpython-312.pyc
│     │     │  │  │     ├─ realtime_tools_config_union_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_tool_choice_config.cpython-312.pyc
│     │     │  │  │     ├─ realtime_tool_choice_config_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_tracing_config.cpython-312.pyc
│     │     │  │  │     ├─ realtime_tracing_config_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_audio.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_audio_input.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_audio_input_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_audio_input_turn_detection.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_audio_input_turn_detection_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_audio_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_create_request.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_create_request_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_create_response.cpython-312.pyc
│     │     │  │  │     ├─ realtime_transcription_session_turn_detection.cpython-312.pyc
│     │     │  │  │     ├─ realtime_truncation.cpython-312.pyc
│     │     │  │  │     ├─ realtime_truncation_param.cpython-312.pyc
│     │     │  │  │     ├─ realtime_truncation_retention_ratio.cpython-312.pyc
│     │     │  │  │     ├─ realtime_truncation_retention_ratio_param.cpython-312.pyc
│     │     │  │  │     ├─ response_audio_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_audio_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_audio_transcript_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_audio_transcript_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_cancel_event.cpython-312.pyc
│     │     │  │  │     ├─ response_cancel_event_param.cpython-312.pyc
│     │     │  │  │     ├─ response_content_part_added_event.cpython-312.pyc
│     │     │  │  │     ├─ response_content_part_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_created_event.cpython-312.pyc
│     │     │  │  │     ├─ response_create_event.cpython-312.pyc
│     │     │  │  │     ├─ response_create_event_param.cpython-312.pyc
│     │     │  │  │     ├─ response_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_function_call_arguments_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_function_call_arguments_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_arguments_delta.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_arguments_done.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_completed.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_failed.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_in_progress.cpython-312.pyc
│     │     │  │  │     ├─ response_output_item_added_event.cpython-312.pyc
│     │     │  │  │     ├─ response_output_item_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_text_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_text_done_event.cpython-312.pyc
│     │     │  │  │     ├─ session_created_event.cpython-312.pyc
│     │     │  │  │     ├─ session_updated_event.cpython-312.pyc
│     │     │  │  │     ├─ session_update_event.cpython-312.pyc
│     │     │  │  │     ├─ session_update_event_param.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ responses
│     │     │  │  │  ├─ computer_tool.py
│     │     │  │  │  ├─ computer_tool_param.py
│     │     │  │  │  ├─ custom_tool.py
│     │     │  │  │  ├─ custom_tool_param.py
│     │     │  │  │  ├─ easy_input_message.py
│     │     │  │  │  ├─ easy_input_message_param.py
│     │     │  │  │  ├─ file_search_tool.py
│     │     │  │  │  ├─ file_search_tool_param.py
│     │     │  │  │  ├─ function_tool.py
│     │     │  │  │  ├─ function_tool_param.py
│     │     │  │  │  ├─ input_item_list_params.py
│     │     │  │  │  ├─ parsed_response.py
│     │     │  │  │  ├─ response.py
│     │     │  │  │  ├─ response_audio_delta_event.py
│     │     │  │  │  ├─ response_audio_done_event.py
│     │     │  │  │  ├─ response_audio_transcript_delta_event.py
│     │     │  │  │  ├─ response_audio_transcript_done_event.py
│     │     │  │  │  ├─ response_code_interpreter_call_code_delta_event.py
│     │     │  │  │  ├─ response_code_interpreter_call_code_done_event.py
│     │     │  │  │  ├─ response_code_interpreter_call_completed_event.py
│     │     │  │  │  ├─ response_code_interpreter_call_interpreting_event.py
│     │     │  │  │  ├─ response_code_interpreter_call_in_progress_event.py
│     │     │  │  │  ├─ response_code_interpreter_tool_call.py
│     │     │  │  │  ├─ response_code_interpreter_tool_call_param.py
│     │     │  │  │  ├─ response_completed_event.py
│     │     │  │  │  ├─ response_computer_tool_call.py
│     │     │  │  │  ├─ response_computer_tool_call_output_item.py
│     │     │  │  │  ├─ response_computer_tool_call_output_screenshot.py
│     │     │  │  │  ├─ response_computer_tool_call_output_screenshot_param.py
│     │     │  │  │  ├─ response_computer_tool_call_param.py
│     │     │  │  │  ├─ response_content_part_added_event.py
│     │     │  │  │  ├─ response_content_part_done_event.py
│     │     │  │  │  ├─ response_conversation_param.py
│     │     │  │  │  ├─ response_created_event.py
│     │     │  │  │  ├─ response_create_params.py
│     │     │  │  │  ├─ response_custom_tool_call.py
│     │     │  │  │  ├─ response_custom_tool_call_input_delta_event.py
│     │     │  │  │  ├─ response_custom_tool_call_input_done_event.py
│     │     │  │  │  ├─ response_custom_tool_call_output.py
│     │     │  │  │  ├─ response_custom_tool_call_output_param.py
│     │     │  │  │  ├─ response_custom_tool_call_param.py
│     │     │  │  │  ├─ response_error.py
│     │     │  │  │  ├─ response_error_event.py
│     │     │  │  │  ├─ response_failed_event.py
│     │     │  │  │  ├─ response_file_search_call_completed_event.py
│     │     │  │  │  ├─ response_file_search_call_in_progress_event.py
│     │     │  │  │  ├─ response_file_search_call_searching_event.py
│     │     │  │  │  ├─ response_file_search_tool_call.py
│     │     │  │  │  ├─ response_file_search_tool_call_param.py
│     │     │  │  │  ├─ response_format_text_config.py
│     │     │  │  │  ├─ response_format_text_config_param.py
│     │     │  │  │  ├─ response_format_text_json_schema_config.py
│     │     │  │  │  ├─ response_format_text_json_schema_config_param.py
│     │     │  │  │  ├─ response_function_call_arguments_delta_event.py
│     │     │  │  │  ├─ response_function_call_arguments_done_event.py
│     │     │  │  │  ├─ response_function_tool_call.py
│     │     │  │  │  ├─ response_function_tool_call_item.py
│     │     │  │  │  ├─ response_function_tool_call_output_item.py
│     │     │  │  │  ├─ response_function_tool_call_param.py
│     │     │  │  │  ├─ response_function_web_search.py
│     │     │  │  │  ├─ response_function_web_search_param.py
│     │     │  │  │  ├─ response_image_gen_call_completed_event.py
│     │     │  │  │  ├─ response_image_gen_call_generating_event.py
│     │     │  │  │  ├─ response_image_gen_call_in_progress_event.py
│     │     │  │  │  ├─ response_image_gen_call_partial_image_event.py
│     │     │  │  │  ├─ response_includable.py
│     │     │  │  │  ├─ response_incomplete_event.py
│     │     │  │  │  ├─ response_input_audio.py
│     │     │  │  │  ├─ response_input_audio_param.py
│     │     │  │  │  ├─ response_input_content.py
│     │     │  │  │  ├─ response_input_content_param.py
│     │     │  │  │  ├─ response_input_file.py
│     │     │  │  │  ├─ response_input_file_param.py
│     │     │  │  │  ├─ response_input_image.py
│     │     │  │  │  ├─ response_input_image_param.py
│     │     │  │  │  ├─ response_input_item.py
│     │     │  │  │  ├─ response_input_item_param.py
│     │     │  │  │  ├─ response_input_message_content_list.py
│     │     │  │  │  ├─ response_input_message_content_list_param.py
│     │     │  │  │  ├─ response_input_message_item.py
│     │     │  │  │  ├─ response_input_param.py
│     │     │  │  │  ├─ response_input_text.py
│     │     │  │  │  ├─ response_input_text_param.py
│     │     │  │  │  ├─ response_in_progress_event.py
│     │     │  │  │  ├─ response_item.py
│     │     │  │  │  ├─ response_item_list.py
│     │     │  │  │  ├─ response_mcp_call_arguments_delta_event.py
│     │     │  │  │  ├─ response_mcp_call_arguments_done_event.py
│     │     │  │  │  ├─ response_mcp_call_completed_event.py
│     │     │  │  │  ├─ response_mcp_call_failed_event.py
│     │     │  │  │  ├─ response_mcp_call_in_progress_event.py
│     │     │  │  │  ├─ response_mcp_list_tools_completed_event.py
│     │     │  │  │  ├─ response_mcp_list_tools_failed_event.py
│     │     │  │  │  ├─ response_mcp_list_tools_in_progress_event.py
│     │     │  │  │  ├─ response_output_item.py
│     │     │  │  │  ├─ response_output_item_added_event.py
│     │     │  │  │  ├─ response_output_item_done_event.py
│     │     │  │  │  ├─ response_output_message.py
│     │     │  │  │  ├─ response_output_message_param.py
│     │     │  │  │  ├─ response_output_refusal.py
│     │     │  │  │  ├─ response_output_refusal_param.py
│     │     │  │  │  ├─ response_output_text.py
│     │     │  │  │  ├─ response_output_text_annotation_added_event.py
│     │     │  │  │  ├─ response_output_text_param.py
│     │     │  │  │  ├─ response_prompt.py
│     │     │  │  │  ├─ response_prompt_param.py
│     │     │  │  │  ├─ response_queued_event.py
│     │     │  │  │  ├─ response_reasoning_item.py
│     │     │  │  │  ├─ response_reasoning_item_param.py
│     │     │  │  │  ├─ response_reasoning_summary_part_added_event.py
│     │     │  │  │  ├─ response_reasoning_summary_part_done_event.py
│     │     │  │  │  ├─ response_reasoning_summary_text_delta_event.py
│     │     │  │  │  ├─ response_reasoning_summary_text_done_event.py
│     │     │  │  │  ├─ response_reasoning_text_delta_event.py
│     │     │  │  │  ├─ response_reasoning_text_done_event.py
│     │     │  │  │  ├─ response_refusal_delta_event.py
│     │     │  │  │  ├─ response_refusal_done_event.py
│     │     │  │  │  ├─ response_retrieve_params.py
│     │     │  │  │  ├─ response_status.py
│     │     │  │  │  ├─ response_stream_event.py
│     │     │  │  │  ├─ response_text_config.py
│     │     │  │  │  ├─ response_text_config_param.py
│     │     │  │  │  ├─ response_text_delta_event.py
│     │     │  │  │  ├─ response_text_done_event.py
│     │     │  │  │  ├─ response_usage.py
│     │     │  │  │  ├─ response_web_search_call_completed_event.py
│     │     │  │  │  ├─ response_web_search_call_in_progress_event.py
│     │     │  │  │  ├─ response_web_search_call_searching_event.py
│     │     │  │  │  ├─ tool.py
│     │     │  │  │  ├─ tool_choice_allowed.py
│     │     │  │  │  ├─ tool_choice_allowed_param.py
│     │     │  │  │  ├─ tool_choice_custom.py
│     │     │  │  │  ├─ tool_choice_custom_param.py
│     │     │  │  │  ├─ tool_choice_function.py
│     │     │  │  │  ├─ tool_choice_function_param.py
│     │     │  │  │  ├─ tool_choice_mcp.py
│     │     │  │  │  ├─ tool_choice_mcp_param.py
│     │     │  │  │  ├─ tool_choice_options.py
│     │     │  │  │  ├─ tool_choice_types.py
│     │     │  │  │  ├─ tool_choice_types_param.py
│     │     │  │  │  ├─ tool_param.py
│     │     │  │  │  ├─ web_search_preview_tool.py
│     │     │  │  │  ├─ web_search_preview_tool_param.py
│     │     │  │  │  ├─ web_search_tool.py
│     │     │  │  │  ├─ web_search_tool_param.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ computer_tool.cpython-312.pyc
│     │     │  │  │     ├─ computer_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ custom_tool.cpython-312.pyc
│     │     │  │  │     ├─ custom_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ easy_input_message.cpython-312.pyc
│     │     │  │  │     ├─ easy_input_message_param.cpython-312.pyc
│     │     │  │  │     ├─ file_search_tool.cpython-312.pyc
│     │     │  │  │     ├─ file_search_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ function_tool.cpython-312.pyc
│     │     │  │  │     ├─ function_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ input_item_list_params.cpython-312.pyc
│     │     │  │  │     ├─ parsed_response.cpython-312.pyc
│     │     │  │  │     ├─ response.cpython-312.pyc
│     │     │  │  │     ├─ response_audio_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_audio_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_audio_transcript_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_audio_transcript_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_code_interpreter_call_code_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_code_interpreter_call_code_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_code_interpreter_call_completed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_code_interpreter_call_interpreting_event.cpython-312.pyc
│     │     │  │  │     ├─ response_code_interpreter_call_in_progress_event.cpython-312.pyc
│     │     │  │  │     ├─ response_code_interpreter_tool_call.cpython-312.pyc
│     │     │  │  │     ├─ response_code_interpreter_tool_call_param.cpython-312.pyc
│     │     │  │  │     ├─ response_completed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_computer_tool_call.cpython-312.pyc
│     │     │  │  │     ├─ response_computer_tool_call_output_item.cpython-312.pyc
│     │     │  │  │     ├─ response_computer_tool_call_output_screenshot.cpython-312.pyc
│     │     │  │  │     ├─ response_computer_tool_call_output_screenshot_param.cpython-312.pyc
│     │     │  │  │     ├─ response_computer_tool_call_param.cpython-312.pyc
│     │     │  │  │     ├─ response_content_part_added_event.cpython-312.pyc
│     │     │  │  │     ├─ response_content_part_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_conversation_param.cpython-312.pyc
│     │     │  │  │     ├─ response_created_event.cpython-312.pyc
│     │     │  │  │     ├─ response_create_params.cpython-312.pyc
│     │     │  │  │     ├─ response_custom_tool_call.cpython-312.pyc
│     │     │  │  │     ├─ response_custom_tool_call_input_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_custom_tool_call_input_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_custom_tool_call_output.cpython-312.pyc
│     │     │  │  │     ├─ response_custom_tool_call_output_param.cpython-312.pyc
│     │     │  │  │     ├─ response_custom_tool_call_param.cpython-312.pyc
│     │     │  │  │     ├─ response_error.cpython-312.pyc
│     │     │  │  │     ├─ response_error_event.cpython-312.pyc
│     │     │  │  │     ├─ response_failed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_file_search_call_completed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_file_search_call_in_progress_event.cpython-312.pyc
│     │     │  │  │     ├─ response_file_search_call_searching_event.cpython-312.pyc
│     │     │  │  │     ├─ response_file_search_tool_call.cpython-312.pyc
│     │     │  │  │     ├─ response_file_search_tool_call_param.cpython-312.pyc
│     │     │  │  │     ├─ response_format_text_config.cpython-312.pyc
│     │     │  │  │     ├─ response_format_text_config_param.cpython-312.pyc
│     │     │  │  │     ├─ response_format_text_json_schema_config.cpython-312.pyc
│     │     │  │  │     ├─ response_format_text_json_schema_config_param.cpython-312.pyc
│     │     │  │  │     ├─ response_function_call_arguments_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_function_call_arguments_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_function_tool_call.cpython-312.pyc
│     │     │  │  │     ├─ response_function_tool_call_item.cpython-312.pyc
│     │     │  │  │     ├─ response_function_tool_call_output_item.cpython-312.pyc
│     │     │  │  │     ├─ response_function_tool_call_param.cpython-312.pyc
│     │     │  │  │     ├─ response_function_web_search.cpython-312.pyc
│     │     │  │  │     ├─ response_function_web_search_param.cpython-312.pyc
│     │     │  │  │     ├─ response_image_gen_call_completed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_image_gen_call_generating_event.cpython-312.pyc
│     │     │  │  │     ├─ response_image_gen_call_in_progress_event.cpython-312.pyc
│     │     │  │  │     ├─ response_image_gen_call_partial_image_event.cpython-312.pyc
│     │     │  │  │     ├─ response_includable.cpython-312.pyc
│     │     │  │  │     ├─ response_incomplete_event.cpython-312.pyc
│     │     │  │  │     ├─ response_input_audio.cpython-312.pyc
│     │     │  │  │     ├─ response_input_audio_param.cpython-312.pyc
│     │     │  │  │     ├─ response_input_content.cpython-312.pyc
│     │     │  │  │     ├─ response_input_content_param.cpython-312.pyc
│     │     │  │  │     ├─ response_input_file.cpython-312.pyc
│     │     │  │  │     ├─ response_input_file_param.cpython-312.pyc
│     │     │  │  │     ├─ response_input_image.cpython-312.pyc
│     │     │  │  │     ├─ response_input_image_param.cpython-312.pyc
│     │     │  │  │     ├─ response_input_item.cpython-312.pyc
│     │     │  │  │     ├─ response_input_item_param.cpython-312.pyc
│     │     │  │  │     ├─ response_input_message_content_list.cpython-312.pyc
│     │     │  │  │     ├─ response_input_message_content_list_param.cpython-312.pyc
│     │     │  │  │     ├─ response_input_message_item.cpython-312.pyc
│     │     │  │  │     ├─ response_input_param.cpython-312.pyc
│     │     │  │  │     ├─ response_input_text.cpython-312.pyc
│     │     │  │  │     ├─ response_input_text_param.cpython-312.pyc
│     │     │  │  │     ├─ response_in_progress_event.cpython-312.pyc
│     │     │  │  │     ├─ response_item.cpython-312.pyc
│     │     │  │  │     ├─ response_item_list.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_arguments_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_arguments_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_completed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_failed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_call_in_progress_event.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_list_tools_completed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_list_tools_failed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_mcp_list_tools_in_progress_event.cpython-312.pyc
│     │     │  │  │     ├─ response_output_item.cpython-312.pyc
│     │     │  │  │     ├─ response_output_item_added_event.cpython-312.pyc
│     │     │  │  │     ├─ response_output_item_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_output_message.cpython-312.pyc
│     │     │  │  │     ├─ response_output_message_param.cpython-312.pyc
│     │     │  │  │     ├─ response_output_refusal.cpython-312.pyc
│     │     │  │  │     ├─ response_output_refusal_param.cpython-312.pyc
│     │     │  │  │     ├─ response_output_text.cpython-312.pyc
│     │     │  │  │     ├─ response_output_text_annotation_added_event.cpython-312.pyc
│     │     │  │  │     ├─ response_output_text_param.cpython-312.pyc
│     │     │  │  │     ├─ response_prompt.cpython-312.pyc
│     │     │  │  │     ├─ response_prompt_param.cpython-312.pyc
│     │     │  │  │     ├─ response_queued_event.cpython-312.pyc
│     │     │  │  │     ├─ response_reasoning_item.cpython-312.pyc
│     │     │  │  │     ├─ response_reasoning_item_param.cpython-312.pyc
│     │     │  │  │     ├─ response_reasoning_summary_part_added_event.cpython-312.pyc
│     │     │  │  │     ├─ response_reasoning_summary_part_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_reasoning_summary_text_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_reasoning_summary_text_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_reasoning_text_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_reasoning_text_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_refusal_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_refusal_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_retrieve_params.cpython-312.pyc
│     │     │  │  │     ├─ response_status.cpython-312.pyc
│     │     │  │  │     ├─ response_stream_event.cpython-312.pyc
│     │     │  │  │     ├─ response_text_config.cpython-312.pyc
│     │     │  │  │     ├─ response_text_config_param.cpython-312.pyc
│     │     │  │  │     ├─ response_text_delta_event.cpython-312.pyc
│     │     │  │  │     ├─ response_text_done_event.cpython-312.pyc
│     │     │  │  │     ├─ response_usage.cpython-312.pyc
│     │     │  │  │     ├─ response_web_search_call_completed_event.cpython-312.pyc
│     │     │  │  │     ├─ response_web_search_call_in_progress_event.cpython-312.pyc
│     │     │  │  │     ├─ response_web_search_call_searching_event.cpython-312.pyc
│     │     │  │  │     ├─ tool.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_allowed.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_allowed_param.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_custom.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_custom_param.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_function.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_function_param.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_mcp.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_mcp_param.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_options.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_types.cpython-312.pyc
│     │     │  │  │     ├─ tool_choice_types_param.cpython-312.pyc
│     │     │  │  │     ├─ tool_param.cpython-312.pyc
│     │     │  │  │     ├─ web_search_preview_tool.cpython-312.pyc
│     │     │  │  │     ├─ web_search_preview_tool_param.cpython-312.pyc
│     │     │  │  │     ├─ web_search_tool.cpython-312.pyc
│     │     │  │  │     ├─ web_search_tool_param.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ shared
│     │     │  │  │  ├─ all_models.py
│     │     │  │  │  ├─ chat_model.py
│     │     │  │  │  ├─ comparison_filter.py
│     │     │  │  │  ├─ compound_filter.py
│     │     │  │  │  ├─ custom_tool_input_format.py
│     │     │  │  │  ├─ error_object.py
│     │     │  │  │  ├─ function_definition.py
│     │     │  │  │  ├─ function_parameters.py
│     │     │  │  │  ├─ metadata.py
│     │     │  │  │  ├─ reasoning.py
│     │     │  │  │  ├─ reasoning_effort.py
│     │     │  │  │  ├─ responses_model.py
│     │     │  │  │  ├─ response_format_json_object.py
│     │     │  │  │  ├─ response_format_json_schema.py
│     │     │  │  │  ├─ response_format_text.py
│     │     │  │  │  ├─ response_format_text_grammar.py
│     │     │  │  │  ├─ response_format_text_python.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ all_models.cpython-312.pyc
│     │     │  │  │     ├─ chat_model.cpython-312.pyc
│     │     │  │  │     ├─ comparison_filter.cpython-312.pyc
│     │     │  │  │     ├─ compound_filter.cpython-312.pyc
│     │     │  │  │     ├─ custom_tool_input_format.cpython-312.pyc
│     │     │  │  │     ├─ error_object.cpython-312.pyc
│     │     │  │  │     ├─ function_definition.cpython-312.pyc
│     │     │  │  │     ├─ function_parameters.cpython-312.pyc
│     │     │  │  │     ├─ metadata.cpython-312.pyc
│     │     │  │  │     ├─ reasoning.cpython-312.pyc
│     │     │  │  │     ├─ reasoning_effort.cpython-312.pyc
│     │     │  │  │     ├─ responses_model.cpython-312.pyc
│     │     │  │  │     ├─ response_format_json_object.cpython-312.pyc
│     │     │  │  │     ├─ response_format_json_schema.cpython-312.pyc
│     │     │  │  │     ├─ response_format_text.cpython-312.pyc
│     │     │  │  │     ├─ response_format_text_grammar.cpython-312.pyc
│     │     │  │  │     ├─ response_format_text_python.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ shared_params
│     │     │  │  │  ├─ chat_model.py
│     │     │  │  │  ├─ comparison_filter.py
│     │     │  │  │  ├─ compound_filter.py
│     │     │  │  │  ├─ custom_tool_input_format.py
│     │     │  │  │  ├─ function_definition.py
│     │     │  │  │  ├─ function_parameters.py
│     │     │  │  │  ├─ metadata.py
│     │     │  │  │  ├─ reasoning.py
│     │     │  │  │  ├─ reasoning_effort.py
│     │     │  │  │  ├─ responses_model.py
│     │     │  │  │  ├─ response_format_json_object.py
│     │     │  │  │  ├─ response_format_json_schema.py
│     │     │  │  │  ├─ response_format_text.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ chat_model.cpython-312.pyc
│     │     │  │  │     ├─ comparison_filter.cpython-312.pyc
│     │     │  │  │     ├─ compound_filter.cpython-312.pyc
│     │     │  │  │     ├─ custom_tool_input_format.cpython-312.pyc
│     │     │  │  │     ├─ function_definition.cpython-312.pyc
│     │     │  │  │     ├─ function_parameters.cpython-312.pyc
│     │     │  │  │     ├─ metadata.cpython-312.pyc
│     │     │  │  │     ├─ reasoning.cpython-312.pyc
│     │     │  │  │     ├─ reasoning_effort.cpython-312.pyc
│     │     │  │  │     ├─ responses_model.cpython-312.pyc
│     │     │  │  │     ├─ response_format_json_object.cpython-312.pyc
│     │     │  │  │     ├─ response_format_json_schema.cpython-312.pyc
│     │     │  │  │     ├─ response_format_text.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ static_file_chunking_strategy.py
│     │     │  │  ├─ static_file_chunking_strategy_object.py
│     │     │  │  ├─ static_file_chunking_strategy_object_param.py
│     │     │  │  ├─ static_file_chunking_strategy_param.py
│     │     │  │  ├─ upload.py
│     │     │  │  ├─ uploads
│     │     │  │  │  ├─ part_create_params.py
│     │     │  │  │  ├─ upload_part.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ part_create_params.cpython-312.pyc
│     │     │  │  │     ├─ upload_part.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ upload_complete_params.py
│     │     │  │  ├─ upload_create_params.py
│     │     │  │  ├─ vector_store.py
│     │     │  │  ├─ vector_stores
│     │     │  │  │  ├─ file_batch_create_params.py
│     │     │  │  │  ├─ file_batch_list_files_params.py
│     │     │  │  │  ├─ file_content_response.py
│     │     │  │  │  ├─ file_create_params.py
│     │     │  │  │  ├─ file_list_params.py
│     │     │  │  │  ├─ file_update_params.py
│     │     │  │  │  ├─ vector_store_file.py
│     │     │  │  │  ├─ vector_store_file_batch.py
│     │     │  │  │  ├─ vector_store_file_deleted.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ file_batch_create_params.cpython-312.pyc
│     │     │  │  │     ├─ file_batch_list_files_params.cpython-312.pyc
│     │     │  │  │     ├─ file_content_response.cpython-312.pyc
│     │     │  │  │     ├─ file_create_params.cpython-312.pyc
│     │     │  │  │     ├─ file_list_params.cpython-312.pyc
│     │     │  │  │     ├─ file_update_params.cpython-312.pyc
│     │     │  │  │     ├─ vector_store_file.cpython-312.pyc
│     │     │  │  │     ├─ vector_store_file_batch.cpython-312.pyc
│     │     │  │  │     ├─ vector_store_file_deleted.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ vector_store_create_params.py
│     │     │  │  ├─ vector_store_deleted.py
│     │     │  │  ├─ vector_store_list_params.py
│     │     │  │  ├─ vector_store_search_params.py
│     │     │  │  ├─ vector_store_search_response.py
│     │     │  │  ├─ vector_store_update_params.py
│     │     │  │  ├─ webhooks
│     │     │  │  │  ├─ batch_cancelled_webhook_event.py
│     │     │  │  │  ├─ batch_completed_webhook_event.py
│     │     │  │  │  ├─ batch_expired_webhook_event.py
│     │     │  │  │  ├─ batch_failed_webhook_event.py
│     │     │  │  │  ├─ eval_run_canceled_webhook_event.py
│     │     │  │  │  ├─ eval_run_failed_webhook_event.py
│     │     │  │  │  ├─ eval_run_succeeded_webhook_event.py
│     │     │  │  │  ├─ fine_tuning_job_cancelled_webhook_event.py
│     │     │  │  │  ├─ fine_tuning_job_failed_webhook_event.py
│     │     │  │  │  ├─ fine_tuning_job_succeeded_webhook_event.py
│     │     │  │  │  ├─ realtime_call_incoming_webhook_event.py
│     │     │  │  │  ├─ response_cancelled_webhook_event.py
│     │     │  │  │  ├─ response_completed_webhook_event.py
│     │     │  │  │  ├─ response_failed_webhook_event.py
│     │     │  │  │  ├─ response_incomplete_webhook_event.py
│     │     │  │  │  ├─ unwrap_webhook_event.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ batch_cancelled_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ batch_completed_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ batch_expired_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ batch_failed_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ eval_run_canceled_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ eval_run_failed_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ eval_run_succeeded_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ fine_tuning_job_cancelled_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ fine_tuning_job_failed_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ fine_tuning_job_succeeded_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ realtime_call_incoming_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ response_cancelled_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ response_completed_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ response_failed_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ response_incomplete_webhook_event.cpython-312.pyc
│     │     │  │  │     ├─ unwrap_webhook_event.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ websocket_connection_options.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ audio_model.cpython-312.pyc
│     │     │  │     ├─ audio_response_format.cpython-312.pyc
│     │     │  │     ├─ auto_file_chunking_strategy_param.cpython-312.pyc
│     │     │  │     ├─ batch.cpython-312.pyc
│     │     │  │     ├─ batch_create_params.cpython-312.pyc
│     │     │  │     ├─ batch_error.cpython-312.pyc
│     │     │  │     ├─ batch_list_params.cpython-312.pyc
│     │     │  │     ├─ batch_request_counts.cpython-312.pyc
│     │     │  │     ├─ chat_model.cpython-312.pyc
│     │     │  │     ├─ completion.cpython-312.pyc
│     │     │  │     ├─ completion_choice.cpython-312.pyc
│     │     │  │     ├─ completion_create_params.cpython-312.pyc
│     │     │  │     ├─ completion_usage.cpython-312.pyc
│     │     │  │     ├─ container_create_params.cpython-312.pyc
│     │     │  │     ├─ container_create_response.cpython-312.pyc
│     │     │  │     ├─ container_list_params.cpython-312.pyc
│     │     │  │     ├─ container_list_response.cpython-312.pyc
│     │     │  │     ├─ container_retrieve_response.cpython-312.pyc
│     │     │  │     ├─ create_embedding_response.cpython-312.pyc
│     │     │  │     ├─ embedding.cpython-312.pyc
│     │     │  │     ├─ embedding_create_params.cpython-312.pyc
│     │     │  │     ├─ embedding_model.cpython-312.pyc
│     │     │  │     ├─ eval_create_params.cpython-312.pyc
│     │     │  │     ├─ eval_create_response.cpython-312.pyc
│     │     │  │     ├─ eval_custom_data_source_config.cpython-312.pyc
│     │     │  │     ├─ eval_delete_response.cpython-312.pyc
│     │     │  │     ├─ eval_list_params.cpython-312.pyc
│     │     │  │     ├─ eval_list_response.cpython-312.pyc
│     │     │  │     ├─ eval_retrieve_response.cpython-312.pyc
│     │     │  │     ├─ eval_stored_completions_data_source_config.cpython-312.pyc
│     │     │  │     ├─ eval_update_params.cpython-312.pyc
│     │     │  │     ├─ eval_update_response.cpython-312.pyc
│     │     │  │     ├─ file_chunking_strategy.cpython-312.pyc
│     │     │  │     ├─ file_chunking_strategy_param.cpython-312.pyc
│     │     │  │     ├─ file_content.cpython-312.pyc
│     │     │  │     ├─ file_create_params.cpython-312.pyc
│     │     │  │     ├─ file_deleted.cpython-312.pyc
│     │     │  │     ├─ file_list_params.cpython-312.pyc
│     │     │  │     ├─ file_object.cpython-312.pyc
│     │     │  │     ├─ file_purpose.cpython-312.pyc
│     │     │  │     ├─ image.cpython-312.pyc
│     │     │  │     ├─ images_response.cpython-312.pyc
│     │     │  │     ├─ image_create_variation_params.cpython-312.pyc
│     │     │  │     ├─ image_edit_completed_event.cpython-312.pyc
│     │     │  │     ├─ image_edit_params.cpython-312.pyc
│     │     │  │     ├─ image_edit_partial_image_event.cpython-312.pyc
│     │     │  │     ├─ image_edit_stream_event.cpython-312.pyc
│     │     │  │     ├─ image_generate_params.cpython-312.pyc
│     │     │  │     ├─ image_gen_completed_event.cpython-312.pyc
│     │     │  │     ├─ image_gen_partial_image_event.cpython-312.pyc
│     │     │  │     ├─ image_gen_stream_event.cpython-312.pyc
│     │     │  │     ├─ image_model.cpython-312.pyc
│     │     │  │     ├─ model.cpython-312.pyc
│     │     │  │     ├─ model_deleted.cpython-312.pyc
│     │     │  │     ├─ moderation.cpython-312.pyc
│     │     │  │     ├─ moderation_create_params.cpython-312.pyc
│     │     │  │     ├─ moderation_create_response.cpython-312.pyc
│     │     │  │     ├─ moderation_image_url_input_param.cpython-312.pyc
│     │     │  │     ├─ moderation_model.cpython-312.pyc
│     │     │  │     ├─ moderation_multi_modal_input_param.cpython-312.pyc
│     │     │  │     ├─ moderation_text_input_param.cpython-312.pyc
│     │     │  │     ├─ other_file_chunking_strategy_object.cpython-312.pyc
│     │     │  │     ├─ static_file_chunking_strategy.cpython-312.pyc
│     │     │  │     ├─ static_file_chunking_strategy_object.cpython-312.pyc
│     │     │  │     ├─ static_file_chunking_strategy_object_param.cpython-312.pyc
│     │     │  │     ├─ static_file_chunking_strategy_param.cpython-312.pyc
│     │     │  │     ├─ upload.cpython-312.pyc
│     │     │  │     ├─ upload_complete_params.cpython-312.pyc
│     │     │  │     ├─ upload_create_params.cpython-312.pyc
│     │     │  │     ├─ vector_store.cpython-312.pyc
│     │     │  │     ├─ vector_store_create_params.cpython-312.pyc
│     │     │  │     ├─ vector_store_deleted.cpython-312.pyc
│     │     │  │     ├─ vector_store_list_params.cpython-312.pyc
│     │     │  │     ├─ vector_store_search_params.cpython-312.pyc
│     │     │  │     ├─ vector_store_search_response.cpython-312.pyc
│     │     │  │     ├─ vector_store_update_params.cpython-312.pyc
│     │     │  │     ├─ websocket_connection_options.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ version.py
│     │     │  ├─ _base_client.py
│     │     │  ├─ _client.py
│     │     │  ├─ _compat.py
│     │     │  ├─ _constants.py
│     │     │  ├─ _exceptions.py
│     │     │  ├─ _extras
│     │     │  │  ├─ numpy_proxy.py
│     │     │  │  ├─ pandas_proxy.py
│     │     │  │  ├─ sounddevice_proxy.py
│     │     │  │  ├─ _common.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ numpy_proxy.cpython-312.pyc
│     │     │  │     ├─ pandas_proxy.cpython-312.pyc
│     │     │  │     ├─ sounddevice_proxy.cpython-312.pyc
│     │     │  │     ├─ _common.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _files.py
│     │     │  ├─ _legacy_response.py
│     │     │  ├─ _models.py
│     │     │  ├─ _module_client.py
│     │     │  ├─ _qs.py
│     │     │  ├─ _resource.py
│     │     │  ├─ _response.py
│     │     │  ├─ _streaming.py
│     │     │  ├─ _types.py
│     │     │  ├─ _utils
│     │     │  │  ├─ _compat.py
│     │     │  │  ├─ _datetime_parse.py
│     │     │  │  ├─ _logs.py
│     │     │  │  ├─ _proxy.py
│     │     │  │  ├─ _reflection.py
│     │     │  │  ├─ _resources_proxy.py
│     │     │  │  ├─ _streams.py
│     │     │  │  ├─ _sync.py
│     │     │  │  ├─ _transform.py
│     │     │  │  ├─ _typing.py
│     │     │  │  ├─ _utils.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ _compat.cpython-312.pyc
│     │     │  │     ├─ _datetime_parse.cpython-312.pyc
│     │     │  │     ├─ _logs.cpython-312.pyc
│     │     │  │     ├─ _proxy.cpython-312.pyc
│     │     │  │     ├─ _reflection.cpython-312.pyc
│     │     │  │     ├─ _resources_proxy.cpython-312.pyc
│     │     │  │     ├─ _streams.cpython-312.pyc
│     │     │  │     ├─ _sync.cpython-312.pyc
│     │     │  │     ├─ _transform.cpython-312.pyc
│     │     │  │     ├─ _typing.cpython-312.pyc
│     │     │  │     ├─ _utils.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _version.py
│     │     │  ├─ __init__.py
│     │     │  ├─ __main__.py
│     │     │  └─ __pycache__
│     │     │     ├─ pagination.cpython-312.pyc
│     │     │     ├─ version.cpython-312.pyc
│     │     │     ├─ _base_client.cpython-312.pyc
│     │     │     ├─ _client.cpython-312.pyc
│     │     │     ├─ _compat.cpython-312.pyc
│     │     │     ├─ _constants.cpython-312.pyc
│     │     │     ├─ _exceptions.cpython-312.pyc
│     │     │     ├─ _files.cpython-312.pyc
│     │     │     ├─ _legacy_response.cpython-312.pyc
│     │     │     ├─ _models.cpython-312.pyc
│     │     │     ├─ _module_client.cpython-312.pyc
│     │     │     ├─ _qs.cpython-312.pyc
│     │     │     ├─ _resource.cpython-312.pyc
│     │     │     ├─ _response.cpython-312.pyc
│     │     │     ├─ _streaming.cpython-312.pyc
│     │     │     ├─ _types.cpython-312.pyc
│     │     │     ├─ _version.cpython-312.pyc
│     │     │     ├─ __init__.cpython-312.pyc
│     │     │     └─ __main__.cpython-312.pyc
│     │     ├─ openai-1.107.2.dist-info
│     │     │  ├─ entry_points.txt
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ pip
│     │     │  ├─ py.typed
│     │     │  ├─ _internal
│     │     │  │  ├─ build_env.py
│     │     │  │  ├─ cache.py
│     │     │  │  ├─ cli
│     │     │  │  │  ├─ autocompletion.py
│     │     │  │  │  ├─ base_command.py
│     │     │  │  │  ├─ cmdoptions.py
│     │     │  │  │  ├─ command_context.py
│     │     │  │  │  ├─ index_command.py
│     │     │  │  │  ├─ main.py
│     │     │  │  │  ├─ main_parser.py
│     │     │  │  │  ├─ parser.py
│     │     │  │  │  ├─ progress_bars.py
│     │     │  │  │  ├─ req_command.py
│     │     │  │  │  ├─ spinners.py
│     │     │  │  │  ├─ status_codes.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ autocompletion.cpython-312.pyc
│     │     │  │  │     ├─ base_command.cpython-312.pyc
│     │     │  │  │     ├─ cmdoptions.cpython-312.pyc
│     │     │  │  │     ├─ command_context.cpython-312.pyc
│     │     │  │  │     ├─ index_command.cpython-312.pyc
│     │     │  │  │     ├─ main.cpython-312.pyc
│     │     │  │  │     ├─ main_parser.cpython-312.pyc
│     │     │  │  │     ├─ parser.cpython-312.pyc
│     │     │  │  │     ├─ progress_bars.cpython-312.pyc
│     │     │  │  │     ├─ req_command.cpython-312.pyc
│     │     │  │  │     ├─ spinners.cpython-312.pyc
│     │     │  │  │     ├─ status_codes.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ commands
│     │     │  │  │  ├─ cache.py
│     │     │  │  │  ├─ check.py
│     │     │  │  │  ├─ completion.py
│     │     │  │  │  ├─ configuration.py
│     │     │  │  │  ├─ debug.py
│     │     │  │  │  ├─ download.py
│     │     │  │  │  ├─ freeze.py
│     │     │  │  │  ├─ hash.py
│     │     │  │  │  ├─ help.py
│     │     │  │  │  ├─ index.py
│     │     │  │  │  ├─ inspect.py
│     │     │  │  │  ├─ install.py
│     │     │  │  │  ├─ list.py
│     │     │  │  │  ├─ search.py
│     │     │  │  │  ├─ show.py
│     │     │  │  │  ├─ uninstall.py
│     │     │  │  │  ├─ wheel.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ cache.cpython-312.pyc
│     │     │  │  │     ├─ check.cpython-312.pyc
│     │     │  │  │     ├─ completion.cpython-312.pyc
│     │     │  │  │     ├─ configuration.cpython-312.pyc
│     │     │  │  │     ├─ debug.cpython-312.pyc
│     │     │  │  │     ├─ download.cpython-312.pyc
│     │     │  │  │     ├─ freeze.cpython-312.pyc
│     │     │  │  │     ├─ hash.cpython-312.pyc
│     │     │  │  │     ├─ help.cpython-312.pyc
│     │     │  │  │     ├─ index.cpython-312.pyc
│     │     │  │  │     ├─ inspect.cpython-312.pyc
│     │     │  │  │     ├─ install.cpython-312.pyc
│     │     │  │  │     ├─ list.cpython-312.pyc
│     │     │  │  │     ├─ search.cpython-312.pyc
│     │     │  │  │     ├─ show.cpython-312.pyc
│     │     │  │  │     ├─ uninstall.cpython-312.pyc
│     │     │  │  │     ├─ wheel.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ configuration.py
│     │     │  │  ├─ distributions
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ installed.py
│     │     │  │  │  ├─ sdist.py
│     │     │  │  │  ├─ wheel.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ installed.cpython-312.pyc
│     │     │  │  │     ├─ sdist.cpython-312.pyc
│     │     │  │  │     ├─ wheel.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ exceptions.py
│     │     │  │  ├─ index
│     │     │  │  │  ├─ collector.py
│     │     │  │  │  ├─ package_finder.py
│     │     │  │  │  ├─ sources.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ collector.cpython-312.pyc
│     │     │  │  │     ├─ package_finder.cpython-312.pyc
│     │     │  │  │     ├─ sources.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ locations
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ _distutils.py
│     │     │  │  │  ├─ _sysconfig.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ _distutils.cpython-312.pyc
│     │     │  │  │     ├─ _sysconfig.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ main.py
│     │     │  │  ├─ metadata
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ importlib
│     │     │  │  │  │  ├─ _compat.py
│     │     │  │  │  │  ├─ _dists.py
│     │     │  │  │  │  ├─ _envs.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ _compat.cpython-312.pyc
│     │     │  │  │  │     ├─ _dists.cpython-312.pyc
│     │     │  │  │  │     ├─ _envs.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ pkg_resources.py
│     │     │  │  │  ├─ _json.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ pkg_resources.cpython-312.pyc
│     │     │  │  │     ├─ _json.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ models
│     │     │  │  │  ├─ candidate.py
│     │     │  │  │  ├─ direct_url.py
│     │     │  │  │  ├─ format_control.py
│     │     │  │  │  ├─ index.py
│     │     │  │  │  ├─ installation_report.py
│     │     │  │  │  ├─ link.py
│     │     │  │  │  ├─ scheme.py
│     │     │  │  │  ├─ search_scope.py
│     │     │  │  │  ├─ selection_prefs.py
│     │     │  │  │  ├─ target_python.py
│     │     │  │  │  ├─ wheel.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ candidate.cpython-312.pyc
│     │     │  │  │     ├─ direct_url.cpython-312.pyc
│     │     │  │  │     ├─ format_control.cpython-312.pyc
│     │     │  │  │     ├─ index.cpython-312.pyc
│     │     │  │  │     ├─ installation_report.cpython-312.pyc
│     │     │  │  │     ├─ link.cpython-312.pyc
│     │     │  │  │     ├─ scheme.cpython-312.pyc
│     │     │  │  │     ├─ search_scope.cpython-312.pyc
│     │     │  │  │     ├─ selection_prefs.cpython-312.pyc
│     │     │  │  │     ├─ target_python.cpython-312.pyc
│     │     │  │  │     ├─ wheel.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ network
│     │     │  │  │  ├─ auth.py
│     │     │  │  │  ├─ cache.py
│     │     │  │  │  ├─ download.py
│     │     │  │  │  ├─ lazy_wheel.py
│     │     │  │  │  ├─ session.py
│     │     │  │  │  ├─ utils.py
│     │     │  │  │  ├─ xmlrpc.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ auth.cpython-312.pyc
│     │     │  │  │     ├─ cache.cpython-312.pyc
│     │     │  │  │     ├─ download.cpython-312.pyc
│     │     │  │  │     ├─ lazy_wheel.cpython-312.pyc
│     │     │  │  │     ├─ session.cpython-312.pyc
│     │     │  │  │     ├─ utils.cpython-312.pyc
│     │     │  │  │     ├─ xmlrpc.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ operations
│     │     │  │  │  ├─ build
│     │     │  │  │  │  ├─ build_tracker.py
│     │     │  │  │  │  ├─ metadata.py
│     │     │  │  │  │  ├─ metadata_editable.py
│     │     │  │  │  │  ├─ metadata_legacy.py
│     │     │  │  │  │  ├─ wheel.py
│     │     │  │  │  │  ├─ wheel_editable.py
│     │     │  │  │  │  ├─ wheel_legacy.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ build_tracker.cpython-312.pyc
│     │     │  │  │  │     ├─ metadata.cpython-312.pyc
│     │     │  │  │  │     ├─ metadata_editable.cpython-312.pyc
│     │     │  │  │  │     ├─ metadata_legacy.cpython-312.pyc
│     │     │  │  │  │     ├─ wheel.cpython-312.pyc
│     │     │  │  │  │     ├─ wheel_editable.cpython-312.pyc
│     │     │  │  │  │     ├─ wheel_legacy.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ check.py
│     │     │  │  │  ├─ freeze.py
│     │     │  │  │  ├─ install
│     │     │  │  │  │  ├─ editable_legacy.py
│     │     │  │  │  │  ├─ wheel.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ editable_legacy.cpython-312.pyc
│     │     │  │  │  │     ├─ wheel.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ prepare.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ check.cpython-312.pyc
│     │     │  │  │     ├─ freeze.cpython-312.pyc
│     │     │  │  │     ├─ prepare.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ pyproject.py
│     │     │  │  ├─ req
│     │     │  │  │  ├─ constructors.py
│     │     │  │  │  ├─ req_file.py
│     │     │  │  │  ├─ req_install.py
│     │     │  │  │  ├─ req_set.py
│     │     │  │  │  ├─ req_uninstall.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ constructors.cpython-312.pyc
│     │     │  │  │     ├─ req_file.cpython-312.pyc
│     │     │  │  │     ├─ req_install.cpython-312.pyc
│     │     │  │  │     ├─ req_set.cpython-312.pyc
│     │     │  │  │     ├─ req_uninstall.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ resolution
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ legacy
│     │     │  │  │  │  ├─ resolver.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ resolver.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ resolvelib
│     │     │  │  │  │  ├─ base.py
│     │     │  │  │  │  ├─ candidates.py
│     │     │  │  │  │  ├─ factory.py
│     │     │  │  │  │  ├─ found_candidates.py
│     │     │  │  │  │  ├─ provider.py
│     │     │  │  │  │  ├─ reporter.py
│     │     │  │  │  │  ├─ requirements.py
│     │     │  │  │  │  ├─ resolver.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │  │     ├─ candidates.cpython-312.pyc
│     │     │  │  │  │     ├─ factory.cpython-312.pyc
│     │     │  │  │  │     ├─ found_candidates.cpython-312.pyc
│     │     │  │  │  │     ├─ provider.cpython-312.pyc
│     │     │  │  │  │     ├─ reporter.cpython-312.pyc
│     │     │  │  │  │     ├─ requirements.cpython-312.pyc
│     │     │  │  │  │     ├─ resolver.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ self_outdated_check.py
│     │     │  │  ├─ utils
│     │     │  │  │  ├─ appdirs.py
│     │     │  │  │  ├─ compat.py
│     │     │  │  │  ├─ compatibility_tags.py
│     │     │  │  │  ├─ datetime.py
│     │     │  │  │  ├─ deprecation.py
│     │     │  │  │  ├─ direct_url_helpers.py
│     │     │  │  │  ├─ egg_link.py
│     │     │  │  │  ├─ entrypoints.py
│     │     │  │  │  ├─ filesystem.py
│     │     │  │  │  ├─ filetypes.py
│     │     │  │  │  ├─ glibc.py
│     │     │  │  │  ├─ hashes.py
│     │     │  │  │  ├─ logging.py
│     │     │  │  │  ├─ misc.py
│     │     │  │  │  ├─ packaging.py
│     │     │  │  │  ├─ retry.py
│     │     │  │  │  ├─ setuptools_build.py
│     │     │  │  │  ├─ subprocess.py
│     │     │  │  │  ├─ temp_dir.py
│     │     │  │  │  ├─ unpacking.py
│     │     │  │  │  ├─ urls.py
│     │     │  │  │  ├─ virtualenv.py
│     │     │  │  │  ├─ wheel.py
│     │     │  │  │  ├─ _jaraco_text.py
│     │     │  │  │  ├─ _log.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ appdirs.cpython-312.pyc
│     │     │  │  │     ├─ compat.cpython-312.pyc
│     │     │  │  │     ├─ compatibility_tags.cpython-312.pyc
│     │     │  │  │     ├─ datetime.cpython-312.pyc
│     │     │  │  │     ├─ deprecation.cpython-312.pyc
│     │     │  │  │     ├─ direct_url_helpers.cpython-312.pyc
│     │     │  │  │     ├─ egg_link.cpython-312.pyc
│     │     │  │  │     ├─ entrypoints.cpython-312.pyc
│     │     │  │  │     ├─ filesystem.cpython-312.pyc
│     │     │  │  │     ├─ filetypes.cpython-312.pyc
│     │     │  │  │     ├─ glibc.cpython-312.pyc
│     │     │  │  │     ├─ hashes.cpython-312.pyc
│     │     │  │  │     ├─ logging.cpython-312.pyc
│     │     │  │  │     ├─ misc.cpython-312.pyc
│     │     │  │  │     ├─ packaging.cpython-312.pyc
│     │     │  │  │     ├─ retry.cpython-312.pyc
│     │     │  │  │     ├─ setuptools_build.cpython-312.pyc
│     │     │  │  │     ├─ subprocess.cpython-312.pyc
│     │     │  │  │     ├─ temp_dir.cpython-312.pyc
│     │     │  │  │     ├─ unpacking.cpython-312.pyc
│     │     │  │  │     ├─ urls.cpython-312.pyc
│     │     │  │  │     ├─ virtualenv.cpython-312.pyc
│     │     │  │  │     ├─ wheel.cpython-312.pyc
│     │     │  │  │     ├─ _jaraco_text.cpython-312.pyc
│     │     │  │  │     ├─ _log.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ vcs
│     │     │  │  │  ├─ bazaar.py
│     │     │  │  │  ├─ git.py
│     │     │  │  │  ├─ mercurial.py
│     │     │  │  │  ├─ subversion.py
│     │     │  │  │  ├─ versioncontrol.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ bazaar.cpython-312.pyc
│     │     │  │  │     ├─ git.cpython-312.pyc
│     │     │  │  │     ├─ mercurial.cpython-312.pyc
│     │     │  │  │     ├─ subversion.cpython-312.pyc
│     │     │  │  │     ├─ versioncontrol.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ wheel_builder.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ build_env.cpython-312.pyc
│     │     │  │     ├─ cache.cpython-312.pyc
│     │     │  │     ├─ configuration.cpython-312.pyc
│     │     │  │     ├─ exceptions.cpython-312.pyc
│     │     │  │     ├─ main.cpython-312.pyc
│     │     │  │     ├─ pyproject.cpython-312.pyc
│     │     │  │     ├─ self_outdated_check.cpython-312.pyc
│     │     │  │     ├─ wheel_builder.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _vendor
│     │     │  │  ├─ cachecontrol
│     │     │  │  │  ├─ adapter.py
│     │     │  │  │  ├─ cache.py
│     │     │  │  │  ├─ caches
│     │     │  │  │  │  ├─ file_cache.py
│     │     │  │  │  │  ├─ redis_cache.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ file_cache.cpython-312.pyc
│     │     │  │  │  │     ├─ redis_cache.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ controller.py
│     │     │  │  │  ├─ filewrapper.py
│     │     │  │  │  ├─ heuristics.py
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ serialize.py
│     │     │  │  │  ├─ wrapper.py
│     │     │  │  │  ├─ _cmd.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ adapter.cpython-312.pyc
│     │     │  │  │     ├─ cache.cpython-312.pyc
│     │     │  │  │     ├─ controller.cpython-312.pyc
│     │     │  │  │     ├─ filewrapper.cpython-312.pyc
│     │     │  │  │     ├─ heuristics.cpython-312.pyc
│     │     │  │  │     ├─ serialize.cpython-312.pyc
│     │     │  │  │     ├─ wrapper.cpython-312.pyc
│     │     │  │  │     ├─ _cmd.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ certifi
│     │     │  │  │  ├─ cacert.pem
│     │     │  │  │  ├─ core.py
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  ├─ __main__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ core.cpython-312.pyc
│     │     │  │  │     ├─ __init__.cpython-312.pyc
│     │     │  │  │     └─ __main__.cpython-312.pyc
│     │     │  │  ├─ distlib
│     │     │  │  │  ├─ compat.py
│     │     │  │  │  ├─ database.py
│     │     │  │  │  ├─ index.py
│     │     │  │  │  ├─ locators.py
│     │     │  │  │  ├─ manifest.py
│     │     │  │  │  ├─ markers.py
│     │     │  │  │  ├─ metadata.py
│     │     │  │  │  ├─ resources.py
│     │     │  │  │  ├─ scripts.py
│     │     │  │  │  ├─ t32.exe
│     │     │  │  │  ├─ t64-arm.exe
│     │     │  │  │  ├─ t64.exe
│     │     │  │  │  ├─ util.py
│     │     │  │  │  ├─ version.py
│     │     │  │  │  ├─ w32.exe
│     │     │  │  │  ├─ w64-arm.exe
│     │     │  │  │  ├─ w64.exe
│     │     │  │  │  ├─ wheel.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ compat.cpython-312.pyc
│     │     │  │  │     ├─ database.cpython-312.pyc
│     │     │  │  │     ├─ index.cpython-312.pyc
│     │     │  │  │     ├─ locators.cpython-312.pyc
│     │     │  │  │     ├─ manifest.cpython-312.pyc
│     │     │  │  │     ├─ markers.cpython-312.pyc
│     │     │  │  │     ├─ metadata.cpython-312.pyc
│     │     │  │  │     ├─ resources.cpython-312.pyc
│     │     │  │  │     ├─ scripts.cpython-312.pyc
│     │     │  │  │     ├─ util.cpython-312.pyc
│     │     │  │  │     ├─ version.cpython-312.pyc
│     │     │  │  │     ├─ wheel.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ distro
│     │     │  │  │  ├─ distro.py
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  ├─ __main__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ distro.cpython-312.pyc
│     │     │  │  │     ├─ __init__.cpython-312.pyc
│     │     │  │  │     └─ __main__.cpython-312.pyc
│     │     │  │  ├─ idna
│     │     │  │  │  ├─ codec.py
│     │     │  │  │  ├─ compat.py
│     │     │  │  │  ├─ core.py
│     │     │  │  │  ├─ idnadata.py
│     │     │  │  │  ├─ intranges.py
│     │     │  │  │  ├─ package_data.py
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ uts46data.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ codec.cpython-312.pyc
│     │     │  │  │     ├─ compat.cpython-312.pyc
│     │     │  │  │     ├─ core.cpython-312.pyc
│     │     │  │  │     ├─ idnadata.cpython-312.pyc
│     │     │  │  │     ├─ intranges.cpython-312.pyc
│     │     │  │  │     ├─ package_data.cpython-312.pyc
│     │     │  │  │     ├─ uts46data.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ msgpack
│     │     │  │  │  ├─ exceptions.py
│     │     │  │  │  ├─ ext.py
│     │     │  │  │  ├─ fallback.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ exceptions.cpython-312.pyc
│     │     │  │  │     ├─ ext.cpython-312.pyc
│     │     │  │  │     ├─ fallback.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ packaging
│     │     │  │  │  ├─ licenses
│     │     │  │  │  │  ├─ _spdx.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ _spdx.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ markers.py
│     │     │  │  │  ├─ metadata.py
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ requirements.py
│     │     │  │  │  ├─ specifiers.py
│     │     │  │  │  ├─ tags.py
│     │     │  │  │  ├─ utils.py
│     │     │  │  │  ├─ version.py
│     │     │  │  │  ├─ _elffile.py
│     │     │  │  │  ├─ _manylinux.py
│     │     │  │  │  ├─ _musllinux.py
│     │     │  │  │  ├─ _parser.py
│     │     │  │  │  ├─ _structures.py
│     │     │  │  │  ├─ _tokenizer.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ markers.cpython-312.pyc
│     │     │  │  │     ├─ metadata.cpython-312.pyc
│     │     │  │  │     ├─ requirements.cpython-312.pyc
│     │     │  │  │     ├─ specifiers.cpython-312.pyc
│     │     │  │  │     ├─ tags.cpython-312.pyc
│     │     │  │  │     ├─ utils.cpython-312.pyc
│     │     │  │  │     ├─ version.cpython-312.pyc
│     │     │  │  │     ├─ _elffile.cpython-312.pyc
│     │     │  │  │     ├─ _manylinux.cpython-312.pyc
│     │     │  │  │     ├─ _musllinux.cpython-312.pyc
│     │     │  │  │     ├─ _parser.cpython-312.pyc
│     │     │  │  │     ├─ _structures.cpython-312.pyc
│     │     │  │  │     ├─ _tokenizer.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ pkg_resources
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ platformdirs
│     │     │  │  │  ├─ android.py
│     │     │  │  │  ├─ api.py
│     │     │  │  │  ├─ macos.py
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ unix.py
│     │     │  │  │  ├─ version.py
│     │     │  │  │  ├─ windows.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  ├─ __main__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ android.cpython-312.pyc
│     │     │  │  │     ├─ api.cpython-312.pyc
│     │     │  │  │     ├─ macos.cpython-312.pyc
│     │     │  │  │     ├─ unix.cpython-312.pyc
│     │     │  │  │     ├─ version.cpython-312.pyc
│     │     │  │  │     ├─ windows.cpython-312.pyc
│     │     │  │  │     ├─ __init__.cpython-312.pyc
│     │     │  │  │     └─ __main__.cpython-312.pyc
│     │     │  │  ├─ pygments
│     │     │  │  │  ├─ cmdline.py
│     │     │  │  │  ├─ console.py
│     │     │  │  │  ├─ filter.py
│     │     │  │  │  ├─ filters
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ formatter.py
│     │     │  │  │  ├─ formatters
│     │     │  │  │  │  ├─ bbcode.py
│     │     │  │  │  │  ├─ groff.py
│     │     │  │  │  │  ├─ html.py
│     │     │  │  │  │  ├─ img.py
│     │     │  │  │  │  ├─ irc.py
│     │     │  │  │  │  ├─ latex.py
│     │     │  │  │  │  ├─ other.py
│     │     │  │  │  │  ├─ pangomarkup.py
│     │     │  │  │  │  ├─ rtf.py
│     │     │  │  │  │  ├─ svg.py
│     │     │  │  │  │  ├─ terminal.py
│     │     │  │  │  │  ├─ terminal256.py
│     │     │  │  │  │  ├─ _mapping.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ bbcode.cpython-312.pyc
│     │     │  │  │  │     ├─ groff.cpython-312.pyc
│     │     │  │  │  │     ├─ html.cpython-312.pyc
│     │     │  │  │  │     ├─ img.cpython-312.pyc
│     │     │  │  │  │     ├─ irc.cpython-312.pyc
│     │     │  │  │  │     ├─ latex.cpython-312.pyc
│     │     │  │  │  │     ├─ other.cpython-312.pyc
│     │     │  │  │  │     ├─ pangomarkup.cpython-312.pyc
│     │     │  │  │  │     ├─ rtf.cpython-312.pyc
│     │     │  │  │  │     ├─ svg.cpython-312.pyc
│     │     │  │  │  │     ├─ terminal.cpython-312.pyc
│     │     │  │  │  │     ├─ terminal256.cpython-312.pyc
│     │     │  │  │  │     ├─ _mapping.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ lexer.py
│     │     │  │  │  ├─ lexers
│     │     │  │  │  │  ├─ python.py
│     │     │  │  │  │  ├─ _mapping.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ python.cpython-312.pyc
│     │     │  │  │  │     ├─ _mapping.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ modeline.py
│     │     │  │  │  ├─ plugin.py
│     │     │  │  │  ├─ regexopt.py
│     │     │  │  │  ├─ scanner.py
│     │     │  │  │  ├─ sphinxext.py
│     │     │  │  │  ├─ style.py
│     │     │  │  │  ├─ styles
│     │     │  │  │  │  ├─ _mapping.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ _mapping.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ token.py
│     │     │  │  │  ├─ unistring.py
│     │     │  │  │  ├─ util.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  ├─ __main__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ cmdline.cpython-312.pyc
│     │     │  │  │     ├─ console.cpython-312.pyc
│     │     │  │  │     ├─ filter.cpython-312.pyc
│     │     │  │  │     ├─ formatter.cpython-312.pyc
│     │     │  │  │     ├─ lexer.cpython-312.pyc
│     │     │  │  │     ├─ modeline.cpython-312.pyc
│     │     │  │  │     ├─ plugin.cpython-312.pyc
│     │     │  │  │     ├─ regexopt.cpython-312.pyc
│     │     │  │  │     ├─ scanner.cpython-312.pyc
│     │     │  │  │     ├─ sphinxext.cpython-312.pyc
│     │     │  │  │     ├─ style.cpython-312.pyc
│     │     │  │  │     ├─ token.cpython-312.pyc
│     │     │  │  │     ├─ unistring.cpython-312.pyc
│     │     │  │  │     ├─ util.cpython-312.pyc
│     │     │  │  │     ├─ __init__.cpython-312.pyc
│     │     │  │  │     └─ __main__.cpython-312.pyc
│     │     │  │  ├─ pyproject_hooks
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ _impl.py
│     │     │  │  │  ├─ _in_process
│     │     │  │  │  │  ├─ _in_process.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ _in_process.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ _impl.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ requests
│     │     │  │  │  ├─ adapters.py
│     │     │  │  │  ├─ api.py
│     │     │  │  │  ├─ auth.py
│     │     │  │  │  ├─ certs.py
│     │     │  │  │  ├─ compat.py
│     │     │  │  │  ├─ cookies.py
│     │     │  │  │  ├─ exceptions.py
│     │     │  │  │  ├─ help.py
│     │     │  │  │  ├─ hooks.py
│     │     │  │  │  ├─ models.py
│     │     │  │  │  ├─ packages.py
│     │     │  │  │  ├─ sessions.py
│     │     │  │  │  ├─ status_codes.py
│     │     │  │  │  ├─ structures.py
│     │     │  │  │  ├─ utils.py
│     │     │  │  │  ├─ _internal_utils.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  ├─ __pycache__
│     │     │  │  │  │  ├─ adapters.cpython-312.pyc
│     │     │  │  │  │  ├─ api.cpython-312.pyc
│     │     │  │  │  │  ├─ auth.cpython-312.pyc
│     │     │  │  │  │  ├─ certs.cpython-312.pyc
│     │     │  │  │  │  ├─ compat.cpython-312.pyc
│     │     │  │  │  │  ├─ cookies.cpython-312.pyc
│     │     │  │  │  │  ├─ exceptions.cpython-312.pyc
│     │     │  │  │  │  ├─ help.cpython-312.pyc
│     │     │  │  │  │  ├─ hooks.cpython-312.pyc
│     │     │  │  │  │  ├─ models.cpython-312.pyc
│     │     │  │  │  │  ├─ packages.cpython-312.pyc
│     │     │  │  │  │  ├─ sessions.cpython-312.pyc
│     │     │  │  │  │  ├─ status_codes.cpython-312.pyc
│     │     │  │  │  │  ├─ structures.cpython-312.pyc
│     │     │  │  │  │  ├─ utils.cpython-312.pyc
│     │     │  │  │  │  ├─ _internal_utils.cpython-312.pyc
│     │     │  │  │  │  ├─ __init__.cpython-312.pyc
│     │     │  │  │  │  └─ __version__.cpython-312.pyc
│     │     │  │  │  └─ __version__.py
│     │     │  │  ├─ resolvelib
│     │     │  │  │  ├─ compat
│     │     │  │  │  │  ├─ collections_abc.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ collections_abc.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ providers.py
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ reporters.py
│     │     │  │  │  ├─ resolvers.py
│     │     │  │  │  ├─ structs.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ providers.cpython-312.pyc
│     │     │  │  │     ├─ reporters.cpython-312.pyc
│     │     │  │  │     ├─ resolvers.cpython-312.pyc
│     │     │  │  │     ├─ structs.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ rich
│     │     │  │  │  ├─ abc.py
│     │     │  │  │  ├─ align.py
│     │     │  │  │  ├─ ansi.py
│     │     │  │  │  ├─ bar.py
│     │     │  │  │  ├─ box.py
│     │     │  │  │  ├─ cells.py
│     │     │  │  │  ├─ color.py
│     │     │  │  │  ├─ color_triplet.py
│     │     │  │  │  ├─ columns.py
│     │     │  │  │  ├─ console.py
│     │     │  │  │  ├─ constrain.py
│     │     │  │  │  ├─ containers.py
│     │     │  │  │  ├─ control.py
│     │     │  │  │  ├─ default_styles.py
│     │     │  │  │  ├─ diagnose.py
│     │     │  │  │  ├─ emoji.py
│     │     │  │  │  ├─ errors.py
│     │     │  │  │  ├─ filesize.py
│     │     │  │  │  ├─ file_proxy.py
│     │     │  │  │  ├─ highlighter.py
│     │     │  │  │  ├─ json.py
│     │     │  │  │  ├─ jupyter.py
│     │     │  │  │  ├─ layout.py
│     │     │  │  │  ├─ live.py
│     │     │  │  │  ├─ live_render.py
│     │     │  │  │  ├─ logging.py
│     │     │  │  │  ├─ markup.py
│     │     │  │  │  ├─ measure.py
│     │     │  │  │  ├─ padding.py
│     │     │  │  │  ├─ pager.py
│     │     │  │  │  ├─ palette.py
│     │     │  │  │  ├─ panel.py
│     │     │  │  │  ├─ pretty.py
│     │     │  │  │  ├─ progress.py
│     │     │  │  │  ├─ progress_bar.py
│     │     │  │  │  ├─ prompt.py
│     │     │  │  │  ├─ protocol.py
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ region.py
│     │     │  │  │  ├─ repr.py
│     │     │  │  │  ├─ rule.py
│     │     │  │  │  ├─ scope.py
│     │     │  │  │  ├─ screen.py
│     │     │  │  │  ├─ segment.py
│     │     │  │  │  ├─ spinner.py
│     │     │  │  │  ├─ status.py
│     │     │  │  │  ├─ style.py
│     │     │  │  │  ├─ styled.py
│     │     │  │  │  ├─ syntax.py
│     │     │  │  │  ├─ table.py
│     │     │  │  │  ├─ terminal_theme.py
│     │     │  │  │  ├─ text.py
│     │     │  │  │  ├─ theme.py
│     │     │  │  │  ├─ themes.py
│     │     │  │  │  ├─ traceback.py
│     │     │  │  │  ├─ tree.py
│     │     │  │  │  ├─ _cell_widths.py
│     │     │  │  │  ├─ _emoji_codes.py
│     │     │  │  │  ├─ _emoji_replace.py
│     │     │  │  │  ├─ _export_format.py
│     │     │  │  │  ├─ _extension.py
│     │     │  │  │  ├─ _fileno.py
│     │     │  │  │  ├─ _inspect.py
│     │     │  │  │  ├─ _log_render.py
│     │     │  │  │  ├─ _loop.py
│     │     │  │  │  ├─ _null_file.py
│     │     │  │  │  ├─ _palettes.py
│     │     │  │  │  ├─ _pick.py
│     │     │  │  │  ├─ _ratio.py
│     │     │  │  │  ├─ _spinners.py
│     │     │  │  │  ├─ _stack.py
│     │     │  │  │  ├─ _timer.py
│     │     │  │  │  ├─ _win32_console.py
│     │     │  │  │  ├─ _windows.py
│     │     │  │  │  ├─ _windows_renderer.py
│     │     │  │  │  ├─ _wrap.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  ├─ __main__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ abc.cpython-312.pyc
│     │     │  │  │     ├─ align.cpython-312.pyc
│     │     │  │  │     ├─ ansi.cpython-312.pyc
│     │     │  │  │     ├─ bar.cpython-312.pyc
│     │     │  │  │     ├─ box.cpython-312.pyc
│     │     │  │  │     ├─ cells.cpython-312.pyc
│     │     │  │  │     ├─ color.cpython-312.pyc
│     │     │  │  │     ├─ color_triplet.cpython-312.pyc
│     │     │  │  │     ├─ columns.cpython-312.pyc
│     │     │  │  │     ├─ console.cpython-312.pyc
│     │     │  │  │     ├─ constrain.cpython-312.pyc
│     │     │  │  │     ├─ containers.cpython-312.pyc
│     │     │  │  │     ├─ control.cpython-312.pyc
│     │     │  │  │     ├─ default_styles.cpython-312.pyc
│     │     │  │  │     ├─ diagnose.cpython-312.pyc
│     │     │  │  │     ├─ emoji.cpython-312.pyc
│     │     │  │  │     ├─ errors.cpython-312.pyc
│     │     │  │  │     ├─ filesize.cpython-312.pyc
│     │     │  │  │     ├─ file_proxy.cpython-312.pyc
│     │     │  │  │     ├─ highlighter.cpython-312.pyc
│     │     │  │  │     ├─ json.cpython-312.pyc
│     │     │  │  │     ├─ jupyter.cpython-312.pyc
│     │     │  │  │     ├─ layout.cpython-312.pyc
│     │     │  │  │     ├─ live.cpython-312.pyc
│     │     │  │  │     ├─ live_render.cpython-312.pyc
│     │     │  │  │     ├─ logging.cpython-312.pyc
│     │     │  │  │     ├─ markup.cpython-312.pyc
│     │     │  │  │     ├─ measure.cpython-312.pyc
│     │     │  │  │     ├─ padding.cpython-312.pyc
│     │     │  │  │     ├─ pager.cpython-312.pyc
│     │     │  │  │     ├─ palette.cpython-312.pyc
│     │     │  │  │     ├─ panel.cpython-312.pyc
│     │     │  │  │     ├─ pretty.cpython-312.pyc
│     │     │  │  │     ├─ progress.cpython-312.pyc
│     │     │  │  │     ├─ progress_bar.cpython-312.pyc
│     │     │  │  │     ├─ prompt.cpython-312.pyc
│     │     │  │  │     ├─ protocol.cpython-312.pyc
│     │     │  │  │     ├─ region.cpython-312.pyc
│     │     │  │  │     ├─ repr.cpython-312.pyc
│     │     │  │  │     ├─ rule.cpython-312.pyc
│     │     │  │  │     ├─ scope.cpython-312.pyc
│     │     │  │  │     ├─ screen.cpython-312.pyc
│     │     │  │  │     ├─ segment.cpython-312.pyc
│     │     │  │  │     ├─ spinner.cpython-312.pyc
│     │     │  │  │     ├─ status.cpython-312.pyc
│     │     │  │  │     ├─ style.cpython-312.pyc
│     │     │  │  │     ├─ styled.cpython-312.pyc
│     │     │  │  │     ├─ syntax.cpython-312.pyc
│     │     │  │  │     ├─ table.cpython-312.pyc
│     │     │  │  │     ├─ terminal_theme.cpython-312.pyc
│     │     │  │  │     ├─ text.cpython-312.pyc
│     │     │  │  │     ├─ theme.cpython-312.pyc
│     │     │  │  │     ├─ themes.cpython-312.pyc
│     │     │  │  │     ├─ traceback.cpython-312.pyc
│     │     │  │  │     ├─ tree.cpython-312.pyc
│     │     │  │  │     ├─ _cell_widths.cpython-312.pyc
│     │     │  │  │     ├─ _emoji_codes.cpython-312.pyc
│     │     │  │  │     ├─ _emoji_replace.cpython-312.pyc
│     │     │  │  │     ├─ _export_format.cpython-312.pyc
│     │     │  │  │     ├─ _extension.cpython-312.pyc
│     │     │  │  │     ├─ _fileno.cpython-312.pyc
│     │     │  │  │     ├─ _inspect.cpython-312.pyc
│     │     │  │  │     ├─ _log_render.cpython-312.pyc
│     │     │  │  │     ├─ _loop.cpython-312.pyc
│     │     │  │  │     ├─ _null_file.cpython-312.pyc
│     │     │  │  │     ├─ _palettes.cpython-312.pyc
│     │     │  │  │     ├─ _pick.cpython-312.pyc
│     │     │  │  │     ├─ _ratio.cpython-312.pyc
│     │     │  │  │     ├─ _spinners.cpython-312.pyc
│     │     │  │  │     ├─ _stack.cpython-312.pyc
│     │     │  │  │     ├─ _timer.cpython-312.pyc
│     │     │  │  │     ├─ _win32_console.cpython-312.pyc
│     │     │  │  │     ├─ _windows.cpython-312.pyc
│     │     │  │  │     ├─ _windows_renderer.cpython-312.pyc
│     │     │  │  │     ├─ _wrap.cpython-312.pyc
│     │     │  │  │     ├─ __init__.cpython-312.pyc
│     │     │  │  │     └─ __main__.cpython-312.pyc
│     │     │  │  ├─ tomli
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ _parser.py
│     │     │  │  │  ├─ _re.py
│     │     │  │  │  ├─ _types.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ _parser.cpython-312.pyc
│     │     │  │  │     ├─ _re.cpython-312.pyc
│     │     │  │  │     ├─ _types.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ truststore
│     │     │  │  │  ├─ py.typed
│     │     │  │  │  ├─ _api.py
│     │     │  │  │  ├─ _macos.py
│     │     │  │  │  ├─ _openssl.py
│     │     │  │  │  ├─ _ssl_constants.py
│     │     │  │  │  ├─ _windows.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ _api.cpython-312.pyc
│     │     │  │  │     ├─ _macos.cpython-312.pyc
│     │     │  │  │     ├─ _openssl.cpython-312.pyc
│     │     │  │  │     ├─ _ssl_constants.cpython-312.pyc
│     │     │  │  │     ├─ _windows.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ typing_extensions.py
│     │     │  │  ├─ urllib3
│     │     │  │  │  ├─ connection.py
│     │     │  │  │  ├─ connectionpool.py
│     │     │  │  │  ├─ contrib
│     │     │  │  │  │  ├─ appengine.py
│     │     │  │  │  │  ├─ ntlmpool.py
│     │     │  │  │  │  ├─ pyopenssl.py
│     │     │  │  │  │  ├─ securetransport.py
│     │     │  │  │  │  ├─ socks.py
│     │     │  │  │  │  ├─ _appengine_environ.py
│     │     │  │  │  │  ├─ _securetransport
│     │     │  │  │  │  │  ├─ bindings.py
│     │     │  │  │  │  │  ├─ low_level.py
│     │     │  │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  │  └─ __pycache__
│     │     │  │  │  │  │     ├─ bindings.cpython-312.pyc
│     │     │  │  │  │  │     ├─ low_level.cpython-312.pyc
│     │     │  │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ appengine.cpython-312.pyc
│     │     │  │  │  │     ├─ ntlmpool.cpython-312.pyc
│     │     │  │  │  │     ├─ pyopenssl.cpython-312.pyc
│     │     │  │  │  │     ├─ securetransport.cpython-312.pyc
│     │     │  │  │  │     ├─ socks.cpython-312.pyc
│     │     │  │  │  │     ├─ _appengine_environ.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ exceptions.py
│     │     │  │  │  ├─ fields.py
│     │     │  │  │  ├─ filepost.py
│     │     │  │  │  ├─ packages
│     │     │  │  │  │  ├─ backports
│     │     │  │  │  │  │  ├─ makefile.py
│     │     │  │  │  │  │  ├─ weakref_finalize.py
│     │     │  │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  │  └─ __pycache__
│     │     │  │  │  │  │     ├─ makefile.cpython-312.pyc
│     │     │  │  │  │  │     ├─ weakref_finalize.cpython-312.pyc
│     │     │  │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  │  ├─ six.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ six.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ poolmanager.py
│     │     │  │  │  ├─ request.py
│     │     │  │  │  ├─ response.py
│     │     │  │  │  ├─ util
│     │     │  │  │  │  ├─ connection.py
│     │     │  │  │  │  ├─ proxy.py
│     │     │  │  │  │  ├─ queue.py
│     │     │  │  │  │  ├─ request.py
│     │     │  │  │  │  ├─ response.py
│     │     │  │  │  │  ├─ retry.py
│     │     │  │  │  │  ├─ ssltransport.py
│     │     │  │  │  │  ├─ ssl_.py
│     │     │  │  │  │  ├─ ssl_match_hostname.py
│     │     │  │  │  │  ├─ timeout.py
│     │     │  │  │  │  ├─ url.py
│     │     │  │  │  │  ├─ wait.py
│     │     │  │  │  │  ├─ __init__.py
│     │     │  │  │  │  └─ __pycache__
│     │     │  │  │  │     ├─ connection.cpython-312.pyc
│     │     │  │  │  │     ├─ proxy.cpython-312.pyc
│     │     │  │  │  │     ├─ queue.cpython-312.pyc
│     │     │  │  │  │     ├─ request.cpython-312.pyc
│     │     │  │  │  │     ├─ response.cpython-312.pyc
│     │     │  │  │  │     ├─ retry.cpython-312.pyc
│     │     │  │  │  │     ├─ ssltransport.cpython-312.pyc
│     │     │  │  │  │     ├─ ssl_.cpython-312.pyc
│     │     │  │  │  │     ├─ ssl_match_hostname.cpython-312.pyc
│     │     │  │  │  │     ├─ timeout.cpython-312.pyc
│     │     │  │  │  │     ├─ url.cpython-312.pyc
│     │     │  │  │  │     ├─ wait.cpython-312.pyc
│     │     │  │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  │  ├─ _collections.py
│     │     │  │  │  ├─ _version.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ connection.cpython-312.pyc
│     │     │  │  │     ├─ connectionpool.cpython-312.pyc
│     │     │  │  │     ├─ exceptions.cpython-312.pyc
│     │     │  │  │     ├─ fields.cpython-312.pyc
│     │     │  │  │     ├─ filepost.cpython-312.pyc
│     │     │  │  │     ├─ poolmanager.cpython-312.pyc
│     │     │  │  │     ├─ request.cpython-312.pyc
│     │     │  │  │     ├─ response.cpython-312.pyc
│     │     │  │  │     ├─ _collections.cpython-312.pyc
│     │     │  │  │     ├─ _version.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ vendor.txt
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ typing_extensions.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ __init__.py
│     │     │  ├─ __main__.py
│     │     │  ├─ __pip-runner__.py
│     │     │  └─ __pycache__
│     │     │     ├─ __init__.cpython-312.pyc
│     │     │     ├─ __main__.cpython-312.pyc
│     │     │     └─ __pip-runner__.cpython-312.pyc
│     │     ├─ pip-25.0.1.dist-info
│     │     │  ├─ AUTHORS.txt
│     │     │  ├─ entry_points.txt
│     │     │  ├─ INSTALLER
│     │     │  ├─ LICENSE.txt
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ pydantic
│     │     │  ├─ aliases.py
│     │     │  ├─ alias_generators.py
│     │     │  ├─ annotated_handlers.py
│     │     │  ├─ class_validators.py
│     │     │  ├─ color.py
│     │     │  ├─ config.py
│     │     │  ├─ dataclasses.py
│     │     │  ├─ datetime_parse.py
│     │     │  ├─ decorator.py
│     │     │  ├─ deprecated
│     │     │  │  ├─ class_validators.py
│     │     │  │  ├─ config.py
│     │     │  │  ├─ copy_internals.py
│     │     │  │  ├─ decorator.py
│     │     │  │  ├─ json.py
│     │     │  │  ├─ parse.py
│     │     │  │  ├─ tools.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ class_validators.cpython-312.pyc
│     │     │  │     ├─ config.cpython-312.pyc
│     │     │  │     ├─ copy_internals.cpython-312.pyc
│     │     │  │     ├─ decorator.cpython-312.pyc
│     │     │  │     ├─ json.cpython-312.pyc
│     │     │  │     ├─ parse.cpython-312.pyc
│     │     │  │     ├─ tools.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ env_settings.py
│     │     │  ├─ errors.py
│     │     │  ├─ error_wrappers.py
│     │     │  ├─ experimental
│     │     │  │  ├─ arguments_schema.py
│     │     │  │  ├─ pipeline.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ arguments_schema.cpython-312.pyc
│     │     │  │     ├─ pipeline.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ fields.py
│     │     │  ├─ functional_serializers.py
│     │     │  ├─ functional_validators.py
│     │     │  ├─ generics.py
│     │     │  ├─ json.py
│     │     │  ├─ json_schema.py
│     │     │  ├─ main.py
│     │     │  ├─ mypy.py
│     │     │  ├─ networks.py
│     │     │  ├─ parse.py
│     │     │  ├─ plugin
│     │     │  │  ├─ _loader.py
│     │     │  │  ├─ _schema_validator.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ _loader.cpython-312.pyc
│     │     │  │     ├─ _schema_validator.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ py.typed
│     │     │  ├─ root_model.py
│     │     │  ├─ schema.py
│     │     │  ├─ tools.py
│     │     │  ├─ types.py
│     │     │  ├─ type_adapter.py
│     │     │  ├─ typing.py
│     │     │  ├─ utils.py
│     │     │  ├─ v1
│     │     │  │  ├─ annotated_types.py
│     │     │  │  ├─ class_validators.py
│     │     │  │  ├─ color.py
│     │     │  │  ├─ config.py
│     │     │  │  ├─ dataclasses.py
│     │     │  │  ├─ datetime_parse.py
│     │     │  │  ├─ decorator.py
│     │     │  │  ├─ env_settings.py
│     │     │  │  ├─ errors.py
│     │     │  │  ├─ error_wrappers.py
│     │     │  │  ├─ fields.py
│     │     │  │  ├─ generics.py
│     │     │  │  ├─ json.py
│     │     │  │  ├─ main.py
│     │     │  │  ├─ mypy.py
│     │     │  │  ├─ networks.py
│     │     │  │  ├─ parse.py
│     │     │  │  ├─ py.typed
│     │     │  │  ├─ schema.py
│     │     │  │  ├─ tools.py
│     │     │  │  ├─ types.py
│     │     │  │  ├─ typing.py
│     │     │  │  ├─ utils.py
│     │     │  │  ├─ validators.py
│     │     │  │  ├─ version.py
│     │     │  │  ├─ _hypothesis_plugin.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ annotated_types.cpython-312.pyc
│     │     │  │     ├─ class_validators.cpython-312.pyc
│     │     │  │     ├─ color.cpython-312.pyc
│     │     │  │     ├─ config.cpython-312.pyc
│     │     │  │     ├─ dataclasses.cpython-312.pyc
│     │     │  │     ├─ datetime_parse.cpython-312.pyc
│     │     │  │     ├─ decorator.cpython-312.pyc
│     │     │  │     ├─ env_settings.cpython-312.pyc
│     │     │  │     ├─ errors.cpython-312.pyc
│     │     │  │     ├─ error_wrappers.cpython-312.pyc
│     │     │  │     ├─ fields.cpython-312.pyc
│     │     │  │     ├─ generics.cpython-312.pyc
│     │     │  │     ├─ json.cpython-312.pyc
│     │     │  │     ├─ main.cpython-312.pyc
│     │     │  │     ├─ mypy.cpython-312.pyc
│     │     │  │     ├─ networks.cpython-312.pyc
│     │     │  │     ├─ parse.cpython-312.pyc
│     │     │  │     ├─ schema.cpython-312.pyc
│     │     │  │     ├─ tools.cpython-312.pyc
│     │     │  │     ├─ types.cpython-312.pyc
│     │     │  │     ├─ typing.cpython-312.pyc
│     │     │  │     ├─ utils.cpython-312.pyc
│     │     │  │     ├─ validators.cpython-312.pyc
│     │     │  │     ├─ version.cpython-312.pyc
│     │     │  │     ├─ _hypothesis_plugin.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ validate_call_decorator.py
│     │     │  ├─ validators.py
│     │     │  ├─ version.py
│     │     │  ├─ warnings.py
│     │     │  ├─ _internal
│     │     │  │  ├─ _config.py
│     │     │  │  ├─ _core_metadata.py
│     │     │  │  ├─ _core_utils.py
│     │     │  │  ├─ _dataclasses.py
│     │     │  │  ├─ _decorators.py
│     │     │  │  ├─ _decorators_v1.py
│     │     │  │  ├─ _discriminated_union.py
│     │     │  │  ├─ _docs_extraction.py
│     │     │  │  ├─ _fields.py
│     │     │  │  ├─ _forward_ref.py
│     │     │  │  ├─ _generate_schema.py
│     │     │  │  ├─ _generics.py
│     │     │  │  ├─ _git.py
│     │     │  │  ├─ _import_utils.py
│     │     │  │  ├─ _internal_dataclass.py
│     │     │  │  ├─ _known_annotated_metadata.py
│     │     │  │  ├─ _mock_val_ser.py
│     │     │  │  ├─ _model_construction.py
│     │     │  │  ├─ _namespace_utils.py
│     │     │  │  ├─ _repr.py
│     │     │  │  ├─ _schema_gather.py
│     │     │  │  ├─ _schema_generation_shared.py
│     │     │  │  ├─ _serializers.py
│     │     │  │  ├─ _signature.py
│     │     │  │  ├─ _typing_extra.py
│     │     │  │  ├─ _utils.py
│     │     │  │  ├─ _validate_call.py
│     │     │  │  ├─ _validators.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ _config.cpython-312.pyc
│     │     │  │     ├─ _core_metadata.cpython-312.pyc
│     │     │  │     ├─ _core_utils.cpython-312.pyc
│     │     │  │     ├─ _dataclasses.cpython-312.pyc
│     │     │  │     ├─ _decorators.cpython-312.pyc
│     │     │  │     ├─ _decorators_v1.cpython-312.pyc
│     │     │  │     ├─ _discriminated_union.cpython-312.pyc
│     │     │  │     ├─ _docs_extraction.cpython-312.pyc
│     │     │  │     ├─ _fields.cpython-312.pyc
│     │     │  │     ├─ _forward_ref.cpython-312.pyc
│     │     │  │     ├─ _generate_schema.cpython-312.pyc
│     │     │  │     ├─ _generics.cpython-312.pyc
│     │     │  │     ├─ _git.cpython-312.pyc
│     │     │  │     ├─ _import_utils.cpython-312.pyc
│     │     │  │     ├─ _internal_dataclass.cpython-312.pyc
│     │     │  │     ├─ _known_annotated_metadata.cpython-312.pyc
│     │     │  │     ├─ _mock_val_ser.cpython-312.pyc
│     │     │  │     ├─ _model_construction.cpython-312.pyc
│     │     │  │     ├─ _namespace_utils.cpython-312.pyc
│     │     │  │     ├─ _repr.cpython-312.pyc
│     │     │  │     ├─ _schema_gather.cpython-312.pyc
│     │     │  │     ├─ _schema_generation_shared.cpython-312.pyc
│     │     │  │     ├─ _serializers.cpython-312.pyc
│     │     │  │     ├─ _signature.cpython-312.pyc
│     │     │  │     ├─ _typing_extra.cpython-312.pyc
│     │     │  │     ├─ _utils.cpython-312.pyc
│     │     │  │     ├─ _validate_call.cpython-312.pyc
│     │     │  │     ├─ _validators.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _migration.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ aliases.cpython-312.pyc
│     │     │     ├─ alias_generators.cpython-312.pyc
│     │     │     ├─ annotated_handlers.cpython-312.pyc
│     │     │     ├─ class_validators.cpython-312.pyc
│     │     │     ├─ color.cpython-312.pyc
│     │     │     ├─ config.cpython-312.pyc
│     │     │     ├─ dataclasses.cpython-312.pyc
│     │     │     ├─ datetime_parse.cpython-312.pyc
│     │     │     ├─ decorator.cpython-312.pyc
│     │     │     ├─ env_settings.cpython-312.pyc
│     │     │     ├─ errors.cpython-312.pyc
│     │     │     ├─ error_wrappers.cpython-312.pyc
│     │     │     ├─ fields.cpython-312.pyc
│     │     │     ├─ functional_serializers.cpython-312.pyc
│     │     │     ├─ functional_validators.cpython-312.pyc
│     │     │     ├─ generics.cpython-312.pyc
│     │     │     ├─ json.cpython-312.pyc
│     │     │     ├─ json_schema.cpython-312.pyc
│     │     │     ├─ main.cpython-312.pyc
│     │     │     ├─ mypy.cpython-312.pyc
│     │     │     ├─ networks.cpython-312.pyc
│     │     │     ├─ parse.cpython-312.pyc
│     │     │     ├─ root_model.cpython-312.pyc
│     │     │     ├─ schema.cpython-312.pyc
│     │     │     ├─ tools.cpython-312.pyc
│     │     │     ├─ types.cpython-312.pyc
│     │     │     ├─ type_adapter.cpython-312.pyc
│     │     │     ├─ typing.cpython-312.pyc
│     │     │     ├─ utils.cpython-312.pyc
│     │     │     ├─ validate_call_decorator.cpython-312.pyc
│     │     │     ├─ validators.cpython-312.pyc
│     │     │     ├─ version.cpython-312.pyc
│     │     │     ├─ warnings.cpython-312.pyc
│     │     │     ├─ _migration.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ pydantic-2.11.7.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ pydantic_core
│     │     │  ├─ core_schema.py
│     │     │  ├─ py.typed
│     │     │  ├─ _pydantic_core.cp312-win_amd64.pyd
│     │     │  ├─ _pydantic_core.pyi
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ core_schema.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ pydantic_core-2.33.2.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ python_multipart
│     │     │  ├─ decoders.py
│     │     │  ├─ exceptions.py
│     │     │  ├─ multipart.py
│     │     │  ├─ py.typed
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ decoders.cpython-312.pyc
│     │     │     ├─ exceptions.cpython-312.pyc
│     │     │     ├─ multipart.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ python_multipart-0.0.20.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE.txt
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ sniffio
│     │     │  ├─ py.typed
│     │     │  ├─ _impl.py
│     │     │  ├─ _tests
│     │     │  │  ├─ test_sniffio.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ test_sniffio.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ _version.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ _impl.cpython-312.pyc
│     │     │     ├─ _version.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ sniffio-1.3.1.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ LICENSE
│     │     │  ├─ LICENSE.APACHE2
│     │     │  ├─ LICENSE.MIT
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ sqlalchemy
│     │     │  ├─ connectors
│     │     │  │  ├─ aioodbc.py
│     │     │  │  ├─ asyncio.py
│     │     │  │  ├─ pyodbc.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ aioodbc.cpython-312.pyc
│     │     │  │     ├─ asyncio.cpython-312.pyc
│     │     │  │     ├─ pyodbc.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ cyextension
│     │     │  │  ├─ collections.cp312-win_amd64.pyd
│     │     │  │  ├─ collections.pyx
│     │     │  │  ├─ immutabledict.cp312-win_amd64.pyd
│     │     │  │  ├─ immutabledict.pxd
│     │     │  │  ├─ immutabledict.pyx
│     │     │  │  ├─ processors.cp312-win_amd64.pyd
│     │     │  │  ├─ processors.pyx
│     │     │  │  ├─ resultproxy.cp312-win_amd64.pyd
│     │     │  │  ├─ resultproxy.pyx
│     │     │  │  ├─ util.cp312-win_amd64.pyd
│     │     │  │  ├─ util.pyx
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ dialects
│     │     │  │  ├─ mssql
│     │     │  │  │  ├─ aioodbc.py
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ information_schema.py
│     │     │  │  │  ├─ json.py
│     │     │  │  │  ├─ provision.py
│     │     │  │  │  ├─ pymssql.py
│     │     │  │  │  ├─ pyodbc.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ aioodbc.cpython-312.pyc
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ information_schema.cpython-312.pyc
│     │     │  │  │     ├─ json.cpython-312.pyc
│     │     │  │  │     ├─ provision.cpython-312.pyc
│     │     │  │  │     ├─ pymssql.cpython-312.pyc
│     │     │  │  │     ├─ pyodbc.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ mysql
│     │     │  │  │  ├─ aiomysql.py
│     │     │  │  │  ├─ asyncmy.py
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ cymysql.py
│     │     │  │  │  ├─ dml.py
│     │     │  │  │  ├─ enumerated.py
│     │     │  │  │  ├─ expression.py
│     │     │  │  │  ├─ json.py
│     │     │  │  │  ├─ mariadb.py
│     │     │  │  │  ├─ mariadbconnector.py
│     │     │  │  │  ├─ mysqlconnector.py
│     │     │  │  │  ├─ mysqldb.py
│     │     │  │  │  ├─ provision.py
│     │     │  │  │  ├─ pymysql.py
│     │     │  │  │  ├─ pyodbc.py
│     │     │  │  │  ├─ reflection.py
│     │     │  │  │  ├─ reserved_words.py
│     │     │  │  │  ├─ types.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ aiomysql.cpython-312.pyc
│     │     │  │  │     ├─ asyncmy.cpython-312.pyc
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ cymysql.cpython-312.pyc
│     │     │  │  │     ├─ dml.cpython-312.pyc
│     │     │  │  │     ├─ enumerated.cpython-312.pyc
│     │     │  │  │     ├─ expression.cpython-312.pyc
│     │     │  │  │     ├─ json.cpython-312.pyc
│     │     │  │  │     ├─ mariadb.cpython-312.pyc
│     │     │  │  │     ├─ mariadbconnector.cpython-312.pyc
│     │     │  │  │     ├─ mysqlconnector.cpython-312.pyc
│     │     │  │  │     ├─ mysqldb.cpython-312.pyc
│     │     │  │  │     ├─ provision.cpython-312.pyc
│     │     │  │  │     ├─ pymysql.cpython-312.pyc
│     │     │  │  │     ├─ pyodbc.cpython-312.pyc
│     │     │  │  │     ├─ reflection.cpython-312.pyc
│     │     │  │  │     ├─ reserved_words.cpython-312.pyc
│     │     │  │  │     ├─ types.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ oracle
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ cx_oracle.py
│     │     │  │  │  ├─ dictionary.py
│     │     │  │  │  ├─ oracledb.py
│     │     │  │  │  ├─ provision.py
│     │     │  │  │  ├─ types.py
│     │     │  │  │  ├─ vector.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ cx_oracle.cpython-312.pyc
│     │     │  │  │     ├─ dictionary.cpython-312.pyc
│     │     │  │  │     ├─ oracledb.cpython-312.pyc
│     │     │  │  │     ├─ provision.cpython-312.pyc
│     │     │  │  │     ├─ types.cpython-312.pyc
│     │     │  │  │     ├─ vector.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ postgresql
│     │     │  │  │  ├─ array.py
│     │     │  │  │  ├─ asyncpg.py
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ dml.py
│     │     │  │  │  ├─ ext.py
│     │     │  │  │  ├─ hstore.py
│     │     │  │  │  ├─ json.py
│     │     │  │  │  ├─ named_types.py
│     │     │  │  │  ├─ operators.py
│     │     │  │  │  ├─ pg8000.py
│     │     │  │  │  ├─ pg_catalog.py
│     │     │  │  │  ├─ provision.py
│     │     │  │  │  ├─ psycopg.py
│     │     │  │  │  ├─ psycopg2.py
│     │     │  │  │  ├─ psycopg2cffi.py
│     │     │  │  │  ├─ ranges.py
│     │     │  │  │  ├─ types.py
│     │     │  │  │  ├─ _psycopg_common.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ array.cpython-312.pyc
│     │     │  │  │     ├─ asyncpg.cpython-312.pyc
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ dml.cpython-312.pyc
│     │     │  │  │     ├─ ext.cpython-312.pyc
│     │     │  │  │     ├─ hstore.cpython-312.pyc
│     │     │  │  │     ├─ json.cpython-312.pyc
│     │     │  │  │     ├─ named_types.cpython-312.pyc
│     │     │  │  │     ├─ operators.cpython-312.pyc
│     │     │  │  │     ├─ pg8000.cpython-312.pyc
│     │     │  │  │     ├─ pg_catalog.cpython-312.pyc
│     │     │  │  │     ├─ provision.cpython-312.pyc
│     │     │  │  │     ├─ psycopg.cpython-312.pyc
│     │     │  │  │     ├─ psycopg2.cpython-312.pyc
│     │     │  │  │     ├─ psycopg2cffi.cpython-312.pyc
│     │     │  │  │     ├─ ranges.cpython-312.pyc
│     │     │  │  │     ├─ types.cpython-312.pyc
│     │     │  │  │     ├─ _psycopg_common.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ sqlite
│     │     │  │  │  ├─ aiosqlite.py
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ dml.py
│     │     │  │  │  ├─ json.py
│     │     │  │  │  ├─ provision.py
│     │     │  │  │  ├─ pysqlcipher.py
│     │     │  │  │  ├─ pysqlite.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ aiosqlite.cpython-312.pyc
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ dml.cpython-312.pyc
│     │     │  │  │     ├─ json.cpython-312.pyc
│     │     │  │  │     ├─ provision.cpython-312.pyc
│     │     │  │  │     ├─ pysqlcipher.cpython-312.pyc
│     │     │  │  │     ├─ pysqlite.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ type_migration_guidelines.txt
│     │     │  │  ├─ _typing.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ _typing.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ engine
│     │     │  │  ├─ base.py
│     │     │  │  ├─ characteristics.py
│     │     │  │  ├─ create.py
│     │     │  │  ├─ cursor.py
│     │     │  │  ├─ default.py
│     │     │  │  ├─ events.py
│     │     │  │  ├─ interfaces.py
│     │     │  │  ├─ mock.py
│     │     │  │  ├─ processors.py
│     │     │  │  ├─ reflection.py
│     │     │  │  ├─ result.py
│     │     │  │  ├─ row.py
│     │     │  │  ├─ strategies.py
│     │     │  │  ├─ url.py
│     │     │  │  ├─ util.py
│     │     │  │  ├─ _py_processors.py
│     │     │  │  ├─ _py_row.py
│     │     │  │  ├─ _py_util.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ characteristics.cpython-312.pyc
│     │     │  │     ├─ create.cpython-312.pyc
│     │     │  │     ├─ cursor.cpython-312.pyc
│     │     │  │     ├─ default.cpython-312.pyc
│     │     │  │     ├─ events.cpython-312.pyc
│     │     │  │     ├─ interfaces.cpython-312.pyc
│     │     │  │     ├─ mock.cpython-312.pyc
│     │     │  │     ├─ processors.cpython-312.pyc
│     │     │  │     ├─ reflection.cpython-312.pyc
│     │     │  │     ├─ result.cpython-312.pyc
│     │     │  │     ├─ row.cpython-312.pyc
│     │     │  │     ├─ strategies.cpython-312.pyc
│     │     │  │     ├─ url.cpython-312.pyc
│     │     │  │     ├─ util.cpython-312.pyc
│     │     │  │     ├─ _py_processors.cpython-312.pyc
│     │     │  │     ├─ _py_row.cpython-312.pyc
│     │     │  │     ├─ _py_util.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ event
│     │     │  │  ├─ api.py
│     │     │  │  ├─ attr.py
│     │     │  │  ├─ base.py
│     │     │  │  ├─ legacy.py
│     │     │  │  ├─ registry.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ api.cpython-312.pyc
│     │     │  │     ├─ attr.cpython-312.pyc
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ legacy.cpython-312.pyc
│     │     │  │     ├─ registry.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ events.py
│     │     │  ├─ exc.py
│     │     │  ├─ ext
│     │     │  │  ├─ associationproxy.py
│     │     │  │  ├─ asyncio
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ engine.py
│     │     │  │  │  ├─ exc.py
│     │     │  │  │  ├─ result.py
│     │     │  │  │  ├─ scoping.py
│     │     │  │  │  ├─ session.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ engine.cpython-312.pyc
│     │     │  │  │     ├─ exc.cpython-312.pyc
│     │     │  │  │     ├─ result.cpython-312.pyc
│     │     │  │  │     ├─ scoping.cpython-312.pyc
│     │     │  │  │     ├─ session.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ automap.py
│     │     │  │  ├─ baked.py
│     │     │  │  ├─ compiler.py
│     │     │  │  ├─ declarative
│     │     │  │  │  ├─ extensions.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ extensions.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ horizontal_shard.py
│     │     │  │  ├─ hybrid.py
│     │     │  │  ├─ indexable.py
│     │     │  │  ├─ instrumentation.py
│     │     │  │  ├─ mutable.py
│     │     │  │  ├─ mypy
│     │     │  │  │  ├─ apply.py
│     │     │  │  │  ├─ decl_class.py
│     │     │  │  │  ├─ infer.py
│     │     │  │  │  ├─ names.py
│     │     │  │  │  ├─ plugin.py
│     │     │  │  │  ├─ util.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ apply.cpython-312.pyc
│     │     │  │  │     ├─ decl_class.cpython-312.pyc
│     │     │  │  │     ├─ infer.cpython-312.pyc
│     │     │  │  │     ├─ names.cpython-312.pyc
│     │     │  │  │     ├─ plugin.cpython-312.pyc
│     │     │  │  │     ├─ util.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ orderinglist.py
│     │     │  │  ├─ serializer.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ associationproxy.cpython-312.pyc
│     │     │  │     ├─ automap.cpython-312.pyc
│     │     │  │     ├─ baked.cpython-312.pyc
│     │     │  │     ├─ compiler.cpython-312.pyc
│     │     │  │     ├─ horizontal_shard.cpython-312.pyc
│     │     │  │     ├─ hybrid.cpython-312.pyc
│     │     │  │     ├─ indexable.cpython-312.pyc
│     │     │  │     ├─ instrumentation.cpython-312.pyc
│     │     │  │     ├─ mutable.cpython-312.pyc
│     │     │  │     ├─ orderinglist.cpython-312.pyc
│     │     │  │     ├─ serializer.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ future
│     │     │  │  ├─ engine.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ engine.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ inspection.py
│     │     │  ├─ log.py
│     │     │  ├─ orm
│     │     │  │  ├─ attributes.py
│     │     │  │  ├─ base.py
│     │     │  │  ├─ bulk_persistence.py
│     │     │  │  ├─ clsregistry.py
│     │     │  │  ├─ collections.py
│     │     │  │  ├─ context.py
│     │     │  │  ├─ decl_api.py
│     │     │  │  ├─ decl_base.py
│     │     │  │  ├─ dependency.py
│     │     │  │  ├─ descriptor_props.py
│     │     │  │  ├─ dynamic.py
│     │     │  │  ├─ evaluator.py
│     │     │  │  ├─ events.py
│     │     │  │  ├─ exc.py
│     │     │  │  ├─ identity.py
│     │     │  │  ├─ instrumentation.py
│     │     │  │  ├─ interfaces.py
│     │     │  │  ├─ loading.py
│     │     │  │  ├─ mapped_collection.py
│     │     │  │  ├─ mapper.py
│     │     │  │  ├─ path_registry.py
│     │     │  │  ├─ persistence.py
│     │     │  │  ├─ properties.py
│     │     │  │  ├─ query.py
│     │     │  │  ├─ relationships.py
│     │     │  │  ├─ scoping.py
│     │     │  │  ├─ session.py
│     │     │  │  ├─ state.py
│     │     │  │  ├─ state_changes.py
│     │     │  │  ├─ strategies.py
│     │     │  │  ├─ strategy_options.py
│     │     │  │  ├─ sync.py
│     │     │  │  ├─ unitofwork.py
│     │     │  │  ├─ util.py
│     │     │  │  ├─ writeonly.py
│     │     │  │  ├─ _orm_constructors.py
│     │     │  │  ├─ _typing.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ attributes.cpython-312.pyc
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ bulk_persistence.cpython-312.pyc
│     │     │  │     ├─ clsregistry.cpython-312.pyc
│     │     │  │     ├─ collections.cpython-312.pyc
│     │     │  │     ├─ context.cpython-312.pyc
│     │     │  │     ├─ decl_api.cpython-312.pyc
│     │     │  │     ├─ decl_base.cpython-312.pyc
│     │     │  │     ├─ dependency.cpython-312.pyc
│     │     │  │     ├─ descriptor_props.cpython-312.pyc
│     │     │  │     ├─ dynamic.cpython-312.pyc
│     │     │  │     ├─ evaluator.cpython-312.pyc
│     │     │  │     ├─ events.cpython-312.pyc
│     │     │  │     ├─ exc.cpython-312.pyc
│     │     │  │     ├─ identity.cpython-312.pyc
│     │     │  │     ├─ instrumentation.cpython-312.pyc
│     │     │  │     ├─ interfaces.cpython-312.pyc
│     │     │  │     ├─ loading.cpython-312.pyc
│     │     │  │     ├─ mapped_collection.cpython-312.pyc
│     │     │  │     ├─ mapper.cpython-312.pyc
│     │     │  │     ├─ path_registry.cpython-312.pyc
│     │     │  │     ├─ persistence.cpython-312.pyc
│     │     │  │     ├─ properties.cpython-312.pyc
│     │     │  │     ├─ query.cpython-312.pyc
│     │     │  │     ├─ relationships.cpython-312.pyc
│     │     │  │     ├─ scoping.cpython-312.pyc
│     │     │  │     ├─ session.cpython-312.pyc
│     │     │  │     ├─ state.cpython-312.pyc
│     │     │  │     ├─ state_changes.cpython-312.pyc
│     │     │  │     ├─ strategies.cpython-312.pyc
│     │     │  │     ├─ strategy_options.cpython-312.pyc
│     │     │  │     ├─ sync.cpython-312.pyc
│     │     │  │     ├─ unitofwork.cpython-312.pyc
│     │     │  │     ├─ util.cpython-312.pyc
│     │     │  │     ├─ writeonly.cpython-312.pyc
│     │     │  │     ├─ _orm_constructors.cpython-312.pyc
│     │     │  │     ├─ _typing.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ pool
│     │     │  │  ├─ base.py
│     │     │  │  ├─ events.py
│     │     │  │  ├─ impl.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ events.cpython-312.pyc
│     │     │  │     ├─ impl.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ py.typed
│     │     │  ├─ schema.py
│     │     │  ├─ sql
│     │     │  │  ├─ annotation.py
│     │     │  │  ├─ base.py
│     │     │  │  ├─ cache_key.py
│     │     │  │  ├─ coercions.py
│     │     │  │  ├─ compiler.py
│     │     │  │  ├─ crud.py
│     │     │  │  ├─ ddl.py
│     │     │  │  ├─ default_comparator.py
│     │     │  │  ├─ dml.py
│     │     │  │  ├─ elements.py
│     │     │  │  ├─ events.py
│     │     │  │  ├─ expression.py
│     │     │  │  ├─ functions.py
│     │     │  │  ├─ lambdas.py
│     │     │  │  ├─ naming.py
│     │     │  │  ├─ operators.py
│     │     │  │  ├─ roles.py
│     │     │  │  ├─ schema.py
│     │     │  │  ├─ selectable.py
│     │     │  │  ├─ sqltypes.py
│     │     │  │  ├─ traversals.py
│     │     │  │  ├─ type_api.py
│     │     │  │  ├─ util.py
│     │     │  │  ├─ visitors.py
│     │     │  │  ├─ _dml_constructors.py
│     │     │  │  ├─ _elements_constructors.py
│     │     │  │  ├─ _orm_types.py
│     │     │  │  ├─ _py_util.py
│     │     │  │  ├─ _selectable_constructors.py
│     │     │  │  ├─ _typing.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ annotation.cpython-312.pyc
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ cache_key.cpython-312.pyc
│     │     │  │     ├─ coercions.cpython-312.pyc
│     │     │  │     ├─ compiler.cpython-312.pyc
│     │     │  │     ├─ crud.cpython-312.pyc
│     │     │  │     ├─ ddl.cpython-312.pyc
│     │     │  │     ├─ default_comparator.cpython-312.pyc
│     │     │  │     ├─ dml.cpython-312.pyc
│     │     │  │     ├─ elements.cpython-312.pyc
│     │     │  │     ├─ events.cpython-312.pyc
│     │     │  │     ├─ expression.cpython-312.pyc
│     │     │  │     ├─ functions.cpython-312.pyc
│     │     │  │     ├─ lambdas.cpython-312.pyc
│     │     │  │     ├─ naming.cpython-312.pyc
│     │     │  │     ├─ operators.cpython-312.pyc
│     │     │  │     ├─ roles.cpython-312.pyc
│     │     │  │     ├─ schema.cpython-312.pyc
│     │     │  │     ├─ selectable.cpython-312.pyc
│     │     │  │     ├─ sqltypes.cpython-312.pyc
│     │     │  │     ├─ traversals.cpython-312.pyc
│     │     │  │     ├─ type_api.cpython-312.pyc
│     │     │  │     ├─ util.cpython-312.pyc
│     │     │  │     ├─ visitors.cpython-312.pyc
│     │     │  │     ├─ _dml_constructors.cpython-312.pyc
│     │     │  │     ├─ _elements_constructors.cpython-312.pyc
│     │     │  │     ├─ _orm_types.cpython-312.pyc
│     │     │  │     ├─ _py_util.cpython-312.pyc
│     │     │  │     ├─ _selectable_constructors.cpython-312.pyc
│     │     │  │     ├─ _typing.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ testing
│     │     │  │  ├─ assertions.py
│     │     │  │  ├─ assertsql.py
│     │     │  │  ├─ asyncio.py
│     │     │  │  ├─ config.py
│     │     │  │  ├─ engines.py
│     │     │  │  ├─ entities.py
│     │     │  │  ├─ exclusions.py
│     │     │  │  ├─ fixtures
│     │     │  │  │  ├─ base.py
│     │     │  │  │  ├─ mypy.py
│     │     │  │  │  ├─ orm.py
│     │     │  │  │  ├─ sql.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ base.cpython-312.pyc
│     │     │  │  │     ├─ mypy.cpython-312.pyc
│     │     │  │  │     ├─ orm.cpython-312.pyc
│     │     │  │  │     ├─ sql.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ pickleable.py
│     │     │  │  ├─ plugin
│     │     │  │  │  ├─ bootstrap.py
│     │     │  │  │  ├─ plugin_base.py
│     │     │  │  │  ├─ pytestplugin.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ bootstrap.cpython-312.pyc
│     │     │  │  │     ├─ plugin_base.cpython-312.pyc
│     │     │  │  │     ├─ pytestplugin.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ profiling.py
│     │     │  │  ├─ provision.py
│     │     │  │  ├─ requirements.py
│     │     │  │  ├─ schema.py
│     │     │  │  ├─ suite
│     │     │  │  │  ├─ test_cte.py
│     │     │  │  │  ├─ test_ddl.py
│     │     │  │  │  ├─ test_deprecations.py
│     │     │  │  │  ├─ test_dialect.py
│     │     │  │  │  ├─ test_insert.py
│     │     │  │  │  ├─ test_reflection.py
│     │     │  │  │  ├─ test_results.py
│     │     │  │  │  ├─ test_rowcount.py
│     │     │  │  │  ├─ test_select.py
│     │     │  │  │  ├─ test_sequence.py
│     │     │  │  │  ├─ test_types.py
│     │     │  │  │  ├─ test_unicode_ddl.py
│     │     │  │  │  ├─ test_update_delete.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ test_cte.cpython-312.pyc
│     │     │  │  │     ├─ test_ddl.cpython-312.pyc
│     │     │  │  │     ├─ test_deprecations.cpython-312.pyc
│     │     │  │  │     ├─ test_dialect.cpython-312.pyc
│     │     │  │  │     ├─ test_insert.cpython-312.pyc
│     │     │  │  │     ├─ test_reflection.cpython-312.pyc
│     │     │  │  │     ├─ test_results.cpython-312.pyc
│     │     │  │  │     ├─ test_rowcount.cpython-312.pyc
│     │     │  │  │     ├─ test_select.cpython-312.pyc
│     │     │  │  │     ├─ test_sequence.cpython-312.pyc
│     │     │  │  │     ├─ test_types.cpython-312.pyc
│     │     │  │  │     ├─ test_unicode_ddl.cpython-312.pyc
│     │     │  │  │     ├─ test_update_delete.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ util.py
│     │     │  │  ├─ warnings.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ assertions.cpython-312.pyc
│     │     │  │     ├─ assertsql.cpython-312.pyc
│     │     │  │     ├─ asyncio.cpython-312.pyc
│     │     │  │     ├─ config.cpython-312.pyc
│     │     │  │     ├─ engines.cpython-312.pyc
│     │     │  │     ├─ entities.cpython-312.pyc
│     │     │  │     ├─ exclusions.cpython-312.pyc
│     │     │  │     ├─ pickleable.cpython-312.pyc
│     │     │  │     ├─ profiling.cpython-312.pyc
│     │     │  │     ├─ provision.cpython-312.pyc
│     │     │  │     ├─ requirements.cpython-312.pyc
│     │     │  │     ├─ schema.cpython-312.pyc
│     │     │  │     ├─ util.cpython-312.pyc
│     │     │  │     ├─ warnings.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ types.py
│     │     │  ├─ util
│     │     │  │  ├─ compat.py
│     │     │  │  ├─ concurrency.py
│     │     │  │  ├─ deprecations.py
│     │     │  │  ├─ langhelpers.py
│     │     │  │  ├─ preloaded.py
│     │     │  │  ├─ queue.py
│     │     │  │  ├─ tool_support.py
│     │     │  │  ├─ topological.py
│     │     │  │  ├─ typing.py
│     │     │  │  ├─ _collections.py
│     │     │  │  ├─ _concurrency_py3k.py
│     │     │  │  ├─ _has_cy.py
│     │     │  │  ├─ _py_collections.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ compat.cpython-312.pyc
│     │     │  │     ├─ concurrency.cpython-312.pyc
│     │     │  │     ├─ deprecations.cpython-312.pyc
│     │     │  │     ├─ langhelpers.cpython-312.pyc
│     │     │  │     ├─ preloaded.cpython-312.pyc
│     │     │  │     ├─ queue.cpython-312.pyc
│     │     │  │     ├─ tool_support.cpython-312.pyc
│     │     │  │     ├─ topological.cpython-312.pyc
│     │     │  │     ├─ typing.cpython-312.pyc
│     │     │  │     ├─ _collections.cpython-312.pyc
│     │     │  │     ├─ _concurrency_py3k.cpython-312.pyc
│     │     │  │     ├─ _has_cy.cpython-312.pyc
│     │     │  │     ├─ _py_collections.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ events.cpython-312.pyc
│     │     │     ├─ exc.cpython-312.pyc
│     │     │     ├─ inspection.cpython-312.pyc
│     │     │     ├─ log.cpython-312.pyc
│     │     │     ├─ schema.cpython-312.pyc
│     │     │     ├─ types.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ sqlalchemy-2.0.43.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ starlette
│     │     │  ├─ applications.py
│     │     │  ├─ authentication.py
│     │     │  ├─ background.py
│     │     │  ├─ concurrency.py
│     │     │  ├─ config.py
│     │     │  ├─ convertors.py
│     │     │  ├─ datastructures.py
│     │     │  ├─ endpoints.py
│     │     │  ├─ exceptions.py
│     │     │  ├─ formparsers.py
│     │     │  ├─ middleware
│     │     │  │  ├─ authentication.py
│     │     │  │  ├─ base.py
│     │     │  │  ├─ cors.py
│     │     │  │  ├─ errors.py
│     │     │  │  ├─ exceptions.py
│     │     │  │  ├─ gzip.py
│     │     │  │  ├─ httpsredirect.py
│     │     │  │  ├─ sessions.py
│     │     │  │  ├─ trustedhost.py
│     │     │  │  ├─ wsgi.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ authentication.cpython-312.pyc
│     │     │  │     ├─ base.cpython-312.pyc
│     │     │  │     ├─ cors.cpython-312.pyc
│     │     │  │     ├─ errors.cpython-312.pyc
│     │     │  │     ├─ exceptions.cpython-312.pyc
│     │     │  │     ├─ gzip.cpython-312.pyc
│     │     │  │     ├─ httpsredirect.cpython-312.pyc
│     │     │  │     ├─ sessions.cpython-312.pyc
│     │     │  │     ├─ trustedhost.cpython-312.pyc
│     │     │  │     ├─ wsgi.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ py.typed
│     │     │  ├─ requests.py
│     │     │  ├─ responses.py
│     │     │  ├─ routing.py
│     │     │  ├─ schemas.py
│     │     │  ├─ staticfiles.py
│     │     │  ├─ status.py
│     │     │  ├─ templating.py
│     │     │  ├─ testclient.py
│     │     │  ├─ types.py
│     │     │  ├─ websockets.py
│     │     │  ├─ _exception_handler.py
│     │     │  ├─ _utils.py
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ applications.cpython-312.pyc
│     │     │     ├─ authentication.cpython-312.pyc
│     │     │     ├─ background.cpython-312.pyc
│     │     │     ├─ concurrency.cpython-312.pyc
│     │     │     ├─ config.cpython-312.pyc
│     │     │     ├─ convertors.cpython-312.pyc
│     │     │     ├─ datastructures.cpython-312.pyc
│     │     │     ├─ endpoints.cpython-312.pyc
│     │     │     ├─ exceptions.cpython-312.pyc
│     │     │     ├─ formparsers.cpython-312.pyc
│     │     │     ├─ requests.cpython-312.pyc
│     │     │     ├─ responses.cpython-312.pyc
│     │     │     ├─ routing.cpython-312.pyc
│     │     │     ├─ schemas.cpython-312.pyc
│     │     │     ├─ staticfiles.cpython-312.pyc
│     │     │     ├─ status.cpython-312.pyc
│     │     │     ├─ templating.cpython-312.pyc
│     │     │     ├─ testclient.cpython-312.pyc
│     │     │     ├─ types.cpython-312.pyc
│     │     │     ├─ websockets.cpython-312.pyc
│     │     │     ├─ _exception_handler.cpython-312.pyc
│     │     │     ├─ _utils.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ starlette-0.47.3.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE.md
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ tqdm
│     │     │  ├─ asyncio.py
│     │     │  ├─ auto.py
│     │     │  ├─ autonotebook.py
│     │     │  ├─ cli.py
│     │     │  ├─ completion.sh
│     │     │  ├─ contrib
│     │     │  │  ├─ bells.py
│     │     │  │  ├─ concurrent.py
│     │     │  │  ├─ discord.py
│     │     │  │  ├─ itertools.py
│     │     │  │  ├─ logging.py
│     │     │  │  ├─ slack.py
│     │     │  │  ├─ telegram.py
│     │     │  │  ├─ utils_worker.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ bells.cpython-312.pyc
│     │     │  │     ├─ concurrent.cpython-312.pyc
│     │     │  │     ├─ discord.cpython-312.pyc
│     │     │  │     ├─ itertools.cpython-312.pyc
│     │     │  │     ├─ logging.cpython-312.pyc
│     │     │  │     ├─ slack.cpython-312.pyc
│     │     │  │     ├─ telegram.cpython-312.pyc
│     │     │  │     ├─ utils_worker.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ dask.py
│     │     │  ├─ gui.py
│     │     │  ├─ keras.py
│     │     │  ├─ notebook.py
│     │     │  ├─ rich.py
│     │     │  ├─ std.py
│     │     │  ├─ tk.py
│     │     │  ├─ tqdm.1
│     │     │  ├─ utils.py
│     │     │  ├─ version.py
│     │     │  ├─ _dist_ver.py
│     │     │  ├─ _main.py
│     │     │  ├─ _monitor.py
│     │     │  ├─ _tqdm.py
│     │     │  ├─ _tqdm_gui.py
│     │     │  ├─ _tqdm_notebook.py
│     │     │  ├─ _tqdm_pandas.py
│     │     │  ├─ _utils.py
│     │     │  ├─ __init__.py
│     │     │  ├─ __main__.py
│     │     │  └─ __pycache__
│     │     │     ├─ asyncio.cpython-312.pyc
│     │     │     ├─ auto.cpython-312.pyc
│     │     │     ├─ autonotebook.cpython-312.pyc
│     │     │     ├─ cli.cpython-312.pyc
│     │     │     ├─ dask.cpython-312.pyc
│     │     │     ├─ gui.cpython-312.pyc
│     │     │     ├─ keras.cpython-312.pyc
│     │     │     ├─ notebook.cpython-312.pyc
│     │     │     ├─ rich.cpython-312.pyc
│     │     │     ├─ std.cpython-312.pyc
│     │     │     ├─ tk.cpython-312.pyc
│     │     │     ├─ utils.cpython-312.pyc
│     │     │     ├─ version.cpython-312.pyc
│     │     │     ├─ _dist_ver.cpython-312.pyc
│     │     │     ├─ _main.cpython-312.pyc
│     │     │     ├─ _monitor.cpython-312.pyc
│     │     │     ├─ _tqdm.cpython-312.pyc
│     │     │     ├─ _tqdm_gui.cpython-312.pyc
│     │     │     ├─ _tqdm_notebook.cpython-312.pyc
│     │     │     ├─ _tqdm_pandas.cpython-312.pyc
│     │     │     ├─ _utils.cpython-312.pyc
│     │     │     ├─ __init__.cpython-312.pyc
│     │     │     └─ __main__.cpython-312.pyc
│     │     ├─ tqdm-4.67.1.dist-info
│     │     │  ├─ entry_points.txt
│     │     │  ├─ INSTALLER
│     │     │  ├─ LICENCE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ top_level.txt
│     │     │  └─ WHEEL
│     │     ├─ typing_extensions-4.15.0.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ typing_extensions.py
│     │     ├─ typing_inspection
│     │     │  ├─ introspection.py
│     │     │  ├─ py.typed
│     │     │  ├─ typing_objects.py
│     │     │  ├─ typing_objects.pyi
│     │     │  ├─ __init__.py
│     │     │  └─ __pycache__
│     │     │     ├─ introspection.cpython-312.pyc
│     │     │     ├─ typing_objects.cpython-312.pyc
│     │     │     └─ __init__.cpython-312.pyc
│     │     ├─ typing_inspection-0.4.1.dist-info
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     ├─ uvicorn
│     │     │  ├─ config.py
│     │     │  ├─ importer.py
│     │     │  ├─ lifespan
│     │     │  │  ├─ off.py
│     │     │  │  ├─ on.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ off.cpython-312.pyc
│     │     │  │     ├─ on.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ logging.py
│     │     │  ├─ loops
│     │     │  │  ├─ asyncio.py
│     │     │  │  ├─ auto.py
│     │     │  │  ├─ uvloop.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ asyncio.cpython-312.pyc
│     │     │  │     ├─ auto.cpython-312.pyc
│     │     │  │     ├─ uvloop.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ main.py
│     │     │  ├─ middleware
│     │     │  │  ├─ asgi2.py
│     │     │  │  ├─ message_logger.py
│     │     │  │  ├─ proxy_headers.py
│     │     │  │  ├─ wsgi.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ asgi2.cpython-312.pyc
│     │     │  │     ├─ message_logger.cpython-312.pyc
│     │     │  │     ├─ proxy_headers.cpython-312.pyc
│     │     │  │     ├─ wsgi.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ protocols
│     │     │  │  ├─ http
│     │     │  │  │  ├─ auto.py
│     │     │  │  │  ├─ flow_control.py
│     │     │  │  │  ├─ h11_impl.py
│     │     │  │  │  ├─ httptools_impl.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ auto.cpython-312.pyc
│     │     │  │  │     ├─ flow_control.cpython-312.pyc
│     │     │  │  │     ├─ h11_impl.cpython-312.pyc
│     │     │  │  │     ├─ httptools_impl.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ utils.py
│     │     │  │  ├─ websockets
│     │     │  │  │  ├─ auto.py
│     │     │  │  │  ├─ websockets_impl.py
│     │     │  │  │  ├─ websockets_sansio_impl.py
│     │     │  │  │  ├─ wsproto_impl.py
│     │     │  │  │  ├─ __init__.py
│     │     │  │  │  └─ __pycache__
│     │     │  │  │     ├─ auto.cpython-312.pyc
│     │     │  │  │     ├─ websockets_impl.cpython-312.pyc
│     │     │  │  │     ├─ websockets_sansio_impl.cpython-312.pyc
│     │     │  │  │     ├─ wsproto_impl.cpython-312.pyc
│     │     │  │  │     └─ __init__.cpython-312.pyc
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ utils.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ py.typed
│     │     │  ├─ server.py
│     │     │  ├─ supervisors
│     │     │  │  ├─ basereload.py
│     │     │  │  ├─ multiprocess.py
│     │     │  │  ├─ statreload.py
│     │     │  │  ├─ watchfilesreload.py
│     │     │  │  ├─ __init__.py
│     │     │  │  └─ __pycache__
│     │     │  │     ├─ basereload.cpython-312.pyc
│     │     │  │     ├─ multiprocess.cpython-312.pyc
│     │     │  │     ├─ statreload.cpython-312.pyc
│     │     │  │     ├─ watchfilesreload.cpython-312.pyc
│     │     │  │     └─ __init__.cpython-312.pyc
│     │     │  ├─ workers.py
│     │     │  ├─ _subprocess.py
│     │     │  ├─ _types.py
│     │     │  ├─ __init__.py
│     │     │  ├─ __main__.py
│     │     │  └─ __pycache__
│     │     │     ├─ config.cpython-312.pyc
│     │     │     ├─ importer.cpython-312.pyc
│     │     │     ├─ logging.cpython-312.pyc
│     │     │     ├─ main.cpython-312.pyc
│     │     │     ├─ server.cpython-312.pyc
│     │     │     ├─ workers.cpython-312.pyc
│     │     │     ├─ _subprocess.cpython-312.pyc
│     │     │     ├─ _types.cpython-312.pyc
│     │     │     ├─ __init__.cpython-312.pyc
│     │     │     └─ __main__.cpython-312.pyc
│     │     ├─ uvicorn-0.35.0.dist-info
│     │     │  ├─ entry_points.txt
│     │     │  ├─ INSTALLER
│     │     │  ├─ licenses
│     │     │  │  └─ LICENSE.md
│     │     │  ├─ METADATA
│     │     │  ├─ RECORD
│     │     │  ├─ REQUESTED
│     │     │  └─ WHEEL
│     │     └─ __pycache__
│     │        └─ typing_extensions.cpython-312.pyc
│     ├─ pyvenv.cfg
│     └─ Scripts
│        ├─ activate
│        ├─ activate.bat
│        ├─ Activate.ps1
│        ├─ deactivate.bat
│        ├─ distro.exe
│        ├─ email_validator.exe
│        ├─ fastapi.exe
│        ├─ httpx.exe
│        ├─ openai.exe
│        ├─ pip.exe
│        ├─ pip3.12.exe
│        ├─ pip3.exe
│        ├─ python.exe
│        ├─ pythonw.exe
│        ├─ tqdm.exe
│        └─ uvicorn.exe
└─ README.md

```