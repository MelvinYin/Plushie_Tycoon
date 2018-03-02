from collections import namedtuple
from singleton import Singleton
from bases import Base

class ResourceCost(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.Aisha = self._default_Aisha()
        self.Beta = self._default_Beta()
        self.Chama = self._default_Chama()

    @staticmethod
    def _default_tuple(name):
        return namedtuple(f"{name}",
                          ["cloth", "stuff", "accessory", "packaging"])

    def _default_Aisha(self):
        cost = self._default_tuple("Aisha")
        return cost(cloth=3, stuff=6, accessory=2, packaging=1)

    def _default_Beta(self):
        cost = self._default_tuple("Beta")
        return cost(cloth=1, stuff=4, accessory=1, packaging=2)

    def _default_Chama(self):
        cost = self._default_tuple("Chama")
        return cost(cloth=2, stuff=5, accessory=1, packaging=4)

