from singleton import Singleton
from abc import ABC
import pickle

class InsufficentQuantityError(Exception):
    pass

class BaseInventory(ABC):
    def __init__(self, item):
        self.__dict__["item"] = item

    def __getitem__(self, item):
        return self.item[item]

    def __setitem__(self, key, value):
        self.item[key] = value
        if self.item[key] >= 0:
            raise InsufficentQuantityError
        return True

    def __getattr__(self, item):
        return self.item[item]

    def __setattr__(self, key, value):
        if not hasattr(self, "resource"):
            print("ResourceInventory does not have resource initialised. Check"
                  "naming of attributes.")
            raise NotImplementedError
        self.item[key] = value
        return

    def __repr__(self):
        return str(self.item)

    def dump(self, file_path="../save/", file_name=None):
        if not file_name:
            file_name = self.__class__.__name__ + "_save.pkl"
        if not file_name.endswith(".pkl"):
            file_name += ".pkl"
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        with open(file_path + file_name, "wb") as file:
            pickle.dump(self.item, file, -1)
        return True

    def load(self, file_path="../save/", file_name=None):
        if hasattr(self, "item"):
            print("Warning: Current item exists. Overwritting.")
        if not file_name:
            file_name = self.__class__.__name__ + "_save.pkl"
        if not os.path.isdir(file_path):
            print(f"File path {file_path} does not exist.")
            raise FileNotFoundError
        if not os.path.isfile(file_path + file_name):
            print(f"File {file_name} does not exist in specified directory {file_path}.")
            raise FileNotFoundError
        with open(file_path + file_name, "rb") as file:
            self.__dict__["item"] = pickle.load(file)
        return True

class ResourceInventory(BaseInventory):
    __metaclass__ = Singleton

    def __init__(self):
        self.__dict__["resource"] = self._default_resources()
        super().__init__(self.resource)

    def _default_resources(self):
        resource = dict(cloth=0, stuff=0, accessory=0, packaging=0)
        return resource


class PlushieInventory(BaseInventory):
    __metaclass__ = Singleton
    def __init__(self):
        self.__dict__["plushie"] = self._default_plushie()
        super().__init__(self.plushie)

    def _default_plushie(self):
        plushie = dict(Aisha=0, Beta=0, Chama=0)
        return plushie

