from .db_connection import DBConnection, Usuario
from user.domain.user import Usuario as UsuarioDominio

class Repositorio:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()

    def guardar(self, usuario_dominio: UsuarioDominio):
        usuario = Usuario(nombre=usuario_dominio.nombre, email=usuario_dominio.email, password=usuario_dominio.password)
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def obtener_todos(self):
        return self.session.query(Usuario).all()

    def obtener(self, user_id: str):
        usuario = self.session.query(Usuario).get(user_id)
        return usuario

    def actualizar(self, user_id: str, usuario_dominio: UsuarioDominio):
        usuario = self.session.query(Usuario).get(user_id)
        if usuario:
            usuario.nombre = usuario_dominio.nombre
            usuario.email = usuario_dominio.email
            usuario.password = usuario_dominio.password
            self.session.commit()
            return usuario
        return None

    def eliminar(self, user_id: str):
        usuario = self.session.query(Usuario).get(user_id)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
            return True
        return False