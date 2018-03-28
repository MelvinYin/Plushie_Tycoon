import sys
sys.path.append("../")
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
from bokeh_plots.individual_figure import IndividualFigure


"""
Assume initial_func_count must be an int => equal across all figures.

"""

class FigureSet:
    def __init__(self, full_data, figure_gspecs, figure_ispecs, initial_func_count=0):
        self.FigureInstances = self._construct_individual_figures(full_data, initial_func_count, figure_ispecs)
        self._couple_range()
        self.figure_layout = self._get_figure_layout(figure_gspecs)

    def _construct_individual_figures(self, full_data, initial_func_count, figure_ispecs):
        FigureInstances = []
        for figure_spec in figure_ispecs:
            data = full_data[figure_spec.name]
            FigureInstances.append(IndividualFigure(data, figure_spec, initial_func_count))
        return FigureInstances

    def _couple_range(self):
        ref_x_range = self.FigureInstances[0].figure.x_range
        for FigureInstances in self.FigureInstances:
            FigureInstances.figure.x_range = ref_x_range
        return True

    def _get_figure_layout(self, figure_gspecs):
        row_layouts = []
        tmp_row = []
        for FigureInstances in self.FigureInstances:
            tmp_row.append(FigureInstances.figure)
            if len(tmp_row) == figure_gspecs.figures_per_row:
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
        import sys
        import os
        sys.path.append(os.getcwd().rsplit("\\", 1)[0])
        from defaults import figure_ispec_1, figure_ispec_5, figure_gspecs

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

        output_file("../../bokeh_tmp/line.html")
        fig = FigureSet([example_data_1(), example_data_2()], figure_gspecs,
                             [figure_ispec_1, figure_ispec_5], initial_func_count=12)
        data_to_add = dict()
        data_to_add[figure_ispec_1.name] = (example_data_1()[-1][0], 23)
        data_to_add[figure_ispec_5.name] = (example_data_2()[-1][0], 34)
        fig.figure_update(data_to_add)
        data_to_add[figure_ispec_1.name] = (example_data_1()[-1][0]+1, 45)
        data_to_add[figure_ispec_5.name] = (example_data_2()[-1][0]+1, 56)
        fig.figure_update(data_to_add)
        data_to_add[figure_ispec_1.name] = (example_data_1()[-1][0], 23)
        data_to_add[figure_ispec_5.name] = (example_data_2()[-1][0], 34)
        fig.figure_update(data_to_add)
        layout_w = fig.figure_layout
        if __name__ == "__main__":
            show(layout_w)
        else:
            curdoc().add_root(layout_w)
    main()