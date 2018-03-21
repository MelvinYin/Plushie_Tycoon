from bokeh.models import DataRange1d

from bokeh.models.tickers import AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import HoverTool, BoxZoomTool, PanTool, WheelZoomTool, \
    ResetTool, UndoTool
import math
from bokeh.layouts import row, column

# TODO: create individual plot class first, then create one that merge them all?

def gen_raw_input_data_1():
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

def gen_raw_input_data_2():
    data = dict()
    data[0] = [1, 2]
    data[1] = [2, 3, 2]
    data[2] = [3]
    data[3] = [2, 1]
    data[4] = [1,5]
    data[5] = [6, 6]
    data[6] = [7, 2]
    data[7] = [2]
    return data

class IndiFigure:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.CDS = self.convert_to_CDS()
        self.x_axis_label = "Time Steps"
        self.y_axis_label = "Placeholder"
        self.plot_title = "2Placeholder"
        self.x_range = DataRange1d(follow="end", follow_interval=3)
        self.y_range = DataRange1d(range_padding=0.3)
        self.x_axis_ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
        self.fig = self.gen_fig()


    def convert_to_CDS(self):
        xs = []
        ys = []
        for time_steps, values in self.raw_data.items():
            xs += [int(time_steps) + i/len(values) for i in range(len(values))]
            ys += values
        time_steps_for_hover = [math.floor(i) for i in xs]
        tmp = dict(xs=xs, ys=ys, time_steps_for_hover=time_steps_for_hover)
        return ColumnDataSource(data=tmp)

    def gen_default_fig(self):
        hover = HoverTool(tooltips=[
            ("Point No.", "$index"),
            ("Time Step", "@time_steps_for_hover")],
            names=["points", "points2"])

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

        p.xaxis.ticker = self.x_axis_ticker
        p.xgrid.ticker = self.x_axis_ticker
        p.title.text = self.plot_title
        p.title.align = 'center'
        p.xaxis.axis_label = self.x_axis_label
        p.yaxis.axis_label = self.y_axis_label
        return p

    def gen_fig(self):
        p = self.gen_default_fig()
        p.x("xs", "ys", source=self.CDS, name="points", size=10)
        p.line("xs", "ys", source=self.CDS)
        return p

class WholeFigSet:
    def __init__(self):
        self.IndiFigure = IndiFigure
        self.disp_dim = [100, 100]
        self.full_fig_set = self.get_figure_set()

    def couple_range(self, *args):
        p1 = args[0]
        return_p = [p1]
        for p in args[1:]:
            p.x_range = p1.x_range
            return_p.append(p)
        return return_p

    def get_figure_set(self):
        p1 = self.IndiFigure(gen_raw_input_data_1()).fig
        p2 = self.IndiFigure(gen_raw_input_data_1()).fig
        p3 = self.IndiFigure(gen_raw_input_data_2()).fig
        p4 = self.IndiFigure(gen_raw_input_data_2()).fig
        p5 = self.IndiFigure(gen_raw_input_data_2()).fig
        p6 = self.IndiFigure(gen_raw_input_data_1()).fig
        p1, p2, p3, p4, p5, p6 = self.couple_range(p1, p2, p3, p4, p5, p6)

        layout1 = row(p1, p2, p3)
        layout2 = row(p4, p5, p6)
        full_fig_set = column(layout1, layout2)
        return full_fig_set

if __name__ == "__main__":
    output_file("../../bokeh_tmp/line.html")
    full_fig_set = WholeFigSet().full_fig_set

    show(full_fig_set)
    # curdoc().add_root(layout_)