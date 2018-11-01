from bokeh.plotting import figure, show, ColumnDataSource, curdoc
from bokeh.models import DataRange1d, HoverTool, BoxZoomTool, PanTool, \
    WheelZoomTool, ResetTool, UndoTool, Plot, Text
from bokeh.models.tickers import FixedTicker
import numpy as np

"""
Only data that needs to be reflected in graph or hover, should be in CDS.

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
import os
import inspect

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
        CDS = ColumnDataSource(data=initial_data)
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

        p.x_range = DataRange1d(follow="end", follow_interval=5, range_padding=1, range_padding_units='absolute')
        p.y_range = DataRange1d(follow="end", range_padding=2, range_padding_units='absolute')

        initial_ticks = list(self.tick_label_map.keys())
        ticker = FixedTicker(ticks=initial_ticks)
        p.xaxis.ticker = ticker
        p.xgrid.ticker = ticker

        p.xaxis.major_label_overrides = self.tick_label_map

        p.title.text = Specs.title
        p.title.align = 'center'
        p.xaxis.axis_label = Specs.x_label
        p.yaxis.axis_label = Specs.y_label
        for key in self.CDS.column_names:
            if key != 'time' and key != 'xs':
                p.x("xs", key, source=self.CDS, name=key, size=10)
                p.line("xs", key, source=self.CDS)
        return p

    def _update_xaxis(self):
        ticker = FixedTicker(ticks=list(self.tick_label_map.keys()))
        self.figure.xaxis.ticker = ticker
        self.figure.xgrid.ticker = ticker
        self.figure.xaxis.major_label_overrides = self.tick_label_map
        return True

    def figure_update(self, add_line):
        log(add_line, inspect.currentframe())
        current_time = add_line['time'][0]
        current_x = self.CDS.data['xs'][-1] + 1
        add_line['xs'] = [current_x]

        if current_time > self.CDS.data['time'][-1]:
            self.tick_label_map[current_x] = str(current_time)
            self._update_xaxis()

        self.CDS.stream(add_line)
        return True
