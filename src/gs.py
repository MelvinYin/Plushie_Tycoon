from inventory import ResourceInventory, ProductInventory
from production import Production
from singleton import Singleton
from market import MarketRes, MarketProd
import defaults
from budget import Budget
import copy
import logging
from defaults import Func
import sys


class GSM:
    __metaclass__ = Singleton
    def __init__(self):
        self.res = ResourceInventory()
        self.prod = ProductInventory()
        self.res_price = MarketRes()
        self.prod_price = MarketProd()
        self.budget = Budget()
        self.production = Production()
        self.current_call = None

        self.time_steps = defaults.starting_time

        self.local_history = defaults.history_init
        self.history = defaults.history_init
        self.commit(call=Func.start)

    def prettyp(self):
        string = f"Class: {self.__class__.__name__}\n"
        for key, value in self.__dict__.items():
            tmp = "\tAttr: " + key + "\n\t" \
                  + str(value).replace("\n", "\n\t") + "\n"
            string += tmp
        return string

    def cost_to_produce(self, category, quantity):
        hour_per_prod = self.production.hours_needed[category]
        total_hours = hour_per_prod * quantity
        cost = total_hours * self.production.cost_per_hour
        return cost

    def commit(self, call):
        self.current_call = call
        to_add = defaults.history_add(
            self.res, self.prod, self.res_price, self.prod_price, self.budget,
            self.production, self.time_steps, self.current_call)
        last_index = self.local_history.last_valid_index()
        if not last_index:
            self.local_history.loc[0] = to_add
        else:
            self.local_history.loc[last_index + 1] = to_add
        return True

    def push(self): # SEE IF CAN REMOVE
        self.history = self.history.append(self.local_history, ignore_index=True)
        self.time_steps += 1
        self.local_history = defaults.history_init
        self.commit(call=Func.next_turn)

    def reverse_call(self):
        """ Called either by user with back, or due to errors encountered
        during function call.

        remove_last_call should be called if commit has been called, aka when
        the user initiates a back button. Otherwise, if it's exceptions
        enountered, remove_last_call should be False.
        """
        last_index = self.local_history.last_valid_index()
        if not last_index:
            return False
        new_values = self.local_history.iloc[last_index].to_dict()
        self.local_history.drop(index=last_index, inplace=True)
        self.__dict__.update(new_values)
        return True

    def show_stats(self):   # this should be moved to GS
        logging.info("Current Inventory: \n"
                     + "Resources\n" + str(self.res.prettyp()) + "\n"
                     + "Products\n" + str(self.prod.prettyp()))

        logging.info("Current Budget: " + str(self.budget.prettyp()))

        logging.info("Current Market Prices: \n"
                     + "Resources\n" + str(self.res_price.prettyp()) + "\n"
                     + "Products\n" + str(self.prod_price.prettyp()))

        logging.info("Fixed Costs: \n"
                     + str(self.production.hours_needed) + "\n"
                     + "Cost per hour: " + str(self.production.cost_per_hour))

        logging.info("History: \n" + str(self.prettyp_ext(self.local_history)))

        logging.info("Time elapsed: " + str(self.time_steps))
        return True

    def show_prices(self):
        logging.info("Current Market Prices: \n"
                     + "Resources\n" + str(self.res_price.prettyp()) + "\n"
                     + "Products\n" + str(self.prod_price.prettyp()))
        return True

    def show_history(self):
        logging.info(self.local_history)
        return True

    def copy(self):
        return copy.deepcopy(self)






















