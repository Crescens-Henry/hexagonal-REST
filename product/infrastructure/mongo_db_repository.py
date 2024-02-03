from .db_connection import DBConnection
from product.domain.product import Producto as ProductoDominio
from mongoengine import Document, StringField, FloatField, DoesNotExist

class Producto(Document):
    nombre = StringField(required=True)
    precio = FloatField(required=True)
    

class Repositorio:
    def __init__(self):
        self.connection = DBConnection()

    def guardar(self, producto_dominio: ProductoDominio):
        producto = Producto(nombre=producto_dominio.nombre, precio=producto_dominio.precio)
        producto.save()
        return producto

    def obtener_todos(self):
        return [{**producto.to_mongo().to_dict(), "_id": str(producto.id)} for producto in Producto.objects.all()]

    def obtener(self, product_id: str):
        try:
            producto = Producto.objects.get(id=product_id)
            return {**producto.to_mongo().to_dict(), "_id": str(producto.id)}
        except DoesNotExist:
            return None

    def actualizar(self, product_id: str, producto_dominio: ProductoDominio):
        try:
            producto = Producto.objects.get(id=product_id)
            producto.update(nombre=producto_dominio.nombre, precio=producto_dominio.precio)
            return producto.reload()
        except DoesNotExist:
            return None

    def eliminar(self, product_id: str):
        try:
            producto = Producto.objects.get(id=product_id)
            producto.delete()
            return True
        except DoesNotExist:
            return False