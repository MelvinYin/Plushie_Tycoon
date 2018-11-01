##############################################################################
# Figure Attributes
from enum import Enum, auto, unique

class FigureNames(Enum):
    inventory_res = auto()
    inventory_prod = auto()
    price_res = auto()
    price_prod = auto()
    budget = auto()

class InventoryResSpecs:
    def __init__(self):
        self.name = FigureNames.inventory_res
        self.title = "Inventory Res"
        self.x_label = "Time"
        self.y_label = "Number"

class InventoryProdSpecs:
    def __init__(self):
        self.name = FigureNames.inventory_prod
        self.title = "Inventory Prod"
        self.x_label = "Time"
        self.y_label = "Number"

class PriceResSpecs:
    def __init__(self):
        self.name = FigureNames.price_res
        self.title = "Price Res"
        self.x_label = "Time"
        self.y_label = "Dollars"

class PriceProdSpecs:
    def __init__(self):
        self.name = FigureNames.price_prod
        self.title = "Price Res"
        self.x_label = "Time"
        self.y_label = "Dollars"

class BudgetSpecs:
    def __init__(self):
        self.name = FigureNames.budget
        self.title = "Budget_"
        self.x_label = "Time"
        self.y_label = "Dollars"

class FigureSetSpecs:
    def __init__(self):
        self.figures_per_row = 5

class FigureIndividualSpecs:
    def __init__(self):
        self.inventory_res = InventoryResSpecs()
        self.inventory_prod = InventoryProdSpecs()
        self.price_res = PriceResSpecs()
        self.price_prod = PriceProdSpecs()
        self.budget = BudgetSpecs()

class FigureSpecs:
    def __init__(self):
        self.set = FigureSetSpecs()
        self.figure = FigureIndividualSpecs()

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









