from singleton import Singleton
import defaults

class Production:
    __metaclass__ = Singleton
    def __init__(self):
        self.hours_needed = defaults.hours_needed
        self.cost_per_hour = defaults.cost_per_hour
        self.res_cost = defaults.prod_res_cost

    def __str__(self):
        return defaults.generic_str_fn(self)

    def test_func(self):
        return True
















