class VerificationUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio
    
    def verificar_usuario(self, token_uuid):
        usuario = self.repositorio.obtener_por_uuid(token_uuid)
        if usuario is not None:
            self.repositorio.verificar_usuario(token_uuid)
            return True
        return False