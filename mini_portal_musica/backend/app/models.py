# Importación de los tipos de columnas de SQLAlchemy y la clase base
from sqlalchemy import Column, Integer, String, Text, Date, Float
# Importación de la clase base declarativa para la base de datos principal
from .database import Base

# Definición del modelo Song que representa la tabla de canciones en la base de datos
class Song(Base):
    """
    Modelo SQLAlchemy para la tabla 'songs' en la base de datos principal.
    
    Esta clase representa la estructura completa de una canción en el sistema,
    incluyendo metadatos musicales, información del artista, y datos geográficos.
    
    Attributes:
        id (int): Identificador único autoincremental de cada canción
        title (str): Título de la canción (obligatorio)
        genre (str): Género musical (opcional)
        artist (str): Artista principal (obligatorio)
        discografic (str): Discográfica (opcional)
        album (str): Álbum al que pertenece (opcional)
        description (str): Descripción de la canción (opcional, texto largo)
        album_image (str): URL o ruta de la imagen del álbum (opcional)
        url_video (str): URL de YouTube/Spotify (opcional)
        country (str): País de origen (opcional)
        release_date (Date): Fecha de lanzamiento (opcional)
        lyrics (str): Letra completa de la canción (opcional, texto largo)
        country_latitude (float): Latitud geográfica del país (opcional)
        country_longitude (float): Longitud geográfica del país (opcional)
    """
    
    # Nombre de la tabla en la base de datos
    __tablename__ = "songs"

    # Columna ID - Llave primaria autoincremental con índice
    # primary_key=True: Identificador único de cada registro
    # index=True: Crea un índice para búsquedas más rápidas por ID
    id = Column(Integer, primary_key=True, index=True)
    
    # Columna title - Título de la canción (string de longitud variable)
    # index=True: Índice para búsquedas rápidas por título
    # nullable=False: Campo obligatorio, no puede ser NULL en la base de datos
    title = Column(String, index=True, nullable=False)          # Título de la canción
    
    # Columna genre - Género musical (string de longitud variable)
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    genre = Column(String, nullable=True)                       # Género musical
    
    # Columna artist - Artista principal (string de longitud variable)
    # index=True: Índice para búsquedas rápidas por artista
    # nullable=False: Campo obligatorio, no puede ser NULL en la base de datos
    artist = Column(String, index=True, nullable=False)         # Artista principal
    
    # Columna discografic - Discográfica (string de longitud variable)
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    discografic = Column(String, nullable=True)                 # Discográfica
    
    # Columna album - Álbum al que pertenece (string de longitud variable)
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    album = Column(String, nullable=True)                       # Álbum al que pertenece
    
    # Columna description - Descripción de la canción (texto de longitud ilimitada)
    # Text: Tipo de dato para textos largos
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    description = Column(Text, nullable=True)                   # Descripción de la canción
    
    # Columna album_image - URL o ruta de la imagen del álbum (string)
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    album_image = Column(String, nullable=True)                 # URL/Path imagen del álbum
    
    # Columna url_video - URL de YouTube/Spotify (string)
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    url_video = Column(String, nullable=True)                   # URL de YouTube/Spotify
    
    # Columna country - País de origen (string de longitud variable)
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    country = Column(String, nullable=True)                     # País de origen
    
    # Columna release_date - Fecha de lanzamiento (tipo Date)
    # Date: Almacena fecha sin hora
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    release_date = Column(Date, nullable=True)                  # Fecha de lanzamiento
    
    # Columna lyrics - Letra completa de la canción (texto de longitud ilimitada)
    # Text: Tipo de dato para textos muy largos como letras de canciones
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    lyrics = Column(Text, nullable=True)                        # Letra de la canción
    
    # Columna country_latitude - Latitud geográfica del país (tipo Float)
    # Float: Número decimal para coordenadas geográficas
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    country_latitude = Column(Float, nullable=True)             # Nueva columna
    
    # Columna country_longitude - Longitud geográfica del país (tipo Float)
    # Float: Número decimal para coordenadas geográficas
    # nullable=True: Campo opcional, puede ser NULL en la base de datos
    country_longitude = Column(Float, nullable=True)            # Nueva columna