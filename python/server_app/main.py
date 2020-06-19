"""
Necessary boxes to display:
1. Make tables, to show res consumption to make (perm)
2. Current prices for each item?
3. Current movein/moveout cost per item per unit

"""

# todo: individual_figure.py, CDS.

from utils.sys_path_adder import folders_to_add
from bokeh.plotting import curdoc
import admin_ui
from config.global_config import Res, Prod

folders_to_add(['bokeh_ui', 'config', 'p_model', 'tests', 'gs_components',
                'utils'])
folders_to_add(['figures', 'widgets'], suffix='bokeh_ui')
folders_to_add(['mocked_data'], suffix='tests')
folders_to_add(['p_model'], suffix='gs_components')

import grpc_pb2_grpc
import grpc_pb2
import grpc
import concurrent.futures

class Admin:
    def __init__(self, portno):
        self.portno = portno
        self.ui = admin_ui.UI(portno)
        self.admin_send = AdminSend(self.ui.figure_update)

class AdminSend(grpc_pb2_grpc.AdminSendServicer):
    def __init__(self, callback):
        self.callback = callback

    def sendCall(self, request, context):
        self.callback(self._format_changes(request))
        return grpc_pb2.NullObject()

    def _format_changes(self, request):
        output = dict()
        output['userid'] = request.userid
        for res in Res:
            tag = "transaction_" + res.__name__
            if res.__name__ in request.buySell:
                output[tag] = request.buySell[res.__name__]
            else:
                output[tag] = 0
        for prod in Prod:
            tag = "transaction_" + prod.__name__
            if prod.__name__ in request.buySell:
                output[tag] = request.buySell[prod.__name__]
            else:
                output[tag] = 0

            tag = "production_" + prod.__name__
            if prod.__name__ in request.make:
                output[tag] = request.buySell[prod.__name__]
            else:
                output[tag] = 0
        return output

def run():
    portno = 50003
    admin = Admin(portno)
    curdoc().add_root(admin.ui.layout)
    # show(ui.ui.ui_layout)

run()
"""
python -m grpc_tools.protoc --proto_path . --python_out=. --grpc_python_out=. 
./grpc.proto
"""