import pandas as pd
from collections import namedtuple
try:
    from .base import Res, Prod, Func
    from .figure import FigureNames
except:
    from base import Res, Prod, Func
    from figure import FigureNames

class InitValues:
    def __init__(self):
        self.production = self._get_production()
        self.budget = 10000
        self.inventory = self._get_inventory()
        self.market = self._get_market()
        self.console = self._get_console()
        self.time = 0

    def _get_console(self):
        return "Init_text<p>"

    def _get_production(self):
        res_ratio = self._get_res_ratio()
        hours_needed = self._get_hours_needed()
        cost_per_hour = self._get_cost_per_hour()
        production = dict()
        production['hours_needed'] = hours_needed
        production['res_ratio'] = res_ratio
        production['cost_per_hour'] = cost_per_hour
        # production = ProductionTuple(hours_needed, res_ratio,
        #                              cost_per_hour)
        assert isinstance(hours_needed, dict)
        assert isinstance(list(hours_needed.values())[0], int)
        assert isinstance(cost_per_hour, int)
        return production

    def _get_res_ratio(self):
        # Plushie Resource Cost
        _res_ratio = dict()
        _res_ratio[Prod.aisha.name] = [3, 6, 2, 1]
        _res_ratio[Prod.beta.name] = [1, 4, 1, 2]
        _res_ratio[Prod.chama.name] = [2, 5, 1, 4]

        res_ratio = dict()
        for i, prod in enumerate(Prod):
            local_map = dict()
            for j, res in enumerate(Res):
                local_map[res.name] = _res_ratio[prod.name][j]
            res_ratio[prod.name] = local_map
        for res in Res:
            local_map = dict()
            for prod in Prod:
                local_map[prod.name] = res_ratio[prod.name][res.name]
            res_ratio[res.name] = local_map
        return res_ratio

    def _get_hours_needed(self):
        # Plushie Production Hours
        _p_hours = [30, 24, 36]
        hours_needed = dict()
        for i, prod in enumerate(Prod):
            hours_needed[prod.name] = _p_hours[i]
        return hours_needed

    def _get_cost_per_hour(self):
        # Cost Per Production Hour
        cost_per_hour = 3
        return cost_per_hour

    def _get_budget(self):
        # Starting Statistics
        _init_budget = 1000000
        return _init_budget

    def _get_inventory(self):
        res = self._get_res()
        prod = self._get_prod()
        inventory = {**res, **prod}
        inventory['tier'] = 0

        weights = dict()
        weights[Res.cloth.name] = 0.1
        weights[Res.stuffing.name] = 0.05
        weights[Res.accessory.name] = 0.3
        weights[Res.packaging.name] = 0.05
        weights[Prod.aisha.name] = 0.05
        weights[Prod.beta.name] = 0.05
        weights[Prod.chama.name] = 0.05
        inventory['weight'] = weights

        volume = dict()
        volume[Res.cloth.name] = 0.1
        volume[Res.stuffing.name] = 0.3
        volume[Res.accessory.name] = 0.01
        volume[Res.packaging.name] = 0.2
        volume[Prod.aisha.name] = 0.2
        volume[Prod.beta.name] = 0.2
        volume[Prod.chama.name] = 0.2
        inventory['volume'] = volume

        assert isinstance(inventory, dict)
        # assert isinstance(list(inventory.values())[0], int)
        return inventory

    def _get_market(self):
        res = self._get_res_price()
        prod = self._get_prod_price()
        market = {**res, **prod}
        assert isinstance(res, dict)
        assert isinstance(prod, dict)
        assert isinstance(list(res.values())[0], int)
        assert isinstance(list(prod.values())[0], int)
        return market

    def _get_res(self):
        _s_res = [1001, 1002, 1003, 1004]
        starting_res = dict()
        for i, res in enumerate(Res):
            starting_res[res.name] = _s_res[i]
        return starting_res

    def _get_prod(self):
        _s_prod = [101, 102, 103]
        starting_prod = dict()
        for i, prod in enumerate(Prod):
            starting_prod[prod.name] = _s_prod[i]
        return starting_prod

    def _get_res_price(self):
        _s_res_price = [10, 20, 18, 12]
        starting_res_price = dict()
        for i, res in enumerate(Res):
            starting_res_price[res.name] = _s_res_price[i]
        return starting_res_price

    def _get_prod_price(self):
        _s_prod_price = [80, 76, 52]
        starting_prod_price = dict()
        for i, prod in enumerate(Prod):
            starting_prod_price[prod.name] = _s_prod_price[i]
        return starting_prod_price
