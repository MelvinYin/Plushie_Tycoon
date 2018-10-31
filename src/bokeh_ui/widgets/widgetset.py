from bokeh.layouts import row, column

try:
    from .individual import TransactionWidget, ButtonWidget
except ModuleNotFoundError:
    from individual import TransactionWidget, ButtonWidget


class WidgetSet:
    def __init__(self, callback, specs):
        self.widgets = self._construct_individual_widgets(callback,
                                                          specs.widget)
        self.layout = self._assemble_layout(specs.set)

    def _construct_individual_widgets(self, callback, specs):
        widgets = []
        widgets.append(TransactionWidget(callback, specs.transaction_1))
        widgets.append(ButtonWidget(callback, specs.button_1))
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


