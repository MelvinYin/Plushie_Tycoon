import copy
from global_config import starting_res, starting_prod, Res, Prod

from inventory import InventoryBackend
from market import MarketBackend
from budget import BudgetBackend
from production import ProductionBackend

from collections import defaultdict


class Inventory:
    def __init__(self, inventory_values):
        self.inventory = InventoryBackend(inventory_values)

    def add(self, category, quantity):
        return self.inventory.add(category, quantity)

    def sub(self, category, quantity):
        return self.inventory.sub(category, quantity)

    def replace(self, category, quantity):
        return self.inventory.replace(category, quantity)

    def get(self, category):
        return self.inventory.get(category)

    def return_data(self):
        data = defaultdict(dict)
        for key in Res:
            data[Res][key] = self.get(key)
        for key in Prod:
            data[Prod][key] = self.get(key)
        data = dict(data)
        return data

class Market:
    def __init__(self, market_values):
        self.market = MarketBackend(market_values)

    def get(self, category):
        return self.market.get(category)

    def return_data(self):
        data = defaultdict(dict)
        for key in Res:
            data[Res][key] = self.get(key)
        for key in Prod:
            data[Prod][key] = self.get(key)
        data = dict(data)
        return data

class Budget:
    def __init__(self, init_values):
        self.budget = BudgetBackend(init_values)

    def get(self):
        return self.budget.get()

    def sub(self, other):
        return self.budget.sub(other)

    def add(self, other):
        return self.budget.add(other)

    def replace(self, other):
        return self.budget.replace(other)

    def return_data(self):
        data = dict()
        data['budget'] = self.get()
        return data

class Production:
    def __init__(self, init_values):
        self.production = ProductionBackend(init_values)

    def get(self, category):
        return self.production.get_cost(category)

    def return_data(self):
        data = defaultdict(dict)
        for key in Prod:
            data[Prod][key] = self.get(key)
        data = dict(data)
        return data


