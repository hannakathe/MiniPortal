# → Punto de entrada de FastAPI.

""" Main module for FastAPI application. 
Aquí arrancamos la app, registramos routers (por ejemplo songs.py) y configuramos middlewares."""

# Interface web dinamicamente generada por FastAPI en /docs (Swagger UI) y /redoc (ReDoc) http://127.0.0.1:8000/docs


# Importación de FastAPI y componentes necesarios
from fastapi import FastAPI
# Importación de middleware CORS para permitir solicitudes cross-origin
from fastapi.middleware.cors import CORSMiddleware
# Importación de los routers definidos en la aplicación
from .routers import songs, contact, recommendations
# Importación de modelos y configuración de base de datos para contactos
from . import models_contact, database_contact  # Importar modelos y base de datos de contactos

# Crear todas las tablas en la base de datos de contactos si no existen
# Esto asegura que la estructura de la BD esté disponible al iniciar la aplicación
models_contact.BaseContact.metadata.create_all(bind=database_contact.engine)  # Crear tablas de contactos

# Crear la instancia principal de la aplicación FastAPI
# title: Título que aparecerá en la documentación automática
app = FastAPI(title="Micrositio Musical 🎶")

# 🔥 Configuración de CORS (Cross-Origin Resource Sharing)
# Middleware que permite solicitudes desde diferentes orígenes (dominios)
app.add_middleware(
    CORSMiddleware,  # Clase del middleware CORS
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen
    # O reemplaza "*" por ["http://127.0.0.1:5500"] si usas Live Server
    allow_credentials=True,  # Permite el envío de cookies y credenciales
    allow_methods=["*"],     # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],     # Permite todos los headers en las solicitudes
)


# incluir router - Registrar los routers en la aplicación principal
# Cada router agrupa endpoints relacionados bajo un prefijo común

# Registrar el router de canciones (endpoints para gestión de canciones)
app.include_router(songs.router)
# Registrar el router de contactos (endpoints para formulario de contacto)
app.include_router(contact.router)
# Registrar el router de recomendaciones (endpoints para sistema de recomendación)
app.include_router(recommendations.router)