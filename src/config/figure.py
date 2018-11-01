##############################################################################
# Figure Attributes

class ResSpec:
    def __init__(self):
        self.name = 'Res'
        self.title = "Res plot"
        self.x_label = "x_"
        self.y_label = "y_"

class ProdSpec:
    def __init__(self):
        self.name = 'Prod'
        self.title = "Prod plot"
        self.x_label = "x_"
        self.y_label = "y_"

class FigureSetSpecs:
    def __init__(self):
        self.figures_per_row = 3

class FigureIndividualSpecs:
    def __init__(self):
        self.res = ResSpec()
        self.prod = ProdSpec()

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









