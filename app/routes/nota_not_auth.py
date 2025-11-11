from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.database.database import DBConnection
from app.services.usuario import UsuarioService
from app.services.notas import NotasService

router = APIRouter(
    prefix="/notasnotauth", tags=["Notas not auth"]
)


db_connection = DBConnection()
usuario_service = UsuarioService()
notas_service = NotasService()

# rota para vizualizão de nota sem autenticação

@router.get("/{id}")
def buscar_nota(id: str):

    notas = db_connection.find_one(
         "notas", 
        {"id": id},  
        {"_id": 0}
    )
    return JSONResponse(notas)
