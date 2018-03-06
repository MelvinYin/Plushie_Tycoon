from resources import ResourceCost
from inventory import ResourceInventory, PlushieInventory
from market import MarketResource, MarketPlushie
from production import ProductionCost
from budget import Budget
from singleton import Singleton


class GSM:
    __metaclass__ = Singleton
    def __init__(self):
        self.m_resource = MarketResource()
        self.m_plushie = MarketPlushie()
        self.resource_cost = ResourceCost()
        self.resources = ResourceInventory()
        self.plushies = PlushieInventory()
        self.budget = Budget()
        self.production_cost = ProductionCost()
        self.time_steps = 0

    def update(self, GS):
        self.__dict__ = GS.__dict__

