"""
Necessary boxes to display:
1. Make tables, to show res consumption to make (perm)
2. Current prices for each item?
3. Current movein/moveout cost per item per unit

"""

# todo: individual_figure.py, CDS.
from utils.sys_path_adder import folders_to_add
from bokeh.plotting import curdoc

folders_to_add(['bokeh_ui', 'config', 'p_model', 'tests', 'gs_components',
                'utils'])
folders_to_add(['figures', 'widgets'], suffix='bokeh_ui')
folders_to_add(['mocked_data'], suffix='tests')
folders_to_add(['p_model'], suffix='gs_components')

from ui_interface import UIInterface

def run():
    port_no = "50001"
    ui = UIInterface(port_no)
    curdoc().add_root(ui.ui.ui_layout)
    # show(ui.ui.ui_layout)

run()
"""
python -m grpc_tools.protoc --proto_path . --python_out=. --grpc_python_out=. 
./grpc.proto
"""