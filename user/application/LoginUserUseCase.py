from user.infrastructure.security.utils import verify_password, create_access_token

class AuthenticationUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def autenticar_usuario(self, email: str, password: str):
        usuario = self.repositorio.obtener_por_email(email)
        if usuario is not None:
            if not usuario.verified:
                return {"error": "El usuario no está verificado."}
            if isinstance(usuario, dict):
                password_valida = verify_password(password, usuario['password'])
            else:
                password_valida = verify_password(password, usuario.password)
            if password_valida:
                access_token = create_access_token(subject=usuario.id)
                return {"access_token": access_token, "token_type": "bearer"}
        return None