from fastapi import APIRouter
from user.application.createUserUseCase import CreateUserUseCase
from user.domain.Models.Usuario import Usuario

crear_usuario_router = APIRouter()

def initialize_endpoints(repositorio):
    createUserUsercase = CreateUserUseCase(repositorio)

    @crear_usuario_router.post("/")
    async def crear_usuario(usuario: Usuario):
        usuario_creado = createUserUsercase.crear_usuario(usuario.name,usuario.last_name, usuario.cellphone,usuario.email, usuario.password)
        return {"mensaje": "Porfavor verifique el email para activar cuenta", "\nusuario": usuario_creado}