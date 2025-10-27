from sqlalchemy import Integer,String,Column,ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Embeddings(Base):
    __tablename__ = "embeddings"
    id = Column(Integer, primary_key=True, index=True)
    #file_id = Column(Integer)
    chunk_index = Column(Integer)
    content=Column(String)
    embedding = Column(String)
    created_at = Column(String) 
    file_id = Column(Integer, ForeignKey("files.id"))  # 👈 FK to files table
    file = relationship("models.file.File", back_populates="embeddings")

