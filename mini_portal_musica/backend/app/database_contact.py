# → Configuración de la conexión a la base de datos para contactos (contact.db)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# Base de datos separada
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "contact.db")

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocalContact = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseContact = declarative_base()

def get_db_contact():
    db = SessionLocalContact()
    try:
        yield db
    finally:
        db.close()


# Crear todas las tablas (si no existen)
BaseContact.metadata.create_all(bind=engine)
