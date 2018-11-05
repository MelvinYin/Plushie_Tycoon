from gs_subclass import Inventory, Market, Budget, Production
from global_config import GSConstructor, save_folder, save_file_name, Func
import copy
from logs import log
import inspect
import os
import pickle
from collections import defaultdict


class GSGlobal:
    def __init__(self, GSDataClass):
        self.inventory = Inventory(GSDataClass.inventory)
        self.market = Market(GSDataClass.market)
        self.budget = Budget(GSDataClass.budget)
        self.production = Production(GSDataClass.production)
        self.current_call = None
        self.current_time = GSDataClass.time
        self.history = defaultdict(list)

    def return_data(self):
        GS_dataclass = GSConstructor()
        _production = self.production.return_data()
        GS_dataclass.load_production(_production['hours_needed'],
                                     _production['res_cost'],
                                     _production['cost_per_hour'])
        _budget = self.budget.return_data()
        GS_dataclass.load_budget(_budget['budget'])

        _inventory = self.inventory.return_data()
        GS_dataclass.load_inventory(_inventory['res'], _inventory['prod'])

        _market = self.market.return_data()
        GS_dataclass.load_market(_market['res'], _market['prod'])
        GS_dataclass.time = self.current_time
        return GS_dataclass

    # def return_data(self):
    #     # Hard-coding var name instead of putting it in a __dict__ loop,
    #     # so name changes can be made to both.
    #     GS_dataclass = GSConstructor()
    #     GS_dataclass.production = self.production.return_data()
    #     GS_dataclass.budget = self.budget.return_data()
    #     GS_dataclass.inventory = self.inventory.return_data()
    #     GS_dataclass.market = self.market.return_data()
    #     GS_dataclass.time = self.current_time
    #     return GS_dataclass

    def get(self, classification, *args):
        if classification == 'inventory':
            return self.inventory.get(*args)
        elif classification == 'market':
            return self.market.get(*args)
        elif classification == 'budget':
            return self.budget.get()
        elif classification == 'production':
            return self.production.get(*args)
        elif classification == 'time':
            return self.current_time
        else:
            raise Exception

    def sub(self, classification, *args):
        if classification == 'inventory':
            return self.inventory.sub(*args)
        elif classification == 'budget':
            return self.budget.sub(*args)
        else:
            raise Exception

    def add(self, classification, *args):
        if classification == 'inventory':
            return self.inventory.add(*args)
        elif classification == 'budget':
            return self.budget.add(*args)
        elif classification == 'time':
            self.current_time += 1
            return True
        else:
            raise Exception

    def implement_callstack(self, callstack):
        # Weird format for now
        for action, cat_quantity in callstack.items():
            for category, quantity in cat_quantity.items():
                if action == Func.buy:
                    self.buy(category, quantity)
                elif action == Func.sell:
                    self.sell(category, quantity)
                elif action == Func.make:
                    self.make(category, quantity)
                else:
                    raise Exception
        self.current_time += 1
        return True

    # Taken from GE
    def buy(self, category, quantity):
        self.inventory.add(category, quantity)
        price = self.market.get(category)
        total_cost = price * quantity
        self.budget.sub('budget', total_cost)
        return 'update'

    def sell(self, category, quantity):
        self.inventory.sub(category, quantity)
        price = self.market.get(category)
        total_cost = price * quantity
        self.budget.add('budget', total_cost)
        return 'update'

    def make(self, category, quantity):
        cost, materials = self.production.get(category)
        for _category, material in materials.items():
            self.inventory.sub(_category, material * quantity)
        self.budget.sub('budget', cost * quantity)
        self.inventory.add(category, quantity)
        return 'update'
#     Taken from GE end

