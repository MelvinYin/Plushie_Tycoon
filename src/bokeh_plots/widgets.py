from individual_widget import IndividualWidget
from bokeh.layouts import row, column
from bokeh.plotting import output_file, show
import sys
sys.path.append("../")
import defaults


class WidgetSet:
    def __init__(self, widget_callback):
        self.widget_ispecs = defaults.widget_ispecs
        self.row_width = 5000   # no diff
        self.row_height = 200   # Distance between widget set rows
        self.widget_callback = widget_callback
        self.widgets = self._construct_individual_widgets()
        self.widget_layout = self._get_widget_layout()

    def _construct_individual_widgets(self):
        widgets = []
        for ispec in self.widget_ispecs:
            widgets.append(IndividualWidget(ispec, self.widget_callback).widget)
        return widgets

    def _get_widget_layout(self):
        row_layouts = []
        tmp_row = []
        for widget in self.widgets:
            tmp_row.append(widget)
            if len(tmp_row) == defaults.widgets_per_row:
                row_layouts.append(row(tmp_row))
                tmp_row = []
        if tmp_row:
            _row = row(tmp_row)
            _row.width = self.row_width
            _row.height = self.row_height
            row_layouts.append(_row)
        widget_layout = column(*row_layouts)
        return widget_layout

if __name__ == "__main__":
    output_file("../../bokeh_tmp/line.html")
    layout_w = WidgetSet(lambda x: x).widget_layout
    show(layout_w)
