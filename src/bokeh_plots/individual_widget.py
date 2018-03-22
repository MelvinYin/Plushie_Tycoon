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
sys.path.append("../")
import defaults
from defaults import widget_gspecs


# TODO: eventually when parameters are pulled into a config file, spin TI and
# TODO: other individual widgets into their own separate class.
# TODO: variable names need to match as well.

class IndividualWidget:
    def __init__(self, specs, widget_callback):
        self.title = specs.title
        self.button_label = specs.button_label
        self.TI_placeholder = specs.TI_placeholder
        self.RBG_labels = specs.RBG_labels
        self.RBG_active = None
        self.w_callback = widget_callback

        self.input_val = None
        self.active_RBG = None

        self.text_intrinsic_dim = widget_gspecs.text_intrinsic_dim
        self.text_display_dim = widget_gspecs.text_display_dim

        # CBG_intrinsic makes no diff
        self.RBG_display_dim = widget_gspecs.RBG_display_dim

        self.TI_intrinsic_dim = widget_gspecs.TI_intrinsic_dim
        self.TI_display_dim = widget_gspecs.TI_display_dim

        self.button_intrinsic_dim = widget_gspecs.button_intrinsic_dim
        self.button_display_dim = widget_gspecs.button_display_dim

        self.TI = self._set_TI()
        self.header = self._set_header()
        self.RBG = self._set_RBG()
        self.button = self._set_button()

        self.widget = self._widget_assemble()

    def _RBG_callback(self, active_button):
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

    def _set_RBG(self):
        RBG = RadioButtonGroup()
        RBG.labels = self.RBG_labels
        RBG.active = self.RBG_active
        RBG.on_click(self._RBG_callback)
        return RBG

    def _text_callback(self, attr, old, new):
        self.input_val = new

    def _set_TI(self):
        TI = TextInput()
        TI.width = self.TI_intrinsic_dim[0]
        TI.height = self.TI_intrinsic_dim[1]
        TI.placeholder = self.TI_placeholder
        TI.on_change("value", self._text_callback)
        TI.title = None
        return TI

    def _button_callback(self):
        if not self.input_val:
            print("Value not set.")
        elif not self.active_RBG:
            print("No category selected.")
        elif not re.fullmatch("[0-9]+", self.input_val):
            print("Invalid input value.")
        else:
            print(tuple([self.title, self.active_RBG, self.input_val]))
            self.w_callback(tuple([self.title, self.active_RBG, self.input_val]))
        return

    def _set_button(self):
        button = Button()
        button.label = self.button_label
        button.width = self.button_intrinsic_dim[0]
        button.height = self.button_intrinsic_dim[1]
        button.on_click(self._button_callback)
        return button

    def _set_header(self):
        header = Plot()
        header.x_range = DataRange1d()
        header.y_range = DataRange1d()
        header.width = self.text_intrinsic_dim[0]
        header.height = self.text_intrinsic_dim[1]
        header.x_range = DataRange1d()
        header.toolbar.logo = None
        text_raw = dict(xs=[0], ys=[0], text=[self.title])
        text_CDS = ColumnDataSource(data=text_raw)
        text = Text(x="xs", y="ys", text="text", text_align="center")
        header.add_glyph(text_CDS, text)
        return header

    def _widget_assemble(self):
        TI_disp = row(self.TI, width=self.TI_display_dim[0], height=self.TI_display_dim[1])
        RBG_disp = row(self.RBG, width=self.RBG_display_dim[0], height=self.RBG_display_dim[1])
        header_disp = row(self.header, width=self.text_display_dim[0], height=self.text_display_dim[1])
        button_disp = row(self.button, width=self.button_display_dim[0], height=self.button_display_dim[1])
        TI_and_button = row(TI_disp, button_disp)
        widget = column(header_disp, RBG_disp, TI_and_button)
        return widget


# if __name__ == "__main__":
#     output_file("../../bokeh_tmp/line.html")
#     figure_set = IndividualWidget().widget_set
#     show(figure_set)