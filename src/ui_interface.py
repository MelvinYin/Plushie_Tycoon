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
        self.specs = specs
        self.ui = UI(self._adapt_for_ui(initial_data), self.callback, specs)

    def callback(self, call):
        log(call, inspect.currentframe())
        try:
            updated_data, to_do = self.raw_callback(call)
        except InvalidInputException:
            return False
        except InsufficientQuantityError:
            return False
        except:
            raise
        if to_do == 'update':
            cleaned_output = self._adapt_for_ui(updated_data)
            log(cleaned_output, inspect.currentframe())
        elif to_do == "reload":
            cleaned_output = self._adapt_for_ui(updated_data)
            log(cleaned_output, inspect.currentframe())
            # self.ui.reload(cleaned_output)
            self.ui = UI(cleaned_output, self.callback, self.specs)
            return None
        elif to_do == 'pause':
            return None
        else:
            raise Exception
        return cleaned_output

    def _adapt_for_ui(self, GSDataClass):
        adapted = defaultdict(dict)
        input_to_res = GSDataClass.inventory[Res]
        for key, values in input_to_res.items():
            adapted[FigureNames.inventory_res][key.name] = [values]
        adapted[FigureNames.inventory_res]['time'] = [GSDataClass.time]

        input_to_prod = GSDataClass.inventory[Prod]
        for key, values in input_to_prod.items():
            adapted[FigureNames.inventory_prod][key.name] = [values]
        adapted[FigureNames.inventory_prod]['time'] = [GSDataClass.time]

        input_to_res = GSDataClass.market[Res]
        for key, values in input_to_res.items():
            adapted[FigureNames.price_res][key.name] = [values]
        adapted[FigureNames.price_res]['time'] = [GSDataClass.time]

        input_to_prod = GSDataClass.market[Prod]
        for key, values in input_to_prod.items():
            adapted[FigureNames.price_prod][key.name] = [values]
        adapted[FigureNames.price_prod]['time'] = [GSDataClass.time]

        input_to_prod = GSDataClass.budget
        for key, values in input_to_prod.items():
            adapted[FigureNames.budget][key] = [values]
        adapted[FigureNames.budget]['time'] = [GSDataClass.time]

        adapted = dict(adapted)
        log(adapted, inspect.currentframe())
        return adapted

    def __getattr__(self, item):
        return self.ui.__getattribute__(item)