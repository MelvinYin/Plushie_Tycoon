from singleton import Singleton
from bases import Base

class MarketResource(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.cloth = 10
        self.stuff = 20
        self.accessory = 18
        self.packaging = 12


class MarketPlushie(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.Aisha = 80
        self.Beta = 76
        self.Chama = 52
