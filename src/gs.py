from inventory import ResourceInventory, ProductInventory
from production import ProductionCost
from singleton import Singleton
from market import MarketRes, MarketProd
import defaults
from budget import Budget
from time_stuff import TimeSteps
import copy
import logging


class GSM:
    __metaclass__ = Singleton
    def __init__(self):
        self.MarketRes = MarketRes()
        self.MarketProd = MarketProd()
        self.ResourceInv = ResourceInventory()
        self.ProductInv = ProductInventory()
        self.Budget = Budget()
        self.ProductionCost = ProductionCost()
        self.TimeSteps = TimeSteps()

        self.res_price = self.MarketRes
        self.prod_price = self.MarketProd
        self.prod_res_cost = defaults.prod_res_cost
        self.res = self.ResourceInv
        self.prod = self.ProductInv
        self.budget = self.Budget
        self.cost_per_hour = self.ProductionCost.cost_per_hour
        self.prod_hours = self.ProductionCost.prod_hours
        self.time_steps = self.TimeSteps

        self.value_history = []
        self.callstack = []

        self.commit(call=None, ignore_no_call=True)

    def cost_to_produce(self, type, quantity):
        prod_time_required = self.prod_hours[type] * quantity
        cost = prod_time_required * self.cost_per_hour
        return cost

    def commit(self, call=None, ignore_no_call=False):
        self.value_history.append(self.__dict__.copy())
        if call:
            assert call in defaults.func
            self.callstack.append(call)
        elif not ignore_no_call:
            logging.warning("GSM history added but no call added to"
                          "callstack.")
        return True

    def push(self):
        self.value_history = [copy.deepcopy(self.__dict__)]
        self.callstack = []

    def reverse_call(self, remove_last_call=False):
        """ Called either by user with back, or due to errors encountered
        during function call. """
        if remove_last_call:
            assert self.callstack, "No previous call in current turn."
            del self.callstack[-1]
        self.__dict__ = self.value_history.pop()
        return True























