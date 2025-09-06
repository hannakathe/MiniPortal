# recommendations.py
from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .. import schemas, database, models
from openai import OpenAI
from fastapi.responses import JSONResponse
import json

router = APIRouter(
    prefix="/api/recommendations",
    tags=["Recommendations"]
)

# Configurar cliente OpenRouter/OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# Dependencia DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Recomendaciones básicas por género (se mantiene igual)
@router.get("/", response_model=list[schemas.Song])
def recommend_songs(genre: str, db: Session = Depends(get_db)):
    songs = db.query(models.Song).filter(models.Song.genre == genre).all()
    if not songs:
        raise HTTPException(status_code=404, detail="No se encontraron recomendaciones")
    return songs

# 2️⃣ Recomendaciones IA tipo chat (mensaje libre del usuario)
@router.post("/chat-recommendations", response_model=list[schemas.Song])
async def chat_recommendations(message: str = Form(...), db: Session = Depends(get_db)):
    """
    Chat interactivo para recomendar canciones.
    El usuario puede pedir canciones por género, estado de ánimo, artista, etc.
    """
    try:
        # Obtener todos los títulos disponibles en la BD
        canciones_disponibles = [s.title for s in db.query(models.Song).all()]

        if not canciones_disponibles:
            raise HTTPException(status_code=404, detail="No hay canciones en la base de datos")

        # Crear prompt para la IA
        prompt = f"""
        Eres un recomendador musical experto.
        La base de datos contiene estas canciones:
        {canciones_disponibles}

        Según este mensaje del usuario: "{message}", 
        sugiere hasta 5 canciones de la base de datos.
        Responde SOLO con un JSON de títulos exactos.
        """

        # Llamada a OpenRouter/OpenAI
        respuesta = client.chat.completions.create(
            model="gpt-oss-20b:free",
            messages=[
                {"role": "system", "content": "Eres un recomendador musical experto."},
                {"role": "user", "content": prompt}
            ]
        )

        recomendaciones_raw = respuesta.choices[0].message.content.strip()

        # Parsear JSON devuelto por la IA
        try:
            titulos = json.loads(recomendaciones_raw)
        except json.JSONDecodeError:
            return JSONResponse(content={
                "mensaje": "No se pudieron obtener recomendaciones válidas",
                "raw_response": recomendaciones_raw
            })

        # Filtrar en BD solo las canciones que existen
        if titulos:
            songs = db.query(models.Song).filter(models.Song.title.in_(titulos)).all()
            return songs

        return JSONResponse(content={
            "mensaje": "La IA no devolvió ninguna canción válida",
            "raw_response": recomendaciones_raw
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error IA: {str(e)}")
