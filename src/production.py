from singleton import Singleton
from config.global_config import hours_needed, cost_per_hour, prod_res_cost

class Production:
    __metaclass__ = Singleton
    def __init__(self):
        self.hours_needed = hours_needed
        self.cost_per_hour = cost_per_hour
        self.res_cost = prod_res_cost

    def get_cost(self, category):
        hours = self.hours_needed[category]
        materials = self.res_cost[category]
        cost = hours * self.cost_per_hour
        return cost, materials

