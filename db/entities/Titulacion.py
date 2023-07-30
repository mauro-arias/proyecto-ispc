from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, UniqueConstraint, ForeignKey, DateTime
from db.db import Base
from datetime import datetime


class Titulacion(Base):
    __tablename__ = "titulaciones"
    __table_args__ = (UniqueConstraint('carrera_id', 'facultad_id', 'universidad_id',
                      'campus_id', name='uix_table_carrera_facultad_universidad_campus_estado'),)
    id = Column(Integer, primary_key=True)
    carrera_id = Column(Integer, ForeignKey("carreras.id"))
    facultad_id = Column(Integer, ForeignKey("facultades.id"))
    universidad_id = Column(Integer, ForeignKey("universidades.id"))
    campus_id = Column(Integer, ForeignKey("campus.id"))
    estado_id = Column(Integer, ForeignKey("estados.id"))
    fecha_alta = Column(DateTime, default=datetime.now)
    fecha_modificacion = Column(
        DateTime, default=datetime.now, onupdate=datetime.now)
    fecha_baja = Column(DateTime, nullable=True)

    carrera = relationship("Carrera", backref="related_carreras")
    facultad = relationship("Facultad", backref="related_facultades")
    universidad = relationship("Universidad", backref="related_universidades")
    campus = relationship("Campus", backref="related_campus")
    estado = relationship("Estado", backref="related_estados_titulaciones")
