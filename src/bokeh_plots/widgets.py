
from individual_widget import IndividualWidget
from bokeh.layouts import row, column
from bokeh.plotting import output_file, show, curdoc
import sys
sys.path.append("../")
import defaults



class WidgetSet:
    def __init__(self, widget_callback, widget_ispecs=None):
        if not widget_ispecs:
            self.widget_ispecs = defaults.widget_ispecs
        else:
            self.widget_ispecs = widget_ispecs
        self.row_width = 5000   # no diff
        self.row_height = 200   # Distance between widget set rows
        self.widget_callback = widget_callback
        self.widgets = self._construct_individual_widgets()
        self.widget_layout = self._get_widget_layout()

    def _construct_individual_widgets(self):
        widgets = []
        for ispec in self.widget_ispecs:
            widgets.append(IndividualWidget(self.widget_callback, ispec).widget_layout)
        return widgets

    def _get_widget_layout(self):
        row_layouts = []
        tmp_row = []
        for widget in self.widgets:
            tmp_row.append(widget)
            if len(tmp_row) == defaults.widgets_per_row:
                _row = row(tmp_row)
                _row.width = self.row_width
                _row.height = self.row_height
                row_layouts.append(_row)
                tmp_row = []
        if tmp_row:
            _row = row(tmp_row)
            _row.width = self.row_width
            _row.height = self.row_height
            row_layouts.append(_row)
        widget_layout = column(*row_layouts)
        return widget_layout

# For testing
if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    def main():
        from collections import namedtuple
        from enum import Enum, auto
        class Func(Enum):
            buy_res = auto()
            sell_res = auto()
            buy_prod = auto()
            make_prod = auto()
            sell_prod = auto()
            show_stats = auto()
            show_prices = auto()
            save = auto()
            load = auto()
            quit = auto()
            save_quit = auto()
            next_turn = auto()
            show_history = auto()
            back = auto()
            start = auto()

        class Res(Enum):
            cloth = 1
            stuff = 2
            accessory = 3
            packaging = 4

        class Prod(Enum):
            aisha = 1
            beta = 2
            chama = 3

        class Others(Enum):
            reset = auto()

        widget_iindices = ["name", "title", "button_label", "TI_placeholder",
                           "RBG_labels"]
        WidgetIspecs = namedtuple("WidgetIspecs", widget_iindices)
        widget_ispecs_1 = WidgetIspecs(
            name=Func.buy_res,
            title="buy_res",
            button_label="buy",
            TI_placeholder="Placeholder",
            RBG_labels=list(Res) + [Others.reset])

        widget_ispecs_3 = WidgetIspecs(
            name=Func.buy_prod,
            title="buy_prod",
            button_label="buy",
            TI_placeholder="Placeholder",
            RBG_labels=list(Prod) + [Others.reset])

        def widget_callback(command_to_run):
            print("from widget callback")
            print(command_to_run)
            return

        output_file("../../bokeh_tmp/line.html")
        layout_w = WidgetSet(widget_callback,
                             [widget_ispecs_1, widget_ispecs_3]).widget_layout
        curdoc().add_root(layout_w)
        # show(layout_w)


    main()
    # Expected output: tuple(<Func.something>, <Res.something>, int of quantity)

