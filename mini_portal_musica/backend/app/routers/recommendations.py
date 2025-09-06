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
    #RECORDAR: CAMBIAR API KEY NUEVA EN PRESENTACIÓN
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
    songs = db.query(models.Song).filter(models.Song.genre.ilike(f"%{genre}%")).all()
    if not songs:
        raise HTTPException(status_code=404, detail="No se encontraron recomendaciones")
    return songs



# 2️⃣ Recomendaciones tipo chat usando IA y validando contra BD
@router.post("/chat-recommendations", response_model=list[schemas.Song])
async def chat_recommendations(message: str = Form(...), db: Session = Depends(get_db)):
    todos_titulos = [c.title for c in db.query(models.Song).all()]
    if not todos_titulos:
        raise HTTPException(status_code=404, detail="No hay canciones en la base de datos")

    try:
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

        recomendaciones = respuesta.choices[0].message.content.strip()
        print("RESPUESTA IA:", recomendaciones)  # <--- depuración

        try:
            titulos = json.loads(recomendaciones)
        except Exception as e:
            print("ERROR PARSEANDO JSON:", e)
            return JSONResponse(content={
                "mensaje": "No se pudo parsear la respuesta de la IA",
                "raw_response": recomendaciones
            })

        if titulos:
            songs = db.query(models.Song).filter(models.Song.title.in_(titulos)).all()
            return songs

        return JSONResponse(content={
            "mensaje": "No se pudieron obtener recomendaciones válidas",
            "raw_response": recomendaciones
        })

    except Exception as e:
        print("ERROR GENERAL:", e)
        raise HTTPException(status_code=500, detail=f"Error IA: {str(e)}")
    except Exception as e:
        if "401" in str(e):
            raise HTTPException(status_code=500, detail="API Key inválida o expirada")
        raise HTTPException(status_code=500, detail=f"Error IA: {str(e)}")

