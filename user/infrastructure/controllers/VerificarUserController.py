from fastapi import APIRouter
from user.application.verificationUserUseCase import VerificationUserUseCase

verificar_usuario_router = APIRouter()

def initialize_endpoints(repositorio):
    verificationUserUseCase = VerificationUserUseCase(repositorio)


    @verificar_usuario_router.put("/")
    async def verificar(uuid: str):
            if verificationUserUseCase.verificar_usuario(uuid):
                return {"message": "Cuenta verificada"}
            else:
                return {"message": "No se encontró el usuario"}