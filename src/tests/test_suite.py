from bokeh.plotting import show
from bokeh.layouts import row
import os
import sys
import unittest

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from bokeh_ui.figures.individual_figure import IndividualFigure
from config.global_config import Res, Prod
from config.figure import ResSpec, ProdSpec
from mocked_data.mock_figure import mock_init, mock_update1, mock_update2, \
    mock_update3

test_GE = True

@unittest.skipIf(test_GE == False, "")
class TestGE(unittest.TestCase):
    def test_individual_figure(self):
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
        show(layout)