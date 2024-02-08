class GetUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def obtener_usuario(self, user_id: str):
        return self.repositorio.obtener(user_id)