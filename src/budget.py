from singleton import Singleton
import logging
import defaults
from exceptions import InsufficientQuantityError


class Budget:
    __metaclass__ = Singleton
    def __init__(self):
        self.value = defaults.starting_budget

    def __repr__(self):
        return super().__repr__()

    def prettyp(self):
        string = f"Class: {self.__class__.__name__}\n"
        for key, value in self.__dict__.items():
            tmp = "\tAttr: " + key + "\n\t" \
                  + str(value).replace("\n", "\n\t") + "\n"
            string += tmp
        return string

    def test_func(self):
        return True

    def sub(self, other):
        item = self.value - other
        if item < 0:
            logging.warning(f"Insufficient quantity in {self.__class__}. "
                            f"Attempting to deduct {other} from {self.value}.")
            raise InsufficientQuantityError
        self.value = item
        return True

    def add(self, other):
        self.value += other
        return True

    def replace(self, other):
        assert isinstance(other, float) or isinstance(other, int)
        assert other >= 0
        self.value = other
        return True
