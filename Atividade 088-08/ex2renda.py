from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Domicilio:
    id: int
    renda: float

class Estrato(Enum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()


d1 = Domicilio(10,23000.0)

def estrato (domicilio: Domicilio) -> Estrato:
    ''''''

    if domicilio.renda > 22000:
        return Estrato.A
    
print(estrato(d1).name)
