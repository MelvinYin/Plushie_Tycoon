from singleton import Singleton
from abc import ABC
import pickle
from bases import Base

class ResourceInventory(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.cloth = 0
        self.stuff = 0
        self.accessory = 0
        self.packaging = 0

class PlushieInventory(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.aisha = 0
        self.beta = 0
        self.chama = 0

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