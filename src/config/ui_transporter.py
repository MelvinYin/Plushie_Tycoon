from base import res_members
from global_config import FigureNames, Prod, Res
from enum import Enum
from copy import deepcopy

def enum_to_str(enum_arr):
    # This should convert enum representations to displayed names in UI.
    # Currently rather trivial since we take the .name, but it can eventually
    # be something more fancy. Maybe.
    if isinstance(enum_arr, Enum):
        return enum_arr.name
    str_arr = list(i.name for i in enum_arr)
    return str_arr

class Transporter:
    def __init__(self):
        self.data = dict()

    def return_data(self):
        return self

    def load(self, GS):
        # item_cost_table
        index_in_enum = GS.inventory.get_index()
        index = dict()
        index['Item'] = enum_to_str(index_in_enum)
        movein_cost = GS.inventory.get_all_movein_cost(1)
        moveout_cost = GS.inventory.get_all_moveout_cost(1)
        storage_cost = GS.inventory.get_all_storage_cost(1)
        assert tuple(movein_cost.keys()) == tuple(moveout_cost.keys()) \
               == tuple(storage_cost.keys())
        fields = dict()
        fields['Movein'] = list(movein_cost.values())
        fields['Moveout'] = list(moveout_cost.values())
        fields['Storage'] = list(storage_cost.values())
        output = dict()
        output['CDS'] = {**index, **fields}
        output['index'] = index['Item']
        self.data[FigureNames.item_cost_table] = output

    #     item_properties_table
        weights = GS.inventory.get('weight')
        volumes = GS.inventory.get('volume')
        assert tuple(weights.keys()) == tuple(volumes.keys())
        properties = dict()
        properties['Weight'] = list(weights.values())
        properties['Volume'] = list(volumes.values())
        output = dict()
        output['CDS'] = {**index, **properties}
        output['index'] = index['Item']
        self.data[FigureNames.item_properties_table] = deepcopy(output)

    #     res_ratio_table
        index = dict()
        index['Resource'] = [i.name for i in res_members]
        data = dict()
        data[Prod.aisha.name] = [3, 6, 2, 1]
        data[Prod.beta.name] = [1, 4, 1, 2]
        data[Prod.chama.name] = [2, 5, 1, 4]
        output = dict()
        output['CDS'] = {**index, **data}
        output['index'] = index['Resource']
        self.data[FigureNames.res_ratio_table] = deepcopy(output)

    #     console_output
        self.data[FigureNames.console_output] = ''

    #     inventory_res
        inv_values = GS.inventory.return_data()
        # todo: eventually remove return_data, and access it directly, maybe.
        adapted = dict()
        for key, values in inv_values.items():
            if key in Res:
                adapted[key.name] = [values]
        adapted['time'] = [GS.current_time]
        self.data[FigureNames.inventory_res] = deepcopy(adapted)

    #     inventory_prod
        adapted = dict()
        for key, values in inv_values.items():
            if key in Prod:
                adapted[key.name] = [values]
        adapted['time'] = [GS.current_time]
        self.data[FigureNames.inventory_prod] = deepcopy(adapted)

    #     price_res
        market_vals = GS.market.return_data()
        adapted = dict()
        for key, values in market_vals.items():
            if key in Res:
                adapted[key.name] = [values]
        adapted['time'] = [GS.current_time]
        self.data[FigureNames.price_res] = deepcopy(adapted)

    #     price_prod
        adapted = dict()
        for key, values in market_vals.items():
            if key in Prod:
                adapted[key.name] = [values]
        adapted['time'] = [GS.current_time]
        self.data[FigureNames.price_prod] = deepcopy(adapted)

    #     budget
        adapted = dict()
        adapted['budget'] = GS.budget.return_data()['budget']
        adapted['time'] = [GS.current_time]
        self.data[FigureNames.budget] = deepcopy(adapted)
        self.check(self.data)
        return True

    def check(self, data):
        return True

    def get(self, fig_name):
        assert fig_name in FigureNames
        return self.data[fig_name]


