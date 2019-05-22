from bokeh.layouts import row, column
import inspect

from logs import log
from global_config import Res, Prod, FigureNames, FigSpecs
from .individual_figure import IndividualFigure, ConsoleOutput, \
    ResourceRatioTable, ItemPropertiesTable

class FigureSet:
    def __init__(self, full_data):
        self.FigInstances = self._construct_individual_figures(full_data)
        self._couple_range()
        self.figures_per_row = 3
        self.layout = self._get_figure_layout()

    def _construct_individual_figures(self, full_data):
        FigInstances = []
        FigInstances.append(
            IndividualFigure(full_data[FigureNames.inventory_res],
                             FigSpecs['inventory_res']))
        FigInstances.append(
            IndividualFigure(full_data[FigureNames.inventory_prod],
                             FigSpecs['inventory_prod']))
        FigInstances.append(
            IndividualFigure(full_data[FigureNames.price_res],
                             FigSpecs['price_res']))
        FigInstances.append(
            IndividualFigure(full_data[FigureNames.price_prod],
                             FigSpecs['price_prod']))
        FigInstances.append(
            IndividualFigure(full_data[FigureNames.budget],
                             FigSpecs['budget']))
        FigInstances.append(ConsoleOutput())
        FigInstances.append(ResourceRatioTable(
            full_data[FigureNames.res_ratio_table]))
        FigInstances.append(ItemPropertiesTable(
            full_data[FigureNames.item_properties_table]))
        # FigInstances.append(MoveCostTable(
        #     full_data[FigureNames.move_cost_table],
        #     specs.move_cost_table))
        return FigInstances

    def _couple_range(self):
        ref_x_range = self.FigInstances[0].figure.x_range
        self.FigInstances[1].figure.x_range = ref_x_range
        self.FigInstances[2].figure.x_range = ref_x_range
        self.FigInstances[3].figure.x_range = ref_x_range
        self.FigInstances[4].figure.x_range = ref_x_range
        return True

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

    def figure_update(self, data_to_add):
        log(data_to_add, inspect.currentframe())
        for fig_label, value in data_to_add.items():
            for FigInstance in self.FigInstances:
                if FigInstance.name == fig_label:
                    FigInstance.figure_update(value)
                    break
        return True
