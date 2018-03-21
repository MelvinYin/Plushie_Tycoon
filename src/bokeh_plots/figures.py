from bokeh.models import DataRange1d

from bokeh.models.tickers import AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import HoverTool, BoxZoomTool, PanTool, WheelZoomTool, \
    ResetTool, UndoTool
import math
from bokeh.layouts import row, column

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
        self.CDS = self.convert_to_CDS(self.raw_data)
        self.x_axis_label = "Time Steps"
        self.y_axis_label = "Placeholder"
        self.plot_title = "2Placeholder"
        self.x_range = DataRange1d(follow="end", follow_interval=3)
        self.y_range = DataRange1d(range_padding=0.3)
        self.x_axis_ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
        self.fig = self.gen_default_fig()
        self.gen_fig()

    def convert_to_CDS(self, data_to_convert):
        xs = []
        ys = []
        print("Convert to CDS")
        print(type(data_to_convert))
        time_steps = list(data_to_convert.keys())
        values = list(data_to_convert.values())
        for j in range(len(time_steps)):
            xs += [int(time_steps[j]) + i/len(values[j]) for i in range(len(values[j]))]
            ys += values[j]
        time_steps_for_hover = [math.floor(i) for i in xs]
        tmp = dict(xs=xs, ys=ys, time_steps_for_hover=time_steps_for_hover)
        x = ColumnDataSource(data=tmp)
        print("Conversion complete.\n")
        return x

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
        self.fig.x("xs", "ys", source=self.CDS, name="points", size=10)
        self.fig.line("xs", "ys", source=self.CDS)
        return

    def ind_fig_update(self, raw_input):
        print("Fig update")
        print(raw_input)
        self.CDS.stream(raw_input)
        print(self.CDS.data)
        print("\n")

        # CDS_addition = self.convert_to_CDS(raw_input)

        return True

class WholeFigSet:
    def __init__(self):
        self.IndiFigure = IndiFigure
        self.disp_dim = [100, 100]

        self.p1 = self.IndiFigure(gen_raw_input_data_1())
        self.p2 = self.IndiFigure(gen_raw_input_data_1())
        self.p3 = self.IndiFigure(gen_raw_input_data_2())
        self.p4 = self.IndiFigure(gen_raw_input_data_2())
        self.p5 = self.IndiFigure(gen_raw_input_data_2())
        self.p6 = self.IndiFigure(gen_raw_input_data_1())

        self.full_fig_set = self.get_figure_set()
        self.couple_range()
        self.get_figure_set()

    def couple_range(self):
        self.p2.fig.x_range = self.p1.fig.x_range
        self.p3.fig.x_range = self.p1.fig.x_range
        self.p4.fig.x_range = self.p1.fig.x_range
        self.p5.fig.x_range = self.p1.fig.x_range
        self.p6.fig.x_range = self.p1.fig.x_range
        return True

    def get_figure_set(self):
        layout1 = row(self.p1.fig, self.p2.fig, self.p3.fig)
        layout2 = row(self.p4.fig, self.p5.fig, self.p6.fig)
        self.full_fig_set = column(layout1, layout2)
        return

    def fig_update(self, data_to_add):
        fig_label = data_to_add[0]
        data_to_add = data_to_add[1]
        if fig_label == "p1":
            self.p1.ind_fig_update(data_to_add)
        # elif fig_label == "p2":
            self.p2.ind_fig_update(data_to_add)
        # elif fig_label == "p3":
            self.p3.ind_fig_update(data_to_add)
        # elif fig_label == "p4":
            self.p4.ind_fig_update(data_to_add)
        # elif fig_label == "p5":
            self.p5.ind_fig_update(data_to_add)
        # elif fig_label == "p6":
            self.p6.ind_fig_update(data_to_add)
        else:
            print("Wrong figure label")
            raise Exception
        return True

if __name__ == "__main__":
    output_file("../../bokeh_tmp/line.html")
    full_fig_set = WholeFigSet().full_fig_set

    show(full_fig_set)
    # curdoc().add_root(layout_)