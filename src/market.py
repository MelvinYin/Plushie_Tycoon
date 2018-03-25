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

    def prettyp(self):
        string = f"Class: {self.__class__.__name__}\n"
        for key, value in self.__dict__.items():
            tmp = "\tAttr: " + key + "\n\t" \
                  + str(value).replace("\n", "\n\t") + "\n"
            string += tmp
        return string

    def test_func(self):
        return True

class MarketProd:
    __metaclass__ = Singleton
    def __init__(self):
        self.value = defaults.starting_prod_price

    def prettyp(self):
        string = f"Class: {self.__class__.__name__}\n"
        for key, value in self.__dict__.items():
            tmp = "\tAttr: " + key + "\n\t" \
                  + str(value).replace("\n", "\n\t") + "\n"
            string += tmp
        return string

    def test_func(self):
        return True
