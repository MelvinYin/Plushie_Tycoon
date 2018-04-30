from inventory import ResourceInventory, ProductInventory
from production import Production
from singleton import Singleton
from market import MarketRes, MarketProd
import defaults
from budget import Budget
import copy
import logging
import sys
from collections import defaultdict


class GSM:
    __metaclass__ = Singleton
    def __init__(self):
        self.res = ResourceInventory()
        self.prod = ProductInventory()
        self.res_price = MarketRes()
        self.prod_price = MarketProd()
        self.budget = Budget()
        self.production = Production()
        self.current_call = None

        self.current_time = defaults.starting_time

        self.history = defaultdict(list)


    def cost_to_produce(self, category, quantity):
        hour_per_prod = self.production.hours_needed[category]
        total_hours = hour_per_prod * quantity
        cost = total_hours * self.production.cost_per_hour
        return cost

    def commit(self, call):
        self.current_call = call
        to_add = {key: self.__dict__[key] for key in self.__dict__ if
                  key != 'history'}
        self.history[self.current_time].append(to_add)
        return True

    def reverse_call(self):
        """ Called either by user with back, or due to errors encountered
        during function call.
        """
        if len(self.history[self.current_time] == 1):
            return False
        previous_state = self.history[self.current_time].pop()
        self.__dict__.update(previous_state)
        return True

    def copy(self):
        return copy.deepcopy(self)






















