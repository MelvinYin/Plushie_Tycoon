from singleton import Singleton
from bases import BaseInventory
import logging
import copy
from global_config import starting_res, starting_prod, Res, Prod


class Inventory(BaseInventory):
    __metaclass__ = Singleton
    def __init__(self):
        self.res = copy.deepcopy(starting_res)  # pd.series
        self.prod = copy.deepcopy(starting_prod)
        self.type_map = self._get_type_map()

    def add(self, category, quantity):
        item_signal = type(category)
        item = self.type_map[item_signal]
        item[category] += quantity
        return True

    def sub(self, category, quantity):
        item_signal = type(category)
        item = self.type_map[item_signal]
        item[category] -= quantity
        return True

    def replace(self, category, quantity):
        item_signal = type(category)
        item = self.type_map[item_signal]
        item[category] = quantity
        return True

    def _get_type_map(self):
        mapping = dict()
        mapping[Res] = self.res
        mapping[Prod] = self.prod

    def get(self, category):
        item_signal = type(category)
        item = self.type_map[item_signal]
        return item[category]
