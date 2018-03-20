from bokeh.plotting import output_file, ColumnDataSource, show
from bokeh.layouts import gridplot, layout
from bokeh.models import Text
from bokeh.models.widgets import Button
from bokeh.models.plots import Plot
from bokeh.models import DataRange1d
from bokeh.models.widgets.inputs import TextInput

output_file("../bokeh_tmp/line.html")

button1 = Button(label="Press Me")
button2 = Button(label="Press Me")
button3 = Button(label="Press Me")
button4 = Button(label="Press Me")

TI1 = TextInput()
TI2 = TextInput()
TI3 = TextInput()
TI4 = TextInput()

xdr1 = DataRange1d()
ydr1 = DataRange1d()
p1 = Plot(x_range=xdr1, y_range=ydr1, plot_width=100, plot_height=100)
text_raw1 = dict(xs=[0], ys=[0], text=["1Placeholder"])
text_CDS1 = ColumnDataSource(data=text_raw1)
text1 = Text(x="xs", y="ys", text="text")
p1.add_glyph(text_CDS1, text1)
p1.toolbar.logo = None

xdr2 = DataRange1d()
ydr2 = DataRange1d()
p2 = Plot(x_range=xdr2, y_range=ydr2, plot_width=100, plot_height=100)
text_raw2 = dict(xs=[10], ys=[10], text=["2Placeholder"])
text_CDS2 = ColumnDataSource(data=text_raw2)
text2 = Text(x="xs", y="ys", text="text")
p2.add_glyph(text_CDS2, text2)
p2.toolbar.logo = None

xdr3 = DataRange1d()
ydr3 = DataRange1d()
p3 = Plot(x_range=xdr3, y_range=ydr3, plot_width=100, plot_height=100)
text_raw3 = dict(xs=[20], ys=[20], text=["3Placeholder"])
text_CDS3 = ColumnDataSource(data=text_raw3)
text3 = Text(x="xs", y="ys", text="text")
p3.add_glyph(text_CDS3, text3)
p3.toolbar.logo = None

xdr4 = DataRange1d()
ydr4 = DataRange1d()
p4 = Plot(x_range=xdr4, y_range=ydr4, plot_width=100, plot_height=100)
text_raw4 = dict(xs=[20], ys=[20], text=["4Placeholder"])
text_CDS4 = ColumnDataSource(data=text_raw4)
text4 = Text(x="xs", y="ys", text="text")
p4.add_glyph(text_CDS4, text4)
p4.toolbar.logo = None

layout1 = layout(p1, button1, TI1)
layout2 = layout(p2, button2, TI2)
layout3 = layout(p3, button3, TI3)
layout4 = layout(p4, button4, TI4)

layout_ = gridplot([[layout1, layout2], [layout3,layout4]])

show(layout_)

