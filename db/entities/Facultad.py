from sqlalchemy import Column, String, Integer, DateTime
from db.db import Base
from datetime import datetime


class Facultad(Base):
    __tablename__ = "facultades"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    fecha_alta = Column(DateTime, default=datetime.now)
    fecha_modificacion = Column(
        DateTime, default=datetime.now, onupdate=datetime.now)
