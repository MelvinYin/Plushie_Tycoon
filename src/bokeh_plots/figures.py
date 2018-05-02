import sys
sys.path.append("../")
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
from bokeh_plots.individual_figure import IndividualFigure

class FigureSet:
    def __init__(self, full_data, FigureSetSpecs, FigureSpecs):
        self.FigureInstances = self._construct_individual_figures(full_data, FigureSpecs)
        self._couple_range()
        self.layout = self._get_figure_layout(FigureSetSpecs)

    def _construct_individual_figures(self, full_data, FigureSpecs):
        FigureInstances = []
        for FigureSpec in FigureSpecs:
            data = full_data[FigureSpec.name]
            FigureInstances.append(IndividualFigure(data, FigureSpec))
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
                if FigureInstance.name == fig_label:
                    FigureInstance.figure_update(value)
                    found_fig = True
                    break
            if not found_fig:
                raise Exception
        return True

if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    def main():
        from defaults import _FigureSpec1, _FigureSpec5, FigureSetSpecs, Res, Prod
        import random
        def get_initial_data1():
            data = dict()
            data['key_1'] = [1, 2, 3, 4, 5]
            data['key_2'] = [2, 3, 4, 5, 6]
            data['key_3'] = [5, 1, 4, 2, 4]
            data['time'] = [2, 3, 3, 3, 4]
            return data

        def get_initial_data2():
            data = dict()
            data['key_1'] = [11, 2, 3, 4, 5]
            data['key_2'] = [12, 3, 4, 5, 6]
            data['key_3'] = [15, 1, 4, 2, 4]
            data['time'] = [2,2, 3, 3, 4]
            return data

        def to_add():
            data = dict()
            data['key_1'] = [random.randint(3, 15)]
            data['key_2'] = [random.randint(3, 15)]
            data['key_3'] = [random.randint(3, 15)]
            data['time'] = [5]
            return data

        def to_add2():
            data = dict()
            data['key_1'] = [random.randint(3, 15)]
            data['key_2'] = [random.randint(3, 15)]
            data['key_3'] = [random.randint(3, 15)]
            data['time'] = [6]
            return data

        tot_fig_1 = dict()
        tot_fig_1[Res] = get_initial_data1()
        tot_fig_1[Prod] = get_initial_data2()


        fig = FigureSet(tot_fig_1, FigureSetSpecs, [_FigureSpec1, _FigureSpec5])

        data_to_add = dict()
        data_to_add[Res] = to_add()
        data_to_add[Prod] = to_add()
        fig.figure_update(data_to_add)
        data_to_add = dict()
        data_to_add[Res] = to_add()
        data_to_add[Prod] = to_add()
        fig.figure_update(data_to_add)
        data_to_add = dict()
        data_to_add[Res] = to_add2()
        data_to_add[Prod] = to_add2()
        fig.figure_update(data_to_add)
        data_to_add = dict()
        data_to_add[Res] = to_add2()
        data_to_add[Prod] = to_add2()
        fig.figure_update(data_to_add)
        layout_w = fig.layout
        if __name__ == "__main__":
            show(layout_w)
        else:
            curdoc().add_root(layout_w)
    main()