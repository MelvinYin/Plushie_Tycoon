import sys
sys.path.append("../")
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
from bokeh_plots.individual_figure import IndividualFigure


"""
Assume initial_func_count must be an int => equal across all figures.

"""

class FigureSet:
    def __init__(self, full_data, figure_ispecs, figure_gspecs, initial_func_count=None):
        self.full_data = full_data
        self.figure_ispecs = figure_ispecs
        assert len(self.full_data) == len(self.figure_ispecs)
        self.figure_gspecs = figure_gspecs
        self.FigureInstances = self._construct_individual_figures(initial_func_count)
        self._couple_range()
        self.figure_layout = self._get_figure_layout()

    def _construct_individual_figures(self, initial_func_count=None):
        FigureInstances = []
        for data, figure_spec in zip(self.full_data, self.figure_ispecs):
            FigureInstances.append(IndividualFigure(data, figure_spec, initial_func_count))
        return FigureInstances

    def _couple_range(self):
        ref_x_range = self.FigureInstances[0].figure.x_range
        for FigureInstances in self.FigureInstances:
            FigureInstances.figure.x_range = ref_x_range
        return True

    def _get_figure_layout(self):
        row_layouts = []
        tmp_row = []
        for FigureInstances in self.FigureInstances:
            tmp_row.append(FigureInstances.figure)
            if len(tmp_row) == self.figure_gspecs.figures_per_row:
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
                if FigureInstance.name == fig_label:
                    FigureInstance.figure_update(value)
                    found_fig = True
                    break
            if not found_fig:
                raise Exception
        return True

if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    def main():
        from collections import namedtuple
        from enum import Enum
        import random
        random.seed(10)

        example_max_points=15

        def example_data_1(max_pts=example_max_points):
            data = []
            for i in range(3, 11):
                length = random.randint(1, 4)
                for j in range(length):
                    if max_pts:
                        data.append((i, random.randint(1, 50)))
                    max_pts -= 1
            return data

        def example_data_2(max_pts=example_max_points):
            data = []
            for i in range(2, 7):
                length = random.randint(3, 6)
                for j in range(length):
                    if max_pts:
                        data.append((i, random.randint(2, 45)))
                    max_pts -= 1
            return data

        class Prod(Enum):
            aisha = 1
            beta = 2
            chama = 3

        class Res(Enum):
            cloth = 1
            stuff = 2
            accessory = 3
            packaging = 4

        fig_iindices = ("name", "title", "x_label", "y_label")
        FigureIspecs = namedtuple("FigureIspecs", fig_iindices)
        figure_spec_1 = FigureIspecs(Res.cloth, "title", "x_", "y_")
        figure_spec_5 = FigureIspecs(Prod.aisha, "title", "x_", "y_")

        figure_gindices = ("figures_per_row",)
        FigureGspec = namedtuple("FigureGspec", figure_gindices)
        figure_gspecs = FigureGspec(figures_per_row=3)

        output_file("../../bokeh_tmp/line.html")
        layout_w = FigureSet([example_data_1(), example_data_2()],
                             [figure_spec_1, figure_spec_5], figure_gspecs, initial_func_count=12).figure_layout
        if __name__ == "__main__":
            show(layout_w)
        else:
            curdoc().add_root(layout_w)
    main()