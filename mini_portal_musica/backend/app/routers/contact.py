# Importación de módulos necesarios de FastAPI
from fastapi import APIRouter, Depends
# Importación de Session para manejar la conexión a la base de datos
from sqlalchemy.orm import Session

# Importación de módulos locales
# schemas: contiene los esquemas Pydantic para validación de datos
from .. import schemas
# get_db_contact: función que proporciona la sesión de base de datos
from ..database_contact import get_db_contact
# Contact: modelo SQLAlchemy para la tabla de contactos
from ..models_contact import Contact

# Creación de un router de FastAPI para agrupar endpoints relacionados
router = APIRouter(
    prefix="/api/contact",  # Prefijo base para todas las rutas en este router
    tags=["contact"]       # Etiqueta para documentación automática en Swagger/OpenAPI
)

# Definición de endpoint POST para crear un nuevo contacto
@router.post("/")
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db_contact)):
    """
    Crea un nuevo contacto en la base de datos.
    
    Args:
        contact (schemas.ContactCreate): Datos del contacto validados por el esquema Pydantic
        db (Session): Sesión de base de datos inyectada por dependencia
        
    Returns:
        dict: Respuesta JSON con estado, mensaje y datos del contacto creado
    """
    
    # Crear una nueva instancia del modelo Contact a partir de los datos recibidos
    # contact.dict() convierte el objeto Pydantic a diccionario
    # ** expande el diccionario como argumentos nombrados para el constructor
    new_contact = Contact(**contact.dict())
    
    # Agregar el nuevo contacto a la sesión de base de datos
    db.add(new_contact)
    
    # Confirmar la transacción para persistir los cambios en la base de datos
    db.commit()
    
    # Refrescar la instancia para obtener cualquier dato generado por la BD (como ID autoincremental)
    db.refresh(new_contact)
    
    # Retornar respuesta JSON con formato consistente
    return {"ok": True, "message": "Contacto guardado", "data": new_contact}


# Definición de endpoint GET para obtener todos los contactos
@router.get("/")
def get_contacts(db: Session = Depends(get_db_contact)):
    """
    Obtiene todos los contactos almacenados en la base de datos.
    
    Args:
        db (Session): Sesión de base de datos inyectada por dependencia
        
    Returns:
        dict: Respuesta JSON con estado y lista de todos los contactos
    """
    
    # Consultar todos los registros de la tabla Contact
    contacts = db.query(Contact).all()
    
    # Retornar respuesta JSON con la lista de contactos
    return {"ok": True, "data": contacts}