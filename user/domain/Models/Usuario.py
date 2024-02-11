from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    name: str
    last_name: str
    cellphone: int
    email: str
    password: str
    verified_at: Optional[str] = None