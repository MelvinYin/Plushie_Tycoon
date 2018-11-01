from exceptions import InsufficientQuantityError, RepeatUIAction
import copy
import inspect
import sys
from logs import log
from config.global_config import Func, Res, Prod, res_members, prod_members
from gs import GS


class GE:
    def __init__(self):
        self.GS = GS()
        self.GS.commit(call=dict(command=Func.start))
        self.callback = self._default_callback
        self.func_map = self.get_func_map()

    def _default_callback(self, call):
        func_signal = call['command']
        func = self.func_map[func_signal]
        try:
            return_value = func(call)
        except InsufficientQuantityError:
            self.GS.reverse_call()
            log("InsufficientQuantityError>\n\n", inspect.currentframe())
            raise RepeatUIAction
        GS_update = self._convert_GS_to_dict()
        log("GE Call: {}\n Return: {}".format(call, GS_update),
            inspect.currentframe())
        return GS_update

    def buy(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
        self.GS.inventory.add(category, quantity)
        price = self.GS.market.get(category)
        total_cost = price * quantity
        self.GS.budget.sub(total_cost)
        return True

    def sell(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
        self.GS.inventory.sub(category, quantity)
        price = self.GS.market.get(category)
        total_cost = price * quantity
        self.GS.budget.add(total_cost)
        return True

    def make(self, call):
        self.GS.commit(call=call)
        category = call['category']
        quantity = call['quantity']
        cost, materials = self.GS.production.get_cost(category)
        for _category, material in materials.items():
            self.GS.inventory.sub(_category, material * quantity)
        self.GS.budget.sub(cost * quantity)
        self.GS.inventory.add(category, quantity)
        return True

    def quit(self):
        sys.exit()

    def get_func_map(self):
        mapping = dict()
        mapping[Func.buy] = self.buy
        mapping[Func.sell] = self.sell
        mapping[Func.quit] = self.quit
        mapping[Func.make] = self.make
        mapping[Func.save] = self.GS.save
        mapping[Func.load] = self.GS.load
        mapping[Func.quit] = self.quit
        mapping[Func.next] = self.next_turn
        return mapping

    def next_turn(self):
        self.GS.current_time += 1
        self.GS.commit(call=dict(command=Func.next_turn))
        return

    def _convert_GS_to_dict(self):
        GS_update = dict()
        GS_update['price'] = dict()
        GS_update[Res] = {item: [self.GS.inventory.get(item)] for item\
                in res_members}
        GS_update[Prod] = {item: [self.GS.inventory.get(item)] for
                                       item in prod_members}
        GS_update['price'][Res] = {item: [self.GS.market.get(item)] for
                                           item in res_members}
        GS_update['price'][Prod] = {item: [self.GS.market.get(item)]
                                            for item in prod_members}

        GS_update["time"] = [self.GS.current_time]
        # GS_update[Production.hours_needed] = self.GS.production.hours_needed
        # GS_update[Production.cost_per_hour] = self.GS.production.cost_per_hour
        # GS_update[Production.res_cost] = self.GS.production.res_cost

        # GS_update["current_call"] = self.GS.current_call
        return GS_update

    def back(self):
        ret_value = self.GS.reverse_call()
        if not ret_value:
            log("No previous action logged.", inspect.currentframe())
            return False
        return True

    def copy(self):
        return copy.deepcopy(self)

