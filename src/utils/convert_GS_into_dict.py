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


import grpc
import grpc_pb2
import grpc_pb2_grpc
"""

message UserOutput {
    map<string, int32> prices = 1;
    map<string, int32> quantities = 2;
    message ItemCost {
        map<string, int32> movein = 3;
        map<string, int32> moveout = 4;
        map<string, int32> storage = 5;
    }
    message ItemProperties {
        map<string, int32> weight = 3;
        map<string, int32> volume = 4;
    }
    message ResourceRatio {
        message ResourceRatioPerProduct {
            map<string, int32> ratio = 6;
        }
        map<string, ResourceRatioPerProduct> ratio_per_product = 7;
    }
    string console_output = 8;
    int32 budget = 9;
    int32 time = 10;
    string action = 11;
}"""
from global_config import prod_members
from global_config import FigureNames as FigNms

def convert(grpc_output):
    final_output = dict()
    index = []
    for res in res_members:
        res = res.name
        index.append(res)
    for prod in prod_members:
        prod = prod.name
        index.append(prod)

    item_cost = dict()
    movein = dict()
    for item in index:
        movein[item] = grpc_output.ItemCost.movein[item]
    item_cost['Moveout'] = movein
    moveout = dict()
    for item in index:
        moveout[item] = grpc_output.ItemCost.moveout[item]
    item_cost['Moveout'] = moveout
    storage = dict()
    for item in index:
        storage[item] = grpc_output.ItemCost.storage[item]
    item_cost['Storage'] = storage
    item_cost['Item'] = index
    final_output[FigNms.item_cost_table] = item_cost

    properties = dict()
    weight = dict()
    for item in index:
        weight[item] = grpc_output.ItemProperties.weight[item]
    properties['Weight'] = weight
    volume = dict()
    for item in index:
        volume[item] = grpc_output.ItemCost.volume[item]
    properties['Volume'] = volume
    properties['Item'] = index
    final_output[FigNms.item_properties_table] = properties

    ratios = dict()
    for prod in prod_members:
        prod = prod.name
        local_ratios = []
        for res in res_members:
            res = res.name
            local_ratios.append(grpc_output.ResourceRatio[prod].ratio[res])
        ratios[prod] = local_ratios
    ratios['Resource'] = [i.name for i in res_members]
    final_output[FigNms.res_ratio_table] = ratios

    #     console_output
    final_output[FigureNames.console_output] = grpc_output.console_output

    inventory_res = dict()
    for res in res_members:
        res = res.name
        inventory_res[res] = grpc_output.quantities[res]
    inventory_res['time'] = [grpc_output.time]
    final_output[FigureNames.inventory_res] = inventory_res

    inventory_prod = dict()
    for prod in prod_members:
        prod = prod.name
        inventory_prod[prod] = grpc_output.quantities[prod]
    inventory_prod['time'] = [grpc_output.time]
    final_output[FigureNames.inventory_res] = inventory_prod

    price_res = dict()
    for res in res_members:
        res = res.name
        price_res[res] = grpc_output.prices[res]
    price_res['time'] = [grpc_output.time]
    final_output[FigureNames.price_res] = price_res

    price_prod = dict()
    for prod in prod_members:
        prod = prod.name
        price_prod[prod] = grpc_output.prices[prod]
    price_prod['time'] = [grpc_output.time]
    final_output[FigureNames.price_res] = price_prod

    budget = dict()
    budget['budget'] = grpc_output.budget
    inventory_prod['time'] = [grpc_output.time]
    final_output[FigureNames.budget] = budget

    return final_output



#
#
# def convert(gs):
#     dict_output = dict()
#     index_in_enum = gs.inventory.get_index()
#     index = dict()
#     index['Item'] = enum_to_str(index_in_enum)
#     movein_cost = gs.inventory.get_all_movein_cost(1)
#     moveout_cost = gs.inventory.get_all_moveout_cost(1)
#     storage_cost = gs.inventory.get_all_storage_cost(1)
#     assert tuple(movein_cost.keys()) == tuple(moveout_cost.keys()) == tuple(
#         storage_cost.keys())
#     fields = dict()
#     fields['Movein'] = list(movein_cost.values())
#     fields['Moveout'] = list(moveout_cost.values())
#     fields['Storage'] = list(storage_cost.values())
#     output = dict()
#     output['CDS'] = {**index, **fields}
#     output['index'] = index['Item']
#     dict_output[FigureNames.item_cost_table] = output
#
#     #     item_properties_table
#     weights = gs.inventory.get('weight')
#     volumes = gs.inventory.get('volume')
#     assert tuple(weights.keys()) == tuple(volumes.keys())
#     properties = dict()
#     properties['Weight'] = list(weights.values())
#     properties['Volume'] = list(volumes.values())
#     output = dict()
#     output['CDS'] = {**index, **properties}
#     output['index'] = index['Item']
#     dict_output[FigureNames.item_properties_table] = deepcopy(output)
#
#     #     res_ratio_table
#     index = dict()
#     index['Resource'] = [i.name for i in res_members]
#     data = dict()
#     data[Prod.aisha.name] = [3, 6, 2, 1]
#     data[Prod.beta.name] = [1, 4, 1, 2]
#     data[Prod.chama.name] = [2, 5, 1, 4]
#     output = dict()
#     output['CDS'] = {**index, **data}
#     output['index'] = index['Resource']
#     dict_output[FigureNames.res_ratio_table] = deepcopy(output)
#
#     #     console_output
#     dict_output[FigureNames.console_output] = ''
#
#     #     inventory_res
#     inv_values = gs.inventory.return_data()
#     # todo: eventually remove return_data, and access it directly, maybe.
#     adapted = dict()
#     for key, values in inv_values.items():
#         if key in Res:
#             adapted[key.name] = [values]
#     adapted['time'] = [gs.current_time]
#     dict_output[FigureNames.inventory_res] = deepcopy(adapted)
#
#     #     inventory_prod
#     adapted = dict()
#     for key, values in inv_values.items():
#         if key in Prod:
#             adapted[key.name] = [values]
#     adapted['time'] = [gs.current_time]
#     dict_output[FigureNames.inventory_prod] = deepcopy(adapted)
#
#     #     price_res
#     market_vals = gs.market.return_data()
#     adapted = dict()
#     for key, values in market_vals.items():
#         if key in Res:
#             adapted[key.name] = [values]
#     adapted['time'] = [gs.current_time]
#     dict_output[FigureNames.price_res] = deepcopy(adapted)
#
#     #     price_prod
#     adapted = dict()
#     for key, values in market_vals.items():
#         if key in Prod:
#             adapted[key.name] = [values]
#     adapted['time'] = [gs.current_time]
#     dict_output[FigureNames.price_prod] = deepcopy(adapted)
#
#     #     budget
#     adapted = dict()
#     adapted['budget'] = gs.budget.return_data()['budget']
#     adapted['time'] = [gs.current_time]
#     dict_output[FigureNames.budget] = deepcopy(adapted)
#     # checks here
#     return dict_output