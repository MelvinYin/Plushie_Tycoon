from global_config import Res, Prod, starting_res_price, \
    starting_prod_price

class MarketBackend:
    """
    Does not have external setting capabilities unless value
    explicitly called.
    """
    def __init__(self, market_values):
        self.res = market_values.res
        self.prod = market_values.prod
        self.type_map = self._get_type_map()

    def get(self, category):
        item = self.type_map[type(category)]
        return item[category]

    def _get_type_map(self):
        mapping = dict()
        mapping[Res] = self.res
        mapping[Prod] = self.prod
        return mapping