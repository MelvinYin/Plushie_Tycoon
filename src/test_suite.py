import importlib
import unittest
from unittest.mock import patch
import copy
import defaults
import pandas as pd


ge_file_path = "ge"
ge_file = importlib.import_module(ge_file_path)

test_GE = False



@unittest.skipIf(test_GE == False, "")
class TestGE(unittest.TestCase):

    def check_dict_equal(self, dict_1, dict_2):
        self.assertListEqual(list(dict_1.keys()), list(dict_1.keys()))
        self.assertEqual(len(dict_1), len(dict_2))
        dict_1_values = list(dict_1.values())
        dict_2_values = list(dict_2.values())
        for i in range(len(dict_1_values)):
            value_1 = dict_1_values[i]
            value_2 = dict_2_values[i]
            self.assertEqual(type(value_1), type(value_2))
            if isinstance(value_1, pd.Series) or isinstance(value_1, pd.DataFrame):
                self.check_pd_equal(value_1, value_2)
            elif isinstance(value_1, dict):
                self.check_dict_equal(value_1, value_2)
            elif "__dict__" in dir(value_1):
                self.check_dict_equal(value_1.__dict__, value_2.__dict__)
            else:
                self.assertEqual(value_1, value_2)

    def check_pd_equal(self, pd_1, pd_2):
        self.assertEqual(type(pd_1), type(pd_2))
        if isinstance(pd_1, pd.Series):
            pd.testing.assert_series_equal(pd_1, pd_2)
        elif isinstance(pd_1, pd.DataFrame):
            pd.testing.assert_frame_equal(pd_1, pd_2)
        else:
            self.assertEqual(pd_1, pd_2)


    def assert_equal(self, var_1, var_2):
        self.assertEqual(type(var_1), type(var_2))
        if isinstance(var_1, pd.Series) or isinstance(var_2, pd.DataFrame):
            self.check_pd_equal(var_1, var_2)
        elif isinstance(var_1, dict):
            self.check_dict_equal(var_1, var_2)
        elif "__dict__" in dir(var_1):
            self.check_dict_equal(var_1.__dict__, var_2.__dict__)
        else:
            self.assertEqual(var_1, var_2)

    def assert_GE_equal(self, GE1, GE2):
        self.assert_equal(GE1.GSM.res_price, GE2.GSM.res_price)
        self.assert_equal(GE1.GSM.prod_price, GE2.GSM.prod_price)
        self.assert_equal(GE1.GSM.prod_res_cost, GE2.GSM.prod_res_cost)
        self.assert_equal(GE1.GSM.res, GE2.GSM.res)
        self.assert_equal(GE1.GSM.prod, GE2.GSM.prod)
        self.assert_equal(GE1.GSM.budget, GE2.GSM.budget)
        self.assert_equal(GE1.GSM.cost_per_hour, GE2.GSM.cost_per_hour)
        self.assert_equal(GE1.GSM.prod_hours, GE2.GSM.prod_hours)
        self.assert_equal(GE1.GSM.time_steps, GE2.GSM.time_steps)
        return True

    def test_show_stats(self):
        GE = ge_file.GEM()
        GE_test = copy.deepcopy(GE)
        GE(("show_stats",))
        self.assert_GE_equal(GE, GE_test)

    def test_buy_res_stuff(self):
        GE = ge_file.GEM()
        GE_test = copy.deepcopy(GE)
        GE(("buy_res","stuff", 20))
        GE_test.GSM.res.stuff += 20
        cost = GE_test.GSM.res_price.stuff * 20
        GE_test.GSM.budget -= cost
        self.assert_GE_equal(GE, GE_test)

    def test_sell_res_cloth(self):
        GE = ge_file.GEM()
        GE_test = copy.deepcopy(GE)
        GE(("sell_res","cloth", 20))
        GE_test.GSM.res.cloth -= 20
        cost = GE_test.GSM.res_price.cloth * 20
        GE_test.GSM.budget += cost
        self.assert_GE_equal(GE, GE_test)

    def test_buy_prod_aisha(self):
        GE = ge_file.GEM()
        GE_test = copy.deepcopy(GE)
        GE(("buy_prod", "aisha", 5))
        GE_test.GSM.prod.aisha += 5
        cost = GE_test.GSM.prod_price.aisha * 5
        GE_test.GSM.budget -= cost
        self.assert_GE_equal(GE, GE_test)

    def test_make_prod_beta(self):
        GE = ge_file.GEM()
        GE_test = copy.deepcopy(GE)
        GE(("make_prod", "beta", 5))
        GE_test.GSM.prod.beta += 5
        res_needed = GE_test.GSM.prod_res_cost.beta * 5
        GE_test.GSM.res -= res_needed
        cost = GE_test.GSM.prod_hours.beta * GE_test.GSM.cost_per_hour
        GE_test.GSM.budget -= cost
        self.assert_GE_equal(GE, GE_test)

    def test_sell_prod_chama(self):
        GE = ge_file.GEM()
        GE_test = copy.deepcopy(GE)
        GE(("sell_prod", "chama", 7))
        GE_test.GSM.prod.chama -= 7
        cost = GE_test.GSM.prod_price.chama * 7
        GE_test.GSM.budget += cost
        self.assert_GE_equal(GE, GE_test)





import market







if __name__ == '__main__':
    unittest.main(verbosity=0)