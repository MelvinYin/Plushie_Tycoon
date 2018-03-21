from ui_interface import UIInterface
# TODO: defaults need to add in label of individual widgets, and figs
from widgets import WholeWidgetSet
from figures import WholeFigSet
from bokeh.plotting import output_file, show, curdoc
from bokeh.layouts import column

output_file("../../bokeh_tmp/line.html")

class main:
    def __init__(self):
        self.fig_set = WholeFigSet()
        self.i = 8
        self.wid_set = WholeWidgetSet(self.widget_callback)


    def figure_update(self, update_values):
        self.i += 1
        return self.fig_set.fig_update(update_values)

    def widget_callback(self, *args):
        data_to_append = dict()
        data_to_append["xs"] = [self.i]
        data_to_append["ys"] = [self.i+12]
        data_to_append["time_steps_for_hover"] = [self.i]

        self.figure_update(["p1", data_to_append])

    def main(self):
        layout_w = self.wid_set.get_widget_set()
        layout_f = self.fig_set.full_fig_set

        layout_full = column(layout_f, layout_w)

        # show(layout_full)
        curdoc().add_root(layout_full)

main().main()

