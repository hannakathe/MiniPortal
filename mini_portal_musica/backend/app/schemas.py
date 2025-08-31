from pydantic import BaseModel
from datetime import date
from pydantic import BaseModel, EmailStr


# Base común (campos que pueden recibirse/enviarse)

# ------------------------------
# Songs
# ------------------------------
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
        from_attributes = True   # <- Esto permite a Pydanticv2 leer objetos de SQLAlchemy



# ------------------------------
# Perfil del estudiante (Yo)
# ------------------------------
class Profile(BaseModel):
    id: int
    nombre: str
    carrera: str
    universidad: str
    email: EmailStr
    descripcion: str

    class Config:
        from_attributes = True


# ------------------------------
# Contacto (formulario)
# ------------------------------
class Contact(BaseModel):
    nombre: str
    email: EmailStr
    mensaje: str
