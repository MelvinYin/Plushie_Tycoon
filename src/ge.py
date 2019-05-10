from collections import defaultdict
from copy import deepcopy
from exceptions import InsufficientQuantityError, RepeatUIAction
import copy
import inspect
import sys
from logs import log
from global_config import Func, GSConstructor
from gs_main import GSM

nested_defaultdict = defaultdict(lambda: defaultdict(int))

# class BillGenerator:
#     """
#     todo: generate a new bill for every new order, to display.
#     """
#     def __init__(self):
#         self.text = ""
#         self.orders = deepcopy(nested_defaultdict)
#         self.callstack = []
#
#     def _generate_boilerplate(self):
#         boilerplate = "Itemised Bill\n" \
#                       "---------------\n" \
#                       "{}\n" \
#                       "---------------\n" \
#                       "Summary\n" \
#                       "Change in Inventory:\n" \
#                       "{}\n" \
#                       "Change in Budget:\n" \
#                       "{}\n"
#         return boilerplate
#
#     def add_item(self, call):
#         self.callstack.append(call)
#
#     # todo: buy and sell should be different, so we can eventually have
#     #  execution algorithms and delayed execution, see how gs_global
#     #  implement this.
#     def _compress_callstack(self):
#         callstack = deepcopy(nested_defaultdict)
#         for call in self.callstack:
#             action = call['command']
#             assert action in (Func.buy, Func.sell, Func.make)
#             category = call['category']
#             quantity = call['quantity']
#             callstack[action][category] += quantity
#         return callstack
#
#     def generate_bill(self, pricing_data):
#         orders = deepcopy(nested_defaultdict)
#         movements = defaultdict(int)
#         text = ""
#         for call in self.callstack:
#             command = call['command']
#             category = call['category']
#             quantity = call['quantity']
#             orders[command][category] += quantity
#             if command == 'buy':
#                 text += f"Order: Buy {category} x {quantity}"
#                 movements[category] += quantity
#             if command == 'sell':
#                 text += f"Order: Sell {category} x {quantity}"
#                 movements[category] -= quantity
#             if command == 'make':
#                 text += f"Order: Make {category} x {quantity}"
#                 orders[command][category] += quantity
#
#         text += "-------------\n"
#         text += "Summary\n"
#         compressed_callstack = self._compress_callstack()
#         for action, remainder in compressed_callstack.items():
#             text += f"{action}:\n"
#             for category, quantity in remainder.items():
#                 text += f"{category} + {quantity}"
#
#     def _format_text(self, to_write):
#         output = ""
#         assert 'command' in to_write, to_write
#         command = to_write['command']
#         category = ""
#         quantity = ""
#         if 'category' in to_write:
#             category = to_write['category']
#         if 'quantity' in to_write:
#             quantity = to_write['quantity']
#         output += "Command called: {} {} {}".format(command, category,
#                                                     quantity)
#         return output
#
#     def add_text(self, text):
#         formatted_text = self._format_text(text)
#         self.text += formatted_text
#         return True


class BillGenerator:
    """
    todo: generate a new bill for every new order, to display.
    """
    def __init__(self):
        self.text = ""
        self.orders = deepcopy(nested_defaultdict)
        self.pricing_data = defaultdict(dict)
        self.callstack = []
        self.order_section = ""


    def _generate_boilerplate(self):
        boilerplate = "Itemised Bill\n" \
                      "---------------\n" \
                      "{}\n" \
                      "---------------\n" \
                      "Summary\n" \
                      "Change in Inventory:\n" \
                      "{}\n" \
                      "Change in Budget:\n" \
                      "{}\n"
        return boilerplate

    def buy(self, category, quantity, cost_per_unit, movein_cost):
        self.order_section += f"Buy: {category} x {quantity}"
        self.pricing_data[category]['cost_per_unit'] = cost_per_unit
        self.pricing_data[category]['movein_cost'] = movein_cost
        self.callstack.append(dict(command='buy', category=category,
                                   quantity=quantity))

    def sell(self, category, quantity, cost_per_unit, moveout_cost):
        self.order_section += f"Sell: {category} x {quantity}"
        self.pricing_data[category]['cost_per_unit'] = cost_per_unit
        self.pricing_data[category]['moveout_cost'] = moveout_cost
        self.callstack.append(dict(command='sell', category=category,
                                   quantity=quantity))

    def make(self, category, quantity, cost_per_unit, movein_cost,
             ingredients, ingredient_moveout_cost):


    def _compress_callstack(self):
        callstack = deepcopy(nested_defaultdict)
        for call in self.callstack:
            action = call['command']
            assert action in (Func.buy, Func.sell, Func.make)
            category = call['category']
            quantity = call['quantity']
            callstack[action][category] += quantity
        return callstack



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

