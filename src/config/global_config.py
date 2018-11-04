import pandas as pd
try:
    from .base import Res, Prod, ProdPrice, Func, \
        res_members, prod_members
    from .figure import FigureSpecs, FigureNames
    from .widget import WidgetSpecs
    from .gs_data_construct import GSConstructor
except:
    from base import Res, Prod, Func, res_members, prod_members
    from figure import FigureSpecs, FigureNames
    from widget import WidgetSpecs
    from gs_data_construct import GSConstructor

# Plushie Resource Cost
_res_cost = dict()
_res_cost[Prod.aisha] = [3,6,2,1]
_res_cost[Prod.beta] = [1,4,1,2]
_res_cost[Prod.chama] = [2,5,1,4]
prod_res_cost = pd.DataFrame(_res_cost, index=res_members)

# Plushie Production Hours
_p_hours = [30, 24, 36]
hours_needed = dict()
for i, prod in enumerate(prod_members):
    hours_needed[prod] = _p_hours[i]

# Cost Per Production Hour
cost_per_hour = 3

# Starting Statistics
starting_budget = 10000000

_s_res = [1001,1002,1003,1004]
starting_res = dict()
for i, res in enumerate(res_members):
    starting_res[res] = _s_res[i]

_s_prod = [101,102,103]
starting_prod = dict()
for i, prod in enumerate(prod_members):
    starting_prod[prod] = _s_prod[i]

_s_res_price = [10,20,18,12]
starting_res_price = dict()
for i, res in enumerate(res_members):
    starting_res_price[res] = _s_res_price[i]

_s_prod_price = [80,76,52]
starting_prod_price = dict()
for i, prod in enumerate(prod_members):
    starting_prod_price[prod] = _s_prod_price[i]

_history_columns = ["res", "prod", "res_price", "prod_price", "budget", "production",
           "time_steps", "current_call"]

history_init = pd.DataFrame(columns=_history_columns)

starting_time = 0

save_folder = "../save/"
save_file_name = "game_save.pkl"

class UISpecs:
    def __init__(self):
        self.figures = FigureSpecs()
        self.widgets = WidgetSpecs()

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




