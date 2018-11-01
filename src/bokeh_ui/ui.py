from .figures.figureset import FigureSet
from .widgets.widgetset import WidgetSet
from bokeh.layouts import column
from exceptions import InvalidInputException, InsufficientQuantityError
from global_config import Res, Prod
from collections import defaultdict

class UI:
    def __init__(self, initial_data, ui_callback, specs):
        """
        UI_callback: Takes in as input (<Func:...>, (args)), return as output
        a dict that is used to update figure_set.
        """
        self.ui_callback = ui_callback
        self.initial_data = self._clean_ui_input(initial_data)
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
        to_add = self._clean_ui_input(to_add)
        self.figure_set.figure_update(to_add)
        return True

    def _clean_ui_input(self, ui_input):
        to_ui = defaultdict(dict)
        input_to_res = ui_input[Res]
        for key, values in input_to_res.items():
            print(input_to_res)
            to_ui['Res'][key.name] = values
        to_ui['Res']['time'] = ui_input['time']
        input_to_prod = ui_input[Prod]
        for key, values in input_to_prod.items():
            to_ui['Prod'][key.name] = values
        to_ui['Res']['time'] = ui_input['time']
        to_ui = dict(to_ui)
        return to_ui
