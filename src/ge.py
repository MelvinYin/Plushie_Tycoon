from exceptions import InsufficientQuantityError, RepeatUIAction
import copy
import inspect
import sys
from logs import log
from global_config import Func, GSConstructor
from gs_main import GSM

class GE:
    def __init__(self):
        GS_dataclass = GSConstructor()
        GS_dataclass.load_init()
        assert GS_dataclass.is_complete()
        self.GS = GSM(GS_dataclass)
        self.GS.commit(call=dict(command=Func.start))
        self.callback = self._default_callback
        self.func_map = self.get_func_map()

    def return_data(self):
        return self.GS.return_data()

    def _default_callback(self, call):
        func_signal = call['command']
        func = self.func_map[func_signal]
        try:
            return_value = func(call)
        except InsufficientQuantityError:
            self.GS.reverse_call()
            log("InsufficientQuantityError>\n\n", inspect.currentframe())
            raise RepeatUIAction
        GS_update = self.GS.return_data()
        log("GE Call: {}\n Return: {}".format(call, GS_update),
            inspect.currentframe())
        return GS_update, return_value

    def buy(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
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
        mapping[Func.save] = self.GS.save
        mapping[Func.load] = self.GS.load
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

