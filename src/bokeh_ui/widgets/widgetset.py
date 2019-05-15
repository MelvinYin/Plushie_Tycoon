from bokeh.layouts import row, column

try:
    from .individual import TransactionWidget, ButtonWidget
except ModuleNotFoundError:
    from individual import TransactionWidget, ButtonWidget


class WidgetSet:
    def __init__(self, callback):
        self.widgets_per_row = 3
        self.width = 0
        self.height = 0
        self.widgets = self._construct_individual_widgets(callback)
        self.layout = self._assemble_layout()

    def _construct_individual_widgets(self, callback):
        widgets = []
        widgets.append(TransactionWidget(callback))
        widgets.append(ButtonWidget(callback))
        return widgets

    def _assemble_layout(self):
        row_layouts = []
        tmp_row = []
        for widget in self.widgets:
            tmp_row.append(widget.layout)
            if len(tmp_row) == self.widgets_per_row:
                _row = row(tmp_row)
                _row.width = self.width
                _row.height = self.height
                row_layouts.append(_row)
                tmp_row = []
        if tmp_row:
            _row = row(tmp_row)
            _row.width = self.width
            _row.height = self.height
            row_layouts.append(_row)
        layout = column(*row_layouts)
        return layout


