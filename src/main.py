"""
Necessary boxes to display:
1. Make tables, to show res consumption to make (perm)
2. Current prices for each item?
3. Current movein/moveout cost per item per unit

"""

import sys
from utils.sys_path_adder import folders_to_add
from bokeh.plotting import show, curdoc

folders_to_add(['bokeh_ui', 'config', 'p_model', 'tests', 'gs_components',
                'utils'])
folders_to_add(['figures', 'widgets'], suffix='bokeh_ui')
folders_to_add(['mocked_data'], suffix='tests')
folders_to_add(['p_model'], suffix='gs_components')

from ui_interface import UIInterface
import inspect
from logs import log, remake_log
import old_logs
from ge import GE

old_logs.set_logging_level()

from global_config import UISpecs
import random
from collections import defaultdict
import copy
random.seed(1)

def main():
    remake_log()
    ge = GE()
    callback = ge.callback
    init_data = ge.return_data()
    log(init_data, inspect.currentframe())
    # callback(dict(command=Func.buy, category=Res.cloth, quantity=10))

    ui = UIInterface(init_data, callback, UISpecs())
    # calls = mocked_transaction_callbacks()
    # ui.ui_callback(calls[0])
    # show(ui.ui_layout)
    curdoc().add_root(ui.ui_layout)

main()
