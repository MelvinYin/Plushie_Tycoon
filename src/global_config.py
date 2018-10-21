import pandas as pd
from enum import Enum, auto, unique
from collections import namedtuple

###############################################################################

# Resource signal values for internal use
@unique
class Res(Enum):
    cloth = 1
    stuff = 2
    accessory = 3
    packaging = 4

# Plushie signal values for internal use
@unique
class Prod(Enum):
    aisha = 1
    beta = 2
    chama = 3

# Resource price signal values for internal use
@unique
class ResPrice(Enum):
    cloth = 1
    stuff = 2
    accessory = 3
    packaging = 4

# Plushie price signal values for internal use
@unique
class ProdPrice(Enum):
    aisha = 1
    beta = 2
    chama = 3

@unique
class Others(Enum):
    next_turn = 1
    quit = 3

# Function signal values for internal use
@unique
class Func(Enum):
    buy = auto()
    sell = auto()
    make = auto()
    save = auto()
    load = auto()
    quit = auto()
    next = auto()
    back = auto()
    start = auto()

# Production signal values for internal use
@unique
class Production(Enum):
    hours_needed = auto()
    cost_per_hour = auto()
    res_cost = auto()


###############################################################################

# Plushie Resource Cost
_res_cost = dict()
_res_cost[Prod.aisha] = [3,6,2,1]
_res_cost[Prod.beta] = [1,4,1,2]
_res_cost[Prod.chama] = [2,5,1,4]
prod_res_cost = pd.DataFrame(_res_cost, index=Res)

# Plushie Production Hours
_p_hours = [30, 24, 36]
hours_needed = pd.Series(_p_hours, Prod)

# Cost Per Production Hour
cost_per_hour = 3

# Starting Statistics
starting_budget = 10000000

_s_res = [1000,1000,1000,1000]
starting_res = pd.Series(_s_res, Res, name="starting_res")

_s_prod = [100,100,100]
starting_prod = pd.Series(_s_prod, Prod, name="starting_prod")

_s_res_price = [10,20,18,12]
starting_res_price = pd.Series(_s_res_price, Res, name="starting_res_price")

_s_prod_price = [80,76,52]
starting_prod_price = pd.Series(_s_prod_price, Prod, name="starting_prod_price")


_history_columns = ["res", "prod", "res_price", "prod_price", "budget", "production",
           "time_steps", "current_call"]

history_init = pd.DataFrame(columns=_history_columns)

starting_time = 0

save_folder = "../save/"
save_file_name = "game_save.pkl"

###############################################################################

"""
For convenience, available values:
Res
Prod
ResPrice
ProdPrice
Others
Func
Production

prod_res_cost
hours_needed
cost_per_hour
starting_budget
starting_res
starting_prod
starting_res_price
starting_prod_price
history_init
starting_time
save_folder
save_file_name

"""

##############################################################################
# Widget Specs

from collections import namedtuple
from enum import Enum, auto, unique

# TO USE:
# from widget_config import transaction_specs, button_specs, set_specs

##############################################################################
# Global

# from global_config import Res, Prod, Func

##############################################################################
# Internal

@unique
class WidgetNames(Enum):
    Transaction = auto()
    Action = auto()

##############################################################################
# Widget Attributes

class TransactionWidgetSpecs:
    def __init__(self):
        self.name = WidgetNames.Transaction
        self.width = 350
        self.height = 0
        self.header = self.set_header()
        self.RBG1 = self.set_RBG1()
        self.RBG2 = self.set_RBG2()
        self.RBG3 = self.set_RBG3()
        self.TI = self.set_TI()
        self.button = self.set_button()
        self.layout = self.set_layout()

    def set_header(self):
        Header = namedtuple("Header", 'width height title')
        header = Header(width=0,  # Text box
                        height=0,
                        title='TITLE123')
        return header

    def set_RBG1(self):
        labelmap = dict()
        labelmap[Func.buy] = "Func 1"
        labelmap[Func.sell] = "Func 2"
        labelmap[Func.make] = "Func 3"
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=400,
                   height=17,
                   labels=[Func.buy, Func.sell, Func.make],
                   labelmap = labelmap)
        return RBG

    def set_RBG2(self):
        labelmap = dict()
        labelmap[Res] = "Cat 1"
        labelmap[Prod] = "Cat 2"
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=400,
                   height=17,
                   labels=[Res, Prod],
                   labelmap = labelmap)
        return RBG

    def set_RBG3(self):
        labelmap = dict()
        labelmap[Res.cloth] = "Prod 1"
        labelmap[Res.stuff] = "Prod 2"
        labelmap[Res.accessory] = "Prod 3"
        labelmap[Res.packaging] = "Prod 4"
        labelmap[Prod.aisha] = "Prod 5"
        labelmap[Prod.beta] = "Prod 6"
        labelmap[Prod.chama] = "Prod 7"
        # noinspection PyTypeChecker
        assert len(labelmap) == len(Res) + len(Prod)
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=400,
                   height=17,
                   labels=list(Res),
                   labelmap=labelmap)
        return RBG

    def set_TI(self):
        TI_ = namedtuple("Header", 'width height placeholder')
        TI = TI_(width=1,  # Text box
                 height=1,
                 placeholder='PLACEHOLDER123')
        return TI

    def set_button(self):
        Button = namedtuple("Header", 'width height label')
        button = Button(width=50,  # Size of button
                        height=0,
                        label="button123")
        return button

    def set_layout(self):
        Row_Specs = namedtuple("Row_Specs",
            field_names=['height', 'width', 'spacers'])

        header = Row_Specs(height=30,
                         width=100,  # Determine how close RBG is
                         spacers=[0])

        rbg1 = Row_Specs(height=40,
                         width=50,  # Determine when break between rows happen
                         spacers=[0])

        rbg2 = Row_Specs(height=40,
                         width=20,  # Determine how close RBG is
                         spacers=[0])

        rbg3 = Row_Specs(height=30,
                         width=0,  # Determine how close RBG is
                         spacers=[0])

        ti = Row_Specs(height=17,  # Spacing between widget cols
                         width=10,  # Spacing between widgets in same row.
                         spacers=[0])

        button = Row_Specs(height=0,  # Spacing between widget cols
                         width=200,  # Spacing between widgets in same row.
                         spacers=[0])

        layout = [header, rbg1, rbg2, rbg3, ti, button]
        return layout


class ButtonWidgetSpecs:
    def __init__(self):
        self.name = WidgetNames.Action
        self.width = 0
        self.height = 0
        self.header = self.set_header()
        self.RBG = self.set_RBG()
        self.button = self.set_button()
        self.layout = self.set_layout()

    def set_header(self):
        Header = namedtuple("Header", 'width height title')
        header = Header(width=0,  # Text box
                        height=0,
                        title='TITLE123')
        return header

    def set_RBG(self):
        labelmap = dict()
        labelmap[Func.next] = "Func 1"
        labelmap[Func.save] = "Func 2"
        labelmap[Func.load] = "Func 3"
        labelmap[Func.quit] = "Func 4"
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=250,
                   height=17,
                   labels=[Func.next, Func.save, Func.load, Func.quit],
                   labelmap=labelmap)
        return RBG

    def set_button(self):
        Button = namedtuple("Header", 'width height label')
        button = Button(width=0,  # Size of button
                        height=0,
                        label="button123")
        return button

    def set_layout(self):
        Row_Specs = namedtuple("Row_Specs",
            field_names=['height', 'width', 'spacers'])

        row0 = Row_Specs(height=30,
                         width=100,  # Determine how close RBG is
                         spacers=[0])

        row1 = Row_Specs(height=40,
                         width=0,  # Determine when break between rows happen
                         spacers=[0, 0])

        layout = [row0, row1]
        return layout

class WidgetSetSpecs:
    def __init__(self):
        self.widgets_per_row = 3
        self.width = 0
        self.height = 0

class FullWidgetSpecs:
    def __init__(self):
        self.setspecs = WidgetSetSpecs()
        self.transactionw1 = TransactionWidgetSpecs()
        self.buttonw1 = ButtonWidgetSpecs()

##############################################################################
# Figure Attributes







