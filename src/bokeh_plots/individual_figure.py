from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import DataRange1d, HoverTool, BoxZoomTool, PanTool, \
    WheelZoomTool, ResetTool, UndoTool
from bokeh.models.tickers import FixedTicker
import random

# TODO: change in architecture: IF need to receive an ordered list of tuple,
# TODO: with first element as time_step, second as func_step, third as
# TODO: value at that func_step. This allows growth later on, for perhaps
# TODO: an additional arg-msg at the end of the tuple.

# TODO: need a initialisation call, and a update call.
# TODO: actually, hmm try not to merge the two. Might slow down when loading
# TODO: game.

"""
Only data that needs to be reflected in graph or hover, should be in CDS.

self.current_ticks need to be pulled out, because figure.xaxis.ticker cannot 
be retrieved.

Keeping func_steps for now in case of future changes.
"""



class IndividualFigure:
    def __init__(self, initial_data, specs):
        self.initial_data = initial_data
        self.specs = specs
        self.CDS = self._create_initial_CDS()

        self.current_ticks = self._get_initial_ticks()

        self.figure = self._set_initial_figure()
        self._update_xaxis()

    def _create_initial_CDS(self):
        """
        Dict sent to CDS should have list instead of tuple as values, otherwise
        CDS.stream will fail.
        """
        time_steps, func_steps, ys = zip(*self.initial_data)
        to_CDS = dict(func_steps=list(func_steps), ys=list(ys), time_steps=list(time_steps))
        CDS = ColumnDataSource(data=to_CDS)
        return CDS

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

        p.x_range = DataRange1d(follow="end", follow_interval=3)
        p.y_range = DataRange1d(follow="end", range_padding=0.3)

        initial_ticks = self._get_initial_ticks()
        ticker = FixedTicker(ticks=initial_ticks)
        p.xaxis.ticker = ticker
        p.xgrid.ticker = ticker

        p.xaxis.major_label_overrides = self._get_xaxis_labels()

        p.title.text = self.specs.title
        p.title.align = 'center'
        p.xaxis.axis_label = self.specs.x_label
        p.yaxis.axis_label = self.specs.y_label
        p.x("func_steps", "ys", source=self.CDS, name="x", size=10)
        p.line("func_steps", "ys", source=self.CDS)
        return p

    def _get_initial_ticks(self):   # assuming time_step has more than 1???
        time_steps = self.CDS.data["time_steps"]
        func_steps = self.CDS.data["func_steps"]
        prev_time_step = time_steps[0]
        ticks = [prev_time_step]
        for i in range(len(time_steps)):
            if time_steps[i] == prev_time_step:
                continue
            prev_time_step = time_steps[i]
            ticks.append(func_steps[i])
        return ticks

    def _get_xaxis_labels(self):
        ticks = self.current_ticks
        mapping = dict([(ticks[i], str(i)) for i in range(len(ticks))])
        return mapping

    def _update_xaxis(self):
        ticks = self.current_ticks
        ticks.append(self.CDS.data['func_steps'][-1])
        ticker = FixedTicker(ticks=ticks)
        self.figure.xaxis.ticker = ticker
        self.figure.xgrid.ticker = ticker
        xaxis_labels = self._get_xaxis_labels()
        self.figure.xaxis.major_label_overrides = xaxis_labels
        return True

    def figure_update(self, add_line):
        time_step = add_line[0]
        func_step = add_line[1]
        y = add_line[2]
        to_cds = dict(func_steps=[func_step], ys=[y], time_steps=[time_step])
        self.CDS.stream(to_cds)
        if time_step > self.CDS.data['time_steps'][-2]:
            self._update_xaxis()
        return True


if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    random.seed(10)
    def example_data_1():
        data = []
        for i in range(5):
            length = random.randint(1, 4)
            for j in range(length):
                data.append((i, len(data), random.randint(1, 50)))
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
        Figure = IndividualFigure(initial_data, figure_spec_1)
        last_time_step = initial_data[-1][0]
        last_func_step = initial_data[-1][1]
        Figure.figure_update((last_time_step, last_func_step+1, 12))
        Figure.figure_update((last_time_step+1, last_func_step + 2, 24))


        layout_w = Figure.figure
        # curdoc().add_root(layout_w)
        show(layout_w)
    main()

# Expected output: tuple(<Func.something>, <Res.something>, int of quantity)