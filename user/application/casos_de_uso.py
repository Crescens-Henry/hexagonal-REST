# user/application/casos_de_uso.py
from user.domain.user import Usuario

class UserUseCases:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def crear_usuario(self, nombre: str, apellido: str, email: str, password: str):
        usuario = Usuario(nombre, apellido, email, password)
        return self.repositorio.guardar(usuario)

    def obtener_usuarios(self):
        return self.repositorio.obtener_todos()

    def obtener_usuario(self, user_id: str):
        return self.repositorio.obtener(user_id)

    def actualizar_usuario(self, user_id: str, nombre: str, apellido: str, email: str, password: str):
        usuario = Usuario(nombre, apellido, email, password)
        return self.repositorio.actualizar(user_id, usuario)

    def eliminar_usuario(self, user_id: str):
        return self.repositorio.eliminar(user_id)