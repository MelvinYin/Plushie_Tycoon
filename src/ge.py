from exceptions import InsufficientQuantityError, RepeatUIAction
import copy
import os
import pickle
import sys
import logging
from defaults import func
from gs import GSM
import defaults



class GEM:
    def __init__(self):
        self.GSM = GSM()

    def __str__(self):
        tmp = dict()
        for key, value in self.GSM.__dict__.items():
            tmp[str(key)] = str(value)
        return str(tmp)

    def __call__(self, call):
        methods = dict([(func.save_game, self.save_game),
                            (func.load_game, self.load_game),
                            (func.quit_game, self.quit_game),
                            (func.save_quit, self.save_quit),
                            (func.next_turn, self.next_turn),
                            (func.buy_res, self.buy_res),
                            (func.sell_res, self.sell_res),
                            (func.buy_prod, self.buy_prod),
                            (func.make_prod, self.make_prod),
                            (func.sell_prod, self.sell_prod),
                            (func.show_stats, self.show_stats),
                            (func.show_prices, self.show_prices),
                            (func.show_history, self.show_history),
                            (func.back, self.back)
                            ])
        logging.debug(f"Currently running: {call}")
        func_signal, args = call[0], call[1:]
        try:
            if args:
                methods[func_signal](*args)
            else:
                methods[func_signal]()
        except InsufficientQuantityError as e:
            self.GSM.reverse_call(remove_last_call=False)
            raise RepeatUIAction
        return

    def load_game(self, file_path=defaults.def_save_folder, file_name=None):
        if not file_name:
            file_name = defaults.def_save_file_name
        if not os.path.isdir(file_path):
            logging.error(f"File path {file_path} does not exist.")
            raise FileNotFoundError
        if not os.path.isfile(file_path + file_name):
            logging.error(f"File {file_name} does not exist in specified "
                             f"directory {file_path}.")
            raise FileNotFoundError
        with open(file_path + file_name, "rb") as file:
            self.GSM.__dict__ = pickle.load(file)
        self.GSM.push()
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
            pickle.dump(self.GSM.value_history[0], file, -1)
        self.GSM.push()
        return True

    def quit_game(self):
        sys.exit()

    def save_quit(self):
        self.save_game()
        self.quit_game()

    def next_turn(self):
        self.GSM.time_steps += 1
        self.GSM.push()
        return

    def buy_res(self, category, quantity):
        self.GSM.commit(call=(func.buy_res, category, quantity))
        curr_res_p = self.GSM.res_price.value[category]
        cost_to_buy = curr_res_p * quantity
        self.GSM.budget.sub(cost_to_buy)
        self.GSM.res.add(category, quantity)
        return True

    def sell_res(self, category, quantity):
        self.GSM.commit(call=(func.sell_res, category, quantity))
        curr_res_p = self.GSM.res_price.value[category]
        earnings = curr_res_p * quantity
        self.GSM.budget.add(earnings)
        self.GSM.res.sub(category, quantity)
        return True

    def buy_prod(self, category, quantity):
        self.GSM.commit(call=(func.buy_prod, category, quantity))
        curr_prices = self.GSM.prod_price.value[category]
        cost_to_buy = curr_prices * quantity
        self.GSM.budget.sub(cost_to_buy)
        self.GSM.prod.add(category, quantity)
        return True

    def sell_prod(self, category, quantity):
        self.GSM.commit(call=(func.sell_prod, category, quantity))
        curr_prices = self.GSM.prod_price.value[category]
        self.GSM.prod.sub(category, quantity)
        earnings = curr_prices * quantity
        self.GSM.budget.add(earnings)
        return True

    def make_prod(self, category, quantity):
        self.GSM.commit(call=(func.make_prod, category, quantity))
        res_for_type = self.GSM.production.res_cost[category]
        total_res = res_for_type * quantity
        self.GSM.res.sub(total_res)

        cost_to_produce = self.GSM.cost_to_produce(category, quantity)
        self.GSM.budget.sub(cost_to_produce)

        self.GSM.prod.add(category, quantity)
        return True

    def back(self):# TODO: need to deal with previous actions that did nothing? like show stats. perhaps a warning.
        if not self.GSM.callstack:
            logging.info("No previous action logged.")
            return False
        self.GSM.reverse_call(remove_last_call=True)
        #
        # prev_values = self.GSM.value_history.pop()
        # tmp = copy.deepcopy(self.GSM.value_history)
        # self.GSM.__dict__ = prev_values
        # self.GSM.__dict__["value_history"] = tmp
        # del self.GSM.callstack[-1]
        return True


    def show_stats(self):   # this should be moved to GS
        logging.info("Current Inventory: \n"
                     + "Resources\n" + str(self.GSM.res) + "\n"
                     + "Products\n" + str(self.GSM.prod))

        logging.info("Current Budget: " + str(self.GSM.budget))

        logging.info("Current Market Prices: \n"
                     + "Resources\n" + str(self.GSM.res_price) + "\n"
                     + "Products\n" + str(self.GSM.prod_price))

        logging.info("Fixed Costs: \n"
                     + str(self.GSM.production.hours_needed) + "\n"
                     + "Cost per hour: " + str(self.GSM.production.cost_per_hour))

        logging.info("Time elapsed: " + str(self.GSM.time_steps))
        return True

    def show_prices(self):
        logging.info("Current Market Prices: \n"
                     + "Resources\n" + str(self.GSM.res_price) + "\n"
                     + "Products\n" + str(self.GSM.prod_price))
        return True

    def show_history(self):
        logging.info(self.GSM.callstack)
        logging.info(self.GSM.value_history)
        return True

    def copy(self):
        return copy.deepcopy(self)


















