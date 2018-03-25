from ge import GEM
from bokeh_plots.bokeh_ui import Bokeh_UI
from bokeh.plotting import show


class Main:
    def __init__(self):
        self.GE = GEM()
        self.ui = Bokeh_UI(self.widget_callback)

    def widget_callback(self, *args):
        # return
        callback = self.GE(*args)
        self.ui.figure_update(callback)

x = Main()
# show(x.ui.figure_set.figure_layout)