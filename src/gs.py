from gs_subclass import Inventory, Market, Budget, Production
from global_config import GSConstructor, save_folder, save_file_name
import copy
from logs import log
import inspect
import os
import pickle
from collections import defaultdict


class GS:
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
        to_add = {key: self.__dict__[key] for key in self.__dict__ if
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

    def load(self, call, file_path=save_folder, file_name=save_file_name):
        if not os.path.isdir(file_path):
            msg = f"File path {file_path} does not exist."
            log(msg, inspect.currentframe())
            raise FileNotFoundError
        if not os.path.isfile(file_path + file_name):
            msg = f"File {file_name} does not exist in specified " \
                  f"directory {file_path}."
            log(msg, inspect.currentframe())
            raise FileNotFoundError
        with open(file_path + file_name, "rb") as file:
            self.__dict__ = pickle.load(file)
        return 'reload'

    def save(self, call, file_path=save_folder, file_name=save_file_name):
        if not file_name.endswith(".pkl"):
            msg = f"Warning: File name {file_name} provided does not" \
                  f" end with .pkl. Suffix will be added."
            log(msg, inspect.currentframe())
            file_name += ".pkl"
        if not os.path.isdir(file_path):
            msg = f"Warning: File_path {file_path} provided does not" \
                            f" exist. Directory will be created."
            log(msg, inspect.currentframe())
            os.makedirs(file_path)
        with open(file_path + file_name, "wb") as file:
            pickle.dump(self.__dict__, file, -1)
        return 'pause'
