from sqlalchemy import Column, String, Integer, UniqueConstraint
from db.db import Base


class Estado(Base):
    __tablename__ = "estados"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
