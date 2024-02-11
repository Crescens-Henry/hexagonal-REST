from user.domain.entities.user import Usuario


class updateUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def actualizar_usuario(self, user_id: str, nombre: str,last_name:str, cellphone: str, email: str, password: str):
        usuario = Usuario(nombre,last_name,cellphone, email, password)
        return self.repositorio.actualizar(user_id, usuario)