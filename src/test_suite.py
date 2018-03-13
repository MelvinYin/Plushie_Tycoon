import importlib
import unittest
from unittest.mock import patch
import defaults
import pandas as pd
import pickle
import copy


ge_file_path = "ge"
ge_file = importlib.import_module(ge_file_path)

test_GE = True



@unittest.skipIf(test_GE == False, "")
class TestGE(unittest.TestCase):

    def check_list_equal(self, var_1, var_2):
        try:
            self.assertListEqual(var_1, var_2)
            return True
        except AssertionError:
            pass
        assert len(var_1) == len(var_2)
        for i in range(len(var_1)):
            self.assert_equal(var_1[i], var_2[i])


    def check_dict_equal(self, dict_1, dict_2):
        try:
            self.assertDictEqual(dict_1, dict_2)
            return True
        except:
            pass
        self.assertListEqual(list(dict_1.keys()), list(dict_1.keys()))
        self.assertEqual(len(dict_1), len(dict_2))
        dict_1_values = list(dict_1.values())
        dict_2_values = list(dict_2.values())
        for i in range(len(dict_1_values)):
            value_1 = dict_1_values[i]
            value_2 = dict_2_values[i]
            try:
                self.assertEqual(value_1, value_2)
            except:
                pass
            self.assertEqual(type(value_1), type(value_2))
            if isinstance(value_1, pd.Series) or isinstance(value_1, pd.DataFrame):
                self.check_pd_equal(value_1, value_2)
            elif isinstance(value_1, dict):
                self.check_dict_equal(value_1, value_2)
            elif "__dict__" in dir(value_1):
                self.check_dict_equal(value_1.__dict__, value_2.__dict__)
            elif isinstance(value_1, list) or isinstance(value_1, tuple):
                self.check_list_equal(value_1, value_2)
            else:
                self.assert_equal(value_1, value_2)

    def check_pd_equal(self, pd_1, pd_2):
        self.assertEqual(type(pd_1), type(pd_2))
        if isinstance(pd_1, pd.Series):
            pd.testing.assert_series_equal(pd_1, pd_2)
        elif isinstance(pd_1, pd.DataFrame):
            pd.testing.assert_frame_equal(pd_1, pd_2)
        else:
            self.assertEqual(pd_1, pd_2)


    def assert_equal(self, var_1, var_2):
        try:
            self.assertEqual(var_1, var_2)
            return True
        except:
            self.assertEqual(type(var_1), type(var_2))
            if isinstance(var_1, pd.Series) or isinstance(var_2, pd.DataFrame):
                self.check_pd_equal(var_1, var_2)
            elif isinstance(var_1, dict):
                self.check_dict_equal(var_1, var_2)
            elif "__dict__" in dir(var_1):
                self.check_dict_equal(var_1.__dict__, var_2.__dict__)
            elif isinstance(var_1, list) or isinstance(var_1, tuple):
                self.check_list_equal(var_1, var_2)
            else:
                self.assertEqual(var_1, var_2)

    def assert_GE_equal(self, GE1, GE2):
        self.assert_equal(GE1.GSM.res_price, GE2.GSM.res_price)
        self.assert_equal(GE1.GSM.prod_price, GE2.GSM.prod_price)
        self.assert_equal(GE1.GSM.production, GE2.GSM.production)
        self.assert_equal(GE1.GSM.res, GE2.GSM.res)
        self.assert_equal(GE1.GSM.prod, GE2.GSM.prod)
        self.assert_equal(GE1.GSM.budget, GE2.GSM.budget)
        self.assert_equal(GE1.GSM.time_steps, GE2.GSM.time_steps)
        self.assert_equal(GE1.GSM.value_history, GE2.GSM.value_history)
        self.assert_equal(GE1.GSM.callstack, GE2.GSM.callstack)
        return True

    def test_for_test(self):
        GE = ge_file.GEM()
        GE_test = GE.copy()
        self.assert_GE_equal(GE, GE_test)

    def test_show_stats(self):
        GE = ge_file.GEM()
        GE_test = GE.copy()
        GE(("show_stats",))
        self.assert_GE_equal(GE, GE_test)

    def test_buy_res_stuff(self):
        GE = ge_file.GEM()
        GE_test = GE.copy()
        GE(("buy_res","stuff", 20))

        val_hist = copy.deepcopy(GE_test.GSM.__dict__)
        del val_hist["value_history"]
        print(val_hist['res'].value)
        GE_test.GSM.value_history.append(val_hist)
        GE_test.GSM.callstack.append(("buy_res", "stuff", 20))
        GE_test.GSM.res.add("stuff", 20)
        print(val_hist['res'].value)
        cost = defaults.starting_res_price.stuff * 20
        GE_test.GSM.budget.sub(cost)
        self.assert_GE_equal(GE, GE_test)

    def test_sell_res_cloth(self):
        GE = ge_file.GEM()
        GE_test = GE.copy()
        val_hist = copy.deepcopy(GE_test.GSM.__dict__)
        del val_hist["value_history"]
        GE_test.GSM.value_history.append(val_hist)
        GE_test.GSM.callstack.append(("sell_res","cloth", 20))
        GE(("sell_res","cloth", 20))
        GE_test.GSM.res.sub("cloth", 20)
        cost = defaults.starting_res_price.cloth * 20
        GE_test.GSM.budget.add(cost)
        self.assert_GE_equal(GE, GE_test)

    def test_buy_prod_aisha(self):
        GE = ge_file.GEM()
        GE_test = GE.copy()
        val_hist = copy.deepcopy(GE_test.GSM.__dict__)
        del val_hist["value_history"]
        GE_test.GSM.value_history.append(val_hist)
        GE_test.GSM.callstack.append(("buy_prod", "aisha", 5))
        GE(("buy_prod", "aisha", 5))
        GE_test.GSM.prod.add("aisha", 5)
        cost = defaults.starting_prod_price.aisha * 5
        GE_test.GSM.budget.sub(cost)
        self.assert_GE_equal(GE, GE_test)

    def test_make_prod_beta(self):
        GE = ge_file.GEM()
        GE_test = GE.copy()
        val_hist = copy.deepcopy(GE_test.GSM.__dict__)
        del val_hist["value_history"]
        GE_test.GSM.value_history.append(val_hist)
        GE_test.GSM.callstack.append(("make_prod", "beta", 10))
        GE(("make_prod", "beta", 10))
        GE_test.GSM.prod.add("beta", 10)
        res_needed = defaults.prod_res_cost.beta * 10
        GE_test.GSM.res.sub(res_needed)
        cost = defaults.hours_needed.beta * defaults.cost_per_hour * 10
        GE_test.GSM.budget.sub(cost)
        self.assert_GE_equal(GE, GE_test)

    def test_sell_prod_chama(self):
        GE = ge_file.GEM()
        GE_test = GE.copy()
        val_hist = copy.deepcopy(GE_test.GSM.__dict__)
        del val_hist["value_history"]
        GE_test.GSM.value_history.append(val_hist)
        GE_test.GSM.callstack.append(("sell_prod", "chama", 7))
        GE(("sell_prod", "chama", 7))
        GE_test.GSM.prod.sub("chama", 7)
        cost = GE_test.GSM.prod_price.value.chama * 7
        GE_test.GSM.budget.add(cost)
        self.assert_GE_equal(GE, GE_test)

    def test_next_turn(self):
        GE = ge_file.GEM()
        GE_test = GE.copy()
        GE(("next_turn",))
        GE_test.GSM.time_steps = defaults.starting_time + 1
        val_hist = copy.deepcopy(GE_test.GSM.__dict__)
        del val_hist["value_history"]
        GE_test.GSM.value_history = [val_hist]
        self.assert_GE_equal(GE, GE_test)

    def test_save_game(self):
        GE = ge_file.GEM()
        GE_loaded = GE.copy()
        GE_test = GE.copy()
        GE(("sell_prod", "chama", 7))
        GE(("make_prod", "beta", 10))
        GE(("buy_res", "stuff", 20))
        GE(("next_turn",))
        GE(("save_game",))
        GE_test(("sell_prod", "chama", 7))
        GE_test(("make_prod", "beta", 10))
        GE_test(("buy_res", "stuff", 20))
        GE_test(("next_turn",))
        file = open(defaults.def_save_folder + defaults.def_save_file_name, "rb")
        GE_loaded.GSM.__dict__ = pickle.load(file)
        values = copy.deepcopy(GE_loaded.GSM.__dict__)
        GE_loaded.GSM.value_history = [values]
        self.assert_GE_equal(GE_test, GE_loaded)

    def test_load_game(self):
        GE = ge_file.GEM()
        GE_loaded = GE.copy()
        GE_test = GE.copy()
        GE(("sell_prod", "chama", 7))
        GE(("make_prod", "beta", 10))
        GE(("buy_res", "stuff", 20))
        GE(("next_turn",))
        GE(("save_game",))
        GE_loaded(("load_game",))
        GE_test(("sell_prod", "chama", 7))
        GE_test(("make_prod", "beta", 10))
        GE_test(("buy_res", "stuff", 20))
        GE_test(("next_turn",))
        self.assert_GE_equal(GE_test, GE_loaded)

    def test_back(self):
        GE = ge_file.GEM()
        GE_test = GE.copy()
        GE(("sell_prod", "chama", 7))

        GE(("make_prod", "beta", 10))
        GE(("buy_res", "stuff", 20))
        GE(("back",))

        GE_test(("sell_prod", "chama", 7))
        GE_test(("make_prod", "beta", 10))

        self.assert_GE_equal(GE, GE_test)


if __name__ == '__main__':
    unittest.main(verbosity=0)