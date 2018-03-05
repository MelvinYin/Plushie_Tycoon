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
        self.aisha = 80
        self.beta = 76
        self.chama = 52
