# → Configuración de la conexión a la base de datos con SQLAlchemy.
# Este módulo configura la conexión principal a la base de datos de la aplicación

# Importación de módulos de SQLAlchemy para la configuración de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Importación del módulo os para manejo de rutas del sistema operativo
import os


# Usaremos SQLite (archivo local) - Configuración para base de datos SQLite embebida
# Calcular la ruta base del proyecto (dos niveles arriba del archivo actual)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Construir la ruta completa al archivo de base de datos songs.db
DB_PATH = os.path.join(BASE_DIR, "songs.db")

# Crear la URL de conexión para SQLAlchemy en formato SQLite
# sqlite:/// indica que es una base de datos SQLite y / especifica la ruta del archivo
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"


# Crear el motor de base de datos de SQLAlchemy
# El motor es el punto de entrada principal para las operaciones de la base de datos
# Maneja el pool de conexiones y la ejecución de SQL
engine = create_engine(
    # URL de conexión a la base de datos
    SQLALCHEMY_DATABASE_URL,
    # Argumento específico para SQLite que permite múltiples hilos
    # False permite que la misma conexión sea usada por múltiples hilos
    connect_args={"check_same_thread": False}
)

# Crear una fábrica de sesiones configurada
# SessionLocal es una clase que crea nuevas sesiones de base de datos
SessionLocal = sessionmaker(
    autocommit=False,    # Desactivar autocommit - las transacciones deben ser explicitas
    autoflush=False,     # Desactivar autoflush - los flush deben ser explicitos
    bind=engine          # Vincular esta fábrica de sesiones al motor creado
)

# Crear la clase base para los modelos de la base de datos
# Todas las clases de modelos (tablas) heredarán de esta clase
Base = declarative_base()

# Función dependencia para obtener una sesión de base de datos
def get_db():
    """
    Provee una sesión de base de datos para cada request.
    Se asegura de cerrar la sesión al finalizar el request.
    
    Yields:
        Session: Sesión de base de datos SQLAlchemy
        
    Note:
        Esta función está diseñada para ser usada con Depends() en FastAPI
        para inyección de dependencias automática. FastAPI maneja el ciclo de vida
        de la sesión automáticamente por cada request.
    """
    # Crear una nueva sesión de base de datos usando la fábrica de sesiones
    db = SessionLocal()
    try:
        # Yield permite usar esta función como generador para inyección de dependencias
        # FastAPI llamará a esta función para obtener una sesión por request
        yield db
    finally:
        # Bloque finally asegura que la sesión se cierre siempre, incluso si hay errores
        # Esto previene fugas de conexiones a la base de datos y asegura la integridad
        db.close()