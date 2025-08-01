from pydantic import BaseModel
from typing import Optional

# ==== ESPECIES ====
class Especie(BaseModel):
    sp_id: int
    reino: Optional[str]
    phydiv: Optional[str]
    clase: Optional[str]
    orden: Optional[str]
    familia: Optional[str]
    nombre_cientifico: Optional[str]
    origen: Optional[str]
    imagen: Optional[str]
    class Config:
        orm_mode = True

# ==== REPORTES ====
class Reporte(BaseModel):
    id: int
    sp_id: int
    latitud: Optional[float]
    longitud: Optional[float]
    fecha: Optional[str]
    hora: Optional[str]
    descripcion: Optional[str]
    imagen: Optional[str]
    especie: Optional[Especie]  # Relación

    class Config:
        orm_mode = True
