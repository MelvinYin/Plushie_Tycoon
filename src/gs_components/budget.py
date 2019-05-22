from logs import log
import inspect
from exceptions import InsufficientQuantityError


class BudgetBackend:
    def __init__(self, budget):
        self.budget = budget

    def get(self):
        return self.budget

    def sub(self, other):
        item = self.budget - other
        if item < 0:
            msg = f"Insufficient quantity in {self.__class__}. Attempting to " \
                  f"deduct {other} from {self.budget}."
            log(msg, inspect.currentframe())
            raise InsufficientQuantityError
        self.budget = item
        return True

    def add(self, other):
        self.budget += other
        return True

    def replace(self, other):
        assert isinstance(other, float) or isinstance(other, int)
        assert other >= 0
        self.budget = other
        return True
