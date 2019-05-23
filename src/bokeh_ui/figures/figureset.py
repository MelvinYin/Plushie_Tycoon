from bokeh.layouts import row, column
import inspect

from logs import log
from global_config import Res, Prod, FigSpecs
from global_config import FigureNames as FigNms
from .individual_figure import IndividualFigure, ConsoleOutput, \
    ResourceRatioTable, ItemPropertiesTable, ItemCostTable
from ui_transporter import Transporter

class FigureSet:
    def __init__(self, full_data):
        self.FigInstances = self._construct_individual_figures(full_data)
        self.figures_per_row = 3
        self.layout = self._get_figure_layout()

    def _construct_individual_figures(self, tp, couple_range=True):
        assert isinstance(tp, Transporter)
        inv_res = IndividualFigure(tp.get(FigNms.inventory_res),
                             FigSpecs['inventory_res'])
        inv_prod = IndividualFigure(tp.get(FigNms.inventory_prod),
                             FigSpecs['inventory_prod'])
        pr_res = IndividualFigure(tp.get(FigNms.price_res),
                                  FigSpecs['price_res'])
        pr_prod = IndividualFigure(tp.get(FigNms.price_prod),
                                   FigSpecs['price_prod'])
        budget = IndividualFigure(tp.get(FigNms.budget), FigSpecs['budget'])
        # couple range
        if couple_range:
            ref_x_range = inv_res.figure.x_range
            inv_prod.figure.x_range = ref_x_range
            pr_res.figure.x_range = ref_x_range
            pr_prod.figure.x_range = ref_x_range
            budget.figure.x_range = ref_x_range

        console = ConsoleOutput(tp.get(FigNms.console_output))
        ratio_t = ResourceRatioTable(tp.get(FigNms.res_ratio_table))
        prop_t = ItemPropertiesTable(tp.get(FigNms.item_properties_table))
        cost_t = ItemCostTable(tp.get(FigNms.item_cost_table))

        FigInsts = [inv_res, inv_prod, pr_res, pr_prod, budget, console,
                    ratio_t, prop_t, cost_t]
        return FigInsts

    def _get_figure_layout(self):
        row_layouts = []
        tmp_row = []
        for FigInstance in self.FigInstances:
            tmp_row.append(FigInstance.figure)
            if len(tmp_row) == self.figures_per_row:
                row_layouts.append(row(tmp_row))
                tmp_row = []
        if tmp_row:
            row_layouts.append(row(tmp_row))
        figure_layout = column(*row_layouts)
        return figure_layout

    def figure_update(self, tp):
        log(tp, inspect.currentframe())
        for FigInstance in self.FigInstances:
            value = tp.get(FigInstance.name)
            if value is not None:
                FigInstance.figure_update(value)
        return True
