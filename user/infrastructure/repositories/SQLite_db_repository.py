from datetime import datetime
from databases.SQLite.db_connection import DBConnection, Usuario
from user.domain.entities.user import Usuario as UsuarioDominio
from user.infrastructure.security.utils import get_hashed_password

class Repositorio:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()

    def guardar(self, usuario_dominio: UsuarioDominio):
        usuario = Usuario( name=usuario_dominio.name,last_name= usuario_dominio.last_name,cellphone =str( usuario_dominio.cellphone), email=usuario_dominio.email, password=usuario_dominio.password, verified_at=usuario_dominio.verified_at, uuid=usuario_dominio.uuid, verificado=usuario_dominio.verificado)
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
            usuario.name = usuario_dominio.name
            usuario.last_name = usuario_dominio.last_name
            usuario.cellphone = str(usuario_dominio.cellphone)
            usuario.email = usuario_dominio.email
            usuario.password = get_hashed_password(usuario_dominio.password)
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
    
    def obtener_por_uuid(self, uuid):
        usuario = self.session.query(Usuario).filter_by(uuid=uuid).first()
        return usuario
    
    def verificar_usuario(self, uuid):
        try:
            usuario = self.session.query(Usuario).filter_by(uuid=uuid).one()
            self.session.query(Usuario).filter_by(id=usuario.id).update({Usuario.verificado: True,  Usuario.verified_at: datetime.now().isoformat()})
            self.session.commit()
            return usuario
        except:
            return None