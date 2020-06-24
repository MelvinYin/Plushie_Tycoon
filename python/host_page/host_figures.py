from collections import defaultdict

from bokeh.models import DataTable, TableColumn, ColumnDataSource
from bokeh.models.widgets import Button, Div

from config.global_config import Res, Prod

class TransactionTable:
    def __init__(self):
        self.width = 500
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
        for category, ratio in data.items():
            assert isinstance(category, str)
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