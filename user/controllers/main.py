from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()
class Login(BaseModel):
    email: str
    password: str
class Usuario(BaseModel):
    nombre: str
    email: str
    password: str

def initialize_endpoints(casos_de_uso):
    @router.post("/api/users")
    async def crear_usuario(usuario: Usuario):
        usuario_creado = casos_de_uso.crear_usuario(usuario.nombre, usuario.email, usuario.password)
        casos_de_uso.enviar_email(usuario_creado.email, usuario_creado)
        return {"mensaje": "Porfavor verifique el email para verificar", "\nusuario": usuario_creado}

    @router.post("/verificar/{uuid}")
    async def verificar(uuid: str):
        if casos_de_uso.verificar_usuario(uuid):
            return {"message": "Cuenta verificada"}
        else:
            return {"message": "No se encontró el usuario"}

    @router.get("/api/users")
    async def obtener_usuarios():
        return casos_de_uso.obtener_usuarios()

    @router.get("/api/users/{user_id}")
    async def obtener_usuario(user_id: str):
        usuario = casos_de_uso.obtener_usuario(user_id)
        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario

    @router.put("/api/users/{user_id}")
    async def actualizar_usuario(user_id: str, usuario: Usuario):
        usuario_actualizado = casos_de_uso.actualizar_usuario(user_id, usuario.nombre, usuario.email, usuario.password)
        if usuario_actualizado is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario_actualizado

    @router.delete("/api/users/{user_id}")
    async def eliminar_usuario(user_id: str):
        if not casos_de_uso.eliminar_usuario(user_id):
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"mensaje": "Usuario eliminado"}

    @router.post("/api/login")
    async def login(login: Login):
        usuario = casos_de_uso.autenticar_usuario(login.email, login.password)
        if usuario is None:
            raise HTTPException(status_code=400, detail="Email o contraseña incorrectos")
        return {"mensaje": "Login exitoso", "usuario": usuario}