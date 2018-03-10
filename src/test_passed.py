import importlib
import unittest
from unittest.mock import patch
import copy
import pandas as pd

ui_file_path = "ui"
ui_file = importlib.import_module(ui_file_path)


test_UI = True


@unittest.skipIf(test_UI==False, "")
class TestUI(unittest.TestCase):
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
class TestResourceInventory(unittest.TestCase):
    def test_ResourceInventory(self):
        ResInv = inventory.ResourceInventory()
        def_cloth = defaults.starting_res.cloth
        def_stuff = defaults.starting_res.stuff
        def_accessory = defaults.starting_res.accessory
        def_packaging = defaults.starting_res.packaging
        self.assertEqual(ResInv.cloth, def_cloth)
        self.assertEqual(ResInv.stuff, def_stuff)
        self.assertEqual(ResInv.accessory, def_accessory)
        self.assertEqual(ResInv.packaging, def_packaging)

        self.assertEqual(ResInv["cloth"], def_cloth)
        self.assertEqual(ResInv["stuff"], def_stuff)
        self.assertEqual(ResInv["accessory"], def_accessory)
        self.assertEqual(ResInv["packaging"], def_packaging)

        value = ResInv.cloth + 13
        self.assertEqual(value, def_cloth + 13)
        self.assertEqual(ResInv.cloth, def_cloth)

        value = ResInv.stuff - 7
        self.assertEqual(value, def_stuff - 7)
        self.assertEqual(ResInv.stuff, def_stuff)

        ResInv.accessory += 6
        self.assertEqual(ResInv.accessory, def_accessory + 6)
        ResInv.accessory -= 6

        ResInv.packaging -= 3
        self.assertEqual(ResInv.packaging, def_packaging - 3)
        ResInv.packaging += 3

        value = ResInv.cloth * 13
        self.assertEqual(value, def_cloth * 13)
        self.assertEqual(ResInv.cloth, def_cloth)

        value = ResInv["stuff"] / 7
        self.assertEqual(value, def_stuff / 7)
        self.assertEqual(ResInv.stuff, def_stuff)

        ResInv.stuff *= 6
        self.assertEqual(ResInv.stuff, def_stuff * 6)
        ResInv.stuff /= 6

        ResInv["cloth"] /= 3
        self.assertEqual(ResInv.cloth, def_cloth / 3)
        ResInv.cloth *= 3

        value = ResInv.cloth
        self.assertEqual(value, def_cloth)

        self.assertTrue(ResInv.test_func())


class TestProductInventory(unittest.TestCase):
    def test_ProductInventory(self):
        ProdInv = inventory.ProductInventory()
        def_aisha = defaults.starting_prod.aisha
        def_beta = defaults.starting_prod.beta
        def_chama = defaults.starting_prod.chama

        self.assertEqual(ProdInv.aisha, def_aisha)
        self.assertEqual(ProdInv.beta, def_beta)
        self.assertEqual(ProdInv.chama, def_chama)

        self.assertEqual(ProdInv["aisha"], def_aisha)
        self.assertEqual(ProdInv["beta"], def_beta)
        self.assertEqual(ProdInv["chama"], def_chama)

        value = ProdInv.aisha + 13
        self.assertEqual(value, def_aisha + 13)
        self.assertEqual(ProdInv.aisha, def_aisha)

        value = ProdInv.beta - 7
        self.assertEqual(value, def_beta - 7)
        self.assertEqual(ProdInv.beta, def_beta)

        ProdInv.chama += 6
        self.assertEqual(ProdInv.chama, def_chama + 6)
        ProdInv.chama -= 6

        ProdInv.beta -= 3
        self.assertEqual(ProdInv.beta, def_beta - 3)
        ProdInv.beta += 3

        value = ProdInv.aisha * 13
        self.assertEqual(value, def_aisha * 13)
        self.assertEqual(ProdInv.aisha, def_aisha)

        value = ProdInv["beta"] / 7
        self.assertEqual(value, def_beta / 7)
        self.assertEqual(ProdInv.beta, def_beta)

        ProdInv.beta *= 6
        self.assertEqual(ProdInv.beta, def_beta * 6)
        ProdInv.beta /= 6

        ProdInv["aisha"] /= 3
        self.assertEqual(ProdInv.aisha, def_aisha / 3)
        ProdInv.aisha *= 3

        value = ProdInv.aisha
        self.assertEqual(value, def_aisha)

        self.assertTrue(ProdInv.test_func())

file_path = "budget"
budget_file = importlib.import_module(file_path)

class TestBudget(unittest.TestCase):
    def test_budget(self):
        budget = budget_file.Budget()
        def_budget = defaults.starting_budget

        self.assertEqual(budget, def_budget)

        value = budget + 13
        self.assertEqual(value, def_budget + 13)
        self.assertEqual(budget, def_budget)

        value = budget - 7
        self.assertEqual(value, def_budget - 7)
        self.assertEqual(budget, def_budget)

        budget += 6
        self.assertEqual(budget, def_budget + 6)
        budget -= 6

        budget -= 3
        self.assertEqual(budget, def_budget - 3)
        budget += 3

        value = budget * 13
        self.assertEqual(value, def_budget * 13)
        self.assertEqual(budget, def_budget)

        value = budget / 7
        self.assertEqual(value, def_budget / 7)
        self.assertEqual(budget, def_budget)

        budget *= 6
        self.assertEqual(budget, def_budget * 6)
        budget /= 6

        budget /= 3
        self.assertEqual(budget, def_budget / 3)
        budget *= 3

        value = budget
        self.assertEqual(value, def_budget)

        self.assertTrue(budget.test_func())


import market

class TestMarketRes(unittest.TestCase):
    def test_MarketRes(self):
        res_price = market.MarketRes()
        def_price = defaults.starting_res_price
        self.assertEqual(res_price, def_price)

        actual = res_price.stuff
        expect = def_price.stuff
        self.assertEqual(actual, expect)

        actual = res_price['stuff']
        expect = def_price.stuff
        self.assertEqual(actual, expect)

        actual = res_price * def_price  # to simulate price * quantity
        expected = def_price * def_price
        pd.testing.assert_series_equal(actual, expected)
        self.assertEqual(sum(actual), sum(expected))

        self.assertTrue(res_price.test_func())


class TestMarketProd(unittest.TestCase):
    def test_MarketProd(self):
        prod_price = market.MarketProd()
        def_price = defaults.starting_prod_price
        self.assertEqual(prod_price, def_price)

        actual = prod_price.aisha
        expect = def_price.aisha
        self.assertEqual(actual, expect)

        actual = prod_price['beta']
        expect = def_price.beta
        self.assertEqual(actual, expect)

        actual = prod_price * def_price  # to simulate price * quantity
        expected = def_price * def_price
        pd.testing.assert_series_equal(actual, expected)
        self.assertEqual(sum(actual), sum(expected))

        self.assertTrue(prod_price.test_func())