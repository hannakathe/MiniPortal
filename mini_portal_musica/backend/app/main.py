# → Punto de entrada de FastAPI.

""" Main module for FastAPI application. 
Aquí arrancamos la app, registramos routers (por ejemplo songs.py) y configuramos middlewares."""

# Interface web dinamicamente generada por FastAPI en /docs (Swagger UI) y /redoc (ReDoc) http://127.0.0.1:8000/docs


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import songs, contact, recommendations
from . import models_contact, database_contact  # Importar modelos y base de datos de contactos

models_contact.BaseContact.metadata.create_all(bind=database_contact.engine)  # Crear tablas de contactos
app = FastAPI(title="Micrositio Musical 🎶")

# 🔥 Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O reemplaza "*" por ["http://127.0.0.1:5500"] si usas Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# incluir router
app.include_router(songs.router)
app.include_router(contact.router)
app.include_router(recommendations.router)
