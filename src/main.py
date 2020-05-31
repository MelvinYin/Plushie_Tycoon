"""
Necessary boxes to display:
1. Make tables, to show res consumption to make (perm)
2. Current prices for each item?
3. Current movein/moveout cost per item per unit

"""

# todo: individual_figure.py, CDS.

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
from logs import log, remake_log, set_logging_level
from ge import GE

set_logging_level()

from global_config import UISpecs
import random
from collections import defaultdict
import copy
random.seed(1)
from config.global_config import Func, res_members, prod_members


def mocked_transaction_callbacks():
    callbacks = []
    for func in (Func.buy, Func.sell):
        for res in res_members:
            callback = dict(command=func, category=res,
                            quantity=random.randint(0, 10))
            callbacks.append(callback)
        for prod in prod_members:
            callback = dict(command=func, category=prod,
                            quantity=random.randint(0, 10))
            callbacks.append(callback)
    for prod in prod_members:
        callback = dict(command=Func.make, category=prod,
                        quantity=random.randint(0, 10))
        callbacks.append(callback)
    return callbacks


def mocked_button_callbacks():
    funcs = (Func.save, Func.load, Func.back, Func.next, Func.quit)
    callbacks = list([dict(command=func) for func in funcs])
    return callbacks


mock_callbacks = mocked_transaction_callbacks() + mocked_button_callbacks()
import grpc
import grpc_pb2
import grpc_pb2_grpc
from concurrent.futures import ThreadPoolExecutor

from ui_interface import UIInterface


def run():
    port_no = "50051"
    ui = UIInterface(port_no)
    curdoc().add_root(ui.ui.ui_layout)
    # show(ui.ui.ui_layout)
    # with grpc.insecure_channel('localhost:50051') as channel:
    #     stub = grpc_pb2_grpc.UITransferStub(channel)
    #     # ui = MockUI(stub)
    #     ui = UIInterface(stub)


run()

"""
Client side:


def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_pb2_grpc.RouteGuideStub(channel)
        feat = grpc_pb2.Point(a=123)
        feature = stub.GetFeature(feat)
        print(feature)
    # a = grpc_pb2.
    pass



"""