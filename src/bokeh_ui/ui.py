from figures.figureset import FigureSet
from widgets.widgetset import WidgetSet
from bokeh.plotting import curdoc, show
from bokeh.layouts import column

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
        to_add = self.ui_callback(call)
        self.figure_set.figure_update(to_add)
        return True


if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    from figures.mocked import mock_init, mock_update1, mock_update2, \
        mock_update3
    from widgets.mocked import mock_callbacks
    from config.global_config import UISpecs

    call_count = 0
    def callback(call):
        global call_count
        assert call in mock_callbacks
        if call_count == 0:
            call_count += 1
            return mock_update1
        elif call_count == 1:
            call_count += 1
            return mock_update2
        else:
            return mock_update3

    if __name__ == "__main__":
        x = UI(mock_init, callback, UISpecs())
        show(x.ui_layout)
    else:
        x = UI(mock_init, callback, UISpecs())
        curdoc().add_root(x.ui_layout)
























