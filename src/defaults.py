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
    save_game = auto()
    load_game = auto()
    quit_game = auto()
    save_quit = auto()
    next_turn = auto()
    show_history = auto()
    back = auto()

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


# Split between delayed and active func.
# Copy of Function signal values above.
# to_actual_delayed_i = ["buy_res", "sell_res", "buy_prod", "make_prod", "sell_prod",]
#
# to_actual_now_i = ["show_stats", "show_prices", "save_game", "load_game",
#                  "quit_game", "save_quit", "next_turn"]
#
# to_tmp_i = ["show_stats", ]

# func_to_actual_delayed = pd.Series(to_actual_delayed_i, to_actual_delayed_i, name="func_to_actual_delayed")
# func_to_actual_now = pd.Series(to_actual_now_i, to_actual_now_i, name="func_to_actual_now")
# func_to_tmp = pd.Series(to_tmp_i, to_tmp_i, name="func_to_tmp")

starting_time = 0

def_save_folder = "../save/"
def_save_file_name = "game_save.pkl"

def generic_str_fn(self):
    string = f"Class: {self.__class__.__name__}\n"
    for key, value in self.__dict__.items():
        tmp = "\tAttr: " + key + "\n\t" + str(value).replace("\n", "\n\t") + "\n"
        string += tmp
    return string


fig_indices = ("x_label", "y_label", "title")

FigureSpec = namedtuple("FigureSpec", fig_indices)

figure_spec_1 = FigureSpec("x_placeholder", "y_placeholder", "fig_1")
figure_spec_2 = FigureSpec("x_placeholder", "y_placeholder", "fig_2")
figure_spec_3 = FigureSpec("x_placeholder", "y_placeholder", "fig_3")
figure_spec_4 = FigureSpec("x_placeholder", "y_placeholder", "fig_4")
figure_spec_5 = FigureSpec("x_placeholder", "y_placeholder", "fig_5")
figure_spec_6 = FigureSpec("x_placeholder", "y_placeholder", "fig_6")
figure_spec_7 = FigureSpec("x_placeholder", "y_placeholder", "fig_7")

figure_specs = [figure_spec_1, figure_spec_2, figure_spec_3, figure_spec_4,
                figure_spec_5, figure_spec_6, figure_spec_7]

widget_gindices = ["text_intrinsic_dim", "text_display_dim", "RBG_display_dim",
                  "TI_intrinsic_dim", "TI_display_dim", "button_intrinsic_dim",
                   "button_display_dim"]

WidgetGspecs = namedtuple("WidgetGspecs", widget_gindices)

widget_gspecs = WidgetGspecs(
    text_intrinsic_dim = [250, 50],  # width, height of text box
    text_display_dim = [0, 40],  # text width no diff, height determine how near RBG is.

    # RBG_intrinsic makes no diff
    RBG_display_dim = [0, 40],  # width no diff, height determine how close input and button is

    TI_intrinsic_dim = [1, 1],  # size of text_box, with a minimum
    TI_display_dim = [180, 0],  # for width, fix overall widget width together with button_display_dim

    button_intrinsic_dim = [50, 0],  # Size of button
    button_display_dim = [100, 100]  # height determine spacing between widget cols
    )   # width determine spacing between widgets in same row.

widget_iindices = ["title", "button_label", "TI_placeholder", "RBG_labels"]

WidgetIspecs = namedtuple("WidgetIspecs", widget_iindices)

widget_ispecs_1 = WidgetIspecs(
    title = "1Placeholder",
    button_label = "place",
    TI_placeholder = "Placeholder",
    RBG_labels = ["one", "two", "three", "reset", "quit"])

widget_ispecs_2 = WidgetIspecs(
    title = "2Placeholder",
    button_label = "place",
    TI_placeholder = "Placeholder",
    RBG_labels = ["one", "two", "three", "reset", "quit"])

widget_ispecs_3 = WidgetIspecs(
    title = "3Placeholder",
    button_label = "place",
    TI_placeholder = "Placeholder",
    RBG_labels = ["one", "two", "three", "reset", "quit"])

widget_ispecs_4 = WidgetIspecs(
    title = "4Placeholder",
    button_label = "place",
    TI_placeholder = "Placeholder",
    RBG_labels = ["one", "two", "three", "reset", "quit"])

widget_ispecs_5 = WidgetIspecs(
    title = "5Placeholder",
    button_label = "place",
    TI_placeholder = "Placeholder",
    RBG_labels = ["one", "two", "three", "reset", "quit"])

widget_ispecs_6 = WidgetIspecs(
    title = "6Placeholder",
    button_label = "place",
    TI_placeholder = "Placeholder",
    RBG_labels = ["one", "two", "three", "reset", "quit"])

widget_ispecs_7 = WidgetIspecs(
    title = "7Placeholder",
    button_label = "place",
    TI_placeholder = "Placeholder",
    RBG_labels = ["one", "two", "three", "reset", "quit"])

widget_ispecs = [widget_ispecs_1, widget_ispecs_2, widget_ispecs_3,
                 widget_ispecs_4, widget_ispecs_5, widget_ispecs_6,
                 widget_ispecs_7]

figures_per_row = 3
widgets_per_row = 3











