from singleton import Singleton

import defaults
from bases import BaseMarket

class MarketRes(BaseMarket):
    """
    Does not have external setting capabilities unless _price
    explicitly called.
    """
    __metaclass__ = Singleton
    def __init__(self):
        self._price = defaults.starting_res_price
        super().__init__(self._price)

    def test_func(self):
        return True


class MarketProd(BaseMarket):
    __metaclass__ = Singleton

    def __init__(self):
        self._price = defaults.starting_prod_price
        super().__init__(self._price)

    def test_func(self):
        return True
