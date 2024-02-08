from user.infrastructure.security.utils import verify_password

class AuthenticationUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def autenticar_usuario(self, email: str, password: str):
        usuario = self.repositorio.obtener_por_email(email)
        if usuario is not None:
            if isinstance(usuario, dict):
                password_valida = verify_password(password, usuario['password'])
            else:
                password_valida = verify_password(password, usuario.password)
            if password_valida:
                return usuario
        return None