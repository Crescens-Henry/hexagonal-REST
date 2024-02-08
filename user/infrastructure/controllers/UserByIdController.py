from fastapi import APIRouter, HTTPException
from user.application.GetUserUseCase import GetUserUseCase

get_user_by_id_router = APIRouter()

def initialize_endpoints(repositorio):
    getUserUseCase = GetUserUseCase(repositorio)

    @get_user_by_id_router.get("/")
    async def obtener_usuario(user_id: str):
        usuario = getUserUseCase.obtener_usuario(user_id)
        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario