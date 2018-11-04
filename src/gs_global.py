import os
import pickle
from collections import defaultdict
from gs import GS
from gs_subclass import Inventory, Market, Budget, Production
from global_config import save_folder, save_file_name



class GSGlobal:
    def __init__(self, GSDataClass):
        self.gs_current = GS(GSDataClass)

    def return_data(self):
        return self.gs_current.return_data()

    def get(self, *args):
        return self.gs_current.get(*args)

    def add(self, *args):
        return self.gs_current.add(*args)

    def sub(self, *args):
        return self.gs_current.sub(*args)

    def commit(self, call):
        return self.gs_current.commit(call)

    def reverse_call(self):
        return self.gs_current.reverse_call()

    def load(self, call, file_path=save_folder, file_name=save_file_name):
        return self.gs_current.load(call, file_path, file_name)

    def save(self, call, file_path=save_folder, file_name=save_file_name):
        return self.gs_current.load(call, file_path, file_name)