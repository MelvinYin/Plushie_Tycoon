
from individual_widget import IndividualWidget, ButtonWidget
from bokeh.layouts import row, column
from bokeh.plotting import output_file, show, curdoc
import sys
sys.path.append("../")
from collections import namedtuple


class WidgetSet:
    def __init__(self, callback, setspecs, specs):
        self.widgets = self._construct_individual_widgets(specs, callback)
        self.layout = self._assemble_layout(setspecs)

    def _construct_individual_widgets(self, specs, callback):
        widgets = []
        for spec in specs:
            if spec.id == "standard":
                widgets.append(IndividualWidget(callback, spec))
            elif spec.id == "button":
                widgets.append(ButtonWidget(callback, spec))
            else:
                print("Unrecognised widget format.")
                raise Exception
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
    from defaults import widget_setspecs, widget_specs

    def widget_callback(command_to_run):
        print("from widget callback")
        print(command_to_run)
        return

    output_file("../../bokeh_tmp/line.html")
    layout_w = WidgetSet(widget_callback, widget_setspecs, widget_specs).layout
    if __name__ == "__main__":
        show(layout_w)
    else:
        curdoc().add_root(layout_w)
    # Expected output: tuple(<Func.something>, <Res.something>, int of quantity)

