from collections import namedtuple
from singleton import Singleton
from abc import ABC

class MarketResource(metaclass=Singleton):
    def __init__(self):
        self.cloth = 10
        self.stuff = 20
        self.accessory = 18
        self.packaging = 12

    def __call__(self, category):
        return getattr(self, category)

class MarketPlushie(metaclass=Singleton):
    def __init__(self):
        self.Aisha = 80
        self.Beta = 76
        self.Chama = 52

    def __call__(self, category):
        return getattr(self, category)

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