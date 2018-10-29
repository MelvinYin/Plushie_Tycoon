import sys
import os
sys.path.append(os.getcwd() + '/config')
sys.path.append(os.getcwd() + '/bokeh_ui')
sys.path.append(os.getcwd() + '/mocked_data')

from ge import GE
from gs import GS
from bokeh_ui.ui import UI
from mock_ui import mock_UI
from global_config import UISpecs
from bokeh.plotting import curdoc, show
from mock_figure import mock_init, mock_update1, mock_update2, mock_update3
from mock_widget import mocked_transaction_callbacks
import logs
from mock_GE import mock_ge

def main():
    ge = mock_ge()
    callback = ge.callback
    init_data = ge.get_init_data()
    ui = UI(init_data, callback, UISpecs())
    # calls = mocked_transaction_callbacks()
    # ui.ui_callback(calls[0])
    # show(ui.ui_layout)
    curdoc().add_root(ui.ui_layout)

main()
