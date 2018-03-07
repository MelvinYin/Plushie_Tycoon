from singleton import Singleton
from bases import BaseInt
import defaults

class Budget(BaseInt):
    __metaclass__ = Singleton
    def __init__(self):
        self.budget = defaults.starting_budget
        super().__init__(self.budget)

