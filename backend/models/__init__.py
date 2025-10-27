"""Models package - imports all models to ensure they're registered"""
from models.base import Base
from models.file import File
from models.chunk import Embeddings

__all__ = ['Base', 'File', 'Embeddings']
