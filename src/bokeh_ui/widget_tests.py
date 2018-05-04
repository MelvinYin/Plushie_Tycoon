import unittest
from unittest.mock import patch, DEFAULT
from collections import namedtuple


from enum import unique, Enum, auto
from individual_widget import IndividualWidget
from widgets import WidgetSet

class TestStandardWidget(unittest.TestCase):

    @staticmethod
    def _setup_gspec():
        widget_gindices = ["text_intrinsic_dim", "text_display_dim",
                           "RBG_intrinsic_dim", "RBG_display_dim",
                           "TI_intrinsic_dim", "TI_display_dim",
                           "button_intrinsic_dim",
                           "button_display_dim"]

        WidgetGspecs = namedtuple("WidgetGspecs", widget_gindices)

        widget_gspecs = WidgetGspecs(
            text_intrinsic_dim=[250, 50],  # width, height of text box
            text_display_dim=[0, 40],
            # text width no diff, height determine how near RBG is.

            RBG_intrinsic_dim=[400, 0],
            # width affects when break between rows happen
            RBG_display_dim=[0, 40],
            # width no diff, height determine how close input and button is

            TI_intrinsic_dim=[1, 1],  # size of text_box, with a minimum
            TI_display_dim=[180, 0],
            # for width, fix overall widget width together with button_display_dim

            button_intrinsic_dim=[50, 0],  # Size of button
            button_display_dim=[150, 100]
            # height determine spacing between widget cols
        )  # width determine spacing between widgets in same row.
        return widget_gspecs

    @staticmethod
    def _setup_Func():
        @unique
        class Func(Enum):
            buy_res = auto()
            sell_res = auto()
            buy_prod = auto()
            make_prod = auto()
            sell_prod = auto()
            show_stats = auto()
            show_prices = auto()
            save = auto()
            load = auto()
            quit = auto()
            save_quit = auto()
            next_turn = auto()
            show_history = auto()
            back = auto()
            start = auto()
        return Func

    @staticmethod
    def _setup_Res():
        @unique
        class Res(Enum):
            cloth = 1
            stuff = 2
            accessory = 3
            packaging = 4
        return Res

    @staticmethod
    def _setup_Others():
        @unique
        class Others(Enum):
            next = auto()
            quit = auto()
            reset = auto()
        return Others

    @classmethod
    def _setup_ispec_1(cls):
        widget_iindices = ["name", "title", "button_label", "TI_placeholder",
                           "RBG_labels"]
        WidgetIspecs = namedtuple("WidgetIspecs", widget_iindices)
        widget_ispecs_1 = WidgetIspecs(
            name=cls.Func.buy_res,
            title="buy_res",
            button_label="buy",
            TI_placeholder="Placeholder",
            RBG_labels=list(cls.Res) + [cls.Others.reset])
        return widget_ispecs_1


    @classmethod
    def _setup_ispec_6(cls):
        widget_iindices = ["name", "title", "button_label", "TI_placeholder",
                           "RBG_labels"]
        WidgetIspecs = namedtuple("WidgetIspecs", widget_iindices)
        widget_ispecs_6 = WidgetIspecs(
            name=cls.Others,
            title="Others",
            button_label="Submit",
            TI_placeholder="Placeholder",
            RBG_labels=list(cls.Others))
        return widget_ispecs_6

    @classmethod
    def _callback_1(cls, args):
        cls.return_value = args
        return

    @classmethod
    def setUpClass(cls):
        cls.Func = cls._setup_Func()
        cls.Res = cls._setup_Res()
        cls.Others = cls._setup_Others()

        cls.widget_ispecs_1 = cls._setup_ispec_1()
        cls.widget_ispecs_6 = cls._setup_ispec_6()
        cls.widget_gspecs = cls._setup_gspec()

        cls.callback_1 = cls._callback_1

    def test_std(self):
        with patch("individual_widget.widget_gspecs", new=self.widget_gspecs) as _:
            RBG_num = 0
            Enum_num = RBG_num + 1 # Because Enum starts from 1
            quantity = 12

            individual_widget = IndividualWidget(self.callback_1, self.widget_ispecs_1)
            individual_widget._RBG_callback(RBG_num)  # 0-th RBG button
            individual_widget._text_callback("0", "0", str(quantity))  # input_val
            individual_widget._button_callback()
            self.assertEqual(self.return_value, (self.Func.buy_res, (self.Res(Enum_num), quantity)))

    def test_next(self):
        with patch("individual_widget.widget_gspecs", new=self.widget_gspecs) as _:
            RBG_num = 0
            Enum_num = RBG_num + 1  # Because Enum starts from 1

            individual_widget = IndividualWidget(self.callback_1, self.widget_ispecs_6)
            individual_widget._RBG_callback(0)  # Should be next
            individual_widget._text_callback("0", "0", "12")  # input_val
            individual_widget._button_callback()
            self.assertEqual(self.return_value, (self.Others(Enum_num),))











