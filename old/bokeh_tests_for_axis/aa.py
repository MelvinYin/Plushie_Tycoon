from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import DataRange1d, HoverTool, BoxZoomTool, PanTool, \
    WheelZoomTool, ResetTool, UndoTool, FactorRange, Range1d, CategoricalScale, CategoricalAxis, CategoricalTicker, ContinuousTicker
from bokeh.models.tickers import AdaptiveTicker, FixedTicker
import math
import sys
sys.path.append("../")
import defaults
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

def convert_to_desired_format(data):
    xs = []
    ys = []
    time_steps_for_hover = []
    zs = []
    counter = 0
    for time_steps, values in data.items():
        xs += [int(time_steps) + i / len(values) for i in
               range(len(values))]
        ys += values
        zs += list(range(counter, counter + len(values)))
        counter += len(values)
        time_steps_for_hover += [time_steps for _ in range(len(values))]
    converted = dict(xs=xs, ys=ys, zs=zs, time_steps_for_hover=time_steps_for_hover)
    return converted


class IndividualFigure:
    def __init__(self, raw_data, specs):
        self.data_formatted = convert_to_desired_format(raw_data)
        self.CDS = ColumnDataSource(data=self.data_formatted)
        self.time_steps_for_hover = list(set([str(i) for i in self.data_formatted['time_steps_for_hover']]))
        self.x_label = specs.x_label
        self.y_label = specs.y_label
        self.title = specs.title
        self.name = specs.name
        # self.x_range = DataRange1d(follow="end", follow_interval=3)
        # self.y_range = DataRange1d(follow="end", range_padding=0.3)
        # self.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
        self.ticker = FixedTicker(ticks=[0, 1, 2])
        # self.ticker.themed_values(values=[str(i) for i in range(6)])
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
        x = FactorRange(factors=['a13123123', 'b123123123','c'])
        # p = figure(x_range=x, plot_width=400, plot_height=400, tools=tools)
        p = figure(plot_width=400, plot_height=400, tools=tools)
        p.toolbar.active_drag = pan
        p.toolbar.active_scroll = wheelzoom
        p.toolbar.active_tap = None
        p.toolbar.active_inspect = hover
        p.toolbar.logo = None
        # p.x_range=FactorRange(factors=['a13123123', 'b123123123',""])
        # p.xaxis.major_tick_line_color = None
        dict_ = dict()
        dict_
        p.xaxis.major_label_overrides=dict_

        p.xaxis.ticker = FixedTicker(ticks=[0, 1])
        # print(p.xaxis)
        # print(dir(p.xaxis))
        # print(getattr(p.xaxis, "ticker"))
        # print(p.xaxis.__properties__)
        # print(*[str(i) for i in self.data_formatted['time_steps_for_hover']])

        # p.x_range = FactorRange(*[str(i) for i in self.data_formatted['time_steps_for_hover']])
        # p.x_range = FactorRange(
        #     *self.time_steps_for_hover)
        p.xgrid.ticker = FixedTicker(ticks=[0, 1, 2, 7])
        p.title.text = self.title
        p.title.align = 'center'
        p.xaxis.axis_label = self.x_label
        p.yaxis.axis_label = self.y_label
        return p

    def _plot(self):
        self.figure.x("zs", "ys", source=self.CDS, name="x", size=10)
        self.figure.line("zs", "ys", source=self.CDS)
        return True

    def figure_update(self, data_to_add):
        """
        Format: data_to_add, a dict with time_
        steps as key and new value of plot as value.
        """
        formatted_to_add = convert_to_desired_format(data_to_add)
        self.CDS.stream(formatted_to_add)
        return True


# Expected output: tuple(<Func.something>, <Res.something>, int of quantity)


if __name__ == "__main__":
    output_file("../../bokeh_tmp/line.html")
    figure_set = IndividualFigure(example_data_1(), defaults.figure_spec_1).figure

    show(figure_set)
    # curdoc().add_root(layout_)

# TODO: first, try changing axis tick labels such that 1, 2, etc can be displayed
# TODO: at non-1, non-2 positions.