from fastapi import APIRouter
from user.application.updateUserUseCase import updateUserUseCase
from user.domain.Entity.Contact import Contact
from user.domain.Entity.Credential import Credential

update_user_router = APIRouter()

def initialize_endpoints(repositorio):
    updateUserUseCaseById = updateUserUseCase(repositorio)

    @update_user_router.put("/")
    async def actualizar_usuario(user_id: str, contact: Contact, credentials: Credential):
        usuario_actualizado = updateUserUseCaseById.actualizar_usuario(user_id, contact, credentials)
        return usuario_actualizado