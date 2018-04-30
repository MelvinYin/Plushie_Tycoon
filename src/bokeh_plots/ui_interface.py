from figures import FigureSet
from widgets import WidgetSet
from bokeh.plotting import curdoc, show
from bokeh.layouts import column
from defaults import FigureSetSpecs, FigureSpecs, WidgetSetSpecs, WidgetSpecs
from collections import defaultdict
import defaults

class UIInterface:
    def __init__(self, initial_data, ui_callback):
        """
        UI_callback: Takes in as input (<Func:...>, (args)), return as output
        a dict that is used to update figure_set.
        """
        self.ui_callback = ui_callback
        self.initial_data = self.temp_bulk_adapt_ge_to_ui(initial_data)
        # self.initial_data = initial_data
        self.figure_set = FigureSet(self.initial_data, FigureSetSpecs, FigureSpecs)
        self.widget_set = WidgetSet(self.widget_callback, WidgetSetSpecs, WidgetSpecs)
        self.ui_layout = self.plot()

    def _mock_call(self):
        mock_call_1 = (Func.buy_res, (Res.stuff, 10))
        self.widget_callback(mock_call_1)

    def plot(self):
        layout_f = self.figure_set.figure_layout
        layout_w = self.widget_set.widget_layout
        layout_main = column(layout_f, layout_w)
        return layout_main

    def widget_callback(self, call):
        if call[0] == defaults.Others.quit:
            sys.exit()
        else:
            to_add = self.ui_callback(call)
            to_ui = self.temp_adapt_ge_to_ui(to_add)
            self.figure_set.figure_update(to_ui)
        return True

    def temp_adapt_ge_to_ui(self, from_ge):
        to_ui = dict()
        time_step = from_ge["time_steps"]
        for key, value in from_ge.items():
            if key != "time_steps":
                to_ui[key] = (time_step, value)
        return to_ui

    def temp_bulk_adapt_ge_to_ui(self, from_ge_init):
        to_ui_init = dict()
        time_steps = from_ge_init['time_steps']
        for key, values in from_ge_init.items():
            if key != "time_steps":
                tmp = []
                for i, value in enumerate(values):
                    tmp.append((time_steps[i], value))
                to_ui_init[key] = tmp
        return to_ui_init


if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    import random
    import sys
    import os
    sys.path.append(os.getcwd().rsplit("\\", 1)[0])
    from defaults import Func, Res, Prod, Others
    random.seed(10)
    example_max_points = 15
    xs = []
    curr_x = 3
    for i in range(random.randint(4, 7)):
        for j in range(random.randint(1, 5)):
            xs.append(curr_x)
        curr_x += 1

    example_data_1 = []
    example_data_2 = []
    for x in xs:
        example_data_1.append((x, random.randint(1, 50)))
        example_data_2.append((x, random.randint(1, 50)))

    def _get_example_data():
        figure_ispecs = defaults.figure_ispecs
        full_data = []
        for i in range(len(figure_ispecs)):
            if i % 2 == 0:
                full_data.append(example_data_1)
            else:
                full_data.append(example_data_2)
        return full_data

    tmp_i = 10
    def mocked_mapping(call):
        global tmp_i
        return_value = defaultdict(dict)
        return_value[Res.cloth] = (tmp_i, tmp_i * 2 + 50)
        return_value[Res.stuff] = (tmp_i, tmp_i * 2 + 50)
        return_value[Res.accessory] = (tmp_i, tmp_i * 2 + 50)
        return_value[Res.packaging] = (tmp_i, tmp_i * 2 + 50)
        return_value[Prod.aisha] = (tmp_i, tmp_i * 2 + 50)
        return_value[Prod.beta] = (tmp_i, tmp_i * 2 + 50)
        return_value[Prod.chama] = (tmp_i, tmp_i * 2 + 50)
        tmp_i += 1
        return return_value
    mock_call_1 = (Func.buy_res, (Res.stuff, 10))
    mock_call_2 = (Func.sell_prod, (Prod.chama, 20))
    mock_call_3 = (Others, Others.next_turn)
    if __name__ == "__main__":
        x = UIInterface(_get_example_data(), mocked_mapping)
        x.widget_callback(mock_call_1)
        x.widget_callback(mock_call_2)
        x.widget_callback(mock_call_3)
        show(x.ui_layout)
    else:
        x = UIInterface(_get_example_data(), mocked_mapping)
        curdoc().add_root(x.ui_layout)





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




"""




"""

























