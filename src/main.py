import sys
from sys_path_adder import folders_to_add
from bokeh.plotting import show, curdoc

folders_to_add(['bokeh_ui', 'config', 'p_model', 'tests'])
folders_to_add(['figures', 'widgets'], suffix='bokeh_ui')
folders_to_add(['mocked_data'], suffix='tests')

from ui_interface import UIInterface
import inspect
from logs import log, remake_log
import old_logs
from ge import GE

old_logs.set_logging_level()

from global_config import Res, Prod, Func, UISpecs
import random
from collections import defaultdict
import copy
random.seed(1)

mocked_time = [2,2,3,4,5,6,6,7,8,8]
from bokeh.sampledata.stocks import AAPL
# print(AAPL.keys())
# sys.exit()


def main():
    remake_log()
    ge = GE()
    callback = ge.callback
    init_data = ge._convert_GS_to_dict()
    log(init_data, inspect.currentframe())
    # callback(dict(command=Func.buy, category=Res.cloth, quantity=10))

    ui = UIInterface(init_data, callback, UISpecs())
    # calls = mocked_transaction_callbacks()
    # ui.ui_callback(calls[0])
    show(ui.ui_layout)
    curdoc().add_root(ui.ui_layout)

main()
