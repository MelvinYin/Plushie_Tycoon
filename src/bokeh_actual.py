from bokeh.models import Text
from bokeh.models.widgets import Button
from bokeh.models.plots import Plot
from bokeh.models import DataRange1d
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.widgets import CheckboxButtonGroup

from bokeh.models.tickers import AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool, BoxZoomTool, PanTool, WheelZoomTool, \
    ResetTool, UndoTool
import math
from bokeh.layouts import row, column

output_file("../bokeh_tmp/line.html")

# WIDGETS

def prod_widgets_gen():
    xdr1 = DataRange1d()
    ydr1 = DataRange1d()
    p = Plot(x_range=xdr1, y_range=ydr1, width=300, height=50)
    text_raw = dict(xs=[0], ys=[0], text=["1Placeholder"])
    text_CDS = ColumnDataSource(data=text_raw)
    text = Text(x="xs", y="ys", text="text", text_align="center")
    p.add_glyph(text_CDS, text)
    p.toolbar.logo = None
    header = row(p)

    TI = TextInput(width=200, height=70)
    TI.placeholder = "Placeholder"

    CBG = CheckboxButtonGroup(
        labels=["Option 1", "Option 2", "Option 3", "4"], active=[])

    button = Button(label="Press Me")
    button.width = 100

    TI_and_button = row(TI, button)
    TI_and_button.width = 400
    assembled = column(header, CBG, TI_and_button)
    return assembled

layout1 = prod_widgets_gen()
layout2 = prod_widgets_gen()
layout3 = prod_widgets_gen()
layout4 = prod_widgets_gen()

layout_1 = row(layout1, layout2)
layout_2 = row(layout3, layout4)

layout_w = column(layout_1, layout_2)

# PLOTS

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

def convert_to_CDS(raw_data):
    xs = []
    ys = []
    for time_steps, values in raw_data.items():
        xs += [int(time_steps) + i/len(values) for i in range(len(values))]
        ys += values
    time_steps_for_hover = [math.floor(i) for i in xs]
    tmp = dict(xs=xs, ys=ys, time_steps_for_hover=time_steps_for_hover)
    return ColumnDataSource(data=tmp)

def gen_default_fig():
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

    p.xaxis.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
    p.xgrid.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
    p.title.text = "Placeholder"
    p.title.align = 'center'
    p.xaxis.axis_label = "Time Steps"
    p.yaxis.axis_label = "Placeholder"
    return p

def gen_generic_func(raw_data):
    CDS = convert_to_CDS(raw_data)

    p_def = gen_default_fig()
    p = figure(plot_width=p_def.plot_width, plot_height=p_def.plot_height,
               tools=p_def.tools,title=p_def.title,
               toolbar=p_def.toolbar)
    p.x("xs", "ys", source=CDS, name="points", size=10)
    p.line("xs", "ys", source=CDS)
    p.xaxis.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
    p.xgrid.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
    p.xaxis.axis_label = "Time Steps"
    p.yaxis.axis_label = "Placeholder"
    p.toolbar.logo = None
    p.x_range = DataRange1d(follow="end", follow_interval=3)
    p.y_range = DataRange1d(range_padding=0.3)
    return p

def couple_range(*args):
    p1 = args[0]
    return_p = [p1]
    for p in args[1:]:
        p.x_range = p1.x_range
        return_p.append(p)
    return return_p

raw_data_1 = gen_raw_input_data_1()
raw_data_2 = gen_raw_input_data_2()
p1 = gen_generic_func(raw_data_1)
p2 = gen_generic_func(raw_data_1)
p3 = gen_generic_func(raw_data_2)
p4 = gen_generic_func(raw_data_2)
p5 = gen_generic_func(raw_data_2)
p6 = gen_generic_func(raw_data_1)
p1, p2, p3, p4, p5, p6 = couple_range(p1, p2, p3, p4, p5, p6)

layout1 = row(p1, p2, p3)
layout2 = row(p4, p5, p6)
layout_p = column(layout1, layout2)

layout_ = column(layout_p, layout_w)


show(layout_)