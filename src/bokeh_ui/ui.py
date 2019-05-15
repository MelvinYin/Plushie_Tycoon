from figures.figureset import FigureSet
from widgets.widgetset import WidgetSet
from bokeh.layouts import column
from exceptions import InvalidInputException, InsufficientQuantityError
from global_config import Res, Prod, Func
from collections import defaultdict
import inspect
from logs import log

class UI:
    def __init__(self, initial_data, ui_callback, specs):
        """
        UI_callback: Takes in as input (<Func:...>, (args)), return as output
        a dict that is used to update figure_set.
        """
        self.ui_callback = ui_callback
        self.specs = specs
        self.figure_set = FigureSet(initial_data)
        self.widget_set = WidgetSet(self.widget_callback, specs.widgets)
        self.ui_layout = self.plot()

    def reload(self, new_data):
        self.figure_set = FigureSet(new_data)
        self.widget_set = WidgetSet(self.widget_callback, self.specs.widgets)
        self.ui_layout = self.plot()

    def plot(self):
        layout_f = self.figure_set.layout
        layout_w = self.widget_set.layout
        layout_main = column(layout_f, layout_w)
        return layout_main

    def widget_callback(self, call):
        updated_data = self.ui_callback(call)
        if updated_data:
            self.figure_set.figure_update(updated_data)
        return True
