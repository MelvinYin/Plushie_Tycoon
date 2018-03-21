from bokeh.models import DataRange1d

from bokeh.models.tickers import AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import HoverTool, BoxZoomTool, PanTool, WheelZoomTool, \
    ResetTool, UndoTool
import math
from bokeh.layouts import row, column
import time

from widgets import WholeWidgetSet
from figures import WholeFigSet
from bokeh.plotting import output_file, show, curdoc
from bokeh.layouts import column

from bokeh.models import Text
from bokeh.models.widgets import Button
from bokeh.models.plots import Plot
from bokeh.models import DataRange1d
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.widgets import RadioButtonGroup

from bokeh.plotting import output_file, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
import re
import sys

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


class IndiWidgetSet:
    def __init__(self):
        self.set_title = "1Placeholder"
        self.button_label = "place"
        self.TI_placeholder = "Placeholder"
        self.RBG_labels = ["one", "two", "three", "reset", "quit"]
        self.RBG_active = None
        self.text_intrinsic_dim = [250, 50] # width, height of text box
        self.text_display_dim = [0, 40] # text width no diff, height determine how near RBG is.

        # CBG_intrinsic makes no diff
        self.RBG_display_dim = [0, 40]  # width no diff, height determine how close input and button is

        self.TI_intrinsic_dim = [1, 1]  # size of text_box, with a minimum
        self.TI_display_dim = [180, 0] # for width, fix overall widget width together with button_display_dim, min taken of the 2.

        self.button_intrinsic_dim = [50, 0]    # no diff for now
        self.button_display_dim = [100, 0]      # no diff for now

        self.input_val = None
        self.active_RBG = None

        self.TI = TextInput()
        self.header = Plot()
        self.RBG = RadioButtonGroup()
        self.button = Button()

        self.set_TI()
        self.set_header()
        self.set_RBG()
        self.set_button()

        self.widget_set = self.widget_assemble()

    def set_RBG(self):
        self.RBG.labels = self.RBG_labels
        self.RBG.active = self.RBG_active
        self.RBG.on_click(self.RBG_callback)
        return

    def RBG_callback(self, active_button):
        # when resetting, RBG_callback is called through on_click, hence
        # ignore the None value.
        if not active_button:
            return
        if self.RBG_labels[active_button] == "quit":
            sys.exit()
        if self.RBG_labels[active_button] == "reset":
            self.active_RBG = None
            self.RBG.active = None
        else:
            self.active_RBG = self.RBG_labels[active_button]

    def set_TI(self):
        self.TI.width = self.TI_intrinsic_dim[0]
        self.TI.height = self.TI_intrinsic_dim[1]
        self.TI.placeholder = self.TI_placeholder
        self.TI.on_change("value", self.text_callback)
        self.TI.title = None
        return

    def text_callback(self, attr, old, new):
        self.input_val = new

    def button_callback(self):
        # if not self.input_val:
        #     print("Value not set.")
        # elif not self.active_RBG:
        #     print("No category selected.")
        # elif not re.fullmatch("[0-9]+", self.input_val):
        #     print("Invalid input value.")
        # else:
        #     print(tuple([self.set_title, self.active_RBG, self.input_val]))
        data_to_append = dict()
        data_to_append["xs"] = [1, 2]
        data_to_append["ys"] = [1, 2]
        data_to_append["time_steps_for_hover"] = [8, 8]

        fig_class.CDS.stream(data_to_append)

        return

    def set_header(self):
        self.header.x_range = DataRange1d()
        self.header.y_range = DataRange1d()
        self.header.width = self.text_intrinsic_dim[0]
        self.header.height = self.text_intrinsic_dim[1]
        self.header.x_range = DataRange1d()
        self.header.toolbar.logo = None
        text_raw = dict(xs=[0], ys=[0], text=[self.set_title])
        text_CDS = ColumnDataSource(data=text_raw)
        text = Text(x="xs", y="ys", text="text", text_align="center")
        self.header.add_glyph(text_CDS, text)
        return

    def set_button(self):
        self.button.label = self.button_label
        self.button.width = self.button_intrinsic_dim[0]
        self.button.height = self.button_intrinsic_dim[1]
        self.button.on_click(self.button_callback)
        return

    def widget_assemble(self):
        TI_disp = row(self.TI, width=self.TI_display_dim[0], height=self.TI_display_dim[1])
        RBG_disp = row(self.RBG, width=self.RBG_display_dim[0], height=self.RBG_display_dim[1])
        header_disp = row(self.header, width=self.text_display_dim[0], height=self.text_display_dim[1])
        button_disp = row(self.button, width=self.button_display_dim[0], height=self.button_display_dim[1])
        TI_and_button = row(TI_disp, button_disp)
        self.widget_set = column(header_disp, RBG_disp, TI_and_button)
        return self.widget_set


output_file("../../bokeh_tmp/line.html")
fig_class = IndiFigure(gen_raw_input_data_1())
widget_class = IndiWidgetSet()
layout = column(fig_class.fig, widget_class.widget_set)
# show(fig)
curdoc().add_root(layout)


# print("ewiufgfguierfbfuie")
# time.sleep(20)
# data_to_append = dict()
# data_to_append["xs"] = [1,2]
# data_to_append["ys"] = [1,2]
# data_to_append["time_steps_for_hover"] = [8, 8]
#
# fig_class.CDS.stream(data_to_append)
# print("bfuie")
# time.sleep(20)