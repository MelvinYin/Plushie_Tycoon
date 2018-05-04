from bokeh.models.widgets import Button, Div
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.widgets import RadioButtonGroup

from bokeh.plotting import output_file, show, curdoc
from bokeh.layouts import row, column
import re
import sys
sys.path.append("../")
from widget_config import transaction_specs, button_specs

class ButtonComponent:
    def __init__(self, specs, widget_callback):
        self.widget_callback = widget_callback
        self.widget = self._set_button(specs)

    def _set_button(self, specs):
        button = Button()
        button.label = specs.label
        button.width = specs.width
        button.height = specs.height
        button.on_click(self.widget_callback)
        return button

class RBGComponent:
    def __init__(self, specs, callback=None):
        self.widget = self._set_RBG(specs, callback)

    def _set_RBG(self, specs, callback):
        RBG = RadioButtonGroup()
        RBG.width = specs.width
        RBG.height = specs.height
        RBG.labels = [specs.labelmap[label] for label in specs.labels]
        RBG.active = None
        if callback:
            RBG.on_click(callback)
        return RBG

class TextInputComponent:
    def __init__(self, specs, widget_callback):
        self.widget_callback = widget_callback
        self.widget = self._set_TI(specs)
        self._input_val = None

    def _set_TI(self, specs):
        TI = TextInput()
        TI.width = specs.width
        TI.height = specs.height
        TI.placeholder = specs.placeholder
        TI.on_change("value", self.widget_callback)
        TI.title = None
        return TI

class TextBoxComponent:
    def __init__(self, specs):
        self.widget = self._set_TB(specs)

    def _set_TB(self, specs):
        TB = Div(text=specs.title)
        TB.width = specs.width
        TB.height = specs.height
        return TB


class TransactionWidget:
    def __init__(self, callback, specs=transaction_specs):
        self.name = specs.name
        self.specs = specs
        self.widget_callback = callback
        self._input_val = None

        self._input_box = TextInputComponent(specs.TI, self._TI_callback).widget
        self._header = TextBoxComponent(specs.header).widget
        self._RBG1 = RBGComponent(specs.RBG1).widget
        self._RBG2 = RBGComponent(specs.RBG2, self._RBG2_callback).widget
        self._RBG3 = RBGComponent(specs.RBG3).widget
        self._button = ButtonComponent(specs.button, self._button_callback).widget
        self.layout = self._assemble_layout(specs.width, specs.height, specs.layout)

    def _RBG2_callback(self, active_button):
        label_string = self._RBG2.labels[active_button]
        for key, label in self.specs.RBG2.labelmap.items():
            if label == label_string:
                category = key
                break
        # noinspection PyUnboundLocalVariable
        self._RBG3.labels = list(
            [self.specs.RBG3.labelmap[val] for val in list(category)])
        self._RBG3.active = None
        return

    def _build_row(self, specs, components):
        assert len(specs.spacers) == len(components)
        row_elements = []
        for i in range(len(components)):
            row_elements.append(Div(width=specs.spacers[i]))
            row_elements.append(components[i])
        to_display = row(*row_elements, height=specs.height, width=specs.width)
        return to_display

    def _assemble_layout(self, width, height, specs):
        header = self._build_row(specs[0], [self._header])
        rbg1 = self._build_row(specs[1], [self._RBG1])
        rbg2 = self._build_row(specs[2], [self._RBG2])
        rbg3 = self._build_row(specs[3], [self._RBG3])
        inputbox = self._build_row(specs[4], [self._input_box])
        button = self._build_row(specs[5], [self._button])
        layout = column(header, rbg1, rbg2, rbg3, inputbox, button, width=width, height=height)
        return layout

    def _TI_callback(self, attr, old, new):
        self._input_val = new

    def _button_callback(self):
        if self._RBG1.active is None:
            print("No category selected.")
        elif self._RBG2.active is None:
            print("No category selected.")
        elif self._RBG3.active is None:
            print("No category selected.")
        elif not self._input_val:
            print("Value not set.")
        elif not re.fullmatch("[0-9]+", self._input_val.strip()):
            print("Invalid input value.")
        elif self._input_val.startswith("0"):
            print("Invalid input value.")
        else:
            RBG1_label = self._RBG1.labels[self._RBG1.active]
            for key, label in self.specs.RBG1.labelmap.items():
                if label == RBG1_label:
                    RBG1_key = key
                    break
            RBG2_label = self._RBG2.labels[self._RBG2.active]
            for key, label in self.specs.RBG2.labelmap.items():
                if label == RBG2_label:
                    RBG2_key = key
                    break
            RBG3_label = self._RBG3.labels[self._RBG3.active]
            for key, label in self.specs.RBG3.labelmap.items():
                if label == RBG3_label:
                    RBG3_key = key
                    break
            if 'RBG1_key' not in locals() or \
                    'RBG2_key' not in locals() or \
                    'RBG3_key' not in locals():
                raise Exception
            # noinspection PyUnboundLocalVariable
            self.widget_callback([RBG1_key, RBG2_key, RBG3_key,
                int(self._input_val)])
        return


class ButtonWidget:
    def __init__(self, callback, specs=button_specs):
        self.name = specs.name
        self.callback = callback
        self._header = TextBoxComponent(specs.header).widget
        self._RBG = RBGComponent(specs.RBG).widget
        self._button = ButtonComponent(specs.button, self._button_callback).widget
        self.layout = self._assemble_layout(specs.width, specs.height, specs.layout)

    def _button_callback(self):
        if self._RBG.active is None:
            print("No category selected.")
        else:
            self.callback([self._RBG.labels[self._RBG.active]])
        return

    def _build_row(self, specs, components):
        assert len(specs.spacers) == len(components)
        row_elements = []
        for i in range(len(components)):
            row_elements.append(Div(width=specs.spacers[i]))
            row_elements.append(components[i])
        to_display = row(*row_elements, height=specs.height, width=specs.width)
        return to_display

    def _assemble_layout(self, width, height, specs):
        row0 = self._build_row(specs[0], [self._header])
        row1 = self._build_row(specs[1], [self._RBG, self._button])
        layout = column(row0, row1, width=width, height=height)
        return layout




# For testing



if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    from widget_config import transaction_specs, button_specs

    def widget_callback(command_to_run):
        print("from widget callback")
        print(command_to_run)
        return

    widget_1 = TransactionWidget(widget_callback)

    widget_1.widget_callback([transaction_specs.RBG1.labels[0],
                              transaction_specs.RBG2.labels[0],
                              transaction_specs.RBG3.labels[0],
                               10])

    widget_2 = ButtonWidget(widget_callback, button_specs)

    layout_w1 = widget_1.layout
    layout2 = widget_2.layout
    show(row(layout_w1, layout2))
    curdoc().add_root(row(layout_w1))

# Expected output: tuple(<Func.something>, <Res.something>, int of quantity)
