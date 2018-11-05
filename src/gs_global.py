from gs_subclass import Inventory, Market, Budget, Production
from global_config import GSConstructor, save_folder, save_file_name
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
        # Hard-coding var name instead of putting it in a __dict__ loop,
        # so name changes can be made to both.
        GS_dataclass = GSConstructor()
        GS_dataclass.production = self.production.return_data()
        GS_dataclass.budget = self.budget.return_data()
        GS_dataclass.inventory = self.inventory.return_data()
        GS_dataclass.market = self.market.return_data()
        GS_dataclass.time = self.current_time
        return GS_dataclass

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
        for action, calls in callstack.items():
            if action == 'buy_sell':
                # _class is 'inventory', etc
                # category is <Prod.aisha>, etc
                for _class, category_dict in calls.items():
                    if _class == 'inventory':
                        for category, quantity in category_dict.items():
                            self.inventory.add(category, quantity)
                    elif _class == 'market':
                        for category, quantity in category_dict.items():
                            self.market.add(category, quantity)


