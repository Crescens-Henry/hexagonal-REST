from dataclasses import dataclass, field
from .Contact import Contact
from .Credential import Credential
from .Status import Status

@dataclass
class User:
    contact: Contact
    credentials: Credential
    status: Status = field(default_factory=Status)
