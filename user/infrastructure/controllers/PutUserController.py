from fastapi import APIRouter, HTTPException
from user.application.updateUserUseCase import updateUserUseCase
from user.domain.Models.Usuario import Usuario
from user.infrastructure.security.utils import get_hashed_password

update_user_router = APIRouter()

def initialize_endpoints(repositorio):
    updateUserUseCaseById = updateUserUseCase(repositorio)

    @update_user_router.put("/")
    async def actualizar_usuario(user_id: str, usuario: Usuario):
        usuario_actualizado = updateUserUseCaseById.actualizar_usuario(user_id, usuario.nombre, usuario.email, get_hashed_password(usuario.password))
        if usuario_actualizado is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario_actualizado