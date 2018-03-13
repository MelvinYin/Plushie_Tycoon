from inventory import ResourceInventory, ProductInventory
from production import Production
from singleton import Singleton
from market import MarketRes, MarketProd
import defaults
from budget import Budget
import copy
import logging


class GSM:
    __metaclass__ = Singleton
    def __init__(self):
        self.res_price = MarketRes()
        self.prod_price = MarketProd()
        self.res = ResourceInventory()
        self.prod = ProductInventory()
        self.budget = Budget()
        self.production = Production()

        self.time_steps = defaults.starting_time

        self.value_history = []
        self.callstack = []

    def __str__(self):
        return defaults.generic_str_fn(self)


    def cost_to_produce(self, category, quantity):

        hour_per_prod = self.production.hours_needed[category]
        total_hours = hour_per_prod * quantity
        cost = total_hours * self.production.cost_per_hour
        return cost

    def commit(self, call=None, ignore_no_call=False):
        values = self.__dict__.copy()
        del values["value_history"] # to avoid recurrent nesting.
        self.value_history.append(copy.deepcopy(values))
        if call:
            assert call[0] in defaults.Func
            self.callstack.append(call)
        elif not ignore_no_call:
            logging.warning("GSM history added but no call added to"
                          "callstack.")
        return True

    def push(self):
        self.callstack = []
        values = copy.deepcopy(self.__dict__)
        # load_game means values does not have value_history
        if "value_history" in values:
            del values["value_history"]
        self.value_history = [values]


    def reverse_call(self, remove_last_call=False):
        """ Called either by user with back, or due to errors encountered
        during function call.

        remove_last_call should be called if commit has been called, aka when
        the user initiates a back button. Otherwise, if it's exceptions
        enountered, remove_last_call should be False.
        """
        if remove_last_call:
            assert self.callstack, "No previous call in current turn."
            del self.callstack[-1]
        values_to_replace = self.value_history.pop()
        values_to_replace["value_history"] = self.value_history.copy()
        self.__dict__ = values_to_replace
        return True






















