from bokeh.models import Text
from bokeh.models.widgets import Button
from bokeh.models.plots import Plot
from bokeh.models import DataRange1d
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.widgets import RadioButtonGroup

from bokeh.plotting import output_file, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
import sys
import re
sys.path.append("../")
import defaults
from defaults import widget_gspecs


# TODO: eventually when parameters are pulled into a config file, spin TI and
# TODO: other individual widgets into their own separate class.
# TODO: variable names need to match as well.

class IndividualWidget:
    def __init__(self, widget_callback, specs):
        self.title = specs.title
        self.name = specs.name
        self.button_label = specs.button_label
        self.TI_placeholder = specs.TI_placeholder
        self.RBG_labels = specs.RBG_labels
        self.RBG_active = None
        self.widget_callback = widget_callback

        self.input_val = None
        self.active_RBG = None

        self.text_intrinsic_dim = widget_gspecs.text_intrinsic_dim
        self.text_display_dim = widget_gspecs.text_display_dim

        self.RBG_intrinsic_dim = widget_gspecs.RBG_intrinsic_dim
        self.RBG_display_dim = widget_gspecs.RBG_display_dim

        self.TI_intrinsic_dim = widget_gspecs.TI_intrinsic_dim
        self.TI_display_dim = widget_gspecs.TI_display_dim

        self.button_intrinsic_dim = widget_gspecs.button_intrinsic_dim
        self.button_display_dim = widget_gspecs.button_display_dim

        self.TI = self._set_TI()
        self.header = self._set_header()
        self.RBG = self._set_RBG()
        self.button = self._set_button()

        self.widget_layout = self._widget_assemble()

    def _RBG_callback(self, active_button):
        # when resetting, RBG_callback is called through on_click, hence
        # ignore the None value.
        if not active_button:
            return
        if self.RBG_labels[active_button] == "quit":
            sys.exit()  # TODO: modified eventually
        if self.RBG_labels[active_button] == "reset":
            self.active_RBG = None
            self.RBG.active = None
        else:
            self.active_RBG = self.RBG_labels[active_button]

    def _set_RBG(self):
        RBG = RadioButtonGroup()
        RBG.width = self.RBG_intrinsic_dim[0]
        RBG.height = self.RBG_intrinsic_dim[1]
        RBG.labels = [label.name for label in self.RBG_labels]
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
        elif not re.fullmatch("[0-9]+", self.input_val.strip()):
            print("Invalid input value.")
        elif self.input_val.startswith("0"):
            print("Invalid input value.")
        else:
            self.widget_callback(tuple([self.name, self.active_RBG, int(self.input_val)]))
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
        widget_layout = column(header_disp, RBG_disp, TI_and_button)
        return widget_layout


# if __name__ == "__main__":
#     output_file("../../bokeh_tmp/line.html")
#     figure_set = IndividualWidget().widget_set
#     show(figure_set)

# For testing



if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    def main():
        from collections import namedtuple
        from enum import Enum, auto
        class Func(Enum):
            buy_res = auto()
            sell_res = auto()
            buy_prod = auto()
            make_prod = auto()
            sell_prod = auto()
            show_stats = auto()
            show_prices = auto()
            save = auto()
            load = auto()
            quit = auto()
            save_quit = auto()
            next_turn = auto()
            show_history = auto()
            back = auto()
            start = auto()

        class Res(Enum):
            cloth = 1
            stuff = 2
            accessory = 3
            packaging = 4

        class Others(Enum):
            reset = auto()

        widget_iindices = ["name", "title", "button_label", "TI_placeholder",
                           "RBG_labels"]
        WidgetIspecs = namedtuple("WidgetIspecs", widget_iindices)
        widget_ispecs_1 = WidgetIspecs(
            name=Func.buy_res,
            title="buy_res",
            button_label="buy",
            TI_placeholder="Placeholder",
            RBG_labels=list(Res) + [Others.reset])

        def widget_callback(command_to_run):
            print("from widget callback")
            print(command_to_run)
            return

        output_file("../../bokeh_tmp/line.html")
        layout_w = IndividualWidget(widget_callback, widget_ispecs_1).widget_layout
        curdoc().add_root(layout_w)
        # show(layout_w)
    main()

# Expected output: tuple(<Func.something>, <Res.something>, int of quantity)
