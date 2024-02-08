class deleteUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio
    
    def eliminar_usuario(self, user_id: str):
        return self.repositorio.eliminar(user_id)