from init_values import InitValues
from base import Res, Prod
import pandas as pd

class GSConstructor:
    def __init__(self):
        self.production = None
        self.budget = None
        self.inventory = None
        self.market = None
        self.time = None
        self.console = None

    def is_complete(self):
        all_full = True
        if None in (self.__dict__.values()):
            all_full = False
        return all_full

    def load_init(self):
        init_values = InitValues()
        self.load_production(init_values.production)
        self.budget = init_values.budget
        self.load_inventory(init_values.inventory)
        self.load_market(init_values.market)
        self.time = init_values.time
        self.load_console(init_values.console)
        return True

    def load_console(self, text):
        assert isinstance(text, str)
        self.console = text
        return True

    def load_production(self, _production):
        hours_needed = _production['hours_needed']
        res_ratio = _production['res_ratio']
        cost_per_hour = _production['cost_per_hour']
        assert isinstance(res_ratio, pd.DataFrame)
        assert isinstance(hours_needed, dict)
        assert set(hours_needed.keys()) == set(Prod)
        assert isinstance(list(hours_needed.values())[0], int)
        assert isinstance(cost_per_hour, int)
        # self.production = ProductionTuple(hours_needed, res_ratio,
        #                                   cost_per_hour)
        self.production = _production
        return True

    def load_budget(self, budget):
        assert isinstance(budget, int) or isinstance(budget, float)
        self.budget = budget
        return True

    def load_market(self, market):
        self.market = market
        assert isinstance(market, dict)
        assert set(market.keys()) == {*set(Res), *set(Prod)}
        assert isinstance(list(market.values())[0], int)
        return True

    def load_inventory(self, inventory):
        assert isinstance(inventory, dict)
        # This is no longer true, because warehouse_tier is inside inventory now
        self.inventory = inventory
        return True





