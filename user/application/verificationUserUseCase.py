class VerificationUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio
    
    def verificar_usuario(self, uuid):
        usuario = self.repositorio.obtener_por_uuid(uuid)
        if usuario is not None:
            self.repositorio.verificar_usuario(uuid)
            return True
        return False