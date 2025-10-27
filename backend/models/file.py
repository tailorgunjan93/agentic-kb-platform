# models/file.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    embeddings = relationship("models.chunk.Embeddings", back_populates="file")