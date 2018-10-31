from bokeh.models.widgets import Button, Div
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.widgets import RadioButtonGroup
from bokeh.layouts import row, column
from logs import log
import re
import os


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
        self.specs = specs
        self.widget = self._set_RBG(callback)

    def set_label_to_category(self, category):
        labels = []
        for label_str, label_enum in self.specs.labelmap.items():
            if label_enum in list(category):
                labels.append(label_str)
        self.widget.labels = labels
        return True

    def get_active(self):
        if self.widget.active is None:
            return None
        label_str = self.widget.labels[self.widget.active]
        label_enum = self.specs.labelmap[label_str]
        return label_enum

    def set_active(self, value):
        self.widget.active = value
        return True

    def _set_RBG(self, callback):
        # specs=namedtuple(typename=RBG, width, height, labels, labelmap)
        RBG = RadioButtonGroup()
        RBG.width = self.specs.width
        RBG.height = self.specs.height
        RBG.labels = list(self.specs.labelmap.keys())
        RBG.active = None
        if callback:
            RBG.on_click(callback)
        return RBG

class TextInputComponent:
    def __init__(self, specs, widget_callback):
        # specs=namedtuple(typename=Header, width, height, placeholder)
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
    def __init__(self, callback, specs):
        # specs.__dict__ = {name, width, height, header, RBG1, RBG2, RBG3,
        # TI, button, layout}
        self.name = specs.name
        self.specs = specs
        self.widget_callback = callback
        self._input_val = None

        self._input_box = TextInputComponent(specs.TI, self._TI_callback)
        self._header = TextBoxComponent(specs.header)
        self._RBG1 = RBGComponent(specs.RBG1)
        self._RBG2 = RBGComponent(specs.RBG2, self._RBG2_callback)
        self._RBG3 = RBGComponent(specs.RBG3)
        self._button = ButtonComponent(specs.button, self._button_callback)
        self.layout = self._assemble_layout(specs.width, specs.height, specs.layout)

    def _RBG2_callback(self, active_button):
        RBG2_selected_category = self._RBG2.get_active()
        # noinspection PyUnboundLocalVariable
        self._RBG3.set_label_to_category(RBG2_selected_category)
        # self.specs.RBG3.labelmap has res_members and prod_members, but
        # category is Enum(Res), so calling list gives tag and other members
        self._RBG3.set_active(None)
        return

    def _build_row(self, specs, components):
        assert len(specs.spacers) == len(components)
        row_elements = []
        for i in range(len(components)):
            row_elements.append(Div(width=specs.spacers[i]))
            row_elements.append(components[i].widget)
        to_display = row(*row_elements, height=specs.height, width=specs.width)
        return to_display

    def _assemble_layout(self, width, height, specs):
        header = self._build_row(specs[0], [self._header])
        rbg1 = self._build_row(specs[1], [self._RBG1])
        rbg2 = self._build_row(specs[2], [self._RBG2])
        rbg3 = self._build_row(specs[3], [self._RBG3])
        inputbox = self._build_row(specs[4], [self._input_box])
        button = self._build_row(specs[5], [self._button])
        layout = column(header, rbg1, rbg2, rbg3, inputbox, button,
                        width=width, height=height)
        self._set_init_RBG3()
        return layout

    def _TI_callback(self, attr, old, new):
        self._input_val = new

    def _button_callback(self):
        RBG1_key = self._RBG1.get_active()
        _RBG2_key = self._RBG2.get_active()
        RBG3_key = self._RBG3.get_active()
        if not RBG1_key or not _RBG2_key or not RBG3_key:
            log(os.getcwd(), "No category selected.")
        elif not self._input_val:
            log(os.getcwd(), "Value not set.")
        elif not re.fullmatch("[0-9]+", self._input_val.strip()):
            log(os.getcwd(), "Invalid input value.")
        elif self._input_val.startswith("0"):
            log(os.getcwd(), "Invalid input value.")
        else:
            callback = dict(command=RBG1_key, category=RBG3_key,
                            quantity=int(self._input_val))
            self.widget_callback(callback)
        return

    def _set_init_RBG3(self):
        for value in self._RBG2.specs.labelmap.values():
            self._RBG3.set_label_to_category(value)
            break
        return


class ButtonWidget:
    def __init__(self, callback, specs):
        # specs.__dict__ = {name, width, height, header, RBG, button, layout}
        self.name = specs.name
        self.callback = callback
        self._header = TextBoxComponent(specs.header)
        self._RBG = RBGComponent(specs.RBG)
        self._button = ButtonComponent(specs.button, self._button_callback)
        self.layout = self._assemble_layout(specs.width, specs.height,
                                            specs.layout)

    def _button_callback(self):
        if self._RBG.get_active() is None:
            log(os.getcwd(), "No category selected.")
        else:
            callback = dict(command=self._RBG.get_active())
            self.callback(callback)
        return

    def _build_row(self, specs, components):
        assert len(specs.spacers) == len(components)
        row_elements = []
        for i in range(len(components)):
            row_elements.append(Div(width=specs.spacers[i]))
            row_elements.append(components[i].widget)
        to_display = row(*row_elements, height=specs.height, width=specs.width)
        return to_display

    def _assemble_layout(self, width, height, specs):
        row0 = self._build_row(specs[0], [self._header])
        row1 = self._build_row(specs[1], [self._RBG, self._button])
        layout = column(row0, row1, width=width, height=height)
        return layout
