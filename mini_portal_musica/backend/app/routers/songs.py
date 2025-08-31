# → Aquí defines los endpoints específicos para canciones (/songs). CRUD

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(
    prefix="/api/songs",
    tags=["Songs"]
)

# Dependencia DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Listar canciones
@router.get("/", response_model=list[schemas.Song])
def get_songs(db: Session = Depends(get_db)):
    return db.query(models.Song).all()

# 2. Obtener canción por id
@router.get("/{song_id}", response_model=schemas.Song)
def get_song(song_id: int, db: Session = Depends(get_db)):
    song = db.query(models.Song).filter(models.Song.id == song_id).first()
    if not song:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return song

# 3. Crear canción
@router.post("/", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    new_song = models.Song(**song.dict())
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song

# 4. Borrar canción
@router.delete("/{song_id}")
def delete_song(song_id: int, db: Session = Depends(get_db)):
    song = db.query(models.Song).filter(models.Song.id == song_id).first()
    if not song:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    db.delete(song)
    db.commit()
    return {"ok": True, "message": "Canción eliminada"}


