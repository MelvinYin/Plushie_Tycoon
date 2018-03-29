from bokeh.models import Text
from bokeh.models.widgets import Button
from bokeh.models.plots import Plot
from bokeh.models import DataRange1d
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.widgets import RadioButtonGroup

from bokeh.plotting import output_file, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
import re

from collections import namedtuple


# TODO: eventually when parameters are pulled into a config file, spin TI and
# TODO: other individual widgets into their own separate class.
# TODO: variable names need to match as well.

class IndividualWidget:
    def __init__(self, widget_callback, specs):
        self.name = specs.name
        self.widget_callback = widget_callback
        self.widget_layout = self._widget_assemble(specs)

        self._input_val = None
        self._RBG_labels = specs.RBG_labels
        self._TI = self._set_TI(specs)
        self._header = self._set_header(specs)
        self._RBG = self._set_RBG(specs)
        self._button = self._set_button(specs)


    def _RBG_callback(self, active_button):
        # when resetting, RBG_callback is called through on_click, hence
        # ignore the None value.
        if self._RBG_labels[active_button].name == 'reset':
            self._RBG.active = None
        return

    def _set_RBG(self, specs):
        RBG = RadioButtonGroup()
        RBG.width = specs.RBG_intrinsic_dim[0]
        RBG.height = specs.RBG_intrinsic_dim[1]
        RBG.labels = [label.name for label in self._RBG_labels]
        RBG.active = None
        RBG.on_click(self._RBG_callback)
        return RBG

    def _text_callback(self, attr, old, new):
        self._input_val = new

    def _set_TI(self, specs):
        TI = TextInput()
        TI.width = specs.TI_intrinsic_dim[0]
        TI.height = specs.TI_intrinsic_dim[1]
        TI.placeholder = specs.TI_placeholder
        TI.on_change("value", self._text_callback)
        TI.title = None
        return TI

    def _button_callback(self):
        if not self._input_val:
            print("Value not set.")
        elif self._RBG.active is None:
            print("No category selected.")
        elif not re.fullmatch("[0-9]+", self._input_val.strip()):
            print("Invalid input value.")
        elif self._input_val.startswith("0"):
            print("Invalid input value.")
        else:
            self.widget_callback(tuple([self.name, (self._RBG_labels[self._RBG.active], int(self._input_val))]))
        return

    def _set_button(self, specs):
        button = Button()
        button.label = specs.button_label
        button.width = specs.button_intrinsic_dim[0]
        button.height = specs.button_intrinsic_dim[1]
        button.on_click(self._button_callback)
        return button

    def _set_header(self, specs):
        header = Plot()
        header.x_range = DataRange1d()
        header.y_range = DataRange1d()
        header.width = specs.text_intrinsic_dim[0]
        header.height = specs.text_intrinsic_dim[1]
        header.x_range = DataRange1d()
        header.toolbar.logo = None
        text_raw = dict(xs=[0], ys=[0], text=[specs.title])
        text_CDS = ColumnDataSource(data=text_raw)
        text = Text(x="xs", y="ys", text="text", text_align="center")
        header.add_glyph(text_CDS, text)
        return header

    def _widget_assemble(self, specs):
        TI_disp = row(self._TI, width=specs.TI_display_dim[0], height=specs.TI_display_dim[1])
        RBG_disp = row(self._RBG, width=specs.RBG_display_dim[0], height=specs.RBG_display_dim[1])
        header_disp = row(self._header, width=specs.text_display_dim[0], height=specs.text_display_dim[1])
        button_disp = row(self._button, width=specs.button_display_dim[0], height=specs.button_display_dim[1])
        TI_and_button = row(TI_disp, button_disp)
        widget_layout = column(header_disp, RBG_disp, TI_and_button)
        return widget_layout


class ButtonWidget:
    def __init__(self, widget_callback, specs):
        self.name = specs.name
        self.widget_callback = widget_callback
        self.widget_layout = self._widget_assemble(specs)

        self._RBG_labels = specs.RBG_labels
        self._header = self._set_header(specs)
        self._RBG = self._set_RBG(specs)
        self._button = self._set_button(specs)

    def _RBG_callback(self, active_button):
        # when resetting, RBG_callback is called through on_click, hence
        # ignore the None value.
        if self._RBG_labels[active_button].name == 'reset':
            self._RBG.active = None
        return

    def _set_RBG(self, specs):
        RBG = RadioButtonGroup()
        RBG.width = specs.RBG_intrinsic_dim[0]
        RBG.height = specs.RBG_intrinsic_dim[1]
        RBG.labels = [label.name for label in self._RBG_labels]
        RBG.active = None
        RBG.on_click(self._RBG_callback)
        return RBG

    def _button_callback(self):
        if self._RBG.active is None:
            print("No category selected.")
        else:
            self.widget_callback((self._RBG_labels[self._RBG.active],))
        return

    def _set_button(self, specs):
        button = Button()
        button.label = specs.button_label
        button.width = specs.button_intrinsic_dim[0]
        button.height = specs.button_intrinsic_dim[1]
        button.on_click(self._button_callback)
        return button

    def _set_header(self, specs):
        header = Plot()
        header.x_range = DataRange1d()
        header.y_range = DataRange1d()
        header.width = specs.text_intrinsic_dim[0]
        header.height = specs.text_intrinsic_dim[1]
        header.x_range = DataRange1d()
        header.toolbar.logo = None
        text_raw = dict(xs=[0], ys=[0], text=[specs.title])
        text_CDS = ColumnDataSource(data=text_raw)
        text = Text(x="xs", y="ys", text="text", text_align="center")
        header.add_glyph(text_CDS, text)
        return header

    def _widget_assemble(self, specs):
        RBG_disp = row(self._RBG, width=specs.RBG_display_dim[0], height=specs.RBG_display_dim[1])
        header_disp = row(self._header, width=specs.text_display_dim[0], height=specs.text_display_dim[1])
        button_disp = row(self._button, width=specs.button_display_dim[0], height=specs.button_display_dim[1])
        widget_layout = column(header_disp, RBG_disp, button_disp)
        return widget_layout


# if __name__ == "__main__":
#     output_file("../../bokeh_tmp/line.html")
#     figure_set = IndividualWidget().widget_set
#     show(figure_set)

# For testing



if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    from collections import namedtuple
    import sys
    import os
    sys.path.append(os.getcwd().rsplit("\\", 1)[0])
    from defaults import widget_ispecs_1, widget_ispecs_6, widget_gspecs

    def widget_callback(command_to_run):
        print("from widget callback")
        print(command_to_run)
        return

    MergedSpec = namedtuple("widget_spec", widget_ispecs_1._fields + widget_gspecs._fields)
    merged_spec_1 = MergedSpec(*(widget_ispecs_1 + widget_gspecs))
    merged_spec_2 = MergedSpec(*(widget_ispecs_6 + widget_gspecs))

    output_file("../../bokeh_tmp/line.html")

    widget_1 = IndividualWidget(widget_callback, merged_spec_1)
    widget_2 = ButtonWidget(widget_callback, merged_spec_2)

    widget_1.widget_callback((merged_spec_1.name, (merged_spec_1.RBG_labels[0], 10)))
    widget_2.widget_callback(
        (merged_spec_2.name, (merged_spec_2.RBG_labels[0], 10)))
    widget_2._button_callback()

    layout_w1 = widget_1.widget_layout
    layout_w2 = widget_2.widget_layout
    show(row(layout_w1, layout_w2))
    curdoc().add_root(row(layout_w1, layout_w2))

# Expected output: tuple(<Func.something>, <Res.something>, int of quantity)
