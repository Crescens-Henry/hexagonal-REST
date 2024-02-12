from datetime import datetime
from databases.SQLite.db_connection import DBConnection, Usuario
from user.domain.Entity.Contact import Contact
from user.domain.Entity.Credential import Credential
from user.domain.Entity.user import User as UsuarioDominio
from databases.SQLite.db_connection import DBConnection

class Repositorio:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()

    def guardar(self, usuario_dominio: UsuarioDominio):
        usuario = Usuario(
            name=usuario_dominio.contact.name,
            last_name=usuario_dominio.contact.last_name,
            cellphone=str(usuario_dominio.contact.cellphone),
            email=usuario_dominio.credentials.email,
            password=usuario_dominio.credentials.password,
            token_uuid=usuario_dominio.status.token_uuid,
            verified=usuario_dominio.status.verified,
        )
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def obtener_todos(self):
        return self.session.query(Usuario).all()

    def obtener(self, user_id: str):
        usuario = self.session.query(Usuario).get(user_id)
        return usuario

    def actualizar(self, user_id: str, contact: Contact, credentials: Credential):
        usuario = self.session.query(Usuario).get(user_id)
        if usuario:
            usuario.name = contact.name
            usuario.last_name = contact.last_name
            usuario.cellphone = str(contact.cellphone)
            usuario.email = credentials.email
            usuario.password = credentials.password
            self.session.commit()
            self.session.refresh(usuario)
        return usuario

    def eliminar(self, user_id: str):
        usuario = self.session.query(Usuario).get(user_id)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
            return True
        return False

    def obtener_por_email(self, email):
        usuario = self.session.query(Usuario).filter_by(email=email).first()
        return usuario
    
    def obtener_por_uuid(self, token_uuid):
        usuario = self.session.query(Usuario).filter_by(token_uuid=token_uuid).first()
        return usuario

    def verificar_usuario(self, token_uuid):
        try:
            usuario = self.session.query(Usuario).filter_by(token_uuid=token_uuid).one()
            self.session.query(Usuario).filter_by(id=usuario.id).update({Usuario.verified: True,  Usuario.verified_at: datetime.now()})
            self.session.commit()
            return usuario
        except:
            print ("Error")
            return None