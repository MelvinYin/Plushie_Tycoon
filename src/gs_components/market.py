from global_config import Res, Prod, starting_res_price, \
    starting_prod_price

class MarketBackend:
    """
    Does not have external setting capabilities unless value
    explicitly called.
    """
    def __init__(self):
        self.res = starting_res_price
        self.prod = starting_prod_price
        self.type_map = self._get_type_map()

    def get(self, category):
        item = self.type_map[type(category)]
        return item[category]

    def _get_type_map(self):
        mapping = dict()
        mapping[Res] = self.res
        mapping[Prod] = self.prod
        return mapping