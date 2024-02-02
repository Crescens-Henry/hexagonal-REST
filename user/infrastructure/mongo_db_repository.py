from mongoengine import Document, StringField, DoesNotExist
from .db_connection import DBConnection
from user.domain.user import Usuario as UsuarioDominio

class Usuario(Document):
    nombre = StringField(required=True)
    apellido = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)

class Repositorio:
    def __init__(self):
        self.connection = DBConnection()

    def guardar(self, usuario_dominio: UsuarioDominio):
        usuario = Usuario(nombre=usuario_dominio.nombre, apellido=usuario_dominio.apellido, email=usuario_dominio.email, password=usuario_dominio.password)
        usuario.save()
        return usuario

    def obtener_todos(self):
        return [{**usuario.to_mongo().to_dict(), "_id": str(usuario.id)} for usuario in Usuario.objects.all()]

    def obtener(self, user_id: str):
        try:
            usuario = Usuario.objects.get(id=user_id)
            return {**usuario.to_mongo().to_dict(), "_id": str(usuario.id)}
        except DoesNotExist:
            return None

    def actualizar(self, user_id: str, usuario_dominio: UsuarioDominio):
        try:
            usuario = Usuario.objects.get(id=user_id)
            usuario.update(nombre=usuario_dominio.nombre, apellido=usuario_dominio.apellido, email=usuario_dominio.email, password=usuario_dominio.password)
            return usuario.reload()
        except DoesNotExist:
            return None

    def eliminar(self, user_id: str):
        try:
            usuario = Usuario.objects.get(id=user_id)
            usuario.delete()
            return True
        except DoesNotExist:
            return False