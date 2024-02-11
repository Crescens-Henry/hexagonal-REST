from datetime import datetime
from mongoengine import Document, StringField, DoesNotExist, IntField, SequenceField, BooleanField, DateTimeField
from databases.MongoDB.db_connection import DBConnection
from user.domain.entities.user import Usuario as UsuarioDominio
from user.infrastructure.security.utils import get_hashed_password

class Contador(Document):
    contador = IntField(default=1)

class Usuario(Document):
    id = SequenceField(primary_key=True)
    name = StringField(required=True)
    last_name = StringField(required=True)
    cellphone = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    verified_at = DateTimeField()
    uuid = StringField(request=True, unique=True)
    verificado = BooleanField(default=False)

class Repositorio:
    def __init__(self):
        self.connection = DBConnection()

    def guardar(self, usuario_dominio: UsuarioDominio):
        contador = Contador.objects.first()
        if not contador:
            contador = Contador().save()
        else:
            contador.update(inc__contador=1)

        usuario = Usuario(id=contador.contador, name=usuario_dominio.name,last_name= usuario_dominio.last_name,cellphone =str( usuario_dominio.cellphone), email=usuario_dominio.email, password=usuario_dominio.password, verified_at=usuario_dominio.verified_at, uuid=usuario_dominio.uuid, verificado=usuario_dominio.verificado)
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
            usuario.update(
                name=str(usuario_dominio.name),
                last_name=str(usuario_dominio.last_name),
                cellphone=str(usuario_dominio.cellphone),
                email=str(usuario_dominio.email),
                password=str(usuario_dominio.password)
            )
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
    
    def obtener_por_email(self, email):
        try:
            usuario = Usuario.objects.get(email=email)
            return {**usuario.to_mongo().to_dict(), "_id": str(usuario.id)}
        except DoesNotExist:
            return None
        
    def obtener_por_uuid(self, uuid):
        try:
            usuario = Usuario.objects.get(uuid=uuid)
            return {**usuario.to_mongo().to_dict(), "_id": str(usuario.id)}
        except DoesNotExist:
            return None
        
    def verificar_usuario(self, uuid):
        try:
            usuario = Usuario.objects.get(uuid=uuid)
            usuario.update(verificado=True, verified_at=datetime.now().isoformat())
            return usuario.reload()
        except DoesNotExist:
            return None