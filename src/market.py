from singleton import Singleton
from bases import Base
import defaults

class MarketRes(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.res_price = defaults.starting_res_price

class MarketProd(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.prod_price = defaults.starting_prod_price