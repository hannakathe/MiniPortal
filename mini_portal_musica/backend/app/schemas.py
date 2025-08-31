from pydantic import BaseModel
from datetime import date

# Base común (campos que pueden recibirse/enviarse)
class SongBase(BaseModel):
    title: str
    artist: str
    genre: str | None = None
    discografic: str | None = None
    album: str | None = None
    description: str | None = None
    album_image: str | None = None     # URL de la imagen del álbum
    url_video: str | None = None       # YouTube / Spotify
    country: str | None = None
    release_date: date | None = None   # Fecha en formato YYYY-MM-DD
    lyrics: str | None = None          # Letra de la canción

# Para crear canción (no incluye id)
class SongCreate(SongBase):
    pass

# Para leer canción desde la BD (incluye id)
class Song(SongBase):
    id: int

    class Config:
        orm_mode = True   # <- Esto permite a Pydantic leer objetos de SQLAlchemy
