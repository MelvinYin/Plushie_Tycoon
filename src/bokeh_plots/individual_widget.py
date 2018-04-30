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


class ButtonComponent:
    def __init__(self, specs, widget_callback):
        self.widget_callback = widget_callback
        self.widget = self._set_button(specs)

    def _set_button(self, specs):
        button = Button()
        button.label = specs.button_label
        button.width = specs.button_intrinsic_width
        button.height = specs.button_intrinsic_height
        button.on_click(self.widget_callback)
        return button

class RBGComponent:
    def __init__(self, specs, widget_callback=None):
        if not widget_callback:
            self.widget_callback = self._default_RBG_callback
        else:
            self.widget_callback = widget_callback
        self._RBG_labels = specs.RBG_labels
        self.widget = self._set_RBG(specs)

    def _set_RBG(self, specs):
        RBG = RadioButtonGroup()
        RBG.width = specs.RBG_intrinsic_width
        RBG.height = specs.RBG_intrinsic_height
        RBG.labels = [label.name for label in self._RBG_labels]
        RBG.active = None
        RBG.on_click(self.widget_callback)
        return RBG

    def _default_RBG_callback(self, active_button):
        """
        Bokeh RBG on_click triggers, when RBG value has changed, not when it
        is clicked. Hence, when setting self._RBG.active, _RBG_callback
        will be called again, leading to an error due to None being sent to
        self._RBG_labels, hence the need for if not active_button.
        """
        if not active_button:
            return
        if self._RBG_labels[active_button].name == 'reset':
            self.widget.active = None
        return

class TextInputComponent:
    def __init__(self, Specs, widget_callback):
        self.widget_callback = widget_callback
        self.widget = self._set_TI(Specs)
        self._input_val = None

    def _set_TI(self, Specs):
        TI = TextInput()
        TI.width = Specs.TI_intrinsic_width
        TI.height = Specs.TI_intrinsic_height
        TI.placeholder = Specs.TI_placeholder
        TI.on_change("value", self.widget_callback)
        TI.title = None
        return TI

class TextBoxComponent:
    def __init__(self, Specs):
        self.widget = self._set_TB(Specs)

    def _set_TB(self, Specs):
        TB = Plot()
        TB.x_range = DataRange1d()
        TB.y_range = DataRange1d()
        TB.width = Specs.text_intrinsic_width
        TB.height = Specs.text_intrinsic_height
        TB.x_range = DataRange1d()
        TB.toolbar.logo = None
        text_raw = dict(xs=[0], ys=[0], text=[Specs.title])
        text_CDS = ColumnDataSource(data=text_raw)
        text = Text(x="xs", y="ys", text="text", text_align="center")
        TB.add_glyph(text_CDS, text)
        return TB


class IndividualWidget:
    def __init__(self, widget_callback, Specs):
        self.name = Specs.name
        self.widget_callback = widget_callback

        self._input_val = None
        self._RBG_labels = Specs.RBG_labels

        self._TI = TextInputComponent(Specs, self._TI_callback).widget
        self._TB = TextBoxComponent(Specs).widget
        self._RBG = RBGComponent(Specs).widget
        self._button = ButtonComponent(Specs, self._button_callback).widget
        self.widget_layout = self._widget_assemble(Specs)

    def _TI_callback(self, attr, old, new):
        self._input_val = new

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

    def _widget_assemble(self, Specs):
        TI_disp = row(self._TI, width=Specs.TI_display_width, height=Specs.TI_display_height)
        RBG_disp = row(self._RBG, width=Specs.RBG_display_width, height=Specs.RBG_display_height)
        header_disp = row(self._TB, width=Specs.text_display_width, height=Specs.text_display_height)
        button_disp = row(self._button, width=Specs.button_display_width, height=Specs.button_display_height)
        TI_and_button = row(TI_disp, button_disp)
        widget_layout = column(header_disp, RBG_disp, TI_and_button)
        return widget_layout


class ButtonWidget:
    def __init__(self, widget_callback, Specs):
        self.name = Specs.name
        self.widget_callback = widget_callback

        self._RBG_labels = Specs.RBG_labels
        self._TB = TextBoxComponent(Specs).widget
        self._RBG = RBGComponent(Specs).widget
        self._button = ButtonComponent(Specs, self._button_callback).widget
        self.widget_layout = self._widget_assemble(Specs)

    def _button_callback(self):
        if self._RBG.active is None:
            print("No category selected.")
        else:
            self.widget_callback((self._RBG_labels[self._RBG.active],))
        return

    def _widget_assemble(self, Specs):
        RBG_disp = row(self._RBG, width=Specs.RBG_display_width, height=Specs.RBG_display_height)
        header_disp = row(self._TB, width=Specs.text_display_width, height=Specs.text_display_height)
        button_disp = row(self._button, width=Specs.button_display_width, height=Specs.button_display_height)
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
