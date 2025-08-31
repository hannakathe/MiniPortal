# → Modelos de la base de datos con SQLAlchemy.

""" Database models using SQLAlchemy ORM.
Aquí defines cómo se guardan las tablas."""

from sqlalchemy import Column, Integer, String
from .database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    artist = Column(String, index=True, nullable=False)
    album = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    genre = Column(String, nullable=True)

