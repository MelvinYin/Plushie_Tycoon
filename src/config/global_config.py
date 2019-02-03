import pandas as pd
try:
    from .base import Res, Prod, Func, res_members, prod_members, \
        ProductionTuple, BudgetTuple, MarketTuple, InventoryTuple
    from .figure import FigureSpecs, FigureNames
    from .widget import WidgetSpecs
    from .gs_data_construct import GSConstructor
    from .properties import Properties, WarehouseStats
except:
    from base import Res, Prod, Func, res_members, prod_members, \
        ProductionTuple, BudgetTuple, MarketTuple, InventoryTuple
    from figure import FigureSpecs, FigureNames
    from widget import WidgetSpecs
    from gs_data_construct import GSConstructor
    from properties import Properties, WarehouseStats

_history_columns = ["res", "prod", "res_price", "prod_price", "budget", "production",
           "time_steps", "current_call"]

history_init = pd.DataFrame(columns=_history_columns)

# starting_time = 0

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




