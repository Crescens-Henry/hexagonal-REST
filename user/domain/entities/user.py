import uuid


class Usuario:
    def __init__(self, name: str,last_name: str,cellphone:int, email: str, password: str,verified_at:str = None,  user_uuid=None, verificado=False): 
        self.name = name
        self.last_name = last_name
        self.cellphone = cellphone
        self.email = email
        self.password = password
        self.verified_at = verified_at
        self.uuid = user_uuid or str(uuid.uuid4())
        self.verificado = verificado