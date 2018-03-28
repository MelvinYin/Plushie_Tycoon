
from individual_widget import IndividualWidget, ButtonWidget
from bokeh.layouts import row, column
from bokeh.plotting import output_file, show, curdoc
import sys
sys.path.append("../")
from collections import namedtuple


class WidgetSet:
    def __init__(self, widget_callback, widget_gspecs, widget_ispecs):
        self.widget_callback = widget_callback
        self.widgets = self._construct_individual_widgets(widget_ispecs, widget_gspecs)
        self.widget_layout = self._get_widget_layout(widget_gspecs)

    def _construct_individual_widgets(self, widget_ispecs, widget_gspecs):
        widgets = []
        MergedSpec = namedtuple("widget_spec", widget_ispecs[0]._fields + widget_gspecs._fields)
        for ispec in widget_ispecs:
            merged_spec = MergedSpec(*(ispec + widget_gspecs))
            if ispec.format == "standard":
                widgets.append(IndividualWidget(self.widget_callback, merged_spec).widget_layout)
            elif ispec.format == "button":
                widgets.append(ButtonWidget(self.widget_callback,
                                                merged_spec).widget_layout)
            else:
                print("Unrecognised widget format.")
                raise Exception
        return widgets

    def _get_widget_layout(self, widget_gspecs):
        row_layouts = []
        tmp_row = []
        for widget in self.widgets:
            tmp_row.append(widget)
            if len(tmp_row) == widget_gspecs.widgets_per_row:
                _row = row(tmp_row)
                _row.width = widget_gspecs.row_width
                _row.height = widget_gspecs.row_height
                row_layouts.append(_row)
                tmp_row = []
        if tmp_row:
            _row = row(tmp_row)
            _row.width = widget_gspecs.row_width
            _row.height = widget_gspecs.row_height
            row_layouts.append(_row)
        widget_layout = column(*row_layouts)
        return widget_layout

# For testing
if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    import sys
    import os
    sys.path.append(os.getcwd().rsplit("\\", 1)[0])
    from defaults import widget_ispecs_1, widget_ispecs_3, widget_gspecs, widget_ispecs_6

    def widget_callback(command_to_run):
        print("from widget callback")
        print(command_to_run)
        return

    output_file("../../bokeh_tmp/line.html")
    layout_w = WidgetSet(widget_callback, widget_gspecs,
                         [widget_ispecs_1, widget_ispecs_3, widget_ispecs_6]).widget_layout
    if __name__ == "__main__":
        show(layout_w)
    else:
        curdoc().add_root(layout_w)
    # Expected output: tuple(<Func.something>, <Res.something>, int of quantity)

