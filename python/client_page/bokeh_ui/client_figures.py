from bokeh.plotting import figure
from bokeh.models import DataRange1d, HoverTool, BoxZoomTool, PanTool, \
    WheelZoomTool, ResetTool, UndoTool
from bokeh.models.tickers import FixedTicker
import numpy as np
from collections import defaultdict
"""
self.current_ticks need to be pulled out, because figure.xaxis.ticker cannot 
be retrieved.

Func_steps start from len(initial_data) so it is always about the next function
call.

initial_func_count when fed in should be positive int.
"""
import re
from enum import Enum

from bokeh.layouts import row, column
from bokeh.models import DataTable, TableColumn, ColumnDataSource
from bokeh.models.widgets import Button, Div, RadioButtonGroup
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.layouts import Spacer

from config.global_config import UI_FAIL, Func, Res, Prod, FigureNames


class ItemCostTable:
    def __init__(self, data):
        self.name = FigureNames.item_cost_table
        self.title = "Item Cost Table"
        self.width = 250
        self.height = 220

        self._CDS = self._set_CDS(data)
        self._table = self._build_table(data)
        self.figure = self._set_table()

    def _truncate_number(self, number):
        precision = 0
        curr_number = number
        while curr_number // 1 < 0.99 and precision < 10:
            precision += 1
            curr_number *= 10
        if precision == 0:
            return str(round(number))
        elif precision == 10:
            return "0."
        else:
            number = round(number * (10 ** precision)) / (10 ** precision)
            return '{:.{prec}f}'.format(number, prec=precision)

    def _check_initial_data(self, data):
        assert data
        assert isinstance(data, dict)
        ratio_len = None
        for category, ratios in data.items():
            assert isinstance(category, str)
            if ratio_len is None:
                ratio_len = len(ratios)
                assert ratio_len > 0
            else:
                assert len(ratios) == ratio_len
            for ratio in ratios:
                assert ratio >= 0
        return True

    def _set_CDS(self, data):
        for key, values in data.items():
            if key == "Item":
                continue
            new_values = []
            for value in values:
                error_msg = "This should be double, check who sent this in. " \
                            "Otherwise check whether the index column has " \
                            "key as 'Item'."
                assert not isinstance(value, str), error_msg
                new_values.append(self._truncate_number(value))
            data[key] = new_values
        source = ColumnDataSource(data)
        return source

    def _build_table(self, data):
        columns = [TableColumn(field=i, title=i) for i in
                        data.keys()]
        columns[0].width = 700
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width,
                               height=self.height, index_position=None)
        return data_table

    def _set_table(self):
        fig = column(row(Spacer(width=15), Div(text=self.title), height=30),
                     self._table)
        return fig

    def figure_update(self, data):
        # self._check_add_data(add_data)
        to_patch = defaultdict(list)
        for category, ratios in data.items():
            assert isinstance(category, str)
            for i, ratio in enumerate(ratios):
                if category != "Item":
                    ratio = self._truncate_number(ratio)
                to_patch[category].append((i, ratio))
        self._CDS.patch(to_patch)
        return


class ItemPropertiesTable:
    def __init__(self, data):
        self.name = FigureNames.item_properties_table
        self.title = "Properties"
        self.data = data
        self.width = 250
        self.height = 220

        self._CDS = self._set_CDS(data)
        self._table = self._build_table(data)
        self.figure = self._set_table()

    def _get_properties(self, inventory):
        weights = inventory.get('weight')
        volumes = inventory.get('volume')
        assert tuple(weights.keys()) == tuple(volumes.keys())
        properties = dict()
        properties['Weight'] = list(weights.values())
        properties['Volume'] = list(volumes.values())
        return properties

    def _check_initial_data(self, data):
        assert data
        assert isinstance(data, dict)
        ratio_len = None
        for category, ratios in data.items():
            assert isinstance(category, str)
            if ratio_len is None:
                ratio_len = len(ratios)
                assert ratio_len > 0
            else:
                assert len(ratios) == ratio_len
            for ratio in ratios:
                assert isinstance(ratio, int), ratio
                assert ratio >= 0
        return True

    def _set_CDS(self, data):
        source = ColumnDataSource(data)
        return source

    def _build_table(self, data):
        columns = [TableColumn(field=i, title=i) for i in
                        data.keys()]
        columns[0].width = 400
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width, height=self.height,
                               index_position=None)
        return data_table

    def _set_table(self):
        header = row(Spacer(width=15), Div(text=self.title), height=30)
        fig = column(header, self._table)
        return fig

    def figure_update(self, data):
        to_patch = dict()
        for category, ratios in data.items():
            for i, ratio in enumerate(ratios):
                to_patch[category] = [(i, ratio)]
        self._CDS.patch(to_patch)
        return

class ResourceRatioTable:
    def __init__(self, initial_data):
        self.name = FigureNames.res_ratio_table
        self.title = "Production Resource Ratios"
        self.data = initial_data
        self.width = 250
        self.height = 220

        self._CDS = ColumnDataSource(self.data)
        self._table = self._build_table()
        self.figure = self._set_table()

    def _convert_input(self, data):
        resource_ratios = dict()
        for category in data:
            resource_ratios[category.name] = \
                [int(i) for i in data[category].values]
        return resource_ratios

    def _build_table(self):
        columns = [TableColumn(field=i, title=i) for i in self.data.keys()]
        columns[0].width = 800
        data_table = DataTable(source=self._CDS, columns=columns,
                               width=self.width,
                               height=self.height, index_position=None)
        return data_table

    def _set_table(self):
        fig = column(row(Spacer(width=15), Div(text=self.title),
                         height=30), self._table)
        return fig

    def figure_update(self, add_data):
        # add_data = self._convert_input(add_data)
        to_patch = dict()
        for category, ratios in add_data.items():
            for i, ratio in enumerate(ratios):
                to_patch[category] = [(i, ratio)]
        self._CDS.patch(to_patch)
        return


class ConsoleOutput:
    def __init__(self, console_text="<p>"):
        self.name = FigureNames.console_output
        self.title = "Console"
        self.text = console_text
        self.width = 50
        self.height = 20
        self.textbox_width = 400
        self.textbox_height = 380
        # Division by 2 so it fits well and within what bokeh uses.
        self.html_height = int(self.textbox_height / 2)
        self._paragraph = self._build_paragraph()
        self.figure = self._set_textbox()
        self._rollover_count = 20

    def _build_paragraph(self):
        _style = dict()
        _style['overflow-y'] = 'auto'
        _style['height'] = f'{self.html_height}px'
        paragraph = Div(width=self.textbox_width,
                        height=self.textbox_height,
                        text=self.text, style=_style)
        return paragraph

    def _set_textbox(self):
        fig = column(row(Spacer(height=self.height)),
                     row(Spacer(width=self.width), self._paragraph))
        return fig

    def figure_update(self, add_line):
        self._paragraph.text += add_line + "<br>"
        return True

class IndividualFigure:
    def __init__(self, initial_data, specs):
        self.CDS = self._create_initial_CDS(initial_data)
        self.tick_label_map = self._get_initial_ticks_label_mapping()
        self.figure = self._set_initial_figure(specs)
        self._update_xaxis()
        self.name = specs.name

    def _create_initial_CDS(self, initial_data):
        """
        Dict sent to CDS should have list instead of tuple as values, otherwise
        CDS.stream will fail.
        """
        # add test? to make sure all values used in this class is in init_data
        num_values = len(next(iter(initial_data.values())))
        initial_data['xs'] = list(range(num_values))
        CDS = ColumnDataSource(initial_data)
        return CDS

    def _get_initial_ticks_label_mapping(self):
        time = self.CDS.data["time"]
        xs = self.CDS.data['xs']

        time_values, counts = np.unique(time, return_counts=True)
        tick_label_map = dict()
        counter = 0
        for time, count in zip(time_values, counts):
            tick_label_map[xs[counter]] = str(time)
            counter += count
        return tick_label_map

    def _set_initial_figure(self, specs):
        hover = HoverTool(
            tooltips=[("Point No.", "@xs"),
                      ("Time Step", "@time")],
            names=["x", "points2"])

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

        p.x_range = DataRange1d(follow="end", follow_interval=5,
                                range_padding=1, range_padding_units='absolute')
        p.y_range = DataRange1d(follow="end", range_padding=2,
                                range_padding_units='absolute')

        initial_ticks = list(self.tick_label_map.keys())
        ticker = FixedTicker(ticks=initial_ticks)
        p.xaxis.ticker = ticker
        p.xgrid.ticker = ticker

        p.xaxis.major_label_overrides = self.tick_label_map

        p.title.text = specs.title
        p.title.align = 'center'
        p.xaxis.axis_label = specs.x_label
        p.yaxis.axis_label = specs.y_label
        keys_in_figure = list([key for key in self.CDS.column_names
                               if key != 'time' and key != 'xs'])

        # Additional "_" because if legend key is same as data x/y key,
        # legend plot will show data values instead of key (str) value,
        # reported in bokeh issues, see #8394
        for key in keys_in_figure:
            legend_key = key + "_"
            color_value = specs.colormap[key]
            p.x("xs", key, source=self.CDS, name=key, size=10,
                legend_label=legend_key, color=color_value)
            p.line("xs", key, source=self.CDS, legend_label=legend_key,
                   color=color_value)
        p.legend.location = "top_left"
        p.legend.click_policy = "hide"
        return p

    def _update_xaxis(self):
        ticker = FixedTicker(ticks=list(self.tick_label_map.keys()))
        self.figure.xaxis.ticker = ticker
        self.figure.xgrid.ticker = ticker
        self.figure.xaxis.major_label_overrides = self.tick_label_map

    def figure_update(self, add_line):
        current_time = add_line['time'][0]
        current_x = self.CDS.data['xs'][-1] + 1
        add_line['xs'] = [current_x]
        if current_time != self.CDS.data['time'][-1]:
            self.tick_label_map[current_x] = str(current_time)
            self._update_xaxis()
        # log(add_line, inspect.currentframe())

        # Load does not work at this stage because figures do not appear to
        # be able to refresh themselves
        self.CDS.stream(add_line)


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


class TransactionWidget:
    def __init__(self, callback):
        self.widget_callback = callback
        self._input_val = None

        self.width = 500
        self.height = 0

        self._input_box = TextInputComponent(self._TI_specs(),
                                             self._TI_callback)
        self._header = TextBoxComponent(self._header_specs())
        self._RBG1 = RBGComponent(self._RBG1_specs())
        self._RBG2 = RBGComponent(self._RBG2_specs(), self._RBG2_callback)
        self._RBG3 = RBGComponent(self._RBG3_specs())
        self._button = ButtonComponent(self._button_specs(),
                                       self._button_callback)
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
            callback = dict(command=RBG1_key, category=RBG3_key,
                            quantity=int(self._input_val))
            self.widget_callback(callback)
        if msg:
            callback = dict(command=UI_FAIL, message=msg)
            self.widget_callback(callback)
            # log(msg, inspect.currentframe())
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
            # log(msg, inspect.currentframe())
        else:
            callback = dict(command=self._RBG.get_active())
            self.callback(callback)

    def _assemble_layout(self):
        row0 = row(self._header.widget, height=30, width=100)
        row1 = row(self._RBG.widget, self._button.widget, height=40)
        layout = column(row0, row1, width=self.width, height=self.height)
        return layout