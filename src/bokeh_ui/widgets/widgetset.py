
from individual import TransactionWidget, ButtonWidget
from bokeh.layouts import row, column
from bokeh.plotting import output_file, show, curdoc
import sys
sys.path.append("../")

from widget_config import set_specs

# TO USE
# layout_w = WidgetSet(widget_callback).layout

class WidgetSet:
    def __init__(self, callback, setspecs=set_specs):
        self.widgets = self._construct_individual_widgets(callback)
        self.layout = self._assemble_layout(setspecs)

    def _construct_individual_widgets(self, callback):
        widgets = []
        widgets.append(TransactionWidget(callback))
        widgets.append(ButtonWidget(callback))
        return widgets

    def _assemble_layout(self, setspecs):
        row_layouts = []
        tmp_row = []
        for widget in self.widgets:
            tmp_row.append(widget.layout)
            if len(tmp_row) == setspecs.widgets_per_row:
                _row = row(tmp_row)
                _row.width = setspecs.width
                _row.height = setspecs.height
                row_layouts.append(_row)
                tmp_row = []
        if tmp_row:
            _row = row(tmp_row)
            _row.width = setspecs.width
            _row.height = setspecs.height
            row_layouts.append(_row)
        layout = column(*row_layouts)
        return layout

# For testing
if __name__ == "__main__" or str(__name__).startswith("bk_script"):

    def widget_callback(command_to_run):
        print("from widget callback")
        print(command_to_run)
        return

    layout_w = WidgetSet(widget_callback).layout
    if __name__ == "__main__":
        show(layout_w)
    else:
        curdoc().add_root(layout_w)
    # Expected output: tuple(<Func.something>, <Res.something>, int of quantity)

