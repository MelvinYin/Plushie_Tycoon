import importlib
import unittest
from unittest.mock import patch
import pandas as pd
from defaults import Func, Res, Prod
import ui
import inventory
import defaults

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
    desired_output = [(Func.show_stats,), (Func.buy_res, Res.stuff, 20), (Func.sell_res, Res.stuff, 20),
              (Func.buy_prod, Prod.aisha, 10), (Func.make_prod, Prod.beta, 5), (Func.sell_prod, Prod.chama, 7),
              (Func.save_game,), (Func.load_game,), (Func.quit_game,)]
    mocked_input = MockedInput(input_values)

    @patch("ui.user_input")
    def test_main2(self, mock_input):
        mock_input.side_effect = self.mocked_input
        output = []
        for __ in range(len(self.desired_output)):
            output += [ui.action()]
        self.assertListEqual(output, self.desired_output)


class TestResourceInventory(TestCaseBase):
    def test_ResourceInventory(self):
        res = inventory.ResourceInventory()
        def_cloth = defaults.starting_res[Res.cloth]
        def_stuff = defaults.starting_res[Res.stuff]
        def_accessory = defaults.starting_res[Res.accessory]
        def_packaging = defaults.starting_res[Res.packaging]

        self.assertEqual(res.value[Res.cloth], def_cloth)
        self.assertEqual(res.value[Res.stuff], def_stuff)
        self.assertEqual(res.value[Res.accessory], def_accessory)
        self.assertEqual(res.value[Res.packaging], def_packaging)

        value = res.value[Res.cloth] + 13
        self.assertEqual(value, def_cloth + 13)
        self.assertEqual(res.value[Res.cloth], def_cloth)

        value = res.value[Res.stuff] - 7
        self.assertEqual(value, def_stuff - 7)
        self.assertEqual(res.value[Res.stuff], def_stuff)

        res.value[Res.accessory] += 6
        self.assertEqual(res.value[Res.accessory], def_accessory + 6)
        res.value[Res.accessory] -= 6

        value = res.value[Res.cloth] * 13
        self.assertEqual(value, def_cloth * 13)
        self.assertEqual(res.value[Res.cloth], def_cloth)

        value = res.value[Res.stuff] / 7
        self.assertEqual(value, def_stuff / 7)
        self.assertEqual(res.value[Res.stuff], def_stuff)
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
        def_aisha = defaults.starting_prod[Prod.aisha]
        def_beta = defaults.starting_prod[Prod.beta]
        def_chama = defaults.starting_prod[Prod.chama]

        self.assertEqual(prod.value[Prod.aisha], def_aisha)
        self.assertEqual(prod.value[Prod.beta], def_beta)
        self.assertEqual(prod.value[Prod.chama], def_chama)

        value = prod.value[Prod.aisha]+ 13
        self.assertEqual(value, def_aisha + 13)
        self.assertEqual(prod.value[Prod.aisha], def_aisha)

        value = prod.value[Prod.beta] - 7
        self.assertEqual(value, def_beta - 7)
        self.assertEqual(prod.value[Prod.beta], def_beta)

        prod.value[Prod.chama] += 6
        self.assertEqual(prod.value[Prod.chama], def_chama + 6)
        prod.value[Prod.chama] -= 6

        value = prod.value[Prod.aisha] * 13
        self.assertEqual(value, def_aisha * 13)
        self.assertEqual(prod.value[Prod.aisha], def_aisha)

        value = prod.value[Prod.beta] / 7
        self.assertEqual(value, def_beta / 7)
        self.assertEqual(prod.value[Prod.beta], def_beta)

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
