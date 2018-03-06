from exceptions import InsufficentQuantityError
import copy
import os
import pickle
import sys
import logging


class GEM:
    def __init__(self, GSM):
        self.GSM = GSM

    def __call__(self, callstack):
        """ callstack should be a list. """

        GEM_methods = dict(save_game=self.save_game,
                           load_game=self.load_game,
                           quit_game=self.quit_game,
                           save_quit=self.save_quit,
                           next_turn=self.next_turn)

        while callstack:
            call = callstack.pop(0)
            logging.debug(f"Currently running: {call}")
            func, args = call[0], call[1:]

            if func in GEM_methods:
                if args:
                    GEM_methods[func](*args)
                else:
                    GEM_methods[func]()
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
            file_name = "plushie" + "_save.pkl"
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
            file_name = "plushie" + "_save.pkl"
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

    def interpret_call(self, func_in_str):
        if func_in_str == "buy_res":
            func = self.buy_res
        elif func_in_str == "sell_res":
            func = self.sell_res

        elif func_in_str == "buy_plush":
            func = self.buy_plushie
        elif func_in_str == "make_plush":
            func = self.make_plushie
        elif func_in_str == "sell_plush":
            func = self.sell_plushie

        elif func_in_str == "show_stats":
            func = self.show_stats
        elif func_in_str == "show_prices":
            func = self.show_prices

        else:
            logging.error(func_in_str)
            raise Exception
        return func

    def __call__(self):
        func_in_str, args = self.call[0], self.call[1:]
        func = self.interpret_call(func_in_str)
        if args:
            func(*args)
        else:
            func()
        return self.GSI

    def buy_res(self, category, quantity):
        curr_res_p = self.GSI.m_resource[category]
        cost_to_buy = curr_res_p * quantity
        self.GSI.budget -= cost_to_buy
        self.GSI.resources[category] += quantity
        return True

    def sell_res(self, category, quantity):
        curr_res_p = self.GSI.m_resource[category]
        earnings = curr_res_p * quantity
        self.GSI.budget += earnings
        self.GSI.resources[category] -= quantity
        return True

    def buy_plushie(self, category, quantity):
        curr_prices = self.GSI.m_plushie[category]
        cost_to_buy = curr_prices * quantity
        self.GSI.budget -= cost_to_buy
        self.GSI.plushies[category] += quantity
        return True

    def sell_plushie(self, category, quantity):
        curr_prices = self.GSI.m_plushie[category]
        self.GSI.plushies[category] -= quantity
        earnings = curr_prices * quantity
        self.GSI.budget += earnings
        return True

    def make_plushie(self, type, quantity):
        res_for_type = self.GSI.resource_cost[type]
        total_res = res_for_type * quantity
        for category, quantity in total_res.items():
            self.GSI.resources[category] -= quantity

        cost_to_produce = self.GSI.production_cost(type, quantity)
        self.GSI.budget -= cost_to_produce

        self.GSI.plushies[type] += quantity
        return True


    def show_stats(self):
        logging.info("Current Inventory:")
        logging.info(self.GSI.resources)
        logging.info(self.GSI.plushies)

        logging.info("Current Budget:")
        logging.info(self.GSI.budget)

        logging.info("Current Market Prices:")
        logging.info(self.GSI.m_plushie)
        logging.info(self.GSI.m_resource)

        logging.info("Fixed Costs:")
        logging.info(self.GSI.resource_cost)
        logging.info(self.GSI.production_cost)

        logging.info("Time elapsed:")
        logging.info(self.GSI.time_steps)
        return True

    def show_prices(self):
        logging.info("Current Market Prices:")
        logging.info(self.GSI.m_plushie)
        logging.info(self.GSI.m_resource)
        logging.info("\n")
        return
