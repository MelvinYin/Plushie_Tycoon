import os
import pickle
from collections import defaultdict
from gs import GS
from gs_subclass import Inventory, Market, Budget, Production
from global_config import save_folder, save_file_name
from gs_global import GSGlobal
from copy import deepcopy

nested_defaultdict = defaultdict(lambda: defaultdict(int))

class GSM:
    def __init__(self, GSDataClass):
        self.gs_current = GS(GSDataClass)
        self.gsm = GSGlobal(GSDataClass)
        self._callstack = []

    def commit_call(self, call):
        self._callstack.append(call)

    def _build_default_callstack(self):
        callstack = dict()
        default_for_buy_sell_make = dict()
        default_for_buy_sell_make['inventory'] = defaultdict(int)
        default_for_buy_sell_make['market'] = defaultdict(int)
        callstack['buy_sell'] = deepcopy(default_for_buy_sell_make)
        callstack['make'] = deepcopy(default_for_buy_sell_make)
        default_for_add_sub = dict()
        default_for_add_sub['inventory'] = defaultdict(int)
        default_for_add_sub['market'] = defaultdict(int)
        default_for_add_sub['budget'] = defaultdict(int)
        callstack['add_sub'] = deepcopy(default_for_add_sub)
        return callstack

    def _compress_callstack(self):
        # Keeping this separate, instead of updating callstack directly when
        # the functions (buy/sell/etc) are called, so if call signature is
        # changed, we just need to change this function.
        callstack = nested_defaultdict
        for call in self._callstack:
            assert len(call) == 3
            action, category, quantity = call
            if action == 'buy':
                callstack['buy_sell'][category] += quantity
            elif action == 'sell':
                callstack['buy_sell'][category] -= quantity
            elif action == 'make':
                callstack['make'][category] += quantity
            else:
                raise Exception
        return callstack

    def return_data(self):
        return self.gs_current.return_data()

    def get(self, *args):
        return self.gs_current.get(*args)

    def buy(self, *args):
        return self.gs_current.add(*args)

    def sell(self, *args):
        return self.gs_current.sub(*args)

    def make(self, *args):
        return self.gs_current.add(*args)

    def add(self, *args):
        return self.gs_current.add(*args)

    def sub(self, *args):
        return self.gs_current.sub(*args)

    def next_turn(self):
        self._callstack = self._compress_callstack()
        self._callstack = defaultdict(list)
        self.gs_current.add('time')

        return 'update'

    def commit(self, call):
        return self.gs_current.commit(call)

    def reverse_call(self):
        return self.gs_current.reverse_call()

    def load(self, call, file_path=save_folder, file_name=save_file_name):
        return self.gs_current.load(call, file_path, file_name)

    def save(self, call, file_path=save_folder, file_name=save_file_name):
        return self.gs_current.load(call, file_path, file_name)