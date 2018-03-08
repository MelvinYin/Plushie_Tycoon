from singleton import Singleton
import defaults

class ProductionCost:
    __metaclass__ = Singleton
    def __init__(self):
        self.prod_hours = defaults.prod_hours
        self.cost_per_hour = defaults.cost_per_hour

    def __call__(self, category, quantity):
        hours_per_prod = self.prod_hours[category]
        cost = sum(hours_per_prod * self.cost_per_hour * quantity)
        return cost

