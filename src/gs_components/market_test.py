from market import MarketBackend
from global_config import res_members, prod_members, Market

def _create_init_data():

    def _get_market(self):
        res = self._get_res_price()
        prod = self._get_prod_price()
        market = {**res, **prod}
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

def test_market():
    market = MarketBackend()
    assert isinstance(res, dict)
    assert isinstance(prod, dict)
    assert set(res.keys()) == set(res_members)
    assert set(prod.keys()) == set(prod_members)
    assert isinstance(list(res.values())[0], int)
    assert isinstance(list(prod.values())[0], int)