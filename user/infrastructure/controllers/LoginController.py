from fastapi import APIRouter, HTTPException
from user.application.LoginUserUseCase import AuthenticationUserUseCase
from user.domain.Models.Login import Login

login_router = APIRouter()

def initialize_endpoints(repositorio): 
    authenticationUserUseCase = AuthenticationUserUseCase(repositorio)
    
    @login_router.post("/")
    async def login(login: Login):
        usuario = authenticationUserUseCase.autenticar_usuario(login.email, login.password)
        if usuario is None:
            raise HTTPException(status_code=400, detail="Email o contraseña incorrectos")
        return {"usuario": usuario}