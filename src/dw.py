from enum import Enum

class Res(Enum):
    aisha = 1
    beta = 2
    chama = 3


print(list(Res.__members__.keys()))