from ge import GEM
from bokeh.plotting import show
from ui_interface import UIInterface

# Ui_callback takes as input the call from UI (<Func:...), and should return
# the full set of values to update figures

# GEM's callback takes as input the call from UI, and return the full set
# of values to update figures.

# Before even attempting to bring both together, probably a good idea to test
# GE first.

class Main:
    def __init__(self):
        self.GE = GEM()
        self.ui = UIInterface(self.GE.callback)

x = Main()
# show(x.ui.figure_set.figure_layout)