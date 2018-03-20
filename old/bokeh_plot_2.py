from bokeh.models.tickers import FixedTicker, AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.models import CDSView, HoverTool, BoxSelectTool, BoxZoomTool, \
    PanTool, WheelPanTool, WheelZoomTool, ResetTool, UndoTool, RedoTool, \
    ZoomInTool, ZoomOutTool, CrosshairTool, TapTool, Button, Text, DataRange1d
from bokeh.models.plots import Plot
import math
from bokeh.layouts import gridplot, layout, widgetbox
from bokeh.events import ButtonClick
import sys

output_file("../bokeh_tmp/line.html")

xdr = DataRange1d()
ydr = DataRange1d()
p3 = Plot(x_range=xdr, y_range=ydr, plot_width=1000, plot_height=1000)

text_raw = dict(xs=[0, 10, 20], ys=[0, 10, 20], text=["one", "two", "three"])
text_CDS = ColumnDataSource(data=text_raw)
text = Text(x="xs", y="ys", text="text")
p3.add_glyph(text_CDS, text)

def callback(buttonclick_event):
    button.label = "jursvbniugsrfg"
    sys.exit()
button = Button(label="Press Me")
button.label = "jursg"
button.on_event(ButtonClick, callback)

button2 = Button(label="Press Me")
button2.label = "g"
button2.on_event(ButtonClick, callback)

button3 = Button(label="Press Me")
button3.label = "gfrrf"
button3.on_event(ButtonClick, callback)




layout_ = gridplot([[p3], [button, button2], [button3, button2]])
curdoc().add_root(layout_)