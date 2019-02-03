##############################################################################
# Widget Specs

from collections import namedtuple
from enum import Enum, auto, unique

##############################################################################
# Global
try:
    from base import Res, Prod, Func, res_members, prod_members
except:
    from .base import Res, Prod, Func, res_members, prod_members

_WarehouseStats = namedtuple("WarehouseStats", "weight volume")

class WarehouseStats:
    capacity = dict()
    capacity[0] = _WarehouseStats(weight=10000, volume=10000)
    capacity[1] = _WarehouseStats(weight=50000, volume=50000)
    capacity[2] = _WarehouseStats(weight=200000, volume=200000)

    store_cost = dict()
    store_cost[0] = _WarehouseStats(weight=0.005, volume=0.005)
    store_cost[1] = _WarehouseStats(weight=0.005, volume=0.005)
    store_cost[2] = _WarehouseStats(weight=0.005, volume=0.005)

    movein_cost = dict()
    movein_cost[0] = _WarehouseStats(weight=0.005, volume=0.005)
    movein_cost[1] = _WarehouseStats(weight=0.05, volume=0.05)
    movein_cost[2] = _WarehouseStats(weight=0.05, volume=0.05)

    moveout_cost = dict()
    moveout_cost[0] = _WarehouseStats(weight=0.005, volume=0.005)
    moveout_cost[1] = _WarehouseStats(weight=0.05, volume=0.05)
    moveout_cost[2] = _WarehouseStats(weight=0.05, volume=0.05)

Properties = dict()
Properties[Res.cloth] = _WarehouseStats(weight=0.1, volume=0.1)
Properties[Res.stuff] = _WarehouseStats(weight=0.05, volume=0.3)
Properties[Res.accessory] = _WarehouseStats(weight=0.3, volume=0.01)
Properties[Res.packaging] = _WarehouseStats(weight=0.05, volume=0.2)
Properties[Prod.aisha] = _WarehouseStats(weight=0.05, volume=0.2)
Properties[Prod.beta] = _WarehouseStats(weight=0.05, volume=0.2)
Properties[Prod.chama] = _WarehouseStats(weight=0.05, volume=0.2)













