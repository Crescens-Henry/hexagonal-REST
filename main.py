# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from product.application.casos_de_uso import ProductUseCases
from product.infrastructure.mongo_db_repository import Repositorio

app = FastAPI()
repositorio = Repositorio()
casos_de_uso = ProductUseCases(repositorio)

class Producto(BaseModel):
    nombre: str
    precio: float

@app.post("/api/products")
async def crear_producto(producto: Producto):
    producto_creado = casos_de_uso.crear_producto(producto.nombre, producto.precio)
    return {"mensaje": "Usuario creado", "producto": producto_creado}

@app.get("/api/products")
async def obtener_productos():
    return casos_de_uso.obtener_productos()

@app.get("/api/products/{product_id}")
async def obtener_producto(product_id: str):
    producto = casos_de_uso.obtener_producto(product_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return producto

@app.put("/api/products/{product_id}")
async def actualizar_producto(product_id: str, producto: Producto):
    producto_actualizado = casos_de_uso.actualizar_producto(product_id, producto.nombre, producto.precio)
    if producto_actualizado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return producto_actualizado

@app.delete("/api/products/{product_id}")
async def eliminar_producto(product_id: str):
    if not casos_de_uso.eliminar_producto(product_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)