from fastapi import APIRouter, HTTPException
from user.application.deleteUserUseCase import deleteUserUseCase

delete_user_router = APIRouter()

def initialize_endpoints(repositorio):
    deleteUserUseCaseById = deleteUserUseCase(repositorio)

    @delete_user_router.delete("/")
    async def eliminar_usuario(user_id: str):
        if not deleteUserUseCaseById.eliminar_usuario(user_id):
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"mensaje": "Usuario eliminado"}
    