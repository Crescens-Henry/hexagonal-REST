from fastapi import APIRouter
from user.application.updateUserUseCase import updateUserUseCase
from user.domain.Models.Usuario import Usuario

update_user_router = APIRouter()

def initialize_endpoints(repositorio):
    updateUserUseCaseById = updateUserUseCase(repositorio)

    @update_user_router.put("/")
    async def actualizar_usuario(user_id: str, usuario: Usuario):
        usuario_actualizado = updateUserUseCaseById.actualizar_usuario(user_id, usuario.name, usuario.last_name, usuario.cellphone,usuario.email,usuario.password)
        return usuario_actualizado
        