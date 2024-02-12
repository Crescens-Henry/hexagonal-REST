from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    last_name: str
    cellphone: str
    
    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"