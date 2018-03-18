from bokeh.models.tickers import FixedTicker, AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import CDSView, HoverTool, BoxSelectTool, BoxZoomTool, \
    PanTool, WheelPanTool, WheelZoomTool, ResetTool, UndoTool, RedoTool, \
    ZoomInTool, ZoomOutTool, CrosshairTool, TapTool
import math

output_file("line.html")

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

raw_data = gen_raw_input_data()
CDS = convert_to_CDS(raw_data)

hover = HoverTool(tooltips=[
    ("Point No.", "$index"),
    ("Time Step", "@time_steps_for_hover")], names=["points"])

boxzoom = BoxZoomTool()
pan = PanTool()
wheelpan = WheelPanTool()
wheelzoom = WheelZoomTool()
reset = ResetTool()
undo = UndoTool()
crosshair = CrosshairTool()

tools = [pan, boxzoom, wheelzoom, reset, undo, crosshair, hover]


p = figure(plot_width=400, plot_height=400, tools=tools)
p.toolbar.active_drag = pan
p.toolbar.active_scroll = wheelzoom
p.toolbar.active_tap = None
p.toolbar.active_inspect = hover


x = dir(p.yaxis)
for i in x:
    print(i)
p.x("xs", "ys", name="points", source=CDS, size=10)
p.line("xs", "ys", name="line", source=CDS)
p.xaxis.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
p.xgrid.ticker = AdaptiveTicker(min_interval=1, num_minor_ticks=0)
p.title.text = "Placeholder"
p.title.align = 'center'
p.xaxis.axis_label="Time Steps"
p.yaxis.axis_label="Placeholder"
show(p)


