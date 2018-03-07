from exceptions import InsufficentQuantityError
import copy
import os
import pickle
import sys
import logging
from defaults import func


class GEM:
    def __init__(self, GSM):
        self.GSM = GSM

    def __call__(self, callstack):
        """ callstack should be a list. """

        GEM_methods = dict([(func.save_game, self.save_game),
                            (func.load_game, self.load_game),
                            (func.quit_game, self.quit_game),
                            (func.save_quit, self.save_quit),
                            (func.next_turn, self.next_turn)])

        while callstack:
            call = callstack.pop(0)
            logging.debug(f"Currently running: {call}")
            func_signal, args = call[0], call[1:]

            if func_signal in GEM_methods:
                if args:
                    GEM_methods[func_signal](*args)
                else:
                    GEM_methods[func_signal]()
                continue

            GSI = copy.deepcopy(self.GSM)
            loaded_GEI = GEI(call, GSI)
            try:
                updated_GSI = loaded_GEI()
            except InsufficentQuantityError:
                callstack.insert(0, call)
                return ("insufficient_quantity", callstack)

            self.GSM.__dict__ = updated_GSI.__dict__
        return

    def load_game(self, file_path="../save/", file_name=None):
        if not file_name:
            file_name = "game" + "_save.pkl"
        if not os.path.isdir(file_path):
            logging.error(f"File path {file_path} does not exist.")
            raise FileNotFoundError
        if not os.path.isfile(file_path + file_name):
            logging.error(f"File {file_name} does not exist in specified "
                             f"directory {file_path}.")
            raise FileNotFoundError
        with open(file_path + file_name, "rb") as file:
            self.GSM = pickle.load(file)
        return True

    def save_game(self, file_path="../save/", file_name=None):
        if not file_name:
            file_name = "game" + "_save.pkl"
        if not file_name.endswith(".pkl"):
            logging.warning(f"Warning: File name {file_name} provided does not"
                            f" end with .pkl. Suffix will be added.")
            file_name += ".pkl"
        if not os.path.isdir(file_path):
            logging.warning(f"Warning: File_path {file_path} provided does not"
                            f" exist. Directory will be created.")
            os.makedirs(file_path)
        with open(file_path + file_name, "wb") as file:
            pickle.dump(self.GSM, file, -1)
        return True

    def quit_game(self):
        sys.exit()

    def save_quit(self):
        self.save_game()
        self.quit_game()

    def next_turn(self):
        """ Will have more stuff in the future. """
        self.GSM.time_steps += 1
        return


class GEI:
    def __init__(self, call, GSI):
        self.call = call
        self.GSI = GSI

    def __call__(self):
        func_in_str, args = self.call[0], self.call[1:]
        called_func = self.interpret_call(func_in_str)
        if args:
            called_func(*args)
        else:
            called_func()
        return self.GSI

    def interpret_call(self, func_signal):

        GEI_methods = dict([(func.buy_res, self.buy_res),
                            (func.sell_res, self.sell_res),
                            (func.buy_prod, self.buy_prod),
                            (func.make_prod, self.make_prod),
                            (func.sell_prod, self.sell_prod),
                            (func.show_stats, self.show_stats),
                            (func.show_price, self.show_price)])
        try:
            called_func = GEI_methods[func_signal]
        except KeyError:
            logging.error(func_signal)
            raise Exception
        return called_func


    def buy_res(self, category, quantity):
        curr_res_p = self.GSI.res_price[category]
        cost_to_buy = curr_res_p * quantity
        self.GSI.budget -= cost_to_buy
        self.GSI.res[category] += quantity
        return True

    def sell_res(self, category, quantity):
        curr_res_p = self.GSI.res_price[category]
        earnings = curr_res_p * quantity
        self.GSI.budget += earnings
        self.GSI.res[category] -= quantity
        return True

    def buy_prod(self, category, quantity):
        curr_prices = self.GSI.prod_price[category]
        cost_to_buy = curr_prices * quantity
        self.GSI.budget -= cost_to_buy
        self.GSI.prod[category] += quantity
        return True

    def sell_prod(self, category, quantity):
        curr_prices = self.GSI.prod_price[category]
        self.GSI.prod[category] -= quantity
        earnings = curr_prices * quantity
        self.GSI.budget += earnings
        return True

    def make_prod(self, type, quantity):
        res_for_type = self.GSI.prod_res_cost[type]
        total_res = res_for_type * quantity
        for category, quantity in total_res.iteritems():
            self.GSI.res[category] -= quantity

        cost_to_produce = self.GSI.cost_to_produce(type, quantity)
        self.GSI.budget -= cost_to_produce

        self.GSI.prod[type] += quantity
        return True

    def show_stats(self):
        logging.info("Current Inventory: \n"
                     + "Resources\n" + str(self.GSI.res) + "\n"
                     + "Products\n" + str(self.GSI.prod))

        logging.info("Current Budget: " + str(self.GSI.budget))

        logging.info("Current Market Prices: \n"
                     + "Resources\n" + str(self.GSI.res_price) + "\n"
                     + "Products\n" + str(self.GSI.prod_price))

        logging.info("Fixed Costs: \n"
                     + str(self.GSI.prod_res_cost) + "\n"
                     + "Cost per hour: " + str(self.GSI.cost_per_hour))

        logging.info("Time elapsed: " + str(self.GSI.time_steps))
        return True

    def show_price(self):
        logging.info("Current Market Prices: \n"
                     + "Resources\n" + str(self.GSI.res_price) + "\n"
                     + "Products\n" + str(self.GSI.prod_price))
        return
