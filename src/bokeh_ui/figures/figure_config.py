from collections import namedtuple
from enum import Enum, auto, unique

# TO USE:
# from figure_config import res_specs, prod_specs, set_specs

##############################################################################
# Global

from global_config import Res, Prod

##############################################################################
# Figure Attributes

set_indices = ("figures_per_row",)
SetSpecs = namedtuple("FigureSetSpecs", set_indices)
set_specs = SetSpecs(figures_per_row=3)

figure_indices = ("name", "title", "x_label", "y_label")
FigureSpecBase = namedtuple("FigureSpec", figure_indices)

res_specs = FigureSpecBase(Res, "Res plot", "x_", "y_")

prod_specs = FigureSpecBase(Prod, "Prod plot", "x_", "y_")


"""
UNUSED

_FigureSpec8 = _FigureSpecBase(ResPrice.cloth, "ResPrice.cloth", "x_", "y_")
_FigureSpec9 = _FigureSpecBase(ResPrice.stuff, "ResPrice.stuff", "x_", "y_")
_FigureSpec10 = _FigureSpecBase(ResPrice.accessory, "ResPrice.accessory", "x_", "y_")
_FigureSpec11 = _FigureSpecBase(ResPrice.packaging, "ResPrice.packaging", "x_", "y_")

_FigureSpec12 = _FigureSpecBase(ProdPrice.aisha, "ProdPrice.aisha", "x_", "y_")
_FigureSpec13 = _FigureSpecBase(ProdPrice.beta, "ProdPrice.beta", "x_", "y_")
_FigureSpec14 = _FigureSpecBase(ProdPrice.chama, "ProdPrice.chama", "x_", "y_")
_FigureSpec15 = _FigureSpecBase(Production.hours_needed, "Production.hours_needed", "x_", "y_")
_FigureSpec16 = _FigureSpecBase(Production.cost_per_hour, "Production.cost_per_hour", "x_", "y_")
_FigureSpec17 = _FigureSpecBase(Production.res_cost, "Production.res_cost", "x_", "y_")

# FigureSpecs = [_FigureSpec1, _FigureSpec5, _FigureSpec9, _FigureSpec10, _FigureSpec11, _FigureSpec12,
#                _FigureSpec13, _FigureSpec14]


"""

