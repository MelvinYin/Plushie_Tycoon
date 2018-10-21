import pandas as pd
import numpy as np
np.seterr("print")

try:
    from base import Res, Prod, ResPrice, ProdPrice, Others, Func, res_members, \
        prod_members
    from figure import FigureSpecs
    from widget import WidgetSpecs
except:
    from .base import Res, Prod, ResPrice, ProdPrice, Others, Func, \
        res_members, prod_members
    from .figure import FigureSpecs
    from .widget import WidgetSpecs



# Plushie Resource Cost
_res_cost = dict()
_res_cost[Prod.aisha] = [3,6,2,1]
_res_cost[Prod.beta] = [1,4,1,2]
_res_cost[Prod.chama] = [2,5,1,4]
prod_res_cost = pd.DataFrame(_res_cost, index=res_members)

# Plushie Production Hours
_p_hours = [30, 24, 36]
hours_needed = pd.Series(_p_hours, prod_members)

# Cost Per Production Hour
cost_per_hour = 3

# Starting Statistics
starting_budget = 10000000

_s_res = [1000,1000,1000,1000]
starting_res = pd.Series(_s_res, res_members, name="starting_res")

_s_prod = [100,100,100]
starting_prod = pd.Series(_s_prod, prod_members, name="starting_prod")

_s_res_price = [10,20,18,12]
starting_res_price = pd.Series(_s_res_price, res_members, name="starting_res_price")

_s_prod_price = [80,76,52]
starting_prod_price = pd.Series(_s_prod_price, prod_members, name="starting_prod_price")

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



