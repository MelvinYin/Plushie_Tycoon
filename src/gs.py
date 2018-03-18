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
        self.res = ResourceInventory()
        self.prod = ProductInventory()
        self.res_price = MarketRes()
        self.prod_price = MarketProd()
        self.budget = Budget()
        self.production = Production()
        self.time_steps = defaults.starting_time

        self.value_history = []
        self.callstack = []

        self.long_term_store = dict()

    def __str__(self):
        return defaults.generic_str_fn(self)

    def cost_to_produce(self, category, quantity):
        hour_per_prod = self.production.hours_needed[category]
        total_hours = hour_per_prod * quantity
        cost = total_hours * self.production.cost_per_hour
        return cost

    def to_store_self(self):
        """
        Value history and long_term_store not kept, to avoid recurrent
        nesting.
        Call self.__dict__.update(to_store) to update when reversing.
        Neglected: value_history, long_term_store.
        Eventually change it to a memento.
        """
        to_store = dict()
        to_store["res"] = copy.deepcopy(self.res)
        to_store["prod"] = copy.deepcopy(self.prod)
        to_store["res_price"] = copy.deepcopy(self.res_price)
        to_store["prod_price"] = copy.deepcopy(self.prod_price)
        to_store["budget"] = copy.deepcopy(self.budget)
        to_store["production"] = copy.deepcopy(self.production)
        to_store["time_steps"] = copy.deepcopy(self.time_steps)
        to_store["callstack"] = copy.deepcopy(self.callstack)
        return to_store

    @staticmethod
    def to_store_dict(ref_dict):
        to_store = dict()
        to_store["res"] = copy.deepcopy(ref_dict.res)
        to_store["prod"] = copy.deepcopy(ref_dict.prod)
        to_store["res_price"] = copy.deepcopy(ref_dict.res_price)
        to_store["prod_price"] = copy.deepcopy(ref_dict.prod_price)
        to_store["budget"] = copy.deepcopy(ref_dict.budget)
        to_store["production"] = copy.deepcopy(ref_dict.production)
        to_store["time_steps"] = copy.deepcopy(ref_dict.time_steps)
        to_store["callstack"] = copy.deepcopy(ref_dict.callstack)
        return to_store

    def commit(self, call=None):
        if call:
            self.commit_with_call(call)
        else:
            self.commit_no_call()
        return True

    def commit_no_call(self):
        to_store = self.to_store_self()
        self.value_history.append(to_store)
        return True

    def commit_with_call(self, call):
        self.commit_no_call()
        assert call[0] in defaults.Func
        self.callstack.append(call)
        return True

    def push(self):
        self.long_term_store[self.time_steps] = (self.callstack, self.value_history)
        self.callstack = []
        self.value_history = []
        self.commit_no_call()

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
        self.__dict__.update(values_to_replace)
        return True

    def show_stats(self):   # this should be moved to GS
        logging.info("Current Inventory: \n"
                     + "Resources\n" + str(self.res) + "\n"
                     + "Products\n" + str(self.prod))

        logging.info("Current Budget: " + str(self.budget))

        logging.info("Current Market Prices: \n"
                     + "Resources\n" + str(self.res_price) + "\n"
                     + "Products\n" + str(self.prod_price))

        logging.info("Fixed Costs: \n"
                     + str(self.production.hours_needed) + "\n"
                     + "Cost per hour: " + str(self.production.cost_per_hour))

        logging.info("Callstack: \n" + str(self.callstack))
        # logging.info("History: \n" + str(self.value_history))

        logging.info("Time elapsed: " + str(self.time_steps))
        return True

    def show_prices(self):
        logging.info("Current Market Prices: \n"
                     + "Resources\n" + str(self.res_price) + "\n"
                     + "Products\n" + str(self.prod_price))
        return True

    def show_history(self):
        logging.info(self.callstack)
        logging.info(self.value_history)
        return True

    def copy(self):
        return copy.deepcopy(self)






















