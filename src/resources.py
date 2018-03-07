import pandas as pd
from singleton import Singleton
from bases import Base
import defaults

class ResourceCost(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.index = ["cloth", "stuff", "accessory", "packaging"]
        self.aisha = defaults.aisha_res_cost
        self.beta = defaults.beta_res_cost
        self.chama = defaults.chama_res_cost
