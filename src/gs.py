from inventory import ResourceInventory, PlushieInventory
from production import ProductionCost
from singleton import Singleton
from market import MarketRes, MarketProd
import defaults
from budget import Budget


class GSM:
    __metaclass__ = Singleton
    def __init__(self):
        self.res_price = MarketRes()
        self.prod_price = MarketProd()
        self.prod_res_cost = defaults.prod_res_cost
        self.res = ResourceInventory()
        self.prod = PlushieInventory()
        self.budget = Budget().budget
        self.production_cost = ProductionCost()
        self.time_steps = 0

    def update(self, GS):
        self.__dict__ = GS.__dict__

