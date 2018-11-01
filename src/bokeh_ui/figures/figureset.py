from bokeh.layouts import row, column
import inspect

from logs import log
from global_config import Res, Prod, FigureNames
from .individual_figure import IndividualFigure

class FigureSet:
    def __init__(self, full_data, specs):
        self.FigureInstances = self._construct_individual_figures(full_data,
                                                                  specs.figure)
        self._couple_range()
        self.layout = self._get_figure_layout(specs.set)

    def _construct_individual_figures(self, full_data, specs):
        FigureInstances = []
        FigureInstances.append(
            IndividualFigure(full_data[FigureNames.inventory_res],
                             specs.inventory_res))
        FigureInstances.append(
            IndividualFigure(full_data[FigureNames.inventory_prod],
                             specs.inventory_prod))
        FigureInstances.append(
            IndividualFigure(full_data[FigureNames.price_res],
                             specs.price_res))
        FigureInstances.append(
            IndividualFigure(full_data[FigureNames.price_prod],
                             specs.price_prod))
        FigureInstances.append(
            IndividualFigure(full_data[FigureNames.budget],
                             specs.budget))
        return FigureInstances

    def _couple_range(self):
        ref_x_range = self.FigureInstances[0].figure.x_range
        for FigureInstances in self.FigureInstances:
            FigureInstances.figure.x_range = ref_x_range
        return True

    def _get_figure_layout(self, FigureSetSpecs):
        row_layouts = []
        tmp_row = []
        for FigureInstances in self.FigureInstances:
            tmp_row.append(FigureInstances.figure)
            if len(tmp_row) == FigureSetSpecs.figures_per_row:
                row_layouts.append(row(tmp_row))
                tmp_row = []
        if tmp_row:
            row_layouts.append(row(tmp_row))
        figure_layout = column(*row_layouts)
        return figure_layout

    def figure_update(self, data_to_add):
        log(data_to_add, inspect.currentframe())
        for fig_label, value in data_to_add.items():
            for FigureInstance in self.FigureInstances:
                if FigureInstance.name == fig_label:
                    FigureInstance.figure_update(value)
                    break
        return True
