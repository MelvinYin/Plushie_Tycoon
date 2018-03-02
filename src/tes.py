from singleton import Singleton
from abc import ABC
import pickle
import os

class InsufficentQuantityError(Exception):
    pass



class BaseInventory(ABC):
    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return str(self.__repr__())

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        if value < 0:
            raise InsufficentQuantityError
        self.__dict__[key] = value
        return True

    def __setattr__(self, key, value):
        if value is int:
            if value < 0:
                raise InsufficentQuantityError
        super().__setattr__(key, value)
        return

    def dump(self, file_path="../save/", file_name=None):
        if not file_name:
            file_name = self.__class__.__name__ + "_save.pkl"
        if not file_name.endswith(".pkl"):
            file_name += ".pkl"
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        with open(file_path + file_name, "wb") as file:
            pickle.dump(self.__dict__, file, -1)
        return True

    def load(self, file_path="../save/", file_name=None):
        if not file_name:
            file_name = self.__class__.__name__ + "_save.pkl"
        if not os.path.isdir(file_path):
            print(f"File path {file_path} does not exist.")
            raise FileNotFoundError
        if not os.path.isfile(file_path + file_name):
            print(f"File {file_name} does not exist in specified directory {file_path}.")
            raise FileNotFoundError
        with open(file_path + file_name, "rb") as file:
            self.__dict__ = pickle.load(file)
        return True

class ResourceInventory(BaseInventory):
    __metaclass__ = Singleton
    def __init__(self):
        self.cloth = 0
        self.stuff = 0
        self.accessory = 0
        self.packaging = 0

class PlushieInventory(BaseInventory):
    __metaclass__ = Singleton
    def __init__(self):
        self.Aisha = 0
        self.Beta = 0
        self.Chama = 0




x = ResourceInventory()
print(x)
print(x.cloth)
print(x["cloth"])
x.cloth += 1
x["stuff"] += 3
print(x)
print(x.cloth + 34)
x.cloth = x.cloth + 35
x.dump()
x.load()
print(x)