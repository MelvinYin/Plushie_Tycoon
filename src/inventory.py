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

    def __str__(self):
        return defaults.generic_str_fn(self)

    def test_func(self):
        return True


class ProductInventory(BaseInventory):
    __metaclass__ = Singleton
    def __init__(self):
        super().__init__(copy.deepcopy(defaults.starting_prod))

    def __str__(self):
        return defaults.generic_str_fn(self)

    def test_func(self):
        return True
