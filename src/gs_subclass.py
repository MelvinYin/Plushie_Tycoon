import copy
from global_config import starting_res, starting_prod, Res, Prod

from inventory import InventoryBackend
from market import MarketBackend
from budget import BudgetBackend
from production import ProductionBackend


class Inventory:
    def __init__(self):
        self.inventory = InventoryBackend()

    def add(self, category, quantity):
        return self.inventory.add(category, quantity)

    def sub(self, category, quantity):
        return self.inventory.sub(category, quantity)

    def replace(self, category, quantity):
        return self.inventory.replace(category, quantity)

    def get(self, category):
        return self.inventory.get(category)

class Market:
    def __init__(self):
        self.market = MarketBackend()

    def get(self, category):
        return self.market.get(category)

class Budget:
    def __init__(self):
        self.budget = BudgetBackend()

    def get(self):
        return self.budget.get()

    def sub(self, other):
        return self.budget.sub(other)

    def add(self, other):
        return self.budget.add(other)

    def replace(self, other):
        return self.budget.replace(other)

class Production:
    def __init__(self):
        self.production = ProductionBackend()

    def get_cost(self, category):
        return self.production.get_cost(category)
