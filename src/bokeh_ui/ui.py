from .figures.figureset import FigureSet
from .widgets.widgetset import WidgetSet
from bokeh.layouts import column
from exceptions import InvalidInputException, InsufficientQuantityError

class UI:
    def __init__(self, initial_data, ui_callback, specs):
        """
        UI_callback: Takes in as input (<Func:...>, (args)), return as output
        a dict that is used to update figure_set.
        """
        self.ui_callback = ui_callback
        self.initial_data = initial_data
        self.figure_set = FigureSet(self.initial_data, specs.figures)
        self.widget_set = WidgetSet(self.widget_callback, specs.widgets)
        self.ui_layout = self.plot()

    def plot(self):
        layout_f = self.figure_set.layout
        layout_w = self.widget_set.layout
        layout_main = column(layout_f, layout_w)
        return layout_main

    def widget_callback(self, call):
        try:
            to_add = self.ui_callback(call)
        except InvalidInputException:
            return False
        except InsufficientQuantityError:
            return False
        except:
            raise
        self.figure_set.figure_update(to_add)
        return True
