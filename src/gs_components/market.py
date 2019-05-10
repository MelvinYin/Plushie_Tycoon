from global_config import Res, Prod

class Market:
    """
    Does not have external setting capabilities unless value
    explicitly called.
    """
    def __init__(self, market_values):
        self.market = market_values

    def set_values(self, values):
        for category, quantity in values.items():
            self.market[category] = quantity
        return True

    def get(self, category):
        return self.market[category]

    def return_data(self):
        return self.market
