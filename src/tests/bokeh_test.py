from bokeh.plotting import curdoc, show
from bokeh.layouts import row
import sys
import os
src_path = sys.path[0].rsplit("/", maxsplit=1)[0]
sys.path.append(src_path)

from bokeh_ui.figures.figureset import FigureSet
from bokeh_ui.figures.individual_figure import IndividualFigure
from figure import FigureSpecs, InventoryResSpecs, InventoryProdSpecs
from global_config import Res, Prod, UISpecs
from widget import WidgetIndividualSpecs
from logs import log
from mocked_data.mock_figure import mock_init, mock_update1, mock_update2, \
    mock_update3
from mocked_data.mock_GE import mock_ge
from bokeh_ui.ui import UI
from bokeh_ui.widgets.individual import TransactionWidget, ButtonWidget
from bokeh_ui.widgets.widgetset import WidgetSet
import old_logs

old_logs.set_logging_level()

test_figureset = False
test_individual_figure = False
test_individual_widget = False
test_widgetset = False
test_ui = True

def individual_figure():
    res_fig = IndividualFigure(mock_init[Res], InventoryResSpecs())
    prod_fig = IndividualFigure(mock_init[Prod], InventoryProdSpecs())

    res_fig.figure_update(mock_update1[Res])
    res_fig.figure_update(mock_update2[Res])
    res_fig.figure_update(mock_update3[Res])

    prod_fig.figure_update(mock_update1[Prod])
    prod_fig.figure_update(mock_update2[Prod])
    prod_fig.figure_update(mock_update3[Prod])

    layout_w = res_fig.figure
    layout_ = prod_fig.figure
    layout = row(layout_w, layout_)
    return layout

def figureset():
    fig = FigureSet(mock_init)
    fig.figure_update(mock_update1)
    fig.figure_update(mock_update2)
    fig.figure_update(mock_update3)
    layout_w = fig.layout
    return layout_w

def individual_widget():
    def widget_callback(command_to_run):
        log(os.getcwd(), "from widget callback")
        log(os.getcwd(), command_to_run)
        return

    widget_1 = TransactionWidget(widget_callback,
                                 WidgetIndividualSpecs().transaction_1)
    widget_1.widget_callback([
        list(WidgetIndividualSpecs().transaction_1.RBG1.labelmap.keys())[0],
        list(WidgetIndividualSpecs().transaction_1.RBG3.labelmap.keys())[0],
        10])
    widget_2 = ButtonWidget(widget_callback, WidgetIndividualSpecs().button_1)
    layout_w1 = widget_1.layout
    layout2 = widget_2.layout
    layout = row(layout_w1, layout2)
    return layout

def widgetset():
    def widget_callback(command_to_run):
        log(os.getcwd(), "from widget callback")
        log(os.getcwd(), command_to_run)
        return
    layout_w = WidgetSet(widget_callback, UISpecs().widgets).layout
    return layout_w

def ui():
    ge = mock_ge()
    callback = ge.callback
    x = UI(mock_init, callback, UISpecs())
    return x.ui_layout

if __name__ == "__main__" or str(__name__).startswith("bk_script"):
    func_map = dict()
    func_map[test_figureset] = figureset
    func_map[test_individual_figure] = individual_figure
    func_map[test_individual_widget] = individual_widget
    func_map[test_widgetset] = WidgetSet
    func_map[test_ui] = ui
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

