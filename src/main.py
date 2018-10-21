import sys
import os
sys.path.append(os.getcwd() + '/config')
sys.path.append(os.getcwd() + '/bokeh_ui')

from ge import GE
from gs import GS
from bokeh_ui.ui import UI
from bokeh_ui.mocked_ui import mock_UI
from global_config import UISpecs
from bokeh.plotting import curdoc, show


def main():
    ge = GE()
    callback = ge.callback
    init_data = ge.get_init_data()
    ui = UI(init_data, callback, UISpecs())
    # show(ui.ui_layout)
    curdoc().add_root(ui.ui_layout)

main()
