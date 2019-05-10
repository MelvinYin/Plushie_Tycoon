from collections import defaultdict
import copy
import inspect
import os
import pickle

from gs_subclass import Inventory, Market, Budget, Production
from logs import log

class GS:
    def __init__(self, GSDataClass):
        self.inventory = Inventory(GSDataClass.inventory)
        self.market = Market(GSDataClass.market)
        self.budget = Budget(GSDataClass.budget)
        self.production = Production(GSDataClass.production)
        self.current_call = None
        self.current_time = GSDataClass.time
        self.history = defaultdict(list)

    def format_output(self):
        output = ""
        assert 'command' in self.current_call, self.current_call
        command = self.current_call['command']
        category = ""
        quantity = ""
        if 'category' in self.current_call:
            category = self.current_call['category']
        if 'quantity' in self.current_call:
            quantity = self.current_call['quantity']
        output += "<br />Command called: {} {} {}<br />"\
            .format(command, category, quantity)
        return output

    def movein_cost(self, category, quantity):
        return self.inventory.movein_cost(category, quantity)

    def moveout_cost(self, category, quantity):
        return self.inventory.moveout_cost(category, quantity)

    def storage_cost(self):
        return self.inventory.storage_cost()

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

    def commit(self, call):
        self.current_call = call
        # if self.__dict__ is used directly in to_add, when to_add is
        # updated, every entry in self.history[self.current_time] gets
        # updated as well.
        copied_dict = copy.deepcopy(self.__dict__)
        to_add = {key: copied_dict[key] for key in copied_dict if
                  key != 'history'}
        self.history[self.current_time].append(to_add)
        return True

    def reverse_call(self):
        """ Called either by user with back, or due to errors encountered
        during function call.
        """
        if len(self.history[self.current_time]) == 1:
            return False
        previous_state = self.history[self.current_time].pop()
        self.__dict__.update(previous_state)
        return True
