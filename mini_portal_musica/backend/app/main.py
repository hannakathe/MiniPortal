# → Punto de entrada de FastAPI.

""" Main module for FastAPI application. 
Aquí arrancamos la app, registramos routers (por ejemplo songs.py) y configuramos middlewares."""

# Interface web dinamicamente generada por FastAPI en /docs (Swagger UI) y /redoc (ReDoc) http://127.0.0.1:8000/docs


from fastapi import FastAPI
from .routers import songs, profile, contact, recommendations

app = FastAPI(title="Micrositio Musical 🎶")

# incluir router
app.include_router(songs.router)
app.include_router(profile.router)
app.include_router(contact.router)
app.include_router(recommendations.router)
