from ge import GEM
from figures import FigureSet
from widgets import WidgetSet
from exceptions import RepeatUIAction
from bokeh.plotting import curdoc, show
from bokeh.layouts import column

class UIInterface:
    def __init__(self):
        self.figure_set = FigureSet()
        self.widget_set = WidgetSet(self.widget_callback)
        self.ge = GEM()


        layout_f = FigureSet().figure_layout
        layout_w = WidgetSet(self.widget_callback).widget_layout
        show(column(layout_f, layout_w))
        curdoc().add_root(column(layout_f, layout_w)) # need a plot function later in UIInterface

    def widget_callback(self, command_to_run):
        try:
            to_add = self.ge.callback(command_to_run)
        except RepeatUIAction:
            return False    # for now
        self.figure_set.figure_update(to_add)
        return True

"""
widget_callback need to be supplied to widget_set, whose args is what widgets 
will provide, i.e. tuple(<Func.something>, <Res.something>, int of quantity).
Does not need to return anything, just need to call figure_update in its body.

figure_update is a command that need to be called, for the figures to be updated.
Input args need to be a dict, whose key is label of each figure, from
Res.cloth, etc. Value is a dict, whose key is time_steps and value is the 
value desired. (keeping it like this for now).

GEM now has a callback mtd that can be sent.

"""


if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    x = UIInterface()