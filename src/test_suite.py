import importlib
import unittest
from unittest.mock import patch
import copy
import defaults

ui_file_path = "ui"
ui_file = importlib.import_module(ui_file_path)

ge_file_path = "ge"
ge_file = importlib.import_module(ui_file_path)

test_UI = True
test_GE = True

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



@unittest.skipIf(test_GE == False, "")
class TestUI(unittest.TestCase):
    class MockedUI:
        def __init__(self, values):
            self.count = -1
            self.values = values

        def __call__(self, *args, **kwargs):
            self.count += 1
            return self.values[self.count]

    input_values_a = [("show_stats",), ("buy_res","stuff", 20),
                    ("sell_res","cloth", 20), ("buy_res","accessory", 12),
                    ("sell_res","packaging", 17), ("buy_prod", "aisha", 10),
                    ("make_prod", "beta", 5), ("sell_prod","chama", 7)]

    def create_GE_output(self, GSM_dict):
        output = [GSM_dict.copy()]
        GSM_dict.res["stuff"] += 20
        GSM_dict.budget
        output.append(GSM_dict.copy())

        GSM_dict.res["cloth"] -= 20
        output.append(GSM_dict.copy())

        GSM_dict.res["accessory"] += 12
        output.append(GSM_dict.copy())

        GSM_dict.res["packaging"] -= 17
        output.append(GSM_dict.copy())

        GSM_dict.prod["aisha"] += 10
        output.append(GSM_dict.copy())

        GSM_dict.prod["beta"] += 5
        output.append(GSM_dict.copy())

        GSM_dict.prod["chama"] -= 7
        output.append(GSM_dict.copy())


    GE = ge_file.GEM()
    GE_template = copy.deepcopy(GE.GSM..__dict__)
    expected_output_a = [GE.GSM.__dict__, ]

    input_values_b = [
                    ("save_game",), ("load_game",), ("quit_game",)]
    mocked_ui = MockedUI(input_values)

    @patch("ui.action")
    def test_GE(self, mock_input):
        mock_input.side_effect = self.mocked_ui
        GE = ge_file.GEM()
        output = []
        for __ in range(len(self.desired_output)):
            output += [ui_file.action()]
        self.assertListEqual(output, self.desired_output)















        # ("buy_prod", "aisha", 10), ("make_prod", "beta", 5), (
        # "sell_prod", "chama", 7), \
        # ("save_game",), ("load_game",), ("show_stats",), ("quit_game",)


# class TestMain(unittest.TestCase):
#
#     def mocked_input(self, *args):
#         callstack = ["show_stats", "buy_res", "stuff 20"]
#         # for i in callstack:
#         #     return i
#         return ("show_stats",)
#
#     @patch("ui.action")
#     def test_main2(self, mocked_input=DEFAULT):
#         mocked_input.side_effect = self.mocked_input
#         __ = sgs.main2()


if __name__ == '__main__':
    unittest.main(verbosity=2)