from bokeh.models import Text
from bokeh.models.widgets import Button
from bokeh.models.plots import Plot
from bokeh.models import DataRange1d
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.widgets import RadioButtonGroup

from bokeh.models.tickers import AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import HoverTool, BoxZoomTool, PanTool, WheelZoomTool, \
    ResetTool, UndoTool
import math
from bokeh.layouts import row, column
import re
import sys

output_file("../bokeh_tmp/line.html")
# TODO: each set of widgets need to be considered as a separate class, for callback and final output of results to GE to make sense, and for it to scale.
# TODO: need a quit button
# WIDGETS

class WidgetSet:
    def __init__(self):
        self.set_title = "1Placeholder"
        self.button_label = "place"
        self.TI_placeholder = "Placeholder"
        self.RBG_labels = ["one", "two", "three", "reset", "quit"]
        self.RBG_active = None
        self.text_intrinsic_dim = [300, 50]
        self.text_display_dim = [200, 40]

        # CBG_intrinsic makes no diff
        self.RBG_display_dim = [100, 40]

        self.TI_intrinsic_dim = [1, 1]
        self.TI_display_dim = [190, 50]

        self.button_intrinsic_dim = [50, 50]    # no diff for now
        self.button_display_dim = [50, 50]      # no diff for now

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
        if not self.input_val:
            print("Value not set.")
        elif not self.active_RBG:
            print("No category selected.")
        elif not re.fullmatch("[0-9]+", self.input_val):
            print("Invalid input value.")
        else:
            print(tuple([self.active_RBG, self.input_val]))
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

layout1 = WidgetSet().widget_set
# show(layout1)
curdoc().add_root(layout1)