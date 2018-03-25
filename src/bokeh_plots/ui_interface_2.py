from figures import FigureSet
from widgets import WidgetSet
from exceptions import RepeatUIAction
from bokeh.plotting import curdoc, show
from bokeh.layouts import column
from defaults import Func, Res, Prod
from collections import defaultdict
import copy
import defaults

class UIInterface:
    def __init__(self):
        self.figure_set = FigureSet()
        self.widget_set = WidgetSet(self.widget_callback)
        self.tmp_i = 10

    def plot(self):
        layout_f = self.figure_set.figure_layout
        layout_w = self.widget_set.widget_layout
        layout_main = layout_w
        layout_main = column(layout_f, layout_w)
        # show(layout_main)
        curdoc().add_root(layout_main)

    def widget_callback(self, call):
        """
        :param call: tuple(<Func.something>, <Res.something>, int of quantity)
        """
        to_add = self.mocked_mapping(call)
        self.figure_set.figure_update(to_add)
        return True

    def mocked_mapping(self, call):
        loaded_figures = copy.deepcopy(defaults.loaded_figures)
        func_label, func_args = call[0], call[1:]
        assert func_label in Func
        # send_to_ge, get output
        return_value = defaultdict(dict)
        return_value[Res.cloth][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Res.stuff][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Res.accessory][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Res.packaging][self.tmp_i] = self.tmp_i * 2 + 50
        # loaded_figures.remove(Res.cloth)
        return_value[Prod.aisha][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Prod.beta][self.tmp_i] = self.tmp_i * 2 + 50
        return_value[Prod.chama][self.tmp_i] = self.tmp_i * 2 + 50

        self.tmp_i += 1
        return return_value

    def mock_call(self):
        mock_call_1 = (Func.buy_res, Res.cloth, [10])
        self.widget_callback(mock_call_1)

if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    x = UIInterface()
    x.mock_call()
    x.plot()


# TODO: I need some form of a fake iwdget callback input and output






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

