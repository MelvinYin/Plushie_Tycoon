from singleton import Singleton

class ProductionCost(metaclass=Singleton):
    def __init__(self):
        self.plushie_manhours = self.default_hours()
        self.cost_per_hour = self.def_cost_per_hour()

    def default_hours(self):
        plushie_manhours = dict(Aisha=30, Beta=24, Chama=36)
        return plushie_manhours

    def def_cost_per_hour(self):
        return 2

    def get_hours(self, category):
        """ Might want to make this complicated in future, like scaling """
        return self.plushie_manhours[category]

    def __call__(self, category, quantity):
        total_cost = self.cost_per_hour * self.get_hours(category) * quantity
        return total_cost