from fastapi import APIRouter
from .. import schemas

router = APIRouter(
    prefix="/api/contact",
    tags=["Contact"]
)

# Guardamos los mensajes de contacto en memoria temporalmente
contacts_db = []

@router.post("/", response_model=schemas.Contact)
def send_contact(contact: schemas.Contact):
    contacts_db.append(contact.dict())
    return contact
