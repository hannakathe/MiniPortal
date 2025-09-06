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


# 2️⃣ Recomendaciones tipo chat usando IA y validando contra BD
@router.post("/chat-recommendations", response_model=list[schemas.Song])
async def chat_recommendations(message: str = Form(...), db: Session = Depends(get_db)):
    """
    Envía un mensaje a la IA para obtener recomendaciones musicales basadas en la BD.
    """
    # Obtener todos los títulos de la BD
    todos_titulos = [c.title for c in db.query(models.Song).all()]

    if not todos_titulos:
        raise HTTPException(status_code=404, detail="No hay canciones en la base de datos")

    try:
        # Prompt para IA: solo puede sugerir títulos existentes
        prompt = f"""
        Eres un recomendador musical experto.
        Basado en el mensaje del usuario: "{message}"
        Solo sugiere canciones de la siguiente lista de títulos disponibles en la base de datos:
        {todos_titulos}
        Responde únicamente con un JSON de títulos válidos, ejemplo: ["titulo1", "titulo2", "titulo3"]
        """

        respuesta = client.chat.completions.create(
            model="gpt-oss-20b:free",
            messages=[
                {"role": "system", "content": "Eres un recomendador musical experto."},
                {"role": "user", "content": prompt}
            ]
        )

        # Obtener la respuesta de la IA
        recomendaciones = respuesta.choices[0].message.content.strip()

        # Intentar parsear JSON
        try:
            titulos = json.loads(recomendaciones)
        except:
            titulos = []

        # Buscar en la BD las canciones recomendadas por título
        if titulos:
            songs = db.query(models.Song).filter(models.Song.title.in_(titulos)).all()
            return songs

        return JSONResponse(content={
            "mensaje": "No se pudieron obtener recomendaciones válidas",
            "raw_response": recomendaciones
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error IA: {str(e)}")