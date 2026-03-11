import uuid
from dataclasses import dataclass

@dataclass
class Crop:
    id: uuid.UUID
    type: str
    area: float
    input_management: float
