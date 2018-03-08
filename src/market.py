from singleton import Singleton
from bases import Base
import defaults

class MarketRes(Base):
    def __init__(self):
        self.price = defaults.starting_res_price

class MarketProd(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.price = defaults.starting_prod_price