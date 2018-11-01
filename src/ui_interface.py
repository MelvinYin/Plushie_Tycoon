from figures.figureset import FigureSet
from widgets.widgetset import WidgetSet
from bokeh.layouts import column
from exceptions import InvalidInputException, InsufficientQuantityError
from global_config import Res, Prod, FigureNames
from collections import defaultdict
import inspect
from logs import log
from bokeh_ui.ui import UI

class UIInterface:
    def __init__(self, initial_data, ui_callback, specs):
        self.raw_callback = ui_callback
        self.ui = UI(self._adapt_for_ui(initial_data), self.callback, specs)

    def callback(self, call):
        log(call, inspect.currentframe())
        output = self.raw_callback(call)
        cleaned_output = self._adapt_for_ui(output)
        log(cleaned_output, inspect.currentframe())
        return cleaned_output

    def _adapt_for_ui(self, raw_data):
        adapted = defaultdict(dict)
        input_to_res = raw_data[Res]
        for key, values in input_to_res.items():
            adapted[FigureNames.inventory_res][key.name] = values
        adapted[FigureNames.inventory_res]['time'] = raw_data['time']

        input_to_prod = raw_data[Prod]
        for key, values in input_to_prod.items():
            adapted[FigureNames.inventory_prod][key.name] = values
        adapted[FigureNames.inventory_prod]['time'] = raw_data['time']

        input_to_prod = raw_data['price'][Res]
        for key, values in input_to_prod.items():
            adapted[FigureNames.price_res][key.name] = values
        adapted[FigureNames.price_res]['time'] = raw_data['time']

        input_to_prod = raw_data['price'][Prod]
        for key, values in input_to_prod.items():
            adapted[FigureNames.price_prod][key.name] = values
        adapted[FigureNames.price_prod]['time'] = raw_data['time']

        input_to_prod = raw_data['budget']
        for key, values in input_to_prod.items():
            adapted[FigureNames.budget][key] = values
        adapted[FigureNames.budget]['time'] = raw_data['time']

        adapted = dict(adapted)
        log(adapted, inspect.currentframe())
        return adapted

    def __getattr__(self, item):
        return self.ui.__getattribute__(item)