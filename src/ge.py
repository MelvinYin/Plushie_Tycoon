from exceptions import InsufficientQuantityError, RepeatUIAction
import copy
import os
import pickle
import sys
import logging
from defaults import Func
from gs import GSM
import defaults
from defaults import Res, Prod, ResPrice, ProdPrice, Production
# TODO: time_steps should be handled by GE, not by UI.

# def commit_decr(func_signal):
#     def decr(func):
#         def wrapper(*args, **kwargs):
#             call = tuple([func_signal, *args])
#             self.GSM.commit(call=call)
#             try:
#                 return func(*args, **kwargs)
#             except:
#                 self.GSM.reverse_call(remove_last_call=True)
#                 logging.error(f"Exception thrown: {call}")
#                 raise
#         return wrapper
#     return decr

class GEM:
    def __init__(self):
        self.GSM = GSM()
        self.callback = self.alt_callback

    def _default_callback(self):
        GSM_update = self._convert_GSM_to_dict()
        return GSM_update

    def alt_callback(self, call):
        methods = dict([
            (Func.save, self.save),
            (Func.load, self.load),
            (Func.quit, self.quit),
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
        func_signal, args = call[0], call[1]
        try:
            if args:
                methods[func_signal](*args)
            else:
                methods[func_signal]()
        except InsufficientQuantityError:
            self.GSM.reverse_call()
            raise RepeatUIAction
        GSM_update = self._convert_GSM_to_dict()
        return GSM_update

    def _convert_GSM_to_dict(self):
        GSM_update = dict()
        GSM_update[Res.cloth] = self.GSM.res.value[Res.cloth]
        GSM_update[Res.stuff] = self.GSM.res.value[Res.stuff]
        GSM_update[Res.accessory] = self.GSM.res.value[Res.accessory]
        GSM_update[Res.packaging] = self.GSM.res.value[Res.packaging]

        GSM_update[Prod.aisha] = self.GSM.prod.value[Prod.aisha]
        GSM_update[Prod.beta] = self.GSM.prod.value[Prod.beta]
        GSM_update[Prod.chama] = self.GSM.prod.value[Prod.chama]

        GSM_update[ResPrice.cloth] = self.GSM.res.value[ResPrice.cloth]
        GSM_update[ResPrice.stuff] = self.GSM.res.value[ResPrice.stuff]
        GSM_update[ResPrice.accessory] = self.GSM.res.value[ResPrice.accessory]
        GSM_update[ResPrice.packaging] = self.GSM.res.value[ResPrice.packaging]

        GSM_update[ProdPrice.aisha] = self.GSM.res.value[ProdPrice.aisha]
        GSM_update[ProdPrice.beta] = self.GSM.res.value[ProdPrice.beta]
        GSM_update[ProdPrice.chama] = self.GSM.res.value[ProdPrice.chama]

        GSM_update[Production.hours_needed] = self.GSM.res.value[Production.hours_needed]
        GSM_update[Production.cost_per_hour] = self.GSM.res.value[Production.cost_per_hour]
        GSM_update[Production.res_cost] = self.GSM.res.value[Production.res_cost]

        GSM_update["current_call"] = self.GSM.current_call
        GSM_update["time_steps"] = self.GSM.time_steps
        return GSM_update

    def prettyp(self):
        string = f"Class: {self.__class__.__name__}\n"
        for key, value in self.__dict__.items():
            tmp = "\tAttr: " + key + "\n\t" \
                  + str(value).replace("\n", "\n\t") + "\n"
            string += tmp
        return string

    def __call__(self, call):
        methods = dict([
            (Func.save, self.save),
            (Func.load, self.load),
            (Func.quit, self.quit),
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
        func_signal, args = call[0], call[1]
        try:
            if args:
                methods[func_signal](*args)
            else:
                methods[func_signal]()
        except InsufficientQuantityError:
            self.GSM.reverse_call()
            raise RepeatUIAction
        return self.callback()


    def load(self, file_path=defaults.def_save_folder, file_name=None):
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
        return True

    def save(self, file_path=defaults.def_save_folder, file_name=None):
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
            pickle.dump(self.GSM.__dict__, file, -1)
        return True

    def quit(self):
        sys.exit()

    def save_quit(self):
        self.save()
        self.quit()

    def next_turn(self):
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
        ret_value = self.GSM.reverse_call()
        if not ret_value:
            logging.info("No previous action logged.")
            return False
        return True

    def show_stats(self):
        return self.GSM.show_stats()

    def show_prices(self):
        return self.GSM.show_prices()

    def show_history(self):
        return self.GSM.show_history()

    def copy(self):
        return copy.deepcopy(self)















