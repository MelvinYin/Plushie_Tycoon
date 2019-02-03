from global_config import Res, Prod

class MarketBackend:
    """
    Does not have external setting capabilities unless value
    explicitly called.
    """
    def __init__(self, market_values):
        self.market = market_values

    def get(self, category):
        return self.market[category]