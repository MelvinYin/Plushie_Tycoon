from bokeh.models.tickers import FixedTicker, AdaptiveTicker
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc, output_notebook
from bokeh.models import CDSView, HoverTool, BoxSelectTool, BoxZoomTool, \
    PanTool, WheelPanTool, WheelZoomTool, ResetTool, UndoTool, RedoTool, \
    ZoomInTool, ZoomOutTool, CrosshairTool, TapTool, Button, Text, DataRange1d
from bokeh.models.plots import Plot
import math
from bokeh.layouts import gridplot, layout, widgetbox, row, column, Spacer
from bokeh.events import ButtonClick
import sys
from bokeh.models.widgets import CheckboxButtonGroup
from bokeh.models.widgets.inputs import TextInput

output_file("../bokeh_tmp/line.html")

xdr = DataRange1d()
ydr = DataRange1d()
p3 = Plot(x_range=xdr, y_range=ydr, plot_width=200, plot_height=30)
text_raw = dict(xs=[0], ys=[0], text=["Placeholder"])
text_CDS = ColumnDataSource(data=text_raw)
text = Text(x="xs", y="ys", text="text")
p3.add_glyph(text_CDS, text)
p3.toolbar.logo = None

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

def callback_func(*args):
    print(args)
    print("efnbue")

CBG1 = CheckboxButtonGroup(
        labels=["Option 1", "Option 2", "Option 3", "4"], active=[])
CBG2 = CheckboxButtonGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=[])
CBG3 = CheckboxButtonGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=[])
def update_plot(new):
    print(new)
CBG1.on_click(update_plot)
CBG2.on_click(update_plot)
CBG3.on_click(update_plot)

def textcallback(attr, old, new):
    print(repr(attr), repr(old), repr(new))

def textcallback2(*args):
    print(args)

TI1 = TextInput()
TI1.on_change('value', textcallback)
p3.width = 220
p3.height = 220
TI1.width = 120
CBG1.width = 200
x = dir(CheckboxButtonGroup)
x = CBG1._property_values
for i in x:
    print(i)
layout_tmp1 = layout(p3, CBG1, TI1)
layout_tmp2 = layout(p3, CBG1, TI1)
layout_tmp3 = layout(p3, CBG1, TI1)
layout_ = layout(layout_tmp1, layout_tmp2, layout_tmp3)
layout_.height = 102000
layout_.width = 102000


# layout_ = gridplot([[layout_a], [layout_a]])
# layout__ = gridplot([[layout_], [layout_]])

# layout_ = layout([p3,widgetbox1], [button], [widgetbox1, widgetbox(CBG2), widgetbox(CBG3)])
# show(layout_)


# layout_ = gridplot([[p3], [button, button2], [button3, button2]])
# layout__ = layout([p3, button, button2])
# curdoc().add_root(layout_)
show(layout_)


