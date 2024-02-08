class ObtenerUsuariosUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def obtener_usuarios(self):
        return self.repositorio.obtener_todos()