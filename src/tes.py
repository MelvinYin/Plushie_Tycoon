from singleton import Singleton
from abc import ABC
import pickle
import os

class InsufficentQuantityError(Exception):
    pass

class Base:
    def __init__(self):
        pass

    def __repr__(self):
        return str(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.key = value
        if self.key < 0:
            raise InsufficentQuantityError
        return True

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print("this is")
        print(key)
        print(self.__dict__)
        print(self.__dict__[key])
        if self.__dict__[key] < 0:
            raise InsufficentQuantityError
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
        if self.__dict__:
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
            self.__dict__ = pickle.load(file)
        return True


class ResourceInventory(Base):
    __metaclass__ = Singleton

    def __init__(self):
        self.cloth = 0
        self.stuff = 0
        self.accessory = 0
        self.packaging = 0


x = ResourceInventory()
# print(x)
# print(x.cloth)
# print(x["cloth"])
# x.cloth += 1
# x["stuff"] += 3
# print(x)
# print(x.cloth + 34)
# x.dump()
x.load()