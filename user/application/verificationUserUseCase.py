from user.application.utils.singleton import Singleton
from user.infrastructure.security.utils import get_hashed_password


class VerificationUserUseCase:
    def __init__(self, repositorio):
        self.singleton = Singleton.getInstance()
        self.repositorio = repositorio

    def verificar_usuario(self, uuid: str):
        usuario = self.singleton.usuarios_temporales.pop(uuid, None)
        if usuario is not None:
            usuario.verificado = True
            usuario.password = get_hashed_password(usuario.password)
            self.repositorio.guardar(usuario)
            return True
        return False