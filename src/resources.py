import pandas as pd
from singleton import Singleton
from bases import Base
import default_values

class ResourceCost(Base):
    __metaclass__ = Singleton
    def __init__(self):
        self.index = ["cloth", "stuff", "accessory", "packaging"]
        self.aisha = default_values.aisha_res_cost
        self.beta = default_values.beta_res_cost
        self.chama = default_values.chama_res_cost
