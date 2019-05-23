from inventory import Inventory
from market import Market
from g_market import GlobalMarket
from g_inventory import GlobalInventory
from budget import BudgetBackend

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
        data['budget'] = [self.get()]
        return data

class Production:
    def __init__(self, init_values):
        self.hours_needed = init_values['hours_needed']
        self.cost_per_hour = init_values['cost_per_hour']
        self.res_ratio = init_values['res_ratio']

    def set_values(self, values):
        self.hours_needed = values['hours_needed']
        self.cost_per_hour = values['cost_per_hour']
        self.res_ratio = values['res_ratio']
        return True

    def get(self, category):
        hours = self.hours_needed[category]
        materials = self.res_ratio[category]
        cost = hours * self.cost_per_hour
        return cost, materials

    def return_data(self):
        # I may not want to return everything from production, so hard-coded
        # instead of looping from self.production.__dict__ for now
        data = dict()
        data['hours_needed'] = self.hours_needed
        data['cost_per_hour'] = self.cost_per_hour
        data['res_ratio'] = self.res_ratio
        return data


