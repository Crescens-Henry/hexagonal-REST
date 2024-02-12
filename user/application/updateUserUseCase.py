from user.domain.Entity.Contact import Contact
from user.domain.Entity.Credential import Credential
from user.infrastructure.security.utils import get_hashed_password

class updateUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def actualizar_usuario(self, user_id: str, contact: Contact, credentials: Credential):
        usuario = self.repositorio.obtener(user_id)
        if usuario is None:
            return {"error": "Usuario no encontrado."}

        usuario.contact = contact
        usuario.credentials = Credential(email=credentials.email, password=get_hashed_password(credentials.password))

        contact = usuario.contact
        credentials = usuario.credentials

        return self.repositorio.actualizar(user_id, contact, credentials)