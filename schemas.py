from pydantic import BaseModel
from typing import Optional

# ==== ESPECIES ====

class EspecieBase(BaseModel):
    reino: Optional[str]
    phydiv: Optional[str]
    clase: Optional[str]
    orden: Optional[str]
    familia: Optional[str]
    nombre_cientifico: Optional[str]
    origen: Optional[str]
    imagen: Optional[str]

class EspecieCreate(EspecieBase):
    pass

class Especie(EspecieBase):
    sp_id: int

    model_config = {
        "from_attributes": True
    }

# ==== REPORTES ====

class ReporteBase(BaseModel):
    sp_id: int
    latitud: Optional[float]
    longitud: Optional[float]
    fecha: Optional[str]
    hora: Optional[str]
    descripcion: Optional[str]
    imagen: Optional[str]

class ReporteCreate(ReporteBase):
    pass

class Reporte(ReporteBase):
    id: int

    model_config = {
        "from_attributes": True
    }
