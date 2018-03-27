from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import DataRange1d, HoverTool, BoxZoomTool, PanTool, \
    WheelZoomTool, ResetTool, UndoTool
from bokeh.models.tickers import FixedTicker

"""
Only data that needs to be reflected in graph or hover, should be in CDS.

self.current_ticks need to be pulled out, because figure.xaxis.ticker cannot 
be retrieved.

Func_steps start from len(initial_data) so it is always about the next function
call.
"""
# TODO: back function

class IndividualFigure:
    def __init__(self, initial_data, specs, initial_func_count = None):
        self.specs = specs
        if not initial_func_count:
            self.func_steps = 0
        else:
            assert isinstance(initial_func_count, int) and initial_func_count >= 0
            self.func_steps = initial_func_count

        self.CDS = self._create_initial_CDS(initial_data)
        self.tick_label_map = self._get_initial_ticks_label_mapping()
        self.figure = self._set_initial_figure()
        self._update_initial_func_steps()
        self._update_xaxis()


    def _update_initial_func_steps(self):
        self.func_steps += len(self.CDS.data['time_steps'])
        return True

    def _create_initial_CDS(self, initial_data):
        """
        Dict sent to CDS should have list instead of tuple as values, otherwise
        CDS.stream will fail.
        """
        time_steps, ys = zip(*initial_data)
        to_CDS = dict(func_steps=list(range(self.func_steps, self.func_steps + len(time_steps))), ys=list(ys), time_steps=list(time_steps))
        CDS = ColumnDataSource(data=to_CDS)
        return CDS

    def _get_initial_ticks_label_mapping(self):   # assuming time_step has more than 1?
        time_steps = self.CDS.data["time_steps"]
        current_time = time_steps[0]
        func_steps = self.func_steps
        tick_label_map = dict()
        tick_label_map[func_steps] = str(current_time)
        for i in range(len(time_steps)):
            if time_steps[i] != current_time:
                current_time = time_steps[i]
                tick_label_map[func_steps] = str(current_time)
            func_steps += 1
        return tick_label_map

    def _set_initial_figure(self):
        hover = HoverTool(
            tooltips=[("Point No.", "@func_steps"),
                      ("Time Step", "@time_steps")],
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

        p.x_range = DataRange1d(follow="end", follow_interval=5, range_padding=0.05)
        p.y_range = DataRange1d(follow="end", range_padding=0.1)

        initial_ticks = list(self.tick_label_map.keys())
        ticker = FixedTicker(ticks=initial_ticks)
        p.xaxis.ticker = ticker
        p.xgrid.ticker = ticker

        p.xaxis.major_label_overrides = self.tick_label_map

        p.title.text = self.specs.title
        p.title.align = 'center'
        p.xaxis.axis_label = self.specs.x_label
        p.yaxis.axis_label = self.specs.y_label
        p.x("func_steps", "ys", source=self.CDS, name="x", size=10)
        p.line("func_steps", "ys", source=self.CDS)
        return p

    def _update_xaxis(self):
        ticker = FixedTicker(ticks=list(self.tick_label_map.keys()))
        self.figure.xaxis.ticker = ticker
        self.figure.xgrid.ticker = ticker
        self.figure.xaxis.major_label_overrides = self.tick_label_map
        return True

    def figure_update(self, add_line):
        time_step = add_line[0]
        y = add_line[1]
        to_cds = dict(func_steps=[self.func_steps], ys=[y], time_steps=[time_step])
        if time_step > self.CDS.data['time_steps'][-1]:
            self.tick_label_map[self.func_steps] = str(time_step)
            self._update_xaxis()
        self.CDS.stream(to_cds)
        self.func_steps += 1
        return True


if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    import random
    random.seed(10)
    def example_data_1():
        data = []
        for i in range(3, 8):
            length = random.randint(1, 4)
            for j in range(length):
                data.append((i, random.randint(1, 50)))
        return data

    def main():
        from collections import namedtuple
        from enum import Enum, auto

        class Res(Enum):
            cloth = 1
            stuff = 2
            accessory = 3
            packaging = 4

        fig_indices = ("name", "title", "x_label", "y_label")

        FigureSpec = namedtuple("FigureSpec", fig_indices)

        figure_spec_1 = FigureSpec(Res.cloth, "title", "x_", "y_")

        output_file("../../bokeh_tmp/line.html")
        initial_data = example_data_1()
        Figure = IndividualFigure(initial_data, figure_spec_1, initial_func_count=123)
        last_time_step = initial_data[-1][0]
        Figure.figure_update((last_time_step, 12))
        Figure.figure_update((last_time_step+1, 24))

        layout_w = Figure.figure
        # curdoc().add_root(layout_w)
        show(layout_w)
    main()

# Expected Input: tuple(time_step, quantity)