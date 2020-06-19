from bokeh.models.widgets import Button
from collections import defaultdict
from bokeh.layouts import row, column
from bokeh.models.widgets import Div
from bokeh.models.layouts import Spacer
from bokeh.models import DataTable, TableColumn, ColumnDataSource
import grpc
import grpc_pb2_grpc
import grpc_pb2
from config.global_config import Res, Prod

class TransactionTable:
    def __init__(self):
        self.width = 250
        self.height = 220

        self._CDS = self._set_CDS()
        self._table = self._build_table()
        self.figure = self._set_table()

    def _set_CDS(self):
        data = dict()
        data['userid'] = []
        for res in Res:
            tag = "transaction_" + res.name
            data[tag] = []
        for prod in Prod:
            tag = "transaction_" + prod.name
            data[tag] = []
        source = ColumnDataSource(data)
        return source

    def _build_table(self):
        columns = []
        columns.append(TableColumn(field="userid", title="UserID"))
        for res in Res:
            tag = "transaction_" + res.name
            columns.append(TableColumn(field=tag, title=res.name))
        for prod in Prod:
            tag = "transaction_" + prod.name
            columns.append(TableColumn(field=tag, title=prod.name))
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width, height=self.height,
                               index_position=None)
        return data_table

    def _set_table(self):
        return self._table

    def figure_update(self, data):
        to_patch = defaultdict(list)
        for category, ratio in data.items():
            assert isinstance(category, str)
            if category in self._CDS.data:
                to_patch[category] = [ratio]
        self._CDS.stream(to_patch)
        return


class ProductionTable:
    def __init__(self):
        self.width = 250
        self.height = 220

        self._CDS = self._set_CDS()
        self._table = self._build_table()
        self.figure = self._set_table()

    def _set_CDS(self):
        data = dict()
        data['userid'] = []
        for prod in Prod:
            tag = "production_" + prod.name
            data[tag] = []
        source = ColumnDataSource(data)
        return source

    def _build_table(self):
        columns = []
        for prod in Prod:
            tag = "production_" + prod.name
            columns.append(TableColumn(field=tag, title=prod.name))
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width, height=self.height,
                               index_position=None)
        return data_table

    def _set_table(self):
        return self._table

    def figure_update(self, data):
        to_patch = dict()
        print(data)
        for category, ratio in data.items():
            assert isinstance(category, str)
            print(self._CDS.data)
            if category in self._CDS.data:
                to_patch[category] = [ratio]
        self._CDS.stream(to_patch)
        return

class TextBoxComponent:
    def __init__(self, specs):
        self.widget = self._set_TB(specs)

    def _set_TB(self, specs):
        TB = Div(text=specs['text'])
        TB.width = specs['width']
        TB.height = specs['height']
        return TB


class ButtonComponent:
    def __init__(self, specs, widget_callback):
        self.widget_callback = widget_callback
        self.widget = self._set_button(specs)

    def _set_button(self, specs):
        button = Button()
        button.label = specs['text']
        button.width = specs['width']
        button.height = specs['height']
        button.on_click(self.widget_callback)
        return button

class UI:
    def __init__(self, portno):
        self.portno = portno
        self.transaction_table = TransactionTable()
        self.production_table = ProductionTable()
        self.time_box = self._build_time_box()
        self.next_turn_button = self._build_next_turn()
        self.refresh_button = self._build_refresh()
        self.ping_button = self._build_ping()
        self.layout = self.plot()

    def _build_next_turn(self):
        specs = dict()
        specs['text'] = "Next Turn"
        specs['width'] = 100
        specs['height'] = 50
        button = ButtonComponent(specs, self.widget_callback)
        return button

    def _build_ping(self):
        specs = dict()
        specs['text'] = "Ping"
        specs['width'] = 100
        specs['height'] = 50
        button = ButtonComponent(specs, self.ping_callback)
        return button

    def _build_refresh(self):
        specs = dict()
        specs['text'] = "Refresh"
        specs['width'] = 100
        specs['height'] = 50
        button = ButtonComponent(specs, self.get_calls)
        return button

    def get_calls(self):
        print(f"\n\n\nget_calls called with portno {self.portno}.")
        with grpc.insecure_channel(f'localhost:{self.portno}') as channel:
            stub = grpc_pb2_grpc.AdminPageStub(channel)
            request_object = grpc_pb2.NullObject()
            for call in stub.getCall(request_object):
                print(call)
                call = self._format_changes(call)
                print(call)
                self.figure_update(call)

    def _format_changes(self, request):
        output = dict()
        output['userid'] = request.userid
        for res in Res:
            tag = "transaction_" + res.name
            if res.name.upper() in request.buySell:
                output[tag] = request.buySell[res.name.upper()]
            else:
                output[tag] = 0
        for prod in Prod:
            tag = "transaction_" + prod.name
            if prod.name.upper() in request.buySell:
                output[tag] = request.buySell[prod.name.upper()]
            else:
                output[tag] = 0

            tag = "production_" + prod.name
            if prod.name.upper() in request.make:
                output[tag] = request.make[prod.name.upper()]
            else:
                output[tag] = 0
        return output

    def _build_time_box(self):
        specs = dict()
        specs['text'] = '0'
        specs['height'] = 200
        specs['width'] = 200
        return TextBoxComponent(specs)

    def figure_update(self, update):
        self.time_box.widget.text = '123'
        # self.time_box.widget.text = update['time']
        self.transaction_table.figure_update(update)
        self.production_table.figure_update(update)
        return True

    def plot(self):
        layout = column(self.time_box.widget,
                        row(self.transaction_table.figure,
                            self.production_table.figure),
                        self.next_turn_button.widget,
                        self.refresh_button.widget, self.ping_button.widget)
        return layout

    def widget_callback(self, call):
        print(f"next_turn_button called.")
        with grpc.insecure_channel(f'localhost:{self.portno}') as channel:
            stub = grpc_pb2_grpc.AdminPageStub(channel)
            request_object = grpc_pb2.NullObject()
            return_object = stub.nextTurn(request_object)
            print(return_object.code)
        return True

    def ping_callback(self, call):
        print(f"ping_button called.")
        with grpc.insecure_channel(f'localhost:{self.portno}') as channel:
            stub = grpc_pb2_grpc.AdminPageStub(channel)
            request_object = grpc_pb2.NullObject()
            return_object = stub.ping(request_object)
            print(return_object.code)
        return True
