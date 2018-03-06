from singleton import Singleton
from bases import Base, BaseInt
import default_values

class PlushieHours(Base):
    def __init__(self):
        self.aisha = default_values.aisha_prod_time
        self.beta = default_values.beta_prod_time
        self.chama = default_values.chama_prod_time

class CostPerHour(BaseInt):
    def __init__(self):
        self.cost_per_hour = default_values.cost_per_hour
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

