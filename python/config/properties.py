##############################################################################
# Widget Specs

from collections import namedtuple

##############################################################################
# Global
try:
    from base import Res, Prod, Func
except:
    from .base import Res, Prod, Func

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












