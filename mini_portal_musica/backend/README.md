# Backend Micrositio Musical 🎶

Este backend está desarrollado con **FastAPI**, **SQLAlchemy** y **SQLite**, y sirve para gestionar canciones, mostrar perfil de estudiante, recibir mensajes de contacto y ofrecer recomendaciones musicales, incluyendo recomendaciones “IA” basadas en similitud de contenido.

---

## Estructura del proyecto (backend)
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

```


---

## Dependencias

Instalar todas las librerías necesarias:

```bash
pip install fastapi uvicorn sqlalchemy 

pip install pydantic 

pip install pandas 

pip install scikit-learn
```

---

## Base de datos

- **SQLite**: `songs.db`
- Configuración en `database.py` con:
  - `engine` → motor de SQLite
  - `SessionLocal` → sesión para CRUD
  - `Base` → modelo base SQLAlchemy
- Se puede inicializar la base de datos ejecutando `seed.py` para insertar canciones de prueba.

---

## Endpoints disponibles

### 🎵 Canciones (`/api/songs`)

- `GET /api/songs/` → Listar todas las canciones
- `POST /api/songs/` → Crear una nueva canción
- `GET /api/songs/{song_id}` → Detalle de una canción por ID
- `DELETE /api/songs/{song_id}` → Eliminar canción por ID

**Ejemplo request:**

```json
POST /api/songs/
{
  "title": "Bohemian Rhapsody",
  "genre": "rock",
  "artist": "Queen",
  "album": "A Night at the Opera",
  "description": "Canción icónica de rock",
  "cover": "bohemian.jpg",
  "video": "https://youtu.be/fJ9rUzIMcZQ",
  "country": "UK"
}
```

---

### 👤 Perfil (`/api/profile`)

- `GET /api/profile/` → Retorna información del estudiante

**Ejemplo response:**

```json
{
  "name": "Hanna Abril",
  "career": "Ingeniería de Software",
  "email": "hanna@example.com"
}
```

---

### 📧 Contacto (`/api/contact`)

- `POST /api/contact/` → Enviar formulario de contacto

**Ejemplo response:**

```json
{
  "name": "Juan Perez",
  "email": "juan@example.com",
  "message": "Hola, quiero información sobre la música."
}
```
---
### 🎯 Recomendaciones (`/api/recommendations`)

**Básicas por género**

- `GET /api/recommendations?genre={genero}`
- Ejemplo: `/api/recommendations?genre=rock`

**IA por similitud de contenido**

- `GET /api/recommendations/ai/{song_id}`
- Ejemplo: `/api/recommendations/ai/1`
- Devuelve canciones similares usando TF-IDF y similitud de coseno sobre atributos: género, artista, álbum y descripción.

---

## Uso

1. Ejecutar el servidor:

```bash
uvicorn app.main:app --reload
```

2. Abrir la documentación interactiva de FastAPI:
Visita la [documentación de FastAPI](http://127.0.0.1:8000/docs) para probar los endpoints.

3. Probar endpoints desde /docs o usando herramientas como curl o Postman.

---
## Notas importantes

* La función get_db centraliza la sesión de la base de datos y se reutiliza en todos los routers con Depends.

* La carpeta utils contiene toda la lógica de recomendaciones (get_recommendations y get_recommendations_ai).

* La carpeta routers organiza los endpoints según funcionalidad.

* Permite agregar más routers y endpoints sin modificar la base de datos ni la estructura existente.
