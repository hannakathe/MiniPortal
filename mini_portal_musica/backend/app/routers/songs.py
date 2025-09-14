# → Aquí defines los endpoints específicos para canciones (/songs). CRUD
# Este módulo implementa operaciones CRUD completas para la entidad Song

# Importación de módulos necesarios de FastAPI
from fastapi import APIRouter, Depends, HTTPException
# Importación de Session para manejar la conexión a la base de datos
from sqlalchemy.orm import Session
# Importación de módulos locales (modelos, esquemas y configuración de base de datos)
from .. import models, schemas, database

# Creación de un router de FastAPI para agrupar endpoints de canciones
router = APIRouter(
    prefix="/api/songs",  # Prefijo base para todas las rutas en este router
    tags=["Songs"]       # Etiqueta para documentación automática en Swagger/OpenAPI
)

# Dependencia DB - Función que proporciona la sesión de base de datos
def get_db():
    """
    Provee una sesión de base de datos para cada request.
    Se asegura de cerrar la sesión al finalizar el request.
    
    Yields:
        Session: Sesión de base de datos SQLAlchemy
        
    Note:
        Esta función se usa con Depends() para inyección de dependencias
    """
    # Crear una nueva sesión de base de datos
    db = database.SessionLocal()
    try:
        # Yield permite usar esta función como dependencia con Depends()
        yield db
    finally:
        # Asegurar que la sesión se cierre siempre, incluso si hay errores
        db.close()

# 1. Listar canciones - Endpoint GET para obtener todas las canciones
@router.get("/", response_model=list[schemas.Song])
def get_songs(db: Session = Depends(get_db)):
    """
    Obtiene todas las canciones almacenadas en la base de datos.
    
    Args:
        db (Session): Sesión de base de datos inyectada por dependencia
        
    Returns:
        list[schemas.Song]: Lista de todas las canciones en formato del schema
        
    Note:
        response_model valida y formatea la respuesta automáticamente
    """
    # Consultar y retornar todos los registros de la tabla Song
    return db.query(models.Song).all()

# 2. Obtener canción por id - Endpoint GET para una canción específica
@router.get("/{song_id}", response_model=schemas.Song)
def get_song(song_id: int, db: Session = Depends(get_db)):
    """
    Obtiene una canción específica por su ID.
    
    Args:
        song_id (int): ID de la canción a buscar
        db (Session): Sesión de base de datos inyectada por dependencia
        
    Returns:
        schemas.Song: Canción encontrada
        
    Raises:
        HTTPException: 404 si la canción no existe
    """
    # Buscar la canción por ID en la base de datos
    song = db.query(models.Song).filter(models.Song.id == song_id).first()
    
    # Validar si la canción existe
    if not song:
        # Lanzar excepción HTTP 404 si no se encuentra la canción
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    
    # Retornar la canción encontrada
    return song

# 3. Crear canción - Endpoint POST para agregar nueva canción
@router.post("/", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva canción en la base de datos.
    
    Args:
        song (schemas.SongCreate): Datos de la canción validados por el schema
        db (Session): Sesión de base de datos inyectada por dependencia
        
    Returns:
        schemas.Song: Canción creada con todos sus datos (incluyendo ID generado)
    """
    # Crear una nueva instancia del modelo Song a partir de los datos recibidos
    # song.dict() convierte el objeto Pydantic a diccionario
    # ** expande el diccionario como argumentos nombrados para el constructor
    new_song = models.Song(**song.dict())
    
    # Agregar la nueva canción a la sesión de base de datos
    db.add(new_song)
    
    # Confirmar la transacción para persistir los cambios en la base de datos
    db.commit()
    
    # Refrescar la instancia para obtener cualquier dato generado por la BD (como ID autoincremental)
    db.refresh(new_song)
    
    # Retornar la canción creada (se convierte automáticamente al schema Song)
    return new_song

# 4. Borrar canción - Endpoint DELETE para eliminar una canción
@router.delete("/{song_id}")
def delete_song(song_id: int, db: Session = Depends(get_db)):
    """
    Elimina una canción específica por su ID.
    
    Args:
        song_id (int): ID de la canción a eliminar
        db (Session): Sesión de base de datos inyectada por dependencia
        
    Returns:
        dict: Confirmación de la eliminación con formato JSON
        
    Raises:
        HTTPException: 404 si la canción no existe
    """
    # Buscar la canción por ID en la base de datos
    song = db.query(models.Song).filter(models.Song.id == song_id).first()
    
    # Validar si la canción existe
    if not song:
        # Lanzar excepción HTTP 404 si no se encuentra la canción
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    
    # Eliminar la canción de la sesión de base de datos
    db.delete(song)
    
    # Confirmar la transacción para persistir los cambios en la base de datos
    db.commit()
    
    # Retornar confirmación de la eliminación en formato JSON
    return {"ok": True, "message": "Canción eliminada"}