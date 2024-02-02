# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from user.application.casos_de_uso import UserUseCases
from user.infrastructure.mongo_db_repository import Repositorio

app = FastAPI()
repositorio = Repositorio()
casos_de_uso = UserUseCases(repositorio)

class Usuario(BaseModel):
    nombre: str
    apellido: str
    email: str
    password: str

@app.post("/api/users")
async def crear_usuario(usuario: Usuario):
    usuario_creado = casos_de_uso.crear_usuario(usuario.nombre, usuario.apellido, usuario.email, usuario.password)
    return {"mensaje": "Usuario creado", "usuario": usuario_creado}

@app.get("/api/users")
async def obtener_usuarios():
    return casos_de_uso.obtener_usuarios()

@app.get("/api/users/{user_id}")
async def obtener_usuario(user_id: str):
    usuario = casos_de_uso.obtener_usuario(user_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.put("/api/users/{user_id}")
async def actualizar_usuario(user_id: str, usuario: Usuario):
    usuario_actualizado = casos_de_uso.actualizar_usuario(user_id, usuario.nombre, usuario.apellido, usuario.email, usuario.password)
    if usuario_actualizado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_actualizado

@app.delete("/api/users/{user_id}")
async def eliminar_usuario(user_id: str):
    if not casos_de_uso.eliminar_usuario(user_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)