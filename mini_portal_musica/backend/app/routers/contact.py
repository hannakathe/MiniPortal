from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database_contact import get_db_contact
from ..models_contact import Contact

router = APIRouter(
    prefix="/api/contact",
    tags=["contact"]
)

@router.post("/")
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db_contact)):
    new_contact = Contact(**contact.dict())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"ok": True, "message": "Contacto guardado", "data": new_contact}


@router.get("/")
def get_contacts(db: Session = Depends(get_db_contact)):
    contacts = db.query(Contact).all()
    return {"ok": True, "data": contacts}
