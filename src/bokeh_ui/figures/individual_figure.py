from bokeh.plotting import figure, show, ColumnDataSource, curdoc
from bokeh.models import DataRange1d, HoverTool, BoxZoomTool, PanTool, \
    WheelZoomTool, ResetTool, UndoTool, Plot, Text
from bokeh.models.tickers import FixedTicker
import numpy as np
import copy
import re

"""
self.current_ticks need to be pulled out, because figure.xaxis.ticker cannot 
be retrieved.

Func_steps start from len(initial_data) so it is always about the next function
call.

initial_func_count when fed in should be positive int.

# TODO: back function
"""


"""
xs = func_steps

Initial data should have key as each of the key, no time_step.

Because when loading data, we 
"""
from logs import log
import inspect
from bokeh.layouts import row, column
from bokeh.models.widgets import Paragraph, Div
from bokeh.models.layouts import WidgetBox, Spacer
from bokeh.models import DataTable, TableColumn, ColumnDataSource
from global_config import FigureNames, res_members, Prod, prod_members

class MoveCostTable:
    def __init__(self, initial_data, specs):
        self.name = specs.name
        initial_data = self._convert_input(initial_data)
        self._check_initial_data(initial_data)
        self.initial_data = initial_data
        self.specs = specs
        self._CDS = self._set_CDS()
        self._table = self._build_table()
        self.figure = self._set_table()

    def _convert_input(self, data):
        resource_ratios = dict()
        for category in data:
            resource_ratios[category.name] = \
                [int(i) for i in data[category].values]
        return resource_ratios

    def _check_initial_data(self, data):
        assert data
        assert isinstance(data, dict)
        ratio_len = None
        for category, ratios in data.items():
            assert isinstance(category, str)
            if ratio_len is None:
                ratio_len = len(ratios)
                assert ratio_len > 0
            else:
                assert len(ratios) == ratio_len
            for ratio in ratios:
                assert ratio >= 0
        return True

    def _check_add_data(self, data):
        assert data
        for category, ratios in data.items():
            assert category in self.initial_data
            assert len(ratios) == len(self.initial_data[category])
            for ratio in ratios:
                assert ratio >= 0
        return True

    def _set_CDS(self):
        CDS_input = {**self.specs.index, **self.initial_data}
        source = ColumnDataSource(CDS_input)
        return source

    def _build_table(self):
        columns = [TableColumn(field=i, title=i, width=1000) for i in
                       self.specs.index.keys()]
        columns.extend([TableColumn(field=i, title=i) for i in
                        self.initial_data.keys()])
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.specs.width,
                               height=self.specs.height, index_position=None)
        return data_table

    def _set_table(self):
        fig = column(row(Spacer(width=15), Div(text=self.specs.title),
                         height=22), self._table)
        return fig

    def figure_update(self, add_data):
        add_data = self._convert_input(add_data)
        self._check_add_data(add_data)
        to_patch = dict()
        for category, ratios in add_data.items():
            for i, ratio in enumerate(ratios):
                to_patch[category] = [(i, ratio)]
        self._CDS.patch(to_patch)
        return


class ItemPropertiesTable:
    def __init__(self, inventory):
        self.name = FigureNames.item_properties_table
        self.title = "Properties"
        self.index = self._get_index(inventory)
        self.properties = self._get_properties(inventory)
        self.width = 200
        self.height = 200

        self._CDS = self._set_CDS()
        self._table = self._build_table()
        self.figure = self._set_table()

    def _get_properties(self, inventory):
        weights = inventory.get('weight')
        volumes = inventory.get('volume')
        assert tuple(weights.keys()) == tuple(volumes.keys())
        properties = dict()
        properties['Weight'] = list(weights.values())
        properties['Volume'] = list(volumes.values())
        return properties

    def _get_index(self, inventory):
        weights = inventory.get('weight')
        categories = list(weights.keys())
        index = dict()
        index['Item'] = list(i.name for i in categories)
        for col in index.values():
            for i in col:
                assert isinstance(i, str)
        return index

    def _check_initial_data(self, data):
        assert data
        assert isinstance(data, dict)
        ratio_len = None
        for category, ratios in data.items():
            assert isinstance(category, str)
            if ratio_len is None:
                ratio_len = len(ratios)
                assert ratio_len > 0
            else:
                assert len(ratios) == ratio_len
            for ratio in ratios:
                assert isinstance(ratio, int), ratio
                assert ratio >= 0
        return True

    def _set_CDS(self):
        for i in self.properties.keys():
            assert isinstance(i, str)
        CDS_input = {**self.index, **self.properties}
        source = ColumnDataSource(CDS_input)
        return source

    def _build_table(self):
        columns = [TableColumn(field=i, title=i, width=800) for i in
                       self.index.keys()]
        columns.extend([TableColumn(field=i, title=i) for i in
                        self.properties.keys()])
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width,
                               height=self.height, index_position=None)
        return data_table

    def _set_table(self):
        fig = column(row(Spacer(width=15), Div(text=self.title), height=22),
                     self._table)
        return fig

    def figure_update(self, inventory):
        # add_data = self._convert_input(add_data)
        # self._check_add_data(add_data)
        properties = self._get_properties(inventory)
        to_patch = dict()
        for category, ratios in properties.items():
            for i, ratio in enumerate(ratios):
                to_patch[category] = [(i, ratio)]
        self._CDS.patch(to_patch)
        return

class ResourceRatioTable:
    def __init__(self, initial_data):
        self.name = FigureNames.res_ratio_table
        self.title = "Production Resource Ratios"
        self.index = dict()
        self.index['Resource'] = [i.name for i in res_members]
        self.data = dict()
        self.data[Prod.aisha.name] = [3, 6, 2, 1]
        self.data[Prod.beta.name] = [1, 4, 1, 2]
        self.data[Prod.chama.name] = [2, 5, 1, 4]
        self.width = 200
        self.height = 200

        initial_data = self._convert_input(initial_data)
        self._check_initial_data(initial_data)
        self.initial_data = initial_data
        self._CDS = self._set_CDS()
        self._table = self._build_table()
        self.figure = self._set_table()

    def _convert_input(self, data):
        resource_ratios = dict()
        for category in data:
            resource_ratios[category.name] = \
                [int(i) for i in data[category].values]
        return resource_ratios

    def _check_initial_data(self, data):
        assert data
        assert isinstance(data, dict)
        ratio_len = None
        for category, ratios in data.items():
            assert isinstance(category, str)
            if ratio_len is None:
                ratio_len = len(ratios)
                assert ratio_len > 0
            else:
                assert len(ratios) == ratio_len
            for ratio in ratios:
                assert isinstance(ratio, int), ratio
                assert ratio >= 0
        return True

    def _check_add_data(self, data):
        assert data
        for category, ratios in data.items():
            assert category in self.initial_data
            assert len(ratios) == len(self.initial_data[category])
            for ratio in ratios:
                assert isinstance(ratio, int)
                assert ratio >= 0
        return True

    def _set_CDS(self):
        CDS_input = {**self.index, **self.initial_data}
        source = ColumnDataSource(CDS_input)
        return source

    def _build_table(self):
        columns = [TableColumn(field=i, title=i, width=1000) for i in
                       self.index.keys()]
        columns.extend([TableColumn(field=i, title=i) for i in
                        self.initial_data.keys()])
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width,
                               height=self.height, index_position=None)
        return data_table

    def _set_table(self):
        fig = column(row(Spacer(width=15), Div(text=self.title),
                         height=22), self._table)
        return fig

    def figure_update(self, add_data):
        add_data = self._convert_input(add_data)
        self._check_add_data(add_data)
        to_patch = dict()
        for category, ratios in add_data.items():
            for i, ratio in enumerate(ratios):
                to_patch[category] = [(i, ratio)]
        self._CDS.patch(to_patch)
        return

class ConsoleOutput:
    def __init__(self):
        self.name = FigureNames.console_output
        self.title = "Console"
        self.text = 'Initial<p>'
        self.width = 50
        self.height = 20
        self.textbox_width = 400
        self.textbox_height = 380
        # Division by 2 so it fits well and within what bokeh uses.
        self.html_height = int(self.textbox_height / 2)
        self._paragraph = self._build_paragraph()
        self.figure = self._set_textbox()
        self._rollover_count = 20

    def _build_paragraph(self):
        _style = dict()
        _style['overflow-y'] = 'auto'
        _style['height'] = '{}px'.format(self.html_height)
        paragraph = Div(width=self.textbox_width,
                        height=self.textbox_height,
                        text=self.text, style=_style)
        return paragraph

    def _set_textbox(self):
        fig = column(row(Spacer(height=self.height)),
                     row(Spacer(width=self.width), self._paragraph))
        return fig

    def figure_update(self, add_line):
        self._paragraph.text = add_line['console']
        return True

class IndividualFigure:
    def __init__(self, initial_data, specs):
        self._check_initial_data(initial_data)
        self.CDS = self._create_initial_CDS(initial_data)
        self.tick_label_map = self._get_initial_ticks_label_mapping()
        self.figure = self._set_initial_figure(specs)
        self._update_xaxis()
        self.name = specs.name

    def _check_initial_data(self, data):
        assert data
        num_values = None
        for value in data.values():
            assert isinstance(value, list)
            if num_values is None:
                num_values = len(value)
                continue
            assert len(value) == num_values
        return True

    def _check_add_data(self, data):
        assert data
        for value in data.values():
            assert isinstance(value, list)
            assert len(value) == 1
        return True

    def _create_initial_CDS(self, initial_data):
        """
        Dict sent to CDS should have list instead of tuple as values, otherwise
        CDS.stream will fail.
        """
        num_values = len(next(iter(initial_data.values())))
        initial_data['xs'] = list(range(num_values))
        CDS = ColumnDataSource(data=copy.deepcopy(initial_data))
        return CDS

    def _get_initial_ticks_label_mapping(self):
        time = self.CDS.data["time"]
        xs = self.CDS.data['xs']

        time_values, counts = np.unique(time, return_counts=True)
        tick_label_map = dict()
        counter = 0
        for time, count in zip(time_values, counts):
            tick_label_map[xs[counter]] = str(time)
            counter += count
        return tick_label_map

    def _set_initial_figure(self, Specs):
        hover = HoverTool(
            tooltips=[("Point No.", "@xs"),
                      ("Time Step", "@time")],
            names=["x", "points2"])

        boxzoom = BoxZoomTool()
        pan = PanTool()
        wheelzoom = WheelZoomTool()
        reset = ResetTool()
        undo = UndoTool()

        tools = [pan, boxzoom, wheelzoom, reset, undo, hover]

        p = figure(plot_width=400, plot_height=400, tools=tools)
        p.toolbar.active_drag = pan
        p.toolbar.active_scroll = wheelzoom
        p.toolbar.active_tap = None
        p.toolbar.active_inspect = hover
        p.toolbar.logo = None

        p.x_range = DataRange1d(follow="end", follow_interval=5,
                                range_padding=1, range_padding_units='absolute')
        p.y_range = DataRange1d(follow="end", range_padding=2,
                                range_padding_units='absolute')

        initial_ticks = list(self.tick_label_map.keys())
        ticker = FixedTicker(ticks=initial_ticks)
        p.xaxis.ticker = ticker
        p.xgrid.ticker = ticker

        p.xaxis.major_label_overrides = self.tick_label_map

        p.title.text = Specs.title
        p.title.align = 'center'
        p.xaxis.axis_label = Specs.x_label
        p.yaxis.axis_label = Specs.y_label
        keys_in_figure = list([key for key in self.CDS.column_names
                               if key != 'time' and key != 'xs'])

        # Additional "_" because if legend key is same as data x/y key,
        # legend plot will show data values instead of key (str) value,
        # reported in bokeh issues, see #8394
        for key in keys_in_figure:
            legend_key = key + "_"
            color_value = Specs.colormap[key]
            p.x("xs", key, source=self.CDS, name=key, size=10,
                legend=legend_key, color=color_value)
            p.line("xs", key, source=self.CDS, legend=legend_key,
                   color=color_value)

        p.legend.location = "top_left"
        p.legend.click_policy = "hide"

        return p

    def _update_xaxis(self):
        ticker = FixedTicker(ticks=list(self.tick_label_map.keys()))
        self.figure.xaxis.ticker = ticker
        self.figure.xgrid.ticker = ticker
        self.figure.xaxis.major_label_overrides = self.tick_label_map
        return True

    def figure_update(self, add_line):
        current_time = add_line['time'][0]
        current_x = self.CDS.data['xs'][-1] + 1
        add_line['xs'] = [current_x]
        if current_time != self.CDS.data['time'][-1]:
            self.tick_label_map[current_x] = str(current_time)
            self._update_xaxis()
        log(add_line, inspect.currentframe())

        # Load does not work at this stage because figures do not appear to
        # be able to refresh themselves
        self.CDS.stream(add_line)
        return True