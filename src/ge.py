from collections import defaultdict
import copy
import inspect
import pickle
import sys

from exceptions import InsufficientQuantityError, RepeatUIAction
from logs import log
from global_config import Func, GSConstructor, save_folder, save_file_name
from gs_main import GSM

nested_defaultdict = defaultdict(lambda: defaultdict(int))

class ItemisedBillLogger:
    # Only for GS, not for GSGlobal
    def __init__(self):
        self.orders = dict()
        
    def buy(self, category, quantity, price, movein_cost):
        self.orders['buy'] = (category, quantity, price, movein_cost)
        return True
    
    def sell(self, category, quantity, price, moveout_cost):
        self.orders['sell'] = (category, quantity, price, moveout_cost)
        return True
    
    def make(self, category, quantity, movein_cost, res_ratio, moveout_costs):
        self.orders['make'] = (category, quantity, movein_cost, res_ratio, 
                              moveout_costs)
        return True
    
    def generate_bill(self):
        bill = ""
        for action, details in self.orders.items():
            if action == "buy":
                category, quantity, price, movein_cost = details
                cost = quantity * (price + movein_cost)
                bill += f"Order: Buy {category} x {quantity}"
                bill += f"Price per unit: {price}"
                bill += f"Movein cost per unit: {movein_cost}"
                bill += f"Total cost: {cost}"
            elif action == 'sell':
                category, quantity, price, moveout_cost = details
                revenue = quantity * (price - moveout_cost)
                bill += f"Order: Buy {category} x {quantity}"
                bill += f"Price per unit: {price}"
                bill += f"Moveout cost per unit: {moveout_cost}"
                bill += f"Total Revenue: {revenue}"
            elif action == 'make':
                # what form should res_ratio take?
                category, quantity, movein_cost, res_ratio, moveout_costs = \
                    details
                cost = quantity * (res_ratio * moveout_costs)
                bill += f"Order: Make {category} x {quantity}"
                bill += f"Required Resources: {res_ratio}"
                bill += f"Moveout cost per unit: {moveout_costs}"
                bill += f"Total Cost: {cost}"


class GE:
    def __init__(self):
        GS_dataclass = GSConstructor()
        GS_dataclass.load_init()
        assert GS_dataclass.is_complete()
        self.GS = GSM(GS_dataclass)
        self.GS.commit(call=dict(command=Func.start))
        self.callback = self._default_callback
        self.func_map = self.get_func_map()
        self.text = ""

    def return_data(self):
        return self.GS.return_data()

    def return_data_for_ui(self):
        return self.GS.return_data_for_ui()

    def _default_callback(self, call):
        func_signal = call['command']
        func = self.func_map[func_signal]
        try:
            return_value = func(call)
        except InsufficientQuantityError:
            self.GS.reverse_call()
            log("InsufficientQuantityError\n\n", inspect.currentframe())
            raise RepeatUIAction
        GS_update = self.GS.return_data_for_ui()
        # log("GE Call: {}\n Return: {}".format(call, GS_update),
        #     inspect.currentframe())
        return GS_update, return_value

    def buy(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
        self.text += f"Buy: {category} x {quantity}\n"
        self.GS.buy('inventory', category, quantity)
        movein_cost = self.GS.movein_cost(category, quantity)
        price = self.GS.get('market', category)
        total_cost = price * quantity + movein_cost
        self.GS.sub('budget', 'budget', total_cost)
        return 'update'

    def sell(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
        self.GS.sell('inventory', category, quantity)
        moveout_cost = self.GS.moveout_cost(category, quantity)
        price = self.GS.get('market', category)
        total_cost = price * quantity - moveout_cost
        self.GS.add('budget', 'budget', total_cost)
        return 'update'

    def make(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
        cost = 0
        production_cost, materials = self.GS.get('production', category)
        cost += production_cost * quantity
        for _category, material in materials.items():
            self.GS.sub('inventory', _category, material * quantity)
            moveout_cost = self.GS.moveout_cost(_category, material * quantity)
            cost += moveout_cost
        movein_cost = self.GS.movein_cost(category, quantity)
        cost += movein_cost
        self.GS.sub('budget', 'budget', cost)
        self.GS.make('inventory', category, quantity)
        return 'update'

    def quit(self, call):
        sys.exit()

    def get_func_map(self):
        mapping = dict()
        mapping[Func.buy] = self.buy
        mapping[Func.sell] = self.sell
        mapping[Func.quit] = self.quit
        mapping[Func.make] = self.make
        mapping[Func.save] = self.save
        mapping[Func.load] = self.load
        mapping[Func.next] = self.next_turn
        mapping[Func.back] = self.back
        return mapping

    def next_turn(self, call):
        storage_cost = self.GS.storage_cost()
        self.GS.sub('budget', 'budget', storage_cost)
        ret_value = self.GS.next_turn()
        self.GS.commit(call=call)
        return ret_value

    def back(self, call):
        ret_value = self.GS.reverse_call()
        if not ret_value:
            log("No previous action logged.", inspect.currentframe())
            return 'pause'
        return 'update'

    def copy(self):
        return copy.deepcopy(self)

    def save(self, call):
        self.GS.commit(call)
        GS_dataclass = self.GS.return_data()
        with open(save_folder + save_file_name, "wb") as file:
            pickle.dump(GS_dataclass, file, -1)
        return 'pause'

    def load(self, call):
        with open(save_folder + save_file_name, "rb") as file:
            GS_dataclass = pickle.load(file)
        self.GS = GSM(GS_dataclass)
        self.GS.commit(call)
        return 'update'


