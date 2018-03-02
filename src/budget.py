from singleton import Singleton

class Budget(metaclass=Singleton):
    def __init__(self):
        self.budget = self._default_budget()

    def check(self):
        if self.budget < 0:
            raise InsufficentQuantity

    def _default_budget(self):
        return 10000

    def __add__(self, other):
        self.budget += other
        return self

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __sub__(self, other):
        self.budget -= other
        if self.budget < 0:
            raise InsufficentQuantity
        return self

    def __isub__(self, other):
        self.__sub__(other)
        return self

    def __repr__(self):
        return str(self.budget)

    def __str__(self):
        return self.__repr__()

