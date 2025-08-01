from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
# from sqlalchemy import func
import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

DATABASE_URL = os.getenv("DATABASE_URL")
FRONTEND_URL = os.getenv("FRONTEND_URL")

# ==== Inicialización FastAPI ====
app = FastAPI()

# ==== (Opcional) Habilitar CORS para pruebas con frontend ====
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==== Dependencia para obtener la sesión de DB ====
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==== ENDPOINTS ESPECIES ====

@app.get("/especies/GetAll", response_model=list[schemas.Especie])
def especiesGetAllOrder(db: Session = Depends(get_db)):
    return db.query(models.Especies).order_by(models.Especies.nombre_cientifico).all()

@app.get("/especies/GetByReino/{reino}", response_model=list[schemas.Especie])
def especiesGetByReino(reino: str, db: Session = Depends(get_db)):
    return db.query(models.Especies).filter(models.Especies.reino == reino).order_by(models.Especies.nombre_cientifico).all()

@app.get("/especies/GetByReinoTodos/{reino}", response_model=list[schemas.Especie])
def especiesGetByReinoTodos(reino: str, db: Session = Depends(get_db)):
    query = db.query(models.Especies).order_by(models.Especies.nombre_cientifico)
    if reino == "TODOS":
        return query.all()
    return query.filter(models.Especies.reino == reino).all()

# ==== ENDPOINTS REPORTES ====
@app.get("/reportes/GetAll", response_model=list[schemas.Reporte])
def reportesGetAllOrder(db: Session = Depends(get_db)):
    return db.query(models.Reportes).order_by(models.Reportes.id).all()

@app.post("/reportes/", response_model=schemas.Reporte)
def crear_reporte(reporte: schemas.Reporte, db: Session = Depends(get_db)):
    nuevo = models.Reportes(**reporte.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
