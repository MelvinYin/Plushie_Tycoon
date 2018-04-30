from singleton import Singleton
import defaults

class Production:
    __metaclass__ = Singleton
    def __init__(self):
        self.hours_needed = defaults.hours_needed
        self.cost_per_hour = defaults.cost_per_hour
        self.res_cost = defaults.prod_res_cost

    def test_func(self):
        return True
















