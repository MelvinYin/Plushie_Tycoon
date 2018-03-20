from bokeh.models.tickers import AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool, BoxZoomTool, PanTool, WheelZoomTool, \
    ResetTool, UndoTool
import math
from bokeh.layouts import row, column


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
    raw_data = gen_raw_input_data()
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
    return p

def couple_range(*args):
    p1 = args[0]
    return_p = [p1]
    for p in args[1:]:
        p.x_range = p1.x_range
        p.y_range = p1.y_range
        return_p.append(p)
    return return_p


p1 = gen_generic_func()
p2 = gen_generic_func()
p3 = gen_generic_func()
p4 = gen_generic_func()
p5 = gen_generic_func()
p6 = gen_generic_func()
p1, p2, p3, p4, p5, p6 = couple_range(p1, p2, p3, p4, p5, p6)

layout1 = row(p1, p2, p3)
layout2 = row(p4, p5, p6)
layout_ = column(layout1, layout2)
# curdoc().add_root(layout_)

show(layout_)

