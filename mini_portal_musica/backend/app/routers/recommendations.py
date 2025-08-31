from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database
from ..utils.recommender import get_recommendations, get_recommendations_ai

router = APIRouter(
    prefix="/api/recommendations",
    tags=["Recommendations"]
)

# Dependencia DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Recomendaciones básicas por género
@router.get("/", response_model=list[schemas.Song])
def recommend_songs(genre: str, db: Session = Depends(get_db)):
    """
    Recomienda canciones según el género.
    Ejemplo: /api/recommendations?genre=rock
    """
    songs = get_recommendations(db, genre)
    if not songs:
        raise HTTPException(status_code=404, detail="No se encontraron recomendaciones")
    return songs

# 2️⃣ Recomendaciones IA por similitud de contenido
@router.get("/ai/{song_id}", response_model=list[schemas.Song])
def recommend_songs_ai(song_id: int, db: Session = Depends(get_db)):
    """
    Recomienda canciones similares a una canción dada usando IA (similitud de contenido).
    Ejemplo: /api/recommendations/ai/1
    """
    try:
        songs = get_recommendations_ai(db, song_id)
        if not songs:
            raise HTTPException(status_code=404, detail="No se encontraron recomendaciones similares")
        return songs
    except IndexError:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
