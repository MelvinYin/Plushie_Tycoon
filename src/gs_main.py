from collections import defaultdict
from gs import GS
from global_config import save_folder, save_file_name
from gs_global import GSGlobal
from copy import deepcopy

nested_defaultdict = defaultdict(lambda: defaultdict(int))

class GSM:
    def __init__(self, GSDataClass):
        self.gs_current = GS(deepcopy(GSDataClass))
        self.gsm = GSGlobal(deepcopy(GSDataClass))
        self._callstack = []
        self._return_from_global = False

    def commit_call(self, call):
        self._callstack.append(call)

    def _compress_callstack(self):
        # Keeping this separate, instead of updating callstack directly when
        # the functions (buy/sell/etc) are called, so if call signature is
        # changed, we just need to change this function.
        callstack = deepcopy(nested_defaultdict)
        for call in self._callstack:
            action = call['command']
            category = call['category']
            quantity = call['quantity']
            callstack[action][category] += quantity
        return callstack

    def return_data(self):
        if self._return_from_global:
            to_return = self.gsm.return_data()
            self._return_from_global = False
        else:
            to_return = self.gs_current.return_data()
        return to_return

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
        self.gsm.implement_callstack(self._callstack)
        GS_newturn_dataclass = self.gsm.return_data()
        self.gs_current = GS(deepcopy(GS_newturn_dataclass))
        self._callstack = []
        self._return_from_global = True
        return 'update'

    def commit(self, call):
        return self.gs_current.commit(call)

    def reverse_call(self):
        return self.gs_current.reverse_call()

    def load(self, call, file_path=save_folder, file_name=save_file_name):
        return self.gs_current.load(call, file_path, file_name)

    def save(self, call, file_path=save_folder, file_name=save_file_name):
        return self.gs_current.load(call, file_path, file_name)