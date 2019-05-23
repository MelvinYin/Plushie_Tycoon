from global_config import Res, Prod, WarehouseStats
from collections import defaultdict

class InventoryCostCalculator:
    def __init__(self, inventory):
        self.inventory = inventory

    def _calculate_total_weight(self):
        weight = 0
        for item, per_unit_weight in self.inventory['weight'].items():
            weight += per_unit_weight * self.inventory[item]
        return weight

    def _calculate_total_volume(self):
        volume = 0
        for item, per_unit_volume in self.inventory['volume'].items():
            volume += per_unit_volume * self.inventory[item]
        return volume

    def get_storage_cost_for(self, item):
        cost = 0
        tier = self.inventory['tier']
        weight = self.inventory['weight'][item]
        volume = self.inventory['volume'][item]
        cost += WarehouseStats.store_cost[tier].weight * weight
        cost += WarehouseStats.store_cost[tier].volume * volume
        assert cost >= 0
        return cost

    def storage_cost(self):
        cost = 0
        tier = self.inventory['tier']
        total_weight = self._calculate_total_weight()
        cost += WarehouseStats.store_cost[tier].weight * \
                total_weight
        total_volume = self._calculate_total_volume()
        cost += WarehouseStats.store_cost[tier].volume * total_volume
        return cost

    def movein_cost(self, item, quantity):
        cost = 0
        tier = self.inventory['tier']
        weight = self.inventory['weight'][item]
        cost += WarehouseStats.movein_cost[tier].weight * weight
        volume = self.inventory['volume'][item]
        cost += WarehouseStats.movein_cost[tier].volume * volume
        cost *= quantity
        return cost

    def moveout_cost(self, item, quantity):
        cost = 0
        tier = self.inventory['tier']
        weight = self.inventory['weight'][item]
        cost += WarehouseStats.moveout_cost[tier].weight * weight
        volume = self.inventory['volume'][item]
        cost += WarehouseStats.moveout_cost[tier].volume * volume
        cost *= quantity
        return cost

class GlobalInventory:
    def __init__(self, inventory_values):
        self.inventory = inventory_values
        self.calculator = InventoryCostCalculator(inventory_values)
        self.movements = defaultdict(int)

    def get_index(self):
        index = list(self.inventory['weight'].keys())
        return index

    def get_all_movein_cost(self, factor=1):
        costs = dict()
        index = self.get_index()
        for category in index:
            costs[category] = self.get_movein_cost(category) * factor
        return costs

    def get_all_moveout_cost(self, factor=1):
        costs = dict()
        index = self.get_index()
        for category in index:
            costs[category] = self.get_moveout_cost(category) * factor
        return costs

    def get_all_storage_cost(self, factor=1):
        costs = dict()
        index = self.get_index()
        for category in index:
            costs[category] = self.get_storage_cost(category) * factor
        return costs

    def get_movein_cost(self, item):
        value = self.calculator.movein_cost(item, 1)
        assert value >= 0
        return value

    def get_moveout_cost(self, item):
        value = self.calculator.moveout_cost(item, 1)
        assert value >= 0
        return value

    def get_storage_cost(self, item):
        value = self.calculator.get_storage_cost_for(item)
        assert value >= 0
        return value

    def reset_movements(self):
        self.movements = defaultdict(int)
        return True

    def return_data(self):
        return self.inventory

    def movein_cost(self, category, quantity):
        return self.calculator.movein_cost(category, quantity)

    def moveout_cost(self, category, quantity):
        return self.calculator.moveout_cost(category, quantity)

    def get_movement_cost(self):
        cost = 0
        for category, quantity in self.movements.items():
            if quantity > 0:
                cost += self.movein_cost(category, quantity)
            elif quantity < 0:
                cost += self.moveout_cost(category, abs(quantity))
        assert cost >= 0
        return cost

    def storage_cost(self):
        return self.calculator.storage_cost()

    def add(self, category, quantity):
        self.inventory[category] += quantity
        self.movements[category] += quantity
        return True

    def sub(self, category, quantity):
        self.inventory[category] -= quantity
        self.movements[category] -= quantity
        return True

    def replace(self, category, quantity):
        self.inventory[category] = quantity
        return True

    def get(self, category):
        return self.inventory[category]
