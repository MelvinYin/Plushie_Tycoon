from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import DataRange1d, HoverTool, BoxZoomTool, PanTool, \
    WheelZoomTool, ResetTool, UndoTool
from bokeh.models.tickers import AdaptiveTicker
import math
import sys
sys.path.append("../")
import defaults
def example_data_1():
    data = dict()
    data[0] = [1,13, 23]
    data[1] = [23]
    data[2] = [34,23, 34]
    data[3] = [2]
    data[4] = [1,13, 23]
    data[5] = [23]
    data[6] = [34,23, 34]
    data[7] = [2]
    return data

def convert_to_desired_format(data):
    xs = []
    ys = []
    for time_steps, values in data.items():
        xs += [int(time_steps) + i / len(values) for i in
               range(len(values))]
        ys += values
    time_steps_for_hover = [math.floor(i) for i in xs]
    converted = dict(xs=xs, ys=ys, time_steps_for_hover=time_steps_for_hover)
    return converted

def convert_to_CDS(data):
    data_formatted = convert_to_desired_format(data)
    CDS = ColumnDataSource(data=data_formatted)
    return CDS


class IndividualFigure:
    def __init__(self, raw_data, specs):
        self.CDS = convert_to_CDS(raw_data)
        self.x_label = specs.x_label
        self.y_label = specs.y_label
        self.title = specs.title
        self.name = specs.name
        self.x_range = DataRange1d(follow="end", follow_interval=3)
        self.y_range = DataRange1d(follow="end", range_padding=0.3)
        self.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
        self.hover = HoverTool(
            tooltips=[("Point No.", "$index"),
                      ("Time Step", "@time_steps_for_hover")],
            names=["x", "points2"])

        self.figure = self._figure_config()
        self._plot()

    def _figure_config(self):
        hover = self.hover

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

        p.xaxis.ticker = self.ticker
        p.xgrid.ticker = self.ticker
        p.title.text = self.title
        p.title.align = 'center'
        p.xaxis.axis_label = self.x_label
        p.yaxis.axis_label = self.y_label
        return p

    def _plot(self):
        self.figure.x("xs", "ys", source=self.CDS, name="x", size=10)
        self.figure.line("xs", "ys", source=self.CDS)
        return True

    def figure_update(self, data_to_add):
        """
        Format: data_to_add, a dict with time_
        steps as key and new value of plot as value.
        """
        formatted_to_add = convert_to_desired_format(data_to_add)
        self.CDS.stream(formatted_to_add)
        return True



if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    def main():
        from collections import namedtuple
        from enum import Enum, auto
        def example_data_1():
            data = dict()
            data[0] = [1, 13, 23]
            data[1] = [23]
            data[2] = [34, 23, 34]
            data[3] = [2]
            data[4] = [1, 13, 23]
            data[5] = [23]
            data[6] = [34, 23, 34]
            data[7] = [2]
            return data

        class Res(Enum):
            cloth = 1
            stuff = 2
            accessory = 3
            packaging = 4

        fig_indices = ("name", "title", "x_label", "y_label")

        FigureSpec = namedtuple("FigureSpec", fig_indices)

        figure_spec_1 = FigureSpec(Res.cloth, "title", "x_", "y_")

        output_file("../../bokeh_tmp/line.html")
        Figure = IndividualFigure(example_data_1(), figure_spec_1)
        layout_w = Figure.figure
        # curdoc().add_root(layout_w)
        show(layout_w)
    main()

# Expected output: tuple(<Func.something>, <Res.something>, int of quantity)


if __name__ == "__main__":
    output_file("../../bokeh_tmp/line.html")
    figure_set = IndividualFigure(example_data_1(), defaults.figure_spec_1).figure

    show(figure_set)
    # curdoc().add_root(layout_)

# TODO: first, try changing axis tick labels such that 1, 2, etc can be displayed
# TODO: at non-1, non02 po