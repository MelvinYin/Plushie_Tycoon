from bokeh.models.tickers import FixedTicker, AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import CDSView, HoverTool, BoxSelectTool, BoxZoomTool, \
    PanTool, WheelPanTool, WheelZoomTool, ResetTool, UndoTool, RedoTool, \
    ZoomInTool, ZoomOutTool, CrosshairTool, TapTool, Button, Text, DataRange1d
from bokeh.models.plots import Plot
import math
from bokeh.layouts import gridplot, layout
from bokeh.events import ButtonClick
import sys
import os

output_file("../bokeh_tmp/line.html")

def gen_raw_input_data():
    data = dict()
    data[0] = [1,13, 23]
    data[1] = [23]
    data[2] = [34,23, 34]
    data[3] = [2]
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

def gen_generic_func():
    """ Because figure cannot be called by copy.deepcopy. """
    p_def = gen_default_fig()
    p = figure(plot_width=p_def.plot_width, plot_height=p_def.plot_height,
               tools=p_def.tools,title=p_def.title,
               toolbar=p_def.toolbar)
    p.xaxis.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
    p.xgrid.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
    p.xaxis.axis_label = "Time Steps"
    p.yaxis.axis_label = "Placeholder"
    return p


def gen_generic_func2():
    """ Because figure cannot be called by copy.deepcopy. """
    p_def = gen_default_fig()
    p = figure(plot_width=p_def.plot_width, plot_height=p_def.plot_height,
               tools=p_def.tools,title=p_def.title,
               toolbar=p_def.toolbar)
    p.xaxis.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
    p.xgrid.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
    p.xaxis.axis_label = "Time Steps"
    p.yaxis.axis_label = "Placeholder"
    return p

raw_data = gen_raw_input_data()
CDS = convert_to_CDS(raw_data)

p1 = gen_generic_func()
p1.x("xs", "ys", source=CDS, name="points", size=10)
p1.line("xs", "ys", source=CDS)

def callback(buttonclick_event):
    button.label = "jursvbniugsrfg"
    sys.exit()
p2 = gen_generic_func2()
p2.x("xs", "ys", source=CDS, name="points2", size=10)
p2.line("xs", "ys", source=CDS)
p2.x_range = p1.x_range
p2.y_range = p1.y_range
button = Button(label="Press Me")
button.label = "jursg"
button.on_event(ButtonClick, callback)

layout_ = layout([p1, p2], [button])
curdoc().add_root(layout_)



# show(layout_)

