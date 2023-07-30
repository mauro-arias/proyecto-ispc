from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime, UniqueConstraint, ForeignKey
from db.db import Base
from datetime import datetime


class Campus(Base):
    __tablename__ = "campus"
    __table_args__ = (UniqueConstraint('estado_id', name='uix_table_estado'),)
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    estado_id = Column(Integer, ForeignKey("estados.id"))
    fecha_alta = Column(DateTime, default=datetime.now)
    fecha_modificacion = Column(
        DateTime, default=datetime.now, onupdate=datetime.now)
    fecha_baja = Column(DateTime, nullable=True)

    estado = relationship("Estado", backref="related_estados_campus")
