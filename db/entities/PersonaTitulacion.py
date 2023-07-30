from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.db import Base


class PersonaTitulacion(Base):
    __tablename__ = "personas_titulaciones"
    id = Column(Integer, primary_key=True)
    persona_id = Column(Integer, ForeignKey("personas.id"))
    titulacion_id = Column(Integer, ForeignKey("titulaciones.id"))
    tipo_id = Column(Integer, ForeignKey("tipos_persona.id"))
    fecha_alta = Column(DateTime, default=datetime.now)
    fecha_modificacion = Column(
        DateTime, default=datetime.now, onupdate=datetime.now)
    fecha_baja = Column(DateTime, nullable=True)

    persona = relationship("Persona", backref="related_personas")
    titulacion = relationship("Titulacion", backref="related_titulaciones")
    tipopersona = relationship("TipoPersona", backref="related_tipos_persona")
