from singleton import Singleton
import defaults

class Production:
    __metaclass__ = Singleton
    def __init__(self):
        self.hours_needed = defaults.hours_needed
        self.cost_per_hour = defaults.cost_per_hour
        self.res_cost = defaults.prod_res_cost

    def prettyp(self):
        string = f"Class: {self.__class__.__name__}\n"
        for key, value in self.__dict__.items():
            tmp = "\tAttr: " + key + "\n\t" \
                  + str(value).replace("\n", "\n\t") + "\n"
            string += tmp
        return string

    def test_func(self):
        return True
















