from figures import FigureSet
from widgets import WidgetSet
from bokeh.plotting import curdoc, show
from bokeh.layouts import column
from defaults import figure_setspecs, figure_specs, widget_setspecs, widget_specs
import defaults
import sys
from defaults import Res, Prod

class UIInterface:
    def __init__(self, initial_data, ui_callback):
        """
        UI_callback: Takes in as input (<Func:...>, (args)), return as output
        a dict that is used to update figure_set.
        """
        self.ui_callback = ui_callback
        self.initial_data = initial_data
        self.figure_set = FigureSet(self.initial_data, figure_setspecs, figure_specs)
        self.widget_set = WidgetSet(self.widget_callback, widget_setspecs, widget_specs)
        self.ui_layout = self.plot()

    def plot(self):
        layout_f = self.figure_set.layout
        layout_w = self.widget_set.layout
        layout_main = column(layout_f, layout_w)
        return layout_main

    def widget_callback(self, call):
        if call[0] == defaults.Others.quit:
            sys.exit()
        else:
            to_add = self.ui_callback(call)
            self.figure_set.figure_update(to_add)
        return True

    def check_inputs(self, initial_data, ui_callback):
        assert isinstance(initial_data, dict)
        keys1 = list(initial_data.keys())
        assert len(keys1) == 2
        assert Res in keys1
        assert Prod in keys1

        Res_values = initial_data[Res]
        keys = list(Res_values.keys())
        assert sorted(list(Res) + ['time']) == sorted(keys)

        Prod_values = initial_data[Prod]
        keys = list(Prod_values.keys())
        assert sorted(list(Prod) + ['time']) == sorted(keys)

        assert sorted(Res_values['time']) == Res_values['time']
        assert sorted(Prod_values['time']) == Prod_values['time']

        Res_cat_values = list(Res_values.values())
        ref_len = len(Res_cat_values[0])
        assert all([len(x) == ref_len for x in Res_cat_values])

        Prod_cat_values = list(Prod_values.values())
        ref_len = len(Prod_cat_values[0])
        assert all([len(x) == ref_len for x in Prod_cat_values])

        ###





if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    import random
    from defaults import Func, Res, Prod, Others
    from defaults import figure_setspecs, figure_specs, Res, Prod


    def get_initial_data1():
        data = dict()
        data['key_1'] = [1, 2, 3, 4, 5]
        data['key_2'] = [2, 3, 4, 5, 6]
        data['key_3'] = [5, 1, 4, 2, 4]
        data['time'] = [2, 3, 3, 3, 4]
        return data


    def get_initial_data2():
        data = dict()
        data['key_1'] = [11, 2, 3, 4, 5]
        data['key_2'] = [12, 3, 4, 5, 6]
        data['key_3'] = [15, 1, 4, 2, 4]
        data['time'] = [2, 2, 3, 3, 4]
        return data

    tot_fig_1 = dict()
    tot_fig_1[Res] = get_initial_data1()
    tot_fig_1[Prod] = get_initial_data2()


    def mocked_mapping(call):
        def to_add():
            data = dict()
            data['key_1'] = [random.randint(3, 15)]
            data['key_2'] = [random.randint(3, 15)]
            data['key_3'] = [random.randint(3, 15)]
            data['time'] = [5]
            return data
        data_to_add = dict()
        data_to_add[Res] = to_add()
        data_to_add[Prod] = to_add()
        return data_to_add

    def mocked_mapping2(call):
        def to_add():
            data = dict()
            data['key_1'] = [random.randint(3, 15)]
            data['key_2'] = [random.randint(3, 15)]
            data['key_3'] = [random.randint(3, 15)]
            data['time'] = [6]
            return data
        data_to_add = dict()
        data_to_add[Res] = to_add()
        data_to_add[Prod] = to_add()
        return data_to_add
    # mock_call_1 = (Func.buy_res, (Res.stuff, 10))
    # mock_call_2 = (Func.sell_prod, (Prod.chama, 20))
    # mock_call_3 = (Others, Others.next_turn)

    if __name__ == "__main__":
        x = UIInterface(tot_fig_1, mocked_mapping)
        # x.widget_callback(mock_call_1)
        # x.widget_callback(mock_call_2)
        # x.widget_callback(mock_call_3)
        show(x.ui_layout)
    else:
        x = UIInterface(tot_fig_1, mocked_mapping)
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

























