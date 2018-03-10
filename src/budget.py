from singleton import Singleton
import logging
import defaults
from exceptions import InsufficientQuantityError


class Budget:
    __metaclass__ = Singleton
    def __init__(self):
        self._budget = defaults.starting_budget

    def test_func(self):
        return True

    def __eq__(self, other):
        return self._budget == other

    def __add__(self, other):
        item = self._budget + other
        return item

    def __iadd__(self, other):
        self._budget += other
        return self

    def __sub__(self, other):
        item = self._budget - other
        if item < 0:
            logging.warning(f"Insufficient quantity in {self.__class__}. "
                            f"Attempting to deduct {other} from {self.item}.")
            raise InsufficientQuantityError
        return item

    def __isub__(self, other):
        self._budget -= other
        if self._budget < 0:
            logging.warning(f"Insufficient quantity in {self.__class__}. "
                            f"Attempting to deduct {other} from {self._budget}.")
            raise InsufficientQuantityError
        return self

    def __mul__(self, other):
        item = self._budget * other
        return item

    def __imul__(self, other):
        self._budget *= other
        return self

    def __rmul__(self, other):
        item = self.__mul__(other)
        return item

    def __truediv__(self, other):
        item = self._budget / other
        return item

    def __floordiv__(self, other):
        item = self._budget // other
        return item

    def __mod__(self, other):
        item = self._budget % other
        return item

    def __itruediv__(self, other):
        self._budget = self._budget / other
        return self

    def __ifloordiv__(self, other):
        self._budget //= other
        return self

    def __imod__(self, other):
        self._budget = self._budget % other
        return self