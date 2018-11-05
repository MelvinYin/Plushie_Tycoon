import pandas as pd
from collections import namedtuple
try:
    from .base import Res, Prod, Func, res_members, prod_members, \
        ProductionTuple, BudgetTuple, MarketTuple, InventoryTuple
    from .figure import FigureSpecs, FigureNames
    from .widget import WidgetSpecs
except:
    from base import Res, Prod, Func, res_members, prod_members, \
        ProductionTuple, BudgetTuple, MarketTuple, InventoryTuple
    from figure import FigureSpecs, FigureNames
    from widget import WidgetSpecs

class InitValues:
    def __init__(self):
        self.production = self._get_production()
        self.budget = self._get_budget()
        self.inventory = self._get_inventory()
        self.market = self._get_market()
        self.time = 0

    def _get_production(self):
        prod_res_cost = self._get_prod_res_cost()
        hours_needed = self._get_hours_needed()
        cost_per_hour = self._get_cost_per_hour()
        production = ProductionTuple(hours_needed, prod_res_cost, cost_per_hour)
        assert isinstance(prod_res_cost, pd.DataFrame)
        assert isinstance(hours_needed, dict)
        assert set(hours_needed.keys()) == set(prod_members)
        assert isinstance(list(hours_needed.values())[0], int)
        assert isinstance(cost_per_hour, int)
        return production

    def _get_prod_res_cost(self):
        # Plushie Resource Cost
        _res_cost = dict()
        _res_cost[Prod.aisha] = [3, 6, 2, 1]
        _res_cost[Prod.beta] = [1, 4, 1, 2]
        _res_cost[Prod.chama] = [2, 5, 1, 4]
        prod_res_cost = pd.DataFrame(_res_cost, index=res_members)
        return prod_res_cost

    def _get_hours_needed(self):
        # Plushie Production Hours
        _p_hours = [30, 24, 36]
        hours_needed = dict()
        for i, prod in enumerate(prod_members):
            hours_needed[prod] = _p_hours[i]
        return hours_needed

    def _get_cost_per_hour(self):
        # Cost Per Production Hour
        cost_per_hour = 3
        return cost_per_hour

    def _get_budget(self):
        # Starting Statistics
        _init_budget = 1000000
        budget = BudgetTuple(_init_budget)
        assert isinstance(_init_budget, int)
        return budget

    def _get_inventory(self):
        res = self._get_res()
        prod = self._get_prod()
        inventory = InventoryTuple(res, prod)
        assert isinstance(res, dict)
        assert isinstance(prod, dict)
        assert set(res.keys()) == set(res_members)
        assert set(prod.keys()) == set(prod_members)
        assert isinstance(list(res.values())[0], int)
        assert isinstance(list(prod.values())[0], int)
        return inventory

    def _get_market(self):
        res = self._get_res_price()
        prod = self._get_prod_price()
        market = MarketTuple(res, prod)
        assert isinstance(res, dict)
        assert isinstance(prod, dict)
        assert set(res.keys()) == set(res_members)
        assert set(prod.keys()) == set(prod_members)
        assert isinstance(list(res.values())[0], int)
        assert isinstance(list(prod.values())[0], int)
        return market

    def _get_res(self):
        _s_res = [1001, 1002, 1003, 1004]
        starting_res = dict()
        for i, res in enumerate(res_members):
            starting_res[res] = _s_res[i]
        return starting_res

    def _get_prod(self):
        _s_prod = [101, 102, 103]
        starting_prod = dict()
        for i, prod in enumerate(prod_members):
            starting_prod[prod] = _s_prod[i]
        return starting_prod

    def _get_res_price(self):
        _s_res_price = [10, 20, 18, 12]
        starting_res_price = dict()
        for i, res in enumerate(res_members):
            starting_res_price[res] = _s_res_price[i]
        return starting_res_price

    def _get_prod_price(self):
        _s_prod_price = [80, 76, 52]
        starting_prod_price = dict()
        for i, prod in enumerate(prod_members):
            starting_prod_price[prod] = _s_prod_price[i]
        return starting_prod_price

_history_columns = ["res", "prod", "res_price", "prod_price", "budget",
                    "production", "time_steps", "current_call"]

history_init = pd.DataFrame(columns=_history_columns)
