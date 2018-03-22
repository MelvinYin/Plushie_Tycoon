import sys
sys.path.append("../")
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
from individual_figure import IndividualFigure
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
    def __init__(self, full_data=None):
        self.figure_specs = defaults.figure_specs
        self.num_figures = len(self.figure_specs)
        if not full_data:
            self.full_data = self._get_example_data()
        else:
            self.full_data = full_data
        assert len(self.full_data) == len(self.figure_specs)
        self.FigureInstances = self._construct_individual_figures()
        self._couple_range()
        self.figure_layout = self._get_figure_layout()

    def _get_example_data(self):
        full_data = []
        for i in range(self.num_figures):
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
        fig_label = data_to_add[0]
        for FigureInstance in self.FigureInstances:
            if FigureInstance.title == fig_label:
                FigureInstance.figure_update(data_to_add)
        return True

if __name__ == "__main__":
    output_file("../../bokeh_tmp/line.html")
    figure_set = FigureSet().figure_layout

    show(figure_set)
    # curdoc().add_root(layout_)