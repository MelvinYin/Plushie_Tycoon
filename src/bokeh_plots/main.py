import sys
sys.path.append("../")
from widgets import WidgetSet
from figures import FigureSet
from bokeh.plotting import output_file, show, curdoc
from bokeh.layouts import column
# TODO: defaults need to add in label of individual widgets, and figs

output_file("../../bokeh_tmp/line.html")

class main:
    def __init__(self):
        self.figure_set = FigureSet()
        self.i = 8
        self.wid_set = WidgetSet(self.widget_callback)

    def figure_update(self, update_values):
        self.i += 1
        return self.figure_set.figure_update(update_values)

    def widget_callback(self, *args):
        data_to_append = dict()
        data_to_append[self.i] = [self.i+12]

        self.figure_update(["fig_4", data_to_append])

    def main(self):
        layout_w = self.wid_set.widget_layout
        layout_f = self.figure_set.figure_layout

        layout_full = column(layout_f, layout_w)

        # show(layout_full)
        curdoc().add_root(layout_full)


# if __name__ == "__main__":
#     output_file("../../bokeh_tmp/line.html")
#     figure_set = main().main()
#     show(figure_set)

main().main()

