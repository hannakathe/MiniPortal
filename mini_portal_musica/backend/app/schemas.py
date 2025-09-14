# Importación de clases de Pydantic para definir esquemas de validación de datos
from pydantic import BaseModel
# Importación de tipos de datos para fechas y opcionales
from datetime import date
from typing import Optional
# Importación de EmailStr para validación automática de emails
from pydantic import BaseModel, EmailStr


# Base común (campos que pueden recibirse/enviarse)
# Los esquemas Pydantic definen la estructura y validación de los datos
# que se envían y reciben a través de la API

# ------------------------------
# Songs - Esquemas para canciones
# ------------------------------

# Esquema base para canciones - define los campos comunes
class SongBase(BaseModel):
    """
    Esquema base para datos de canciones. Define la estructura común
    para creación, lectura y actualización de canciones.
    
    Fields:
        title (str): Título de la canción (obligatorio)
        artist (str): Artista principal (obligatorio)
        genre (str | None): Género musical (opcional)
        discografic (str | None): Discográfica (opcional)
        album (str | None): Álbum (opcional)
        description (str | None): Descripción (opcional)
        album_image (str | None): URL de imagen del álbum (opcional)
        url_video (str | None): URL de video musical (opcional)
        country (str | None): País de origen (opcional)
        release_date (date | None): Fecha de lanzamiento (opcional)
        lyrics (str | None): Letra completa (opcional)
        country_latitude (float | None): Latitud geográfica (opcional)
        country_longitude (float | None): Longitud geográfica (opcional)
    """
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
    country_latitude: Optional[float] = None
    country_longitude: Optional[float] = None

# Para crear canción (no incluye id) - usado en endpoints POST
class SongCreate(SongBase):
    """
    Esquema específico para creación de canciones.
    Hereda todos los campos de SongBase pero no incluye el ID,
    ya que el ID es generado automáticamente por la base de datos.
    """
    pass

# Para leer canción desde la BD (incluye id) - usado en endpoints GET
class Song(SongBase):
    """
    Esquema para lectura de canciones. Incluye el ID que es generado
    por la base de datos cuando se crea un nuevo registro.
    
    Config:
        from_attributes = True: Permite a Pydantic leer objetos ORM de SQLAlchemy
        y convertirlos automáticamente a este esquema.
    """
    id: int

    class Config:
        from_attributes = True   # <- Esto permite a Pydanticv2 leer objetos de SQLAlchemy



# ------------------------------
# Perfil del estudiante (Yo)
# ------------------------------

# Esquema para el perfil del estudiante - información estática
class Profile(BaseModel):
    """
    Esquema para el perfil del estudiante/desarrollador.
    Representa información estática que no cambia frecuentemente.
    
    Fields:
        id (int): Identificador único
        nombre (str): Nombre completo
        carrera (str): Carrera que estudia
        universidad (str): Universidad donde estudia
        email (EmailStr): Email válido (validado automáticamente)
        descripcion (str): Descripción o biografía
    """
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

# Importación adicional de BaseModel y EmailStr (aunque ya importados arriba)
from pydantic import BaseModel, EmailStr

# Esquema base para contactos - campos comunes para el formulario
class ContactBase(BaseModel):
    """
    Esquema base para datos de contacto del formulario.
    
    Fields:
        nombre (str): Nombre de la persona (obligatorio)
        email (EmailStr): Email válido (obligatorio, validado automáticamente)
        mensaje (str): Mensaje de contacto (obligatorio)
    """
    nombre: str
    email: EmailStr
    mensaje: str

# Esquema para creación de contactos - usado en endpoints POST
class ContactCreate(ContactBase):
    """
    Esquema específico para creación de contactos.
    Hereda todos los campos de ContactBase sin modificaciones.
    """
    pass

# Esquema para lectura de contactos - usado en endpoints GET
class Contact(ContactBase):
    """
    Esquema para lectura de contactos. Incluye el ID generado
    por la base de datos cuando se crea un nuevo mensaje de contacto.
    
    Config:
        from_attributes = True: Permite conversión automática desde objetos ORM
    """
    id: int

    class Config:
        from_attributes = True