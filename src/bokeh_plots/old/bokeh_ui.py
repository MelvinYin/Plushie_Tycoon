import sys
sys.path.append("../")
from bokeh_plots.widgets import WidgetSet
from bokeh_plots.figures import FigureSet
from bokeh.plotting import output_file, show, curdoc
from bokeh.layouts import column
import re
from defaults import Func
class Bokeh_UI:
    def __init__(self, widget_callback):
        self.figure_set = FigureSet()
        self.widget_set = WidgetSet(widget_callback)
        self.launch_ui()

    def figure_update(self, update_values):
        figure_update_succeed = self.figure_set.figure_update(update_values)
        return figure_update_succeed

    def launch_ui(self):
        output_file("../../bokeh_tmp/line.html")
        layout_w = self.widget_set.widget_layout
        layout_f = self.figure_set.figure_layout
        layout_full = column(layout_f, layout_w)
        show(layout_full)
        # curdoc().add_root(layout_full)



# if __name__ == "__main__":
#     output_file("../../bokeh_tmp/line.html")
#     figure_set = main().main()
#     show(figure_set)

# main().main()