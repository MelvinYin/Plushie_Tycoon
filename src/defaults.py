import pandas as pd
from enum import Enum, auto, unique
from collections import namedtuple


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


# Split between delayed and active func.
# Copy of Function signal values above.
# to_actual_delayed_i = ["buy_res", "sell_res", "buy_prod", "make_prod", "sell_prod",]
#
# to_actual_now_i = ["show_stats", "show_prices", "save", "load",
#                  "quit", "save_quit", "next_turn"]
#
# to_tmp_i = ["show_stats", ]

# func_to_actual_delayed = pd.Series(to_actual_delayed_i, to_actual_delayed_i, name="func_to_actual_delayed")
# func_to_actual_now = pd.Series(to_actual_now_i, to_actual_now_i, name="func_to_actual_now")
# func_to_tmp = pd.Series(to_tmp_i, to_tmp_i, name="func_to_tmp")

starting_time = 0

def_save_folder = "../save/"
def_save_file_name = "game_save.pkl"

# def generic_str_fn(self):
#     print("String printed for ")
#     print(self.__class__)
#     string = f"Class: {self.__class__.__name__}\n"
#     for key, value in self.__dict__.items():
#         tmp = "\tAttr: " + key + "\n\t" + str(value).replace("\n", "\n\t") + "\n"
#         string += tmp
#     return string

# loaded_figures = [Res.cloth, Res.stuff, Res.accessory, Res.packaging,
# Prod.aisha, Prod.beta, Prod.chama, ResPrice.cloth, ResPrice.stuff,
# ResPrice.accessory, ResPrice.packaging, ProdPrice.aisha, ProdPrice.beta,
# ProdPrice.chama, Production.hours_needed, Production.cost_per_hour,
# Production.res_cost, "current_call", "time_steps"]

loaded_figures = [Res.cloth, Res.stuff, Res.accessory, Res.packaging,
Prod.aisha, Prod.beta, Prod.chama]

fig_indices = ("name", "title", "x_label", "y_label")

FigureSpec = namedtuple("FigureSpec", fig_indices)

figure_spec_1 = FigureSpec(Res.cloth, "Res.cloth", "x_", "y_")
figure_spec_2 = FigureSpec(Res.stuff, "Res.stuff", "x_", "y_")
figure_spec_3 = FigureSpec(Res.accessory, "Res.accessory", "x_", "y_")
figure_spec_4 = FigureSpec(Res.packaging, "Res.packaging", "x_", "y_")

figure_spec_5 = FigureSpec(Prod.aisha, "Prod.aisha", "x_", "y_")
figure_spec_6 = FigureSpec(Prod.beta, "Prod.beta", "x_", "y_")
figure_spec_7 = FigureSpec(Prod.chama, "Prod.chama", "x_", "y_")

figure_spec_8 = FigureSpec(ResPrice.cloth, "ResPrice.cloth", "x_", "y_")
figure_spec_9 = FigureSpec(ResPrice.stuff, "ResPrice.stuff", "x_", "y_")
figure_spec_10 = FigureSpec(ResPrice.accessory, "ResPrice.accessory", "x_", "y_")
figure_spec_11 = FigureSpec(ResPrice.packaging, "ResPrice.packaging", "x_", "y_")

figure_spec_12 = FigureSpec(ProdPrice.aisha, "ProdPrice.aisha", "x_", "y_")
figure_spec_13 = FigureSpec(ProdPrice.beta, "ProdPrice.beta", "x_", "y_")
figure_spec_14 = FigureSpec(ProdPrice.chama, "ProdPrice.chama", "x_", "y_")
figure_spec_15 = FigureSpec(Production.hours_needed, "Production.hours_needed", "x_", "y_")
figure_spec_16 = FigureSpec(Production.cost_per_hour, "Production.cost_per_hour", "x_", "y_")
figure_spec_17 = FigureSpec(Production.res_cost, "Production.res_cost", "x_", "y_")
figure_spec_18 = FigureSpec("current_call", "current_call", "x_", "y_")
figure_spec_19 = FigureSpec("time_steps", "time_steps", "x_", "y_")

# figure_specs = [figure_spec_1, figure_spec_2, figure_spec_3, figure_spec_4,
#                 figure_spec_5, figure_spec_6, figure_spec_7, figure_spec_8,
#                 figure_spec_9, figure_spec_10, figure_spec_11, figure_spec_12,
#                 figure_spec_13, figure_spec_14, figure_spec_15, figure_spec_16,
#                 figure_spec_17, figure_spec_18, figure_spec_19]

figure_specs = [figure_spec_1, figure_spec_2, figure_spec_3, figure_spec_4,
                figure_spec_5, figure_spec_6, figure_spec_7]

widget_gindices = ["text_intrinsic_dim", "text_display_dim", "RBG_intrinsic_dim", "RBG_display_dim",
                  "TI_intrinsic_dim", "TI_display_dim", "button_intrinsic_dim",
                   "button_display_dim"]

WidgetGspecs = namedtuple("WidgetGspecs", widget_gindices)

widget_gspecs = WidgetGspecs(
    text_intrinsic_dim = [250, 50],  # width, height of text box
    text_display_dim = [0, 40],  # text width no diff, height determine how near RBG is.

    RBG_intrinsic_dim = [400, 0],   # width affects when break between rows happen
    RBG_display_dim = [0, 40],  # width no diff, height determine how close input and button is

    TI_intrinsic_dim = [1, 1],  # size of text_box, with a minimum
    TI_display_dim = [180, 0],  # for width, fix overall widget width together with button_display_dim

    button_intrinsic_dim = [50, 0],  # Size of button
    button_display_dim = [150, 100]  # height determine spacing between widget cols
    )   # width determine spacing between widgets in same row.

widget_iindices = ["name", "title", "button_label", "TI_placeholder", "RBG_labels"]

WidgetIspecs = namedtuple("WidgetIspecs", widget_iindices)

widget_ispecs_1 = WidgetIspecs(
    name=Func.buy_res,
    title = "buy_res",
    button_label = "buy",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Res) + [Others.reset])

widget_ispecs_2 = WidgetIspecs(
name=Func.sell_res,
    title = "sell_res",
    button_label = "sell",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Res) + [Others.reset])

widget_ispecs_3 = WidgetIspecs(
    name=Func.buy_prod,
    title = "buy_prod",
    button_label = "buy",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Prod) + [Others.reset])

widget_ispecs_4 = WidgetIspecs(
    name=Func.make_prod,
    title = "make_prod",
    button_label = "make",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Prod) + [Others.reset])


widget_ispecs_5 = WidgetIspecs(
    name=Func.sell_prod,
    title = "sell_prod",
    button_label = "sell",
    TI_placeholder = "Placeholder",
    RBG_labels=list(Prod) + [Others.reset])

# TODO: Transition eventually to a set of buttons alone, no TI
# TODO: Turn on/off widgets based on Ispecs?
widget_ispecs_6 = WidgetIspecs(
    name=Others,
    title = "Others",
    button_label = "Submit",
    TI_placeholder = "Placeholder",
    RBG_labels = list(Others))

# widget_ispecs_7 = WidgetIspecs(
# name=Func.buy_res,
#     title = "7Placeholder",
#     button_label = "place",
#     TI_placeholder = "Placeholder",
#     RBG_labels = ["one", "two", "three", "reset", "quit"])

widget_ispecs = [widget_ispecs_1, widget_ispecs_2, widget_ispecs_3,
                 widget_ispecs_4, widget_ispecs_5, widget_ispecs_6]

figures_per_row = 3
widgets_per_row = 3









