from bokeh.plotting import figure, show, ColumnDataSource, curdoc
from bokeh.models import DataRange1d, HoverTool, BoxZoomTool, PanTool, \
    WheelZoomTool, ResetTool, UndoTool, Plot, Text
from bokeh.models.tickers import FixedTicker
import numpy as np
import copy
import re
from collections import defaultdict
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
from enum import Enum
from bokeh.layouts import row, column
from bokeh.models.widgets import Paragraph, Div
from bokeh.models.layouts import WidgetBox, Spacer
from bokeh.models import DataTable, TableColumn, ColumnDataSource
from global_config import FigureNames, Prod, Res

def enum_to_str(enum_arr):
    # This should convert enum representations to displayed names in UI.
    # Currently rather trivial since we take the .name, but it can eventually
    # be something more fancy. Maybe.
    if isinstance(enum_arr, Enum):
        return enum_arr.name
    str_arr = list(i.name for i in enum_arr)
    return str_arr


class ItemCostTable:
    def __init__(self, data):
        self.name = FigureNames.item_cost_table
        self.title = "Item Cost Table"
        self.width = 250
        self.height = 220

        self._CDS = self._set_CDS(data)
        self._table = self._build_table(data)
        self.figure = self._set_table()

    def _truncate_number(self, number):
        precision = 0
        curr_number = number
        while curr_number // 1 < 0.99 and precision < 10:
            precision += 1
            curr_number *= 10
        if precision == 0:
            return str(round(number))
        elif precision == 10:
            return "0."
        else:
            number = round(number * (10 ** precision)) / (10 ** precision)
            return '{:.{prec}f}'.format(number, prec=precision)

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

    def _set_CDS(self, data):
        for key, values in data.items():
            if key == "Item":
                continue
            new_values = []
            for value in values:
                error_msg = "This should be double, check who sent this in. " \
                            "Otherwise check whether the index column has " \
                            "key as 'Item'."
                assert not isinstance(value, str), error_msg
                new_values.append(self._truncate_number(value))
            data[key] = new_values
        source = ColumnDataSource(data)
        return source

    def _build_table(self, data):
        columns = [TableColumn(field=i, title=i) for i in
                        data.keys()]
        columns[0].width = 700
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width,
                               height=self.height, index_position=None)
        return data_table

    def _set_table(self):
        fig = column(row(Spacer(width=15), Div(text=self.title), height=30),
                     self._table)
        return fig

    def figure_update(self, data):
        # todo: also need to settle using transporter
        # add_data = self._convert_input(add_data)
        # self._check_add_data(add_data)
        to_patch = defaultdict(list)
        for category, ratios in data.items():
            assert isinstance(category, str)
            for i, ratio in enumerate(ratios):
                if category != "Item":
                    ratio = self._truncate_number(ratio)
                to_patch[category].append((i, ratio))
        self._CDS.patch(to_patch)
        return


class ItemPropertiesTable:
    def __init__(self, data):
        self.name = FigureNames.item_properties_table
        self.title = "Properties"
        self.data = data
        self.width = 250
        self.height = 220

        self._CDS = self._set_CDS(data)
        self._table = self._build_table(data)
        self.figure = self._set_table()

    def _get_properties(self, inventory):
        weights = inventory.get('weight')
        volumes = inventory.get('volume')
        assert tuple(weights.keys()) == tuple(volumes.keys())
        properties = dict()
        properties['Weight'] = list(weights.values())
        properties['Volume'] = list(volumes.values())
        return properties

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

    def _set_CDS(self, data):
        source = ColumnDataSource(data)
        return source

    def _build_table(self, data):
        columns = [TableColumn(field=i, title=i) for i in
                        data.keys()]
        columns[0].width = 400
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width, height=self.height,
                               index_position=None)
        return data_table

    def _set_table(self):
        header = row(Spacer(width=15), Div(text=self.title), height=30)
        fig = column(header, self._table)
        return fig

    def figure_update(self, data):
        to_patch = dict()
        for category, ratios in data.items():
            for i, ratio in enumerate(ratios):
                to_patch[category] = [(i, ratio)]
        self._CDS.patch(to_patch)
        return

class ResourceRatioTable:
    def __init__(self, initial_data):
        self.name = FigureNames.res_ratio_table
        self.title = "Production Resource Ratios"
        self.data = initial_data
        self.width = 250
        self.height = 220

        self._CDS = self._set_CDS()
        self._table = self._build_table()
        self.figure = self._set_table()

    def _convert_input(self, data):
        resource_ratios = dict()
        for category in data:
            resource_ratios[category.name] = \
                [int(i) for i in data[category].values]
        return resource_ratios

    def _set_CDS(self):
        source = ColumnDataSource(self.data)
        return source

    def _build_table(self):
        # todo: see if self.data can be replaced by a CDS call instead
        columns = [TableColumn(field=i, title=i) for i in
                        self.data.keys()]
        columns[0].width = 800
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width,
                               height=self.height, index_position=None)
        return data_table

    def _set_table(self):
        fig = column(row(Spacer(width=15), Div(text=self.title),
                         height=30), self._table)
        return fig

    def figure_update(self, add_data):
        # add_data = self._convert_input(add_data)
        to_patch = dict()
        for category, ratios in add_data.items():
            for i, ratio in enumerate(ratios):
                to_patch[category] = [(i, ratio)]
        self._CDS.patch(to_patch)
        return

class ConsoleOutput:
    def __init__(self, input_):
        self.name = FigureNames.console_output
        self.title = "Console"
        self.text = '<p>'
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
        _style['height'] = f'{self.html_height}px'
        paragraph = Div(width=self.textbox_width,
                        height=self.textbox_height,
                        text=self.text, style=_style)
        return paragraph

    def _set_textbox(self):
        fig = column(row(Spacer(height=self.height)),
                     row(Spacer(width=self.width), self._paragraph))
        return fig

    def figure_update(self, add_line):
        self._paragraph.text += add_line + "<br>"
        return True

class IndividualFigure:
    def __init__(self, initial_data, specs):
        self.CDS = self._create_initial_CDS(initial_data)
        self.tick_label_map = self._get_initial_ticks_label_mapping()
        self.figure = self._set_initial_figure(specs)
        self._update_xaxis()
        self.name = specs.name

    def _create_initial_CDS(self, initial_data):
        """
        Dict sent to CDS should have list instead of tuple as values, otherwise
        CDS.stream will fail.
        """
        # add test? to make sure all values used in this class is in init_data
        num_values = len(next(iter(initial_data.values())))
        initial_data['xs'] = list(range(num_values))
        CDS = ColumnDataSource(initial_data)
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

    def _set_initial_figure(self, specs):
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

        p.title.text = specs.title
        p.title.align = 'center'
        p.xaxis.axis_label = specs.x_label
        p.yaxis.axis_label = specs.y_label
        keys_in_figure = list([key for key in self.CDS.column_names
                               if key != 'time' and key != 'xs'])

        # Additional "_" because if legend key is same as data x/y key,
        # legend plot will show data values instead of key (str) value,
        # reported in bokeh issues, see #8394
        for key in keys_in_figure:
            legend_key = key + "_"
            color_value = specs.colormap[key]
            p.x("xs", key, source=self.CDS, name=key, size=10,
                legend_label=legend_key, color=color_value)
            p.line("xs", key, source=self.CDS, legend_label=legend_key,
                   color=color_value)
        p.legend.location = "top_left"
        p.legend.click_policy = "hide"
        return p

    def _update_xaxis(self):
        ticker = FixedTicker(ticks=list(self.tick_label_map.keys()))
        self.figure.xaxis.ticker = ticker
        self.figure.xgrid.ticker = ticker
        self.figure.xaxis.major_label_overrides = self.tick_label_map

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