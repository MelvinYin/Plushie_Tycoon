from singleton import Singleton
from bases import Base, BaseInt

class PlushieHours(Base):
    def __init__(self):
        self.Aisha = 30
        self.Beta = 24
        self.Chama = 36

class CostPerHour(BaseInt):
    def __init__(self):
        self.cost_per_hour = 3
        super().__init__(self.cost_per_hour)

class ProductionCost(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.plushie_hours = PlushieHours()
        self.cost_per_hour = CostPerHour()

    def __call__(self, category, quantity):
        hours_per_plushie = self.plushie_hours[category]
        cost = hours_per_plushie * self.cost_per_hour * quantity
        return cost

