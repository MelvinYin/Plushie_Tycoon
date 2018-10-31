from bokeh.plotting import curdoc, show
from bokeh.layouts import row
import logging
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from bokeh_ui.figures.individual_figure import IndividualFigure
from config.figure import FigureSpecs, ResSpec, ProdSpec
from config.global_config import Res, Prod, UISpecs
from config.widget import WidgetIndividualSpecs
from figureset import FigureSet
from mocked_data.mock_figure import mock_init, mock_update1, mock_update2, \
    mock_update3
from mocked_data.mock_widget import mock_callbacks
from bokeh_ui.ui import UI
from widgets.individual import TransactionWidget, ButtonWidget
from widgets.widgetset import WidgetSet

test_figureset = False
test_individual_figure = False
test_individual_widget = False
test_widgetset = False
test_ui = True

def individual_figure():
    res_fig = IndividualFigure(mock_init[Res], ResSpec())
    prod_fig = IndividualFigure(mock_init[Prod], ProdSpec())

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
    fig = FigureSet(mock_init, FigureSpecs())
    fig.figure_update(mock_update1)
    fig.figure_update(mock_update2)
    fig.figure_update(mock_update3)
    layout_w = fig.layout
    return layout_w

def individual_widget():
    def widget_callback(command_to_run):
        logging.debug("from widget callback")
        logging.debug(command_to_run)
        return

    widget_1 = TransactionWidget(widget_callback, WidgetIndividualSpecs().transaction_1)
    widget_1.widget_callback([
        WidgetIndividualSpecs().transaction_1.RBG1.labels[0],
        WidgetIndividualSpecs().transaction_1.RBG3.labels[0], 10])
    widget_2 = ButtonWidget(widget_callback, WidgetIndividualSpecs().button_1)
    layout_w1 = widget_1.layout
    layout2 = widget_2.layout
    layout = row(layout_w1, layout2)
    return layout

def widgetset():
    def widget_callback(command_to_run):
        logging.debug("from widget callback")
        logging.debug(command_to_run)
        return
    layout_w = WidgetSet(widget_callback, UISpecs().widgets).layout
    return layout_w

def ui():
    call_count = 0
    def callback(call):
        logging.debug("Call: <{}>".format(call))
        global call_count
        assert call in mock_callbacks
        if call_count == 0:
            call_count += 1
            return mock_update1
        elif call_count == 1:
            call_count += 1
            return mock_update2
        else:
            return mock_update3

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

