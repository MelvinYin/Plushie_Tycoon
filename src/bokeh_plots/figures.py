import sys
sys.path.append("../")
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
from bokeh_plots.individual_figure import IndividualFigure
import defaults

def example_data_1():
    data = dict()
    data[0] = [1,13, 23]
    data[1] = [23]
    data[2] = [34,23, 34]
    data[3] = [2]
    data[4] = [1,13, 23]
    data[5] = [23]
    data[6] = [34,23, 34]
    data[7] = [2]
    return data

def example_data_2():
    data = dict()
    data[0] = [1, 2]
    data[1] = [2, 3, 2]
    data[2] = [3]
    data[3] = [2, 1]
    data[4] = [1,5]
    data[5] = [6, 6]
    data[6] = [7, 2]
    data[7] = [2]
    return data


class FigureSet:
    def __init__(self, full_data=None, figure_specs=None):
        if figure_specs:
            self.figure_specs = figure_specs
        else:
            self.figure_specs = defaults.figure_specs
        if full_data:
            self.full_data = full_data
        else:
            self.full_data = self._get_example_data()
        assert len(self.full_data) == len(self.figure_specs)
        self.FigureInstances = self._construct_individual_figures()
        self._couple_range()
        self.figure_layout = self._get_figure_layout()

    def _get_example_data(self):
        full_data = []
        for i in range(len(self.figure_specs)):
            if i % 2 == 0:
                full_data.append(example_data_1())
            else:
                full_data.append(example_data_2())
        return full_data

    def _construct_individual_figures(self):
        FigureInstances = []
        for data, figure_spec in zip(self.full_data, self.figure_specs):
            FigureInstances.append(IndividualFigure(data, specs=figure_spec))
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
            if len(tmp_row) == defaults.figures_per_row:
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

    def figure_update_next_turn(self, data_to_add):
        for fig_label, value in data_to_add.items():
            found_fig = False
            for FigureInstance in self.FigureInstances:
                if FigureInstance.name == fig_label:
                    FigureInstance.figure_update_next_turn(value)
                    found_fig = True
                    break
            if not found_fig:
                raise Exception
        return True



if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    def main():
        from collections import namedtuple
        from enum import Enum, auto
        def example_data_1():
            data = dict()
            data[0] = [1, 13, 23]
            data[1] = [23]
            data[2] = [34, 23, 34]
            data[3] = [2]
            data[4] = [1, 13, 23]
            data[5] = [23]
            data[6] = [34, 23, 34]
            data[7] = [2]
            return data

        def example_data_2():
            data = dict()
            data[0] = [1, 2]
            data[1] = [2, 3, 2]
            data[2] = [3]
            data[3] = [2, 1]
            data[4] = [1, 5]
            data[5] = [6, 6]
            data[6] = [7, 2]
            data[7] = [2]
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

        fig_indices = ("name", "title", "x_label", "y_label")

        FigureSpec = namedtuple("FigureSpec", fig_indices)

        figure_spec_1 = FigureSpec(Res.cloth, "title", "x_", "y_")
        figure_spec_5 = FigureSpec(Prod.aisha, "title", "x_", "y_")
        output_file("../../bokeh_tmp/line.html")
        layout_w = FigureSet([example_data_1(), example_data_2()],
                             [figure_spec_1, figure_spec_5]).figure_layout
        # curdoc().add_root(layout_w)
        show(layout_w)
    main()