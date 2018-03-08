from inventory import ResourceInventory, ProductInventory
from production import ProductionCost
from singleton import Singleton
from market import MarketRes, MarketProd
import defaults
from budget import Budget


class GSM:
    __metaclass__ = Singleton
    def __init__(self):
        self.MarketRes = MarketRes()
        self.MarketProd = MarketProd()
        self.ResourceInv = ResourceInventory()
        self.ProductInv = ProductInventory()
        self.Budget = Budget()
        self.ProductionCost = ProductionCost()


        self.res_price = self.MarketRes.price
        self.prod_price = self.MarketProd.price
        self.prod_res_cost = defaults.prod_res_cost
        self.res = self.ResourceInv
        self.prod = self.ProductInv
        self.budget = self.Budget.budget
        self.cost_per_hour = defaults.cost_per_hour
        self.prod_hours = self.ProductionCost.prod_hours
        self.time_steps = 0

    def update(self, GS):
        self.__dict__ = GS.__dict__

    def cost_to_produce(self, type, quantity):
        prod_time_required = self.prod_hours[type] * quantity
        cost = prod_time_required * self.cost_per_hour
        return cost




















