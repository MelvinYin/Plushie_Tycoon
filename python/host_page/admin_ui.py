from bokeh.layouts import row, column

from config.global_config import Res, Prod
from grpc_clients import admin_page
from host_figures import TransactionTable, ProductionTable, ButtonComponent, \
    TextBoxComponent


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
        specs['width'] = 70
        specs['height'] = 30
        button = ButtonComponent(specs, self.widget_callback)
        return button

    def _build_ping(self):
        specs = dict()
        specs['text'] = "Ping"
        specs['width'] = 70
        specs['height'] = 30
        button = ButtonComponent(specs, self.ping_callback)
        return button

    def _build_refresh(self):
        specs = dict()
        specs['text'] = "Refresh"
        specs['width'] = 70
        specs['height'] = 30
        button = ButtonComponent(specs, self.get_calls)
        return button

    def get_calls(self):
        print(f"get_calls called with portno {self.portno}.")
        for call in admin_page.getCall(self.portno):
            call = self._format_changes(call)
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
        specs['height'] = 20
        specs['width'] = 50
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
                        row(self.next_turn_button.widget,
                            self.refresh_button.widget, self.ping_button.widget))
        return layout

    def widget_callback(self, call):
        print(f"next_turn_button called.")
        time = admin_page.nextTurn(self.portno).message
        self.time_box.widget.text = time
        return True

    def ping_callback(self, call):
        print(f"ping_button called.")
        admin_page.ping(self.portno)
        return True
