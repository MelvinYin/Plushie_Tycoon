from exceptions import InsufficientQuantityError, RepeatUIAction
import copy
import os
import pickle
import sys
import logging
from defaults import Func
from gs import GSM
import defaults

class GEM:
    def __init__(self):
        self.GSM = GSM()

    def __str__(self):
        return defaults.generic_str_fn(self)

    def __call__(self, call):
        methods = dict([(Func.save_game, self.save_game),
                            (Func.load_game, self.load_game),
                            (Func.quit_game, self.quit_game),
                            (Func.save_quit, self.save_quit),
                            (Func.next_turn, self.next_turn),
                            (Func.buy_res, self.buy_res),
                            (Func.sell_res, self.sell_res),
                            (Func.buy_prod, self.buy_prod),
                            (Func.make_prod, self.make_prod),
                            (Func.sell_prod, self.sell_prod),
                            (Func.show_stats, self.show_stats),
                            (Func.show_prices, self.show_prices),
                            (Func.show_history, self.show_history),
                            (Func.back, self.back)
                            ])
        logging.debug(f"Currently running: {call}")
        func_signal, args = call[0], call[1:]
        try:
            if args:
                methods[func_signal](*args)
            else:
                methods[func_signal]()
        except InsufficientQuantityError:
            self.GSM.reverse_call(remove_last_call=True)
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

    def save_game(self, file_path=defaults.def_save_folder, file_name=None):
        if not file_name:
            file_name = defaults.def_save_file_name
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
        self.GSM.commit(call=(Func.buy_res, category, quantity))
        curr_res_p = self.GSM.res_price.value[category]
        cost_to_buy = curr_res_p * quantity
        self.GSM.budget.sub(cost_to_buy)
        self.GSM.res.add(category, quantity)
        return True

    def sell_res(self, category, quantity):
        self.GSM.commit(call=(Func.sell_res, category, quantity))
        curr_res_p = self.GSM.res_price.value[category]
        earnings = curr_res_p * quantity
        self.GSM.budget.add(earnings)
        self.GSM.res.sub(category, quantity)
        return True

    def buy_prod(self, category, quantity):
        self.GSM.commit(call=(Func.buy_prod, category, quantity))
        curr_prices = self.GSM.prod_price.value[category]
        cost_to_buy = curr_prices * quantity
        self.GSM.budget.sub(cost_to_buy)
        self.GSM.prod.add(category, quantity)
        return True

    def sell_prod(self, category, quantity):
        self.GSM.commit(call=(Func.sell_prod, category, quantity))
        curr_prices = self.GSM.prod_price.value[category]
        self.GSM.prod.sub(category, quantity)
        earnings = curr_prices * quantity
        self.GSM.budget.add(earnings)
        return True

    def make_prod(self, category, quantity):
        self.GSM.commit(call=(Func.make_prod, category, quantity))
        res_for_type = self.GSM.production.res_cost[category]
        total_res = res_for_type * quantity
        self.GSM.res.sub(total_res)

        cost_to_produce = self.GSM.cost_to_produce(category, quantity)
        self.GSM.budget.sub(cost_to_produce)

        self.GSM.prod.add(category, quantity)
        return True

    def back(self):
        if not self.GSM.callstack:
            logging.info("No previous action logged.")
            return False
        self.GSM.reverse_call(remove_last_call=True)

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















