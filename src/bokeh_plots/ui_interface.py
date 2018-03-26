from figures import FigureSet
from widgets import WidgetSet
from exceptions import RepeatUIAction
from bokeh.plotting import curdoc, show
from bokeh.layouts import column
from defaults import Func, Res, Prod
from collections import defaultdict
import defaults
import sys

class UIInterface:
    def __init__(self):
        self.figure_set = FigureSet()
        self.widget_set = WidgetSet(self.widget_callback)
        self.tmp_i = 10

    def plot(self):
        layout_f = self.figure_set.figure_layout
        layout_w = self.widget_set.widget_layout
        layout_main = column(layout_f, layout_w)
        return layout_main


    def widget_callback(self, call):
        if call[0] == defaults.Others.next:
            to_add = self.mocked_mapping(call)
            self.figure_set.figure_update_next_turn(to_add)
        elif call[0] == defaults.Others.quit:
            sys.exit()
        else:
            to_add = self.mocked_mapping(call)
            self.figure_set.figure_update(to_add)
        return True

    def mocked_mapping(self, call):
        return_value = defaultdict(dict)
        return_value[Res.cloth][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Res.stuff][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Res.accessory][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Res.packaging][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Prod.aisha][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Prod.beta][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Prod.chama][self.tmp_i] = self.tmp_i * 2 + 50
        self.tmp_i += 1
        return return_value

    def mock_call(self):
        mock_call_1 = (Func.buy_res, (Res.cloth, [10]))
        self.widget_callback(mock_call_1)

if __name__ == "__main__":
    x = UIInterface()
    # x.mock_call()
    layout = x.plot()
    show(layout)
elif str(__name__).startswith("bk_script"):
    x = UIInterface()
    # x.mock_call()
    layout = x.plot()
    curdoc().add_root(layout)







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






























