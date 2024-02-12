from dataclasses import dataclass
import uuid

@dataclass
class Status:
    token_uuid :str = str(uuid.uuid4())
    verified: bool = False