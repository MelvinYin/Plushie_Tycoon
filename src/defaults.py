import pandas as pd
from enum import Enum, auto, unique
from collections import namedtuple

# TODO: check if widget_ispecs is only sent to individual widgets. Seems like a good idea.
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
    next = 1
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

# Production signal values for internal use
@unique
class Production(Enum):
    hours_needed = auto()
    cost_per_hour = auto()
    res_cost = auto()


# Plushie Resource Cost
res_cost = dict()
res_cost[Prod.aisha] = [3,6,2,1]
res_cost[Prod.beta] = [1,4,1,2]
res_cost[Prod.chama] = [2,5,1,4]
prod_res_cost = pd.DataFrame(res_cost, index=Res)

# Plushie Production Hours
p_hours = [30, 24, 36]
hours_needed = pd.Series(p_hours, Prod)

# Cost Per Production Hour
cost_per_hour = 3

# Starting Statistics
starting_budget = 10000000

s_res = [1000,1000,1000,1000]
starting_res = pd.Series(s_res, Res, name="starting_res")

s_prod = [100,100,100]
starting_prod = pd.Series(s_prod, Prod, name="starting_prod")

s_res_price = [10,20,18,12]
starting_res_price = pd.Series(s_res_price, Res, name="starting_res_price")

s_prod_price = [80,76,52]
starting_prod_price = pd.Series(s_prod_price, Prod, name="starting_prod_price")


history_columns = ["res", "prod", "res_price", "prod_price", "budget", "production",
           "time_steps", "current_call"]

history_add = namedtuple("history_add", field_names=history_columns)

history_init = pd.DataFrame(columns=history_columns)

starting_time = 0

def_save_folder = "../save/"
def_save_file_name = "game_save.pkl"

loaded_figures = [Res.cloth, Res.stuff, Res.accessory, Res.packaging,
Prod.aisha, Prod.beta, Prod.chama]

figure_gindices = ("figures_per_row",)
FigureGspec = namedtuple("FigureGspec", figure_gindices)
figure_gspecs = FigureGspec(figures_per_row=3)

figure_iindices = ("name", "title", "x_label", "y_label")

FigureIspec = namedtuple("FigureIspec", figure_iindices)

figure_ispec_1 = FigureIspec(Res.cloth, "Res.cloth", "x_", "y_")
figure_ispec_2 = FigureIspec(Res.stuff, "Res.stuff", "x_", "y_")
figure_ispec_3 = FigureIspec(Res.accessory, "Res.accessory", "x_", "y_")
figure_ispec_4 = FigureIspec(Res.packaging, "Res.packaging", "x_", "y_")

figure_ispec_5 = FigureIspec(Prod.aisha, "Prod.aisha", "x_", "y_")
figure_ispec_6 = FigureIspec(Prod.beta, "Prod.beta", "x_", "y_")
figure_ispec_7 = FigureIspec(Prod.chama, "Prod.chama", "x_", "y_")

figure_ispec_8 = FigureIspec(ResPrice.cloth, "ResPrice.cloth", "x_", "y_")
figure_ispec_9 = FigureIspec(ResPrice.stuff, "ResPrice.stuff", "x_", "y_")
figure_ispec_10 = FigureIspec(ResPrice.accessory, "ResPrice.accessory", "x_", "y_")
figure_ispec_11 = FigureIspec(ResPrice.packaging, "ResPrice.packaging", "x_", "y_")

figure_ispec_12 = FigureIspec(ProdPrice.aisha, "ProdPrice.aisha", "x_", "y_")
figure_ispec_13 = FigureIspec(ProdPrice.beta, "ProdPrice.beta", "x_", "y_")
figure_ispec_14 = FigureIspec(ProdPrice.chama, "ProdPrice.chama", "x_", "y_")
figure_ispec_15 = FigureIspec(Production.hours_needed, "Production.hours_needed", "x_", "y_")
figure_ispec_16 = FigureIspec(Production.cost_per_hour, "Production.cost_per_hour", "x_", "y_")
figure_ispec_17 = FigureIspec(Production.res_cost, "Production.res_cost", "x_", "y_")
figure_ispec_18 = FigureIspec("current_call", "current_call", "x_", "y_")
figure_ispec_19 = FigureIspec("time_steps", "time_steps", "x_", "y_")

figure_ispecs = [figure_ispec_1, figure_ispec_2, figure_ispec_3, figure_ispec_4,
                figure_ispec_5, figure_ispec_6, figure_ispec_7, figure_ispec_8,
                figure_ispec_9, figure_ispec_10, figure_ispec_11, figure_ispec_12,
                figure_ispec_13, figure_ispec_14, figure_ispec_15, figure_ispec_16,
                figure_ispec_17, figure_ispec_18, figure_ispec_19]

# figure_ispecs = [figure_ispec_1, figure_ispec_2, figure_ispec_3, figure_ispec_4,
#                 figure_ispec_5, figure_ispec_6, figure_ispec_7]

widget_gindices = ["text_intrinsic_dim", "text_display_dim", "RBG_intrinsic_dim", "RBG_display_dim",
                  "TI_intrinsic_dim", "TI_display_dim", "button_intrinsic_dim",
                   "button_display_dim", "widgets_per_row"]

WidgetGspecs = namedtuple("WidgetGspecs", widget_gindices)



widget_gspecs = WidgetGspecs(
    text_intrinsic_dim = [250, 50],  # width, height of text box
    text_display_dim = [0, 40],  # text width no diff, height determine how near RBG is.

    RBG_intrinsic_dim = [400, 0],   # width affects when break between rows happen
    RBG_display_dim = [0, 40],  # width no diff, height determine how close input and button is

    TI_intrinsic_dim = [1, 1],  # size of text_box, with a minimum
    TI_display_dim = [180, 0],  # for width, fix overall widget width together with button_display_dim

    button_intrinsic_dim = [50, 0],  # Size of button
    button_display_dim = [150, 100],  # height determine spacing between widget cols
    # width determine spacing between widgets in same row.

    widgets_per_row = 3
    )

widget_iindices = ["name", "title", "button_label", "TI_placeholder", "RBG_labels"]

WidgetIspecs = namedtuple("WidgetIspecs", widget_iindices)

widget_ispecs_1 = WidgetIspecs(
    name = Func.buy_res,
    title = "buy_res",
    button_label = "buy",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Res) + [Others.reset])

widget_ispecs_2 = WidgetIspecs(
    name = Func.sell_res,
    title = "sell_res",
    button_label = "sell",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Res) + [Others.reset])

widget_ispecs_3 = WidgetIspecs(
    name = Func.buy_prod,
    title = "buy_prod",
    button_label = "buy",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Prod) + [Others.reset])

widget_ispecs_4 = WidgetIspecs(
    name = Func.make_prod,
    title = "make_prod",
    button_label = "make",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Prod) + [Others.reset])


widget_ispecs_5 = WidgetIspecs(
    name = Func.sell_prod,
    title = "sell_prod",
    button_label = "sell",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Prod) + [Others.reset])

# TODO: Transition eventually to a set of buttons alone, no TI
# TODO: Turn on/off widgets based on Ispecs?
widget_ispecs_6 = WidgetIspecs(
    name = Others,
    title = "Others",
    button_label = "Submit",
    TI_placeholder = "Placeholder",
    RBG_labels = list(Others))

widget_ispecs = [widget_ispecs_1, widget_ispecs_2, widget_ispecs_3,
                 widget_ispecs_4, widget_ispecs_5, widget_ispecs_6]











