from fastapi import APIRouter, Body
from user.application.createUserUseCase import CreateUserUseCase
from user.domain.Entity.user import User

crear_usuario_router = APIRouter()

def initialize_endpoints(repositorio):
    createUserUsercase = CreateUserUseCase(repositorio)

    @crear_usuario_router.post("/")
    async def crear_usuario(user: User = Body(...)):
        usuario_creado = createUserUsercase.crear_usuario(user)
        return {"mensaje": "Porfavor verifique el email para activar cuenta", "\nusuario": usuario_creado}