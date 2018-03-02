from singleton import Singleton
from abc import ABC
import pickle
from bases import Base

class InsufficentQuantityError(Exception):
    pass

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
        self.Aisha = 0
        self.Beta = 0
        self.Chama = 0

