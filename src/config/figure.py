##############################################################################
# Figure Attributes
from enum import Enum, auto, unique
from bokeh.palettes import Category10
from base import Res, Prod

class FigureNames(Enum):
    inventory_res = auto()
    inventory_prod = auto()
    price_res = auto()
    price_prod = auto()
    budget = auto()
    console_output = auto()
    res_ratio_table = auto()
    item_cost_table = auto()
    item_properties_table = auto()

class MoveCostTableSpecs:
    def __init__(self):
        self.name = FigureNames.move_cost_table
        self.title = "Production Resource Ratios"
        self.index = dict()
        self.index['Resource'] = [i.name for i in Res]
        self.data = dict()
        self.data[Prod.aisha.name] = [3, 6, 2, 1]
        self.data[Prod.beta.name] = [1, 4, 1, 2]
        self.data[Prod.chama.name] = [2, 5, 1, 4]
        self.width = 200
        self.height = 200

class ResourceRatioTableSpecs:
    def __init__(self):
        self.name = FigureNames.res_ratio_table
        self.title = "Production Resource Ratios"
        self.index = dict()
        self.index['Resource'] = [i.name for i in Res]
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
        self.title = "Inventory (Resources)"
        self.x_label = "Time"
        self.y_label = "Number"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict()
        entries = [res.name for res in Res]
        for i, entry in enumerate(entries):
            colormap[entry] = Category10[10][i]
        return colormap

class InventoryProdSpecs:
    def __init__(self):
        self.name = FigureNames.inventory_prod
        self.title = "Inventory (Products)"
        self.x_label = "Time"
        self.y_label = "Number"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict()
        entries = [prod.name for prod in Prod]
        for i, entry in enumerate(entries):
            colormap[entry] = Category10[10][i]
        return colormap

class PriceResSpecs:
    def __init__(self):
        self.name = FigureNames.price_res
        self.title = "Resource Price"
        self.x_label = "Time"
        self.y_label = "Dollars"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict()
        entries = [res.name for res in Res]
        for i, entry in enumerate(entries):
            colormap[entry] = Category10[10][i]
        return colormap

class PriceProdSpecs:
    def __init__(self):
        self.name = FigureNames.price_prod
        self.title = "Product Price"
        self.x_label = "Time"
        self.y_label = "Dollars"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict()
        entries = [prod.name for prod in Prod]
        for i, entry in enumerate(entries):
            colormap[entry] = Category10[10][i]
        return colormap

class BudgetSpecs:
    def __init__(self):
        self.name = FigureNames.budget
        self.title = "Budget"
        self.x_label = "Time"
        self.y_label = "Dollars"
        self.colormap = self._entry_to_color()

    def _entry_to_color(self):
        colormap = dict(budget=Category10[10][0])
        return colormap

FigSpecs = dict()
FigSpecs['inventory_res'] = InventoryResSpecs()
FigSpecs['inventory_prod'] = InventoryProdSpecs()
FigSpecs['price_res'] = PriceResSpecs()
FigSpecs['price_prod'] = PriceProdSpecs()
FigSpecs['budget'] = BudgetSpecs()
FigSpecs['console'] = ConsoleOutputSpecs()
FigSpecs['res_ratio_table'] = ResourceRatioTableSpecs()
FigSpecs['move_cost_table'] = ResourceRatioTableSpecs()







