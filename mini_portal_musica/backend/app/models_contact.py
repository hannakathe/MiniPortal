# Importación de los tipos de columnas de SQLAlchemy y la clase base
from sqlalchemy import Column, Integer, String, Text
# Importación de la clase base declarativa para la base de datos de contactos
from .database_contact import BaseContact

# Definición del modelo Contact que representa la tabla en la base de datos
class Contact(BaseContact):
    """
    Modelo SQLAlchemy para la tabla 'contacts' en la base de datos de contactos.
    
    Esta clase representa la estructura de la tabla que almacenará los mensajes
    de contacto recibidos a través del formulario.
    
    Attributes:
        id (int): Identificador único autoincremental de cada contacto
        nombre (str): Nombre de la persona que envía el mensaje
        email (str): Dirección de email de contacto
        mensaje (str): Texto del mensaje (puede ser largo, por eso Text)
    """
    
    # Nombre de la tabla en la base de datos
    __tablename__ = "contacts"

    # Columna ID - Llave primaria autoincremental con índice
    # primary_key=True: Identificador único de cada registro
    # index=True: Crea un índice para búsquedas más rápidas por ID
    id = Column(Integer, primary_key=True, index=True)
    
    # Columna nombre - String de longitud variable
    # nullable=False: Campo obligatorio, no puede ser NULL en la base de datos
    nombre = Column(String, nullable=False)
    
    # Columna email - String de longitud variable
    # nullable=False: Campo obligatorio, no puede ser NULL en la base de datos
    email = Column(String, nullable=False)
    
    # Columna mensaje - Texto de longitud ilimitada (para mensajes largos)
    # Text: Tipo de dato para textos largos (diferente de String que tiene límite)
    # nullable=False: Campo obligatorio, no puede ser NULL en la base de datos
    mensaje = Column(Text, nullable=False)