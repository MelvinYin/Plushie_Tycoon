from singleton import Singleton

import defaults
from bases import BaseMarket

class MarketRes:
    """
    Does not have external setting capabilities unless value
    explicitly called.
    """
    __metaclass__ = Singleton
    def __init__(self):
        self.value = defaults.starting_res_price

    def test_func(self):
        return True

class MarketProd:
    __metaclass__ = Singleton
    def __init__(self):
        self.value = defaults.starting_prod_price

    def test_func(self):
        return True

