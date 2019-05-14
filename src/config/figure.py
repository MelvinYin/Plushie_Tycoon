##############################################################################
# Figure Attributes
from enum import Enum, auto, unique
from bokeh.palettes import Category10
from base import res_members, prod_members, Prod

class FigureNames(Enum):
    inventory_res = auto()
    inventory_prod = auto()
    price_res = auto()
    price_prod = auto()
    budget = auto()
    console_output = auto()
    res_ratio_table = auto()

class ResourceRatioTableSpecs:
    def __init__(self):
        self.name = FigureNames.res_ratio_table
        self.title = "Production Resource Ratios"
        self.index = dict()
        self.index['Resource'] = [i.name for i in res_members]
        self.data = dict()
        self.data[Prod.aisha.name] = [3, 6, 2, 1]
        self.data[Prod.beta.name] = [1, 4, 1, 2]
        self.data[Prod.chama.name] = [2, 5, 1, 4]
        self.width = 200
        self.height = 200


class ConsoleOutputSpecs:
    def __init__(self):
        self.name = FigureNames.console_output
        self.title = "Console"
        self.text = 'Initial<p>'
        self.width = 50
        self.height = 20
        self.textbox_width = 400
        self.textbox_height = 380
        # Division by 2 so it fits well and within what bokeh uses.
        self.html_height = int(self.textbox_height / 2)

class InventoryResSpecs:
    def __init__(self):
        self.name = FigureNames.inventory_res
        self.title = "Inventory Res"
        self.x_label = "Time"
        self.y_label = "Number"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict()
        entries = [res.name for res in res_members]
        for i, entry in enumerate(entries):
            colormap[entry] = Category10[10][i]
        return colormap

class InventoryProdSpecs:
    def __init__(self):
        self.name = FigureNames.inventory_prod
        self.title = "Inventory Prod"
        self.x_label = "Time"
        self.y_label = "Number"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict()
        entries = [prod.name for prod in prod_members]
        for i, entry in enumerate(entries):
            colormap[entry] = Category10[10][i]
        return colormap

class PriceResSpecs:
    def __init__(self):
        self.name = FigureNames.price_res
        self.title = "Price Res"
        self.x_label = "Time"
        self.y_label = "Dollars"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict()
        entries = [res.name for res in res_members]
        for i, entry in enumerate(entries):
            colormap[entry] = Category10[10][i]
        return colormap

class PriceProdSpecs:
    def __init__(self):
        self.name = FigureNames.price_prod
        self.title = "Price Prod"
        self.x_label = "Time"
        self.y_label = "Dollars"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict()
        entries = [prod.name for prod in prod_members]
        for i, entry in enumerate(entries):
            colormap[entry] = Category10[10][i]
        return colormap

class BudgetSpecs:
    def __init__(self):
        self.name = FigureNames.budget
        self.title = "Budget_"
        self.x_label = "Time"
        self.y_label = "Dollars"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict(budget=Category10[10][0])
        return colormap

class FigureSetSpecs:
    def __init__(self):
        self.figures_per_row = 3

class FigureIndividualSpecs:
    def __init__(self):
        self.inventory_res = InventoryResSpecs()
        self.inventory_prod = InventoryProdSpecs()
        self.price_res = PriceResSpecs()
        self.price_prod = PriceProdSpecs()
        self.budget = BudgetSpecs()
        self.console = ConsoleOutputSpecs()
        self.res_ratio_table = ResourceRatioTableSpecs()

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









