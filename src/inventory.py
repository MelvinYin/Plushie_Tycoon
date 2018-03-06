from singleton import Singleton
from abc import ABC
import pickle
from bases import Base
import default_values

class ResourceInventory(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.cloth = default_values.starting_cloth
        self.stuff = default_values.starting_stuff
        self.accessory = default_values.starting_accessory
        self.packaging = default_values.starting_packaging

class PlushieInventory(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.aisha = default_values.starting_aisha
        self.beta = default_values.starting_beta
        self.chama = default_values.starting_chama

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