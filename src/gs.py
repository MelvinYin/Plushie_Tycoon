from inventory import ResourceInventory, PlushieInventory
from production import ProductionCost
from singleton import Singleton
from market import MarketRes, MarketProd
import defaults
from budget import Budget


class GSM:
    __metaclass__ = Singleton
    def __init__(self):
        self.res_price = defaults.starting_res_price
        self.prod_price = defaults.starting_prod_price
        self.prod_res_cost = defaults.prod_res_cost
        self.res = defaults.starting_res
        self.prod = defaults.starting_prod
        self.budget = defaults.starting_budget
        self.cost_per_hour = defaults.cost_per_hour
        self.prod_hours = defaults.prod_hours   # can be moved into a Production class
        self.time_steps = 0

    def update(self, GS):
        self.__dict__ = GS.__dict__

    def cost_to_produce(self, type, quantity):
        prod_time_required = self.prod_hours[type] * quantity
        cost = prod_time_required * self.cost_per_hour
        return cost

    def _fluctuation(self):
        
