from sqlalchemy import Column, String, Integer, DateTime
from db.db import Base
from datetime import datetime


class Campus(Base):
    __tablename__ = "campus"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    fecha_alta = Column(DateTime, default=datetime.now)
    fecha_modificacion = Column(
        DateTime, default=datetime.now, onupdate=datetime.now)
    fecha_baja = Column(DateTime, nullable=True)
