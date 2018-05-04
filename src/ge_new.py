from exceptions import InsufficientQuantityError, RepeatUIAction
import copy
import os
import pickle
import sys
import logging
from defaults import Func
from gs import GSM
from defaults import Res, Prod, ResPrice, ProdPrice, Production, save_folder, save_file_name
from enum import Enum, auto

class Func(Enum):
    buy = auto()
    sell = auto()
    make = auto()

class Other_Func(Enum):
    save = auto()
    load = auto()
    quit = auto()



class GEM:
    def __init__(self):
        self.GSM = GSM()
        self.GSM.commit(call=Func.start)
        self.callback = self._default_callback
        self.func_map = self.get_func_map()
        self.other_func_map = self.get_other_func_map()
        self.category_map = self.get_category_map()

    def _default_callback(self, call):
        func_signal = call.pop(0)
        if func_signal in self.func_map:
            return_value = self.passed(self.func_map[func_signal], call)
        elif func_signal in self.other_func_map:
            return_value = self.passed(self.other_func_map[func_signal], call)
        else:
            raise Exception

    def passed(self, func, call):
        category = call.pop(0)
        if category in self.category_map:
            return func(self.category_map[category], call)






class GEM:
    def __init__(self):
        self.GSM = GSM()
        self.GSM.commit(call=Func.start)
        self.callback = self._default_callback

    def _default_callback(self, call):





        methods = dict([
            (Func.save, self.save),
            (Func.load, self.load),
            (Func.quit, self.quit),
            (Func.next_turn, self.next_turn),
            (Func.buy_res, self.buy_res),
            (Func.sell_res, self.sell_res),
            (Func.buy_prod, self.buy_prod),
            (Func.make_prod, self.make_prod),
            (Func.sell_prod, self.sell_prod),
            (Func.back, self.back)])

        logging.debug(f"Callback in GEM: {call}")
        if hasattr(call, "__len__") and len(call) == 1:
            func_signal = call[0]
            args = None
        else:
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

        GSM_update[ResPrice.cloth] = self.GSM.res_price.value[Res.cloth]
        GSM_update[ResPrice.stuff] = self.GSM.res_price.value[Res.stuff]
        GSM_update[ResPrice.accessory] = self.GSM.res_price.value[Res.accessory]
        GSM_update[ResPrice.packaging] = self.GSM.res_price.value[Res.packaging]

        GSM_update[ProdPrice.aisha] = self.GSM.prod_price.value[Prod.aisha]
        GSM_update[ProdPrice.beta] = self.GSM.prod_price.value[Prod.beta]
        GSM_update[ProdPrice.chama] = self.GSM.prod_price.value[Prod.chama]

        # GSM_update[Production.hours_needed] = self.GSM.production.hours_needed
        # GSM_update[Production.cost_per_hour] = self.GSM.production.cost_per_hour
        # GSM_update[Production.res_cost] = self.GSM.production.res_cost

        # GSM_update["current_call"] = self.GSM.current_call
        GSM_update["time_steps"] = self.GSM.current_time
        return GSM_update

    def load(self, file_path=save_folder, file_name=save_file_name):
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

    def save(self, file_path=save_folder, file_name=save_file_name):
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

    def next_turn(self):
        self.GSM.current_time += 1
        self.GSM.commit(call=Func.next_turn)
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
        curr_prices = self.GSM.res_price.value[category]
        earnings = curr_prices * quantity
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
        earnings = curr_prices * quantity
        self.GSM.budget.add(earnings)
        self.GSM.prod.sub(category, quantity)
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

    def copy(self):
        return copy.deepcopy(self)