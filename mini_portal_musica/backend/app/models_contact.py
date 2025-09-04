from sqlalchemy import Column, Integer, String, Text
from .database_contact import BaseContact

class Contact(BaseContact):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    mensaje = Column(Text, nullable=False)
