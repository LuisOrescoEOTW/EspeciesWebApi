from sqlalchemy import Column, Integer, String, ForeignKey, Float
from database import Base
from sqlalchemy.orm import relationship

class Especies(Base):
    __tablename__ = "especies"
    
    sp_id = Column(Integer, primary_key=True, index=True)
    reino = Column(String)
    phydiv = Column(String)
    clase = Column(String)
    orden = Column(String)
    familia = Column(String)
    nombre_cientifico = Column(String)
    origen = Column(String)
    imagen = Column(String)

class Reportes(Base):
    __tablename__ = "reportes"
    
    id = Column(Integer, primary_key=True, index=True)
    sp_id = Column(Integer, ForeignKey("especies.sp_id"))  # clave foránea
    latitud = Column(Float)
    longitud = Column(Float)
    fecha = Column(String)
    hora = Column(String)
    descripcion= Column(String)
    imagen= Column(String) 
    especie = relationship("Especies")  # relación con Especies