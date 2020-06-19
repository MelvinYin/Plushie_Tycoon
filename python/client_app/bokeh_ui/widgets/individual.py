from bokeh.models.widgets import Button, Div
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.widgets import RadioButtonGroup
from bokeh.layouts import row, column
from config.global_config import UI_FAIL, Func, Res, Prod
from logs import log
import re
import os
import inspect


class ButtonComponent:
    def __init__(self, specs, widget_callback):
        self.widget_callback = widget_callback
        self.widget = self._set_button(specs)

    def _set_button(self, specs):
        button = Button()
        button.label = specs['text']
        button.width = specs['width']
        button.height = specs['height']
        button.on_click(self.widget_callback)
        return button

class RBGComponent:
    def __init__(self, specs, callback=None):
        self.specs = specs
        self.widget = self._set_RBG(callback)

    def set_label_to_category(self, category):
        labels = []
        for label_str, label_enum in self.specs['labelmap'].items():
            if label_enum in list(category):
                labels.append(label_str)
        self.widget.labels = labels
        return True

    def get_active(self):
        if self.widget.active is None:
            return None
        label_str = self.widget.labels[self.widget.active]
        label_enum = self.specs['labelmap'][label_str]
        return label_enum

    def set_active(self, value):
        self.widget.active = value
        return True

    def _set_RBG(self, callback):
        RBG = RadioButtonGroup()
        RBG.width = self.specs['width']
        RBG.height = self.specs['height']
        RBG.labels = list(self.specs['labelmap'].keys())
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
        TI.width = specs['width']
        TI.height = specs['height']
        TI.placeholder = specs['text']
        TI.on_change("value", self.widget_callback)
        TI.title = ""
        return TI

class TextBoxComponent:
    def __init__(self, specs):
        self.widget = self._set_TB(specs)

    def _set_TB(self, specs):
        TB = Div(text=specs['text'])
        TB.width = specs['width']
        TB.height = specs['height']
        return TB

# class WarehouseTierWidget:


class TransactionWidget:
    def __init__(self, callback):
        self.widget_callback = callback
        self._input_val = None

        self.width = 500
        self.height = 0

        self._input_box = TextInputComponent(self._TI_specs(), self._TI_callback)
        self._header = TextBoxComponent(self._header_specs())
        self._RBG1 = RBGComponent(self._RBG1_specs())
        self._RBG2 = RBGComponent(self._RBG2_specs(), self._RBG2_callback)
        self._RBG3 = RBGComponent(self._RBG3_specs())
        self._button = ButtonComponent(self._button_specs(), self._button_callback)
        self.layout = self._assemble_layout()

    def _TI_specs(self):
        specs = dict()
        specs['width'] = 100
        specs['height'] = 10
        specs['text'] = 'Quantity'
        return specs

    def _header_specs(self):
        specs = dict()
        specs['width'] = 0
        specs['height'] = 0
        specs['text'] = 'Orders'
        return specs

    def _RBG1_specs(self):
        labelmap = dict()
        labelmap["Buy"] = Func.buy
        labelmap["Sell"] = Func.sell
        labelmap["Make"] = Func.make
        specs = dict()
        specs['width'] = 400
        specs['height'] = 30
        specs['labelmap'] = labelmap
        return specs

    def _RBG2_specs(self):
        labelmap = dict()
        labelmap["Res"] = Res
        labelmap["Prod"] = Prod
        specs = dict()
        specs['width'] = 200
        specs['height'] = 30
        specs['labelmap'] = labelmap
        return specs

    def _RBG3_specs(self):
        labelmap = dict()
        labelmap["cloth"] = Res.cloth
        labelmap["stuffing"] = Res.stuffing
        labelmap["accessory"] = Res.accessory
        labelmap["packaging"] = Res.packaging
        labelmap["aisha"] = Prod.aisha
        labelmap["beta"] = Prod.beta
        labelmap["chama"] = Prod.chama
        specs = dict()
        specs['width'] = 400
        specs['height'] = 30
        specs['labelmap'] = labelmap
        return specs

    def _button_specs(self):
        specs = dict()
        specs['width'] = 50
        specs['height'] = 30
        specs['text'] = 'Send'
        return specs

    def _RBG2_callback(self, active_button):
        RBG2_selected_category = self._RBG2.get_active()
        self._RBG3.set_label_to_category(RBG2_selected_category)
        self._RBG3.set_active(None)

    def _assemble_layout(self):
        header = row(self._header.widget, height=30, width=100)
        rbg1 = row(self._RBG1.widget, height=40, width=50)
        rbg2 = row(Div(width=90), self._RBG2.widget, height=40, width=20)
        rbg3 = row(self._RBG3.widget, height=50, width=0)
        inputbox = row(self._input_box.widget, height=50, width=10)
        button = row(self._button.widget, height=50, width=200)
        layout = column(header, rbg1, rbg2, rbg3, inputbox, button,
                        width=self.width, height=self.height)
        self._set_init_RBG3()
        return layout

    def _TI_callback(self, attr, old, new):
        self._input_val = new

    def _button_callback(self):
        RBG1_key = self._RBG1.get_active()
        _RBG2_key = self._RBG2.get_active()
        RBG3_key = self._RBG3.get_active()
        msg = None
        if not RBG1_key or not _RBG2_key or not RBG3_key:
            msg = "No category selected."
        elif not self._input_val:
            msg = "Value not set."
        elif not re.fullmatch("[0-9]+", self._input_val.strip()):
            msg = "Invalid input value."
        elif self._input_val.startswith("0"):
            msg = "Invalid input value."
        else:
            callback = dict(command=RBG1_key.name, category=RBG3_key.name,
                            quantity=int(self._input_val))
            self.widget_callback(callback)
        if msg:
            callback = dict(command=UI_FAIL, message=msg)
            self.widget_callback(callback)
            log(msg, inspect.currentframe())
        return

    def _set_init_RBG3(self):
        for value in self._RBG2.specs['labelmap'].values():
            self._RBG3.set_label_to_category(value)
            break
        return

class ButtonWidget:
    def __init__(self, callback):
        self.width = 100
        self.height = 50
        self.callback = callback
        self._header = TextBoxComponent(self._textbox_specs())
        self._RBG = RBGComponent(self._RBG_specs())
        self._button = ButtonComponent(self._button_specs(),
                                       self._button_callback)
        self.layout = self._assemble_layout()

    def _button_specs(self):
        specs = dict()
        specs['width'] = 50
        specs['height'] = 30
        specs['text'] = 'Send'
        return specs

    def _textbox_specs(self):
        specs = dict()
        specs['width'] = 0
        specs['height'] = 0
        specs['text'] = 'Actions'
        return specs

    def _RBG_specs(self):
        labelmap = dict()
        labelmap["next"] = Func.next
        labelmap["save"] = Func.save
        labelmap["load"] = Func.load
        labelmap["back"] = Func.back
        labelmap["quit"] = Func.quit
        specs = dict()
        specs['width'] = 250
        specs['height'] = 30
        specs['labelmap'] = labelmap
        return specs

    def _button_callback(self):
        if self._RBG.get_active() is None:
            msg = "No category selected."
            log(msg, inspect.currentframe())
        else:
            callback = dict(command=self._RBG.get_active().name)
            self.callback(callback)

    def _assemble_layout(self):
        row0 = row(self._header.widget, height=30, width=100)
        row1 = row(self._RBG.widget, self._button.widget, height=40)
        layout = column(row0, row1, width=self.width, height=self.height)
        return layout


# def call(attr, old, new):
#     return
# x = ButtonWidget(call)
# from bokeh.plotting import show
# show(x.layout)