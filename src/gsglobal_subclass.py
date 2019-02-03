from gsglobal.inventory import InventoryBackend
from gsglobal.market import MarketBackend
from gsglobal.budget import BudgetBackend
from gsglobal.production import ProductionBackend

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
        data = dict()
        data['res'] = self.inventory.res
        data['prod'] = self.inventory.prod
        return data

class Market:
    def __init__(self, market_values):
        self.market = MarketBackend(market_values)

    def get(self, category):
        return self.market.get(category)

    def return_data(self):
        data = dict()
        data['res'] = self.market.res
        data['prod'] = self.market.prod
        return data

class Budget:
    def __init__(self, init_values):
        self.budget = BudgetBackend(init_values)

    def get(self):
        return self.budget.get()

    def sub(self, _category, other):
        # _category == 'budget', only so budget follows call signature of others
        return self.budget.sub(other)

    def add(self, _category, other):
        return self.budget.add(other)

    def replace(self, _category, other):
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
        # I may not want to return everything from production, so hard-coded
        # instead of looping from self.production.__dict__ for now
        data = dict()
        data['hours_needed'] = self.production.hours_needed
        data['cost_per_hour'] = self.production.cost_per_hour
        data['res_cost'] = self.production.res_cost
        return data


