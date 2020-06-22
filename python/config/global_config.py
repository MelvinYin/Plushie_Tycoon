import inspect
import pandas as pd
import sys
from config.base import Res, Prod, Func
from config.figure import FigureNames, FigSpecs
from config.properties import WarehouseStats
# try:
#     from python.config.base import Res, Prod, Func
#     from python.config.figure import FigureNames, FigSpecs
#     from python.config.properties import WarehouseStats
# except:
#     from base import Res, Prod, Func
#     from figure import FigureNames, FigSpecs
#     from properties import WarehouseStats

UI_FAIL = hash('UI_FAIL')

src_path = inspect.currentframe().f_code.co_filename.rsplit("/", maxsplit=1)[0]
if src_path not in sys.path:
    sys.path.append(src_path)

save_folder = f"{src_path}save/"
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

res_ratio
hours_needed
cost_per_hour
starting_budget
starting_res
starting_prod
starting_res_price
starting_prod_price
starting_time
save_folder
save_file_name

"""




