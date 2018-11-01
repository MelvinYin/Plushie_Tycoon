from singleton import Singleton
import global_config
from logs import log
import inspect
from exceptions import InsufficientQuantityError


class Budget:
    __metaclass__ = Singleton
    def __init__(self):
        self.value = global_config.starting_budget

    def get(self):
        return self.value

    def test_func(self):
        return True

    def sub(self, other):
        item = self.value - other
        if item < 0:
            msg = f"Insufficient quantity in {self.__class__}. Attempting to " \
                  f"deduct {other} from {self.value}."
            log(msg, inspect.currentframe())
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
