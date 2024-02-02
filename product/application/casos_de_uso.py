from product.domain.product import Producto

class ProductUseCases:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def crear_producto(self, nombre: str, precio: str):
        producto = Producto(nombre, precio)
        return self.repositorio.guardar(producto)

    def obtener_productos(self):
        return self.repositorio.obtener_todos()

    def obtener_producto(self, product_id: str):
        return self.repositorio.obtener(product_id)

    def actualizar_producto(self, product_id: str, nombre: str, precio: str):
        producto = Producto(nombre, precio)
        return self.repositorio.actualizar(product_id, producto)

    def eliminar_producto(self, product_id: str):
        return self.repositorio.eliminar(product_id)