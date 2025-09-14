# Importación de módulos necesarios de FastAPI y otras librerías
from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
# Importación de módulos locales (schemas, database, models)
from .. import schemas, database, models
# Importación del cliente OpenAI para interactuar con la API
from openai import OpenAI
# Importación de JSONResponse para respuestas personalizadas
from fastapi.responses import JSONResponse
# Importación de módulos para manejo de JSON y variables de entorno
import json
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env al entorno
load_dotenv()

# Obtener la API key desde las variables de entorno
API_KEY = os.getenv("OPENROUTER_API_KEY")
# Validar que la API key esté presente, sino lanzar error
if not API_KEY:
    raise ValueError("⚠️ No se encontró OPENROUTER_API_KEY en el entorno")

# Creación de un router de FastAPI para agrupar endpoints de recomendaciones
router = APIRouter(
    prefix="/api/recommendations",  # Prefijo base para todas las rutas
    tags=["Recommendations"]        # Etiqueta para documentación automática
)

# Configurar cliente OpenRouter/OpenAI para usar la API de OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",  # URL base de OpenRouter
    api_key=API_KEY                           # API key para autenticación
)

# Dependencia DB - Función que proporciona la sesión de base de datos
def get_db():
    # Crear una nueva sesión de base de datos
    db = database.SessionLocal()
    try:
        # Yield permite usar esta función como dependencia con Depends()
        yield db
    finally:
        # Asegurar que la sesión se cierre siempre, incluso si hay errores
        db.close()


# 1️⃣ Recomendaciones básicas por género
@router.get("/", response_model=list[schemas.Song])
def recommend_songs(genre: str, db: Session = Depends(get_db)):
    """
    Endpoint para obtener recomendaciones de canciones por género.
    
    Args:
        genre (str): Género musical para filtrar las canciones
        db (Session): Sesión de base de datos inyectada por dependencia
        
    Returns:
        list[schemas.Song]: Lista de canciones del género especificado
        
    Raises:
        HTTPException: Si no se encuentran canciones del género especificado
    """
    
    # Consultar canciones que coincidan con el género (búsqueda case-insensitive)
    songs = db.query(models.Song).filter(models.Song.genre.ilike(f"%{genre}%")).all()
    
    # Validar si se encontraron resultados
    if not songs:
        # Lanzar excepción HTTP 404 si no hay canciones
        raise HTTPException(status_code=404, detail="No se encontraron recomendaciones")
    
    # Retornar la lista de canciones (se convierte automáticamente al schema Song)
    return songs


# 2️⃣ Recomendaciones tipo chat usando IA y validando contra BD
@router.post("/chat-recommendations", response_model=list[schemas.Song])
async def chat_recommendations(message: str = Form(...), db: Session = Depends(get_db)):
    """
    Endpoint para obtener recomendaciones mediante IA basadas en un mensaje de texto.
    Usa OpenRouter API para generar recomendaciones y luego valida contra la base de datos.
    
    Args:
        message (str): Mensaje del usuario describiendo sus preferencias musicales
        db (Session): Sesión de base de datos inyectada por dependencia
        
    Returns:
        list[schemas.Song]: Lista de canciones recomendadas por la IA y validadas en BD
        
    Raises:
        HTTPException: Si no hay canciones en la BD o hay errores con la API
    """
    
    # Obtener todos los títulos de canciones disponibles en la base de datos
    todos_titulos = [c.title for c in db.query(models.Song).all()]
    
    # Validar que existan canciones en la base de datos
    if not todos_titulos:
        raise HTTPException(status_code=404, detail="No hay canciones en la base de datos")

    try:
        # Construir el prompt para la IA con el mensaje del usuario y los títulos disponibles
        prompt = f"""
        Eres un recomendador musical experto.
        Basado en el mensaje del usuario: "{message}"
        Solo sugiere canciones de la siguiente lista de títulos disponibles en la base de datos:
        {todos_titulos}
        Responde únicamente con un JSON de títulos válidos, ejemplo: ["titulo1", "titulo2", "titulo3"]
        """
        
        # Hacer la petición a la API de OpenRouter/OpenAI
        respuesta = client.chat.completions.create(
            model="gpt-oss-20b:free",  # Modelo específico de OpenRouter
            messages=[
                {"role": "system", "content": "Eres un recomendador musical experto."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extraer y limpiar la respuesta de la IA
        recomendaciones = respuesta.choices[0].message.content.strip()
        print("RESPUESTA IA:", recomendaciones)  # depuración - para debugging

        try:
            # Intentar parsear la respuesta como JSON
            titulos = json.loads(recomendaciones)
        except Exception as e:
            # Manejar error si la respuesta no es un JSON válido
            print("ERROR PARSEANDO JSON:", e)
            return JSONResponse(content={
                "mensaje": "No se pudo parsear la respuesta de la IA",
                "raw_response": recomendaciones  # Incluir respuesta cruda para debugging
            })

        # Si se obtuvieron títulos válidos, buscar las canciones en la base de datos
        if titulos:
            # Consultar las canciones cuyos títulos estén en la lista de la IA
            songs = db.query(models.Song).filter(models.Song.title.in_(titulos)).all()
            return songs

        # Si no se obtuvieron títulos válidos, retornar mensaje de error
        return JSONResponse(content={
            "mensaje": "No se pudieron obtener recomendaciones válidas",
            "raw_response": recomendaciones
        })

    except Exception as e:
        # Manejo de errores generales de la API
        print("ERROR GENERAL:", e)
        
        # Detectar específicamente errores de autenticación (API key)
        if "401" in str(e):
            raise HTTPException(status_code=500, detail="API Key inválida o expirada")
        
        # Propagrar otros errores con mensaje descriptivo
        raise HTTPException(status_code=500, detail=f"Error IA: {str(e)}")