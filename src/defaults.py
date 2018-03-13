import pandas as pd
from enum import Enum, auto, unique


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

# TODO: some form of a signatures template for others to compare with,
# TODO: like using an isinstance