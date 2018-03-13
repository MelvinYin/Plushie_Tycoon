import importlib
import unittest
from unittest.mock import patch
import copy
import pandas as pd

ui_file_path = "ui"
ui_file = importlib.import_module(ui_file_path)


test_UI = True



class TestCaseBase(unittest.TestCase):

    def assert_pd_series_equal(self, *args, **kwargs):
        return pd.testing.assert_series_equal(*args, **kwargs)


@unittest.skipIf(test_UI==False, "")
class TestUI(TestCaseBase):
    class MockedInput:
        def __init__(self, values):
            self.count = -1
            self.values = values

        def __call__(self, *args, **kwargs):
            self.count += 1
            return self.values[self.count]

    input_values = ["show stats", "buy res", "stuff 20", "sell res", "stuff 20",
              "buy prod", "aisha 10", "make prod", "beta 5", "sell prod",
              "chama 7", "save game", "load game", "quit game", "no"]
    desired_output = [("show_stats",), ("buy_res","stuff", 20), ("sell_res","stuff", 20),
              ("buy_prod", "aisha", 10), ("make_prod", "beta", 5), ("sell_prod","chama", 7),
              ("save_game",), ("load_game",), ("quit_game",)]
    mocked_input = MockedInput(input_values)

    @patch("ui.user_input")
    def test_main2(self, mock_input):
        mock_input.side_effect = self.mocked_input
        output = []
        for __ in range(len(self.desired_output)):
            output += [ui_file.action()]
        self.assertListEqual(output, self.desired_output)



file_path = "inventory"
inventory = importlib.import_module(file_path)
import defaults
class TestResourceInventory(TestCaseBase):
    def test_ResourceInventory(self):
        res = inventory.ResourceInventory()
        def_cloth = defaults.starting_res.cloth
        def_stuff = defaults.starting_res.stuff
        def_accessory = defaults.starting_res.accessory
        def_packaging = defaults.starting_res.packaging

        self.assertEqual(res.value.cloth, def_cloth)
        self.assertEqual(res.value.stuff, def_stuff)
        self.assertEqual(res.value.accessory, def_accessory)
        self.assertEqual(res.value.packaging, def_packaging)

        self.assertEqual(res.value["cloth"], def_cloth)
        self.assertEqual(res.value["stuff"], def_stuff)
        self.assertEqual(res.value["accessory"], def_accessory)
        self.assertEqual(res.value["packaging"], def_packaging)

        value = res.value.cloth + 13
        self.assertEqual(value, def_cloth + 13)
        self.assertEqual(res.value.cloth, def_cloth)

        value = res.value.stuff - 7
        self.assertEqual(value, def_stuff - 7)
        self.assertEqual(res.value.stuff, def_stuff)

        res.value.accessory += 6
        self.assertEqual(res.value.accessory, def_accessory + 6)
        res.value.accessory -= 6

        value = res.value.cloth * 13
        self.assertEqual(value, def_cloth * 13)
        self.assertEqual(res.value.cloth, def_cloth)

        value = res.value["stuff"] / 7
        self.assertEqual(value, def_stuff / 7)
        self.assertEqual(res.value.stuff, def_stuff)
        res.add(defaults.starting_res)
        self.assert_pd_series_equal(res.value, defaults.starting_res * 2)

        res.sub(defaults.starting_res)
        self.assert_pd_series_equal(res.value, defaults.starting_res)

        res.replace(defaults.starting_res * 2)
        self.assert_pd_series_equal(res.value, defaults.starting_res * 2)
        res.sub(defaults.starting_res)

        self.assertTrue(res.test_func())


class TestProductInventory(TestCaseBase):
    def test_ProductInventory(self):
        prod = inventory.ProductInventory()
        def_aisha = defaults.starting_prod.aisha
        def_beta = defaults.starting_prod.beta
        def_chama = defaults.starting_prod.chama

        self.assertEqual(prod.value.aisha, def_aisha)
        self.assertEqual(prod.value.beta, def_beta)
        self.assertEqual(prod.value.chama, def_chama)

        self.assertEqual(prod.value["aisha"], def_aisha)
        self.assertEqual(prod.value["beta"], def_beta)
        self.assertEqual(prod.value["chama"], def_chama)

        value = prod.value.aisha + 13
        self.assertEqual(value, def_aisha + 13)
        self.assertEqual(prod.value.aisha, def_aisha)

        value = prod.value.beta - 7
        self.assertEqual(value, def_beta - 7)
        self.assertEqual(prod.value.beta, def_beta)

        prod.value.chama += 6
        self.assertEqual(prod.value.chama, def_chama + 6)
        prod.value.chama -= 6

        value = prod.value.aisha * 13
        self.assertEqual(value, def_aisha * 13)
        self.assertEqual(prod.value.aisha, def_aisha)

        value = prod.value["beta"] / 7
        self.assertEqual(value, def_beta / 7)
        self.assertEqual(prod.value.beta, def_beta)

        prod.add(defaults.starting_prod)
        self.assert_pd_series_equal(prod.value, defaults.starting_prod * 2)

        prod.sub(defaults.starting_prod)
        self.assert_pd_series_equal(prod.value, defaults.starting_prod)

        prod.replace(defaults.starting_prod * 2)
        self.assert_pd_series_equal(prod.value, defaults.starting_prod * 2)
        prod.sub(defaults.starting_prod)

        self.assertTrue(prod.test_func())


if __name__ == '__main__':
    unittest.main(verbosity=0)
