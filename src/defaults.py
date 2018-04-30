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
    reset = 2
    quit = 3

# Function signal values for internal use
@unique
class Func(Enum):
    buy_res = auto()
    sell_res = auto()
    buy_prod = auto()
    make_prod = auto()
    sell_prod = auto()
    save = auto()
    load = auto()
    quit = auto()
    next_turn = auto()
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
# Figure Attributes
_figure_set_indices = ("figures_per_row",)
_FigureSetSpecsBase = namedtuple("FigureSetSpecs", _figure_set_indices)
FigureSetSpecs = _FigureSetSpecsBase(figures_per_row=3)

_figure_iindices = ("name", "title", "x_label", "y_label")
_FigureSpecBase = namedtuple("FigureSpec", _figure_iindices)

_FigureSpec1 = _FigureSpecBase(Res.cloth, "Res.cloth", "x_", "y_")
_FigureSpec2 = _FigureSpecBase(Res.stuff, "Res.stuff", "x_", "y_")
_FigureSpec3 = _FigureSpecBase(Res.accessory, "Res.accessory", "x_", "y_")
_FigureSpec4 = _FigureSpecBase(Res.packaging, "Res.packaging", "x_", "y_")

_FigureSpec5 = _FigureSpecBase(Prod.aisha, "Prod.aisha", "x_", "y_")
_FigureSpec6 = _FigureSpecBase(Prod.beta, "Prod.beta", "x_", "y_")
_FigureSpec7 = _FigureSpecBase(Prod.chama, "Prod.chama", "x_", "y_")

_FigureSpec8 = _FigureSpecBase(ResPrice.cloth, "ResPrice.cloth", "x_", "y_")
_FigureSpec9 = _FigureSpecBase(ResPrice.stuff, "ResPrice.stuff", "x_", "y_")
_FigureSpec10 = _FigureSpecBase(ResPrice.accessory, "ResPrice.accessory", "x_", "y_")
_FigureSpec11 = _FigureSpecBase(ResPrice.packaging, "ResPrice.packaging", "x_", "y_")

_FigureSpec12 = _FigureSpecBase(ProdPrice.aisha, "ProdPrice.aisha", "x_", "y_")
_FigureSpec13 = _FigureSpecBase(ProdPrice.beta, "ProdPrice.beta", "x_", "y_")
_FigureSpec14 = _FigureSpecBase(ProdPrice.chama, "ProdPrice.chama", "x_", "y_")
_FigureSpec15 = _FigureSpecBase(Production.hours_needed, "Production.hours_needed", "x_", "y_")
_FigureSpec16 = _FigureSpecBase(Production.cost_per_hour, "Production.cost_per_hour", "x_", "y_")
_FigureSpec17 = _FigureSpecBase(Production.res_cost, "Production.res_cost", "x_", "y_")

FigureSpecs = [_FigureSpec1, _FigureSpec2, _FigureSpec3, _FigureSpec4,
               _FigureSpec5, _FigureSpec6, _FigureSpec7, _FigureSpec8,
               _FigureSpec9, _FigureSpec10, _FigureSpec11, _FigureSpec12,
               _FigureSpec13, _FigureSpec14]


# Widget Attributes
_widget_set_indices = ("widgets_per_row", "row_width", "row_height")
_WidgetSetSpecsBase = namedtuple("WidgetSetSpecs", _widget_set_indices)
WidgetSetSpecs = _WidgetSetSpecsBase(widgets_per_row=3,
                                  row_width=5000,
                                  row_height=200)    # Distance between widget set rows

_widget_gindices = ["text_intrinsic_width", "text_intrinsic_height",
                   "text_display_width", "text_display_height",
                   "RBG_intrinsic_width", "RBG_intrinsic_height",
                   "RBG_display_width", "RBG_display_height",
                   "TI_intrinsic_width", "TI_intrinsic_height",
                   "TI_display_width", "TI_display_height",
                   "button_intrinsic_width", "button_intrinsic_height",
                   "button_display_width", "button_display_height"]

_WidgetGspecsBase = namedtuple("WidgetGspecs", _widget_gindices)

_widget_gspecs = _WidgetGspecsBase(
    text_intrinsic_width=250, # Text box
    text_intrinsic_height=50,
    text_display_width=0,
    text_display_height=40,   # Determine how close RBG is

    RBG_intrinsic_width=400,  # Determine when break between rows happen
    RBG_intrinsic_height=0,
    RBG_display_width=0,
    RBG_display_height=40,    # determine how close TI and button is

    TI_intrinsic_width=1,     # size of text_box, with a minimum
    TI_intrinsic_height=1,
    TI_display_width=180,     # fix overall widget width together with
    TI_display_height=0,      # button_display_width

    button_intrinsic_width=50,  # Size of button
    button_intrinsic_height=0,
    button_display_width=150,   # Spacing between widgets in same row.
    button_display_height=100)   # Spacing between widget cols

_widget_iindices = ["format", "name", "title", "button_label", "TI_placeholder", "RBG_labels"]

_WidgetIspecsBase = namedtuple("WidgetIspecs", _widget_iindices)

_widget_ispecs_1 = _WidgetIspecsBase(
    format="standard",
    name=Func.buy_res,
    title=Func.buy_res.name,
    button_label="button1",
    TI_placeholder="Placeholder",
    RBG_labels=list(Res) + [Others.reset])

_widget_ispecs_2 = _WidgetIspecsBase(
    format="standard",
    name=Func.sell_res,
    title=Func.sell_res.name,
    button_label="button2",
    TI_placeholder="Placeholder",
    RBG_labels=list(Res) + [Others.reset])

_widget_ispecs_3 = _WidgetIspecsBase(
    format="standard",
    name=Func.buy_prod,
    title=Func.buy_prod.name,
    button_label="buy",
    TI_placeholder="Placeholder",
    RBG_labels=list(Prod) + [Others.reset])

_widget_ispecs_4 = _WidgetIspecsBase(
    format="standard",
    name=Func.make_prod,
    title=Func.make_prod.name,
    button_label="make",
    TI_placeholder="Placeholder",
    RBG_labels=list(Prod) + [Others.reset])

_widget_ispecs_5 = _WidgetIspecsBase(
    format="standard",
    name=Func.sell_prod,
    title=Func.sell_prod.name,
    button_label="sell",
    TI_placeholder="Placeholder",
    RBG_labels=list(Prod) + [Others.reset])

_widget_ispecs_6 = _WidgetIspecsBase(
    format="button",
    name=Others,
    title="Others",
    button_label="Submit",
    TI_placeholder="",
    RBG_labels=list([Func.next_turn, Others.reset, Func.quit]))

_widget_ispecs = [_widget_ispecs_1, _widget_ispecs_2, _widget_ispecs_3,
                 _widget_ispecs_4, _widget_ispecs_5, _widget_ispecs_6]

_WidgetSpecsBase = namedtuple("WidgetSpecs", field_names=_WidgetIspecsBase._fields + _WidgetGspecsBase._fields)
WidgetSpecs = list([_WidgetSpecsBase(*(ispecs + _widget_gspecs)) for ispecs in _widget_ispecs])
# Order in *() need to be same as order in fields_, otherwise wrong values
# get assigned to the field names.

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

FigureSetSpecs
FigureSpecs
WidgetSetSpecs
WidgetSpecs
"""









