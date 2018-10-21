import sys
sys.path.append("../")
from bokeh.plotting import figure, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
from config.global_config import Res, Prod
try:
    from .individual_figure import IndividualFigure
except:
    from individual_figure import IndividualFigure

class FigureSet:
    def __init__(self, full_data, specs):
        self.FigureInstances = self._construct_individual_figures(full_data,
                                                                  specs.figure)
        self._couple_range()
        self.layout = self._get_figure_layout(specs.set)

    def _construct_individual_figures(self, full_data, specs):
        FigureInstances = []
        res_data = full_data[Res]
        FigureInstances.append(IndividualFigure(res_data, specs.res))
        prod_data = full_data[Prod]
        FigureInstances.append(IndividualFigure(prod_data, specs.prod))
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
        for fig_label, value in data_to_add.items():
            found_fig = False
            for FigureInstance in self.FigureInstances:
                if FigureInstance.name.tag == fig_label.tag:
                    FigureInstance.figure_update(value)
                    found_fig = True
                    break
            if not found_fig:
                raise Exception
        return True

if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    def main():
        from mocked import mock_init, mock_update1, mock_update2, mock_update3
        from config.figure import FigureSpecs

        fig = FigureSet(mock_init, FigureSpecs())
        fig.figure_update(mock_update1)
        fig.figure_update(mock_update2)
        fig.figure_update(mock_update3)
        layout_w = fig.layout
        if __name__ == "__main__":
            show(layout_w)
        else:
            curdoc().add_root(layout_w)

    main()