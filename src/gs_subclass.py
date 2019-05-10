from inventory import Inventory
from market import Market
from budget import BudgetBackend
from production import ProductionBackend

class Budget:
    def __init__(self, init_values):
        self.budget = BudgetBackend(init_values)

    def set_values(self, values):
        self.budget = values['budget']
        return True

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

    def set_values(self, values):
        self.production.hours_needed = values['hours_needed']
        self.production.cost_per_hour = values['cost_per_hour']
        self.production.res_cost = values['res_cost']
        return True

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


