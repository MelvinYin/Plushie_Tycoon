from bokeh.layouts import row, column
import inspect

from logs import log
from config.global_config import FigSpecs
from config.global_config import FigureNames as FigNms
from figures.individual_figure import IndividualFigure, ConsoleOutput, \
    ResourceRatioTable, ItemPropertiesTable, ItemCostTable
from widgets.individual import TransactionWidget, ButtonWidget

class UI:
    def __init__(self, ui_callback):
        """
        UI_callback: Takes in as input (<Func:...>, (args)), return as output
        a dict that is used to update figure_set.
        """
        self.ui_callback = ui_callback
        self.FigInstances = self._construct_individual_figures()
        self.transaction_widget = TransactionWidget(self.widget_callback)
        self.button_widget = ButtonWidget(self.widget_callback)
        self.ui_layout = self.plot()

    def _format_init_data(self, data):
        return data

    def _format_callback_data(self, data):
        return data

    def _construct_individual_figures(self, couple_range=True):
        call = dict()
        call['command'] = "init"
        tp, action = self._format_init_data(self.ui_callback(call))
        print(tp)
        if action == 'pause':
            return self.FigInstances

        inv_res = IndividualFigure(tp[FigNms.inventory_res],
                                   FigSpecs['inventory_res'])
        inv_prod = IndividualFigure(tp[FigNms.inventory_prod],
                                    FigSpecs['inventory_prod'])
        pr_res = IndividualFigure(tp[FigNms.price_res],
                                  FigSpecs['price_res'])
        pr_prod = IndividualFigure(tp[FigNms.price_prod],
                                   FigSpecs['price_prod'])
        budget = IndividualFigure(tp[FigNms.budget], FigSpecs['budget'])
        # couple range
        if couple_range:
            ref_x_range = inv_res.figure.x_range
            inv_prod.figure.x_range = ref_x_range
            pr_res.figure.x_range = ref_x_range
            pr_prod.figure.x_range = ref_x_range
            budget.figure.x_range = ref_x_range

        console = ConsoleOutput(tp[FigNms.console_output])
        ratio_t = ResourceRatioTable(tp[FigNms.res_ratio_table])
        prop_t = ItemPropertiesTable(tp[FigNms.item_properties_table])
        cost_t = ItemCostTable(tp[FigNms.item_cost_table])

        FigInsts = [inv_res, inv_prod, pr_res, pr_prod, budget, console,
                    ratio_t, prop_t, cost_t]
        return FigInsts

    def figure_update(self, tp):
        log(tp, inspect.currentframe())
        for FigInstance in self.FigInstances:
            value = tp[FigInstance.name]
            if value is not None:
                FigInstance.figure_update(value)
        return True

    def reload(self, new_data):
        self.FigInstances = self._construct_individual_figures(new_data)
        self.transaction_widget = TransactionWidget(self.widget_callback)
        self.button_widget = ButtonWidget(self.widget_callback)
        self.ui_layout = self.plot()

    def plot(self):
        figures_per_row = 3
        row_layouts = []
        tmp_row = []
        for FigInstance in self.FigInstances:
            tmp_row.append(FigInstance.figure)
            if len(tmp_row) == figures_per_row:
                row_layouts.append(row(tmp_row))
                tmp_row = []
        if tmp_row:
            row_layouts.append(row(tmp_row))
        layout_f = column(*row_layouts)
        layout_w = row(self.transaction_widget.layout, self.button_widget.layout)
        layout_main = column(layout_f, layout_w)
        return layout_main

    def widget_callback(self, call):
        updated_data, action = self.ui_callback(call)
        if action != 'update':
            return True
        updated_data = self._format_callback_data(updated_data)
        if updated_data:
            self.figure_update(updated_data)
        return True
