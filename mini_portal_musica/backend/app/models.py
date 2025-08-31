from sqlalchemy import Column, Integer, String, Text, Date
from .database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)          # Título de la canción
    genre = Column(String, nullable=True)                       # Género musical
    artist = Column(String, index=True, nullable=False)         # Artista principal
    discografic = Column(String, nullable=True)                 # Discográfica
    album = Column(String, nullable=True)                       # Álbum al que pertenece
    description = Column(Text, nullable=True)                   # Descripción de la canción
    album_image = Column(String, nullable=True)                 # URL/Path imagen del álbum
    url_video = Column(String, nullable=True)                   # URL de YouTube/Spotify
    country = Column(String, nullable=True)                     # País de origen
    release_date = Column(Date, nullable=True)                  # Fecha de lanzamiento
    lyrics = Column(Text, nullable=True)                        # Letra de la canción
