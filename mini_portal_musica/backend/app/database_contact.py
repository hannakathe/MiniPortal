# → Configuración de la conexión a la base de datos para contactos (contact.db)
# Este módulo configura la conexión a una base de datos SQLite separada para contactos

# Importación de módulos de SQLAlchemy para la configuración de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Importación del módulo os para manejo de rutas del sistema operativo
import os


# Base de datos separada - Configuración para una base de datos dedicada a contactos
# Calcular la ruta base del proyecto (dos niveles arriba del archivo actual)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Construir la ruta completa al archivo de base de datos contact.db
DB_PATH = os.path.join(BASE_DIR, "contact.db")

# Crear la URL de conexión para SQLAlchemy en formato SQLite
# sqlite:/// indica que es una base de datos SQLite y / especifica la ruta del archivo
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# Crear el motor de base de datos de SQLAlchemy
# El motor es el punto de entrada principal para las operaciones de la base de datos
engine = create_engine(
    # URL de conexión a la base de datos
    SQLALCHEMY_DATABASE_URL,
    # Argumento específico para SQLite que permite múltiples hilos
    # False permite que la misma conexión sea usada por múltiples hilos
    connect_args={"check_same_thread": False}
)

# Crear una fábrica de sesiones configurada para la base de datos de contactos
# SessionLocalContact es una clase que crea nuevas sesiones de base de datos
SessionLocalContact = sessionmaker(
    autocommit=False,    # Desactivar autocommit - las transacciones deben ser explicitas
    autoflush=False,     # Desactivar autoflush - los flush deben ser explicitos
    bind=engine          # Vincular esta fábrica de sesiones al motor creado
)

# Crear la clase base para los modelos de la base de datos de contactos
# Todas las clases de modelos para contactos heredarán de esta clase
BaseContact = declarative_base()

# Función dependencia para obtener una sesión de base de datos de contactos
def get_db_contact():
    """
    Provee una sesión de base de datos para contactos para cada request.
    Se asegura de cerrar la sesión al finalizar el request.
    
    Yields:
        Session: Sesión de base de datos SQLAlchemy para la base de contactos
        
    Note:
        Esta función está diseñada para ser usada con Depends() en FastAPI
        para inyección de dependencias automática
    """
    # Crear una nueva sesión de base de datos usando la fábrica de sesiones
    db = SessionLocalContact()
    try:
        # Yield permite usar esta función como generador para inyección de dependencias
        # FastAPI llamará a esta función para obtener una sesión por request
        yield db
    finally:
        # Bloque finally asegura que la sesión se cierre siempre, incluso si hay errores
        # Esto previene fugas de conexiones a la base de datos
        db.close()


# Crear todas las tablas en la base de datos (si no existen)
# Esto asegura que los modelos definidos estén disponibles como tablas en la BD
BaseContact.metadata.create_all(bind=engine)