import sys
from bokeh_ui.figures.individual_figure import IndividualFigure
from bokeh.plotting import show, curdoc
from figureset import FigureSet
from mocked_data.mock_figure import mock_init, mock_update1, mock_update2, \
    mock_update3
from config.figure import FigureSpecs

test_figureset = False



def figureset():
    fig = FigureSet(mock_init, FigureSpecs())
    fig.figure_update(mock_update1)
    fig.figure_update(mock_update2)
    fig.figure_update(mock_update3)
    layout_w = fig.layout
    return layout_w

func_map = dict()
func_map[test_figureset] = figureset

if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    layout = None
    for key, function in func_map.items():
        if key:
            layout = function()
            break
    if layout is None:
        sys.exit()
    if __name__ == "__main__":
        show(layout)
    else:
        curdoc().add_root(layout)

