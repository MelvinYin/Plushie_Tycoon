import pandas as pd
from singleton import Singleton
from bases import Base

class ResourceCost(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.index = ["cloth", "stuff", "accessory", "packaging"]
        self.Aisha = self._default_Aisha()
        self.Beta = self._default_Beta()
        self.Chama = self._default_Chama()

    def _default_Aisha(self):
        cost = pd.Series([3,6,2,1], self.index, name="Aisha")
        return cost

    def _default_Beta(self):
        cost = pd.Series([1,4,1,2], self.index, name="Beta")
        return cost

    def _default_Chama(self):
        cost = pd.Series([2,5,1,4], self.index, name="Chama")
        return cost

