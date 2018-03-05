from singleton import Singleton
from bases import BaseInt

class Budget(BaseInt):
    __metaclass__ = Singleton
    def __init__(self):
        self.budget = self._default_budget()
        super().__init__(self.budget)

    def _default_budget(self):
        return 10000000

