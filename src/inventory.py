from singleton import Singleton
from abc import ABC
import pickle
from bases import Base
import defaults

class ResourceInventory(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.cloth = defaults.starting_res.cloth
        self.stuff = defaults.starting_res.stuff
        self.accessory = defaults.starting_res.accessory
        self.packaging = defaults.starting_res.packaging

class ProductInventory(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.aisha = defaults.starting_prod.aisha
        self.beta = defaults.starting_prod.beta
        self.chama = defaults.starting_prod.chama

#
#
# x = ResourceInventory()
# print(x)
# print(x.cloth)
# print(x["cloth"])
# x.cloth += 1
# x["stuff"] += 3
# print(x)
# print(x.cloth + 34)
# x.cloth = x.cloth + 35
# x.dump()
# x.load()
# print(x)