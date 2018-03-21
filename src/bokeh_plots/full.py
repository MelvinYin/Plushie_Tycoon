from widgets import WholeWidgetSet
from figures import WholeFigSet
from bokeh.plotting import output_file, show, curdoc
from bokeh.layouts import column
import os

print(os.getcwd())

output_file("../../bokeh_tmp/line.html")

layout_w = WholeWidgetSet().get_widget_set()
layout_f = WholeFigSet().full_fig_set

layout_full = column(layout_f, layout_w)

# show(layout_full)
curdoc().add_root(layout_full)