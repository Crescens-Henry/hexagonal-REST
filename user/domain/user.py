import uuid


class Usuario:
    def __init__(self, nombre: str, email: str, password: str,  user_uuid=None, verificado=False): 
        self.nombre = nombre
        self.email = email
        self.password = password
        self.uuid = user_uuid or str(uuid.uuid4())
        self.verificado = verificado