import sys
src_path = sys.path[0].rsplit("/", maxsplit=1)[0]
sys.path.append(src_path)

import inspect
from logs import log, remake_log
import old_logs
from ge import GE

old_logs.set_logging_level()

from config.global_config import Res, Prod, Func, res_members, prod_members
import random
from collections import defaultdict
import copy
random.seed(1)

mocked_time = [2,2,3,4,5,6,6,7,8,8]

def main():
    remake_log()
    ge = GE()
    callback = ge.callback
    init_data = ge._convert_GS_to_dict()
    log(init_data, inspect.currentframe())
    print(init_data)
    print(callback(dict(command=Func.buy, category=Res.cloth, quantity=10)))

    # ui = UI(init_data, callback, UISpecs())
    # calls = mocked_transaction_callbacks()
    # ui.ui_callback(calls[0])
    # show(ui.ui_layout)
    # curdoc().add_root(ui.ui_layout)

main()
