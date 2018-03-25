from singleton import Singleton
from abc import ABC
import pickle
from bases import BaseInventory
import defaults
import pandas as pd
import logging
import copy


class ResourceInventory(BaseInventory):
    __metaclass__ = Singleton
    def __init__(self):
        super().__init__(copy.deepcopy(defaults.starting_res))

    def prettyp(self):
        string = f"Class: {self.__class__.__name__}\n"
        for key, value in self.__dict__.items():
            tmp = "\tAttr: " + key + "\n\t" \
                  + str(value).replace("\n", "\n\t") + "\n"
            string += tmp
        return string

    def test_func(self):
        return True


class ProductInventory(BaseInventory):
    __metaclass__ = Singleton
    def __init__(self):
        super().__init__(copy.deepcopy(defaults.starting_prod))

    def prettyp(self):
        string = f"Class: {self.__class__.__name__}\n"
        for key, value in self.__dict__.items():
            tmp = "\tAttr: " + key + "\n\t" \
                  + str(value).replace("\n", "\n\t") + "\n"
            string += tmp
        return string

    def test_func(self):
        return True
