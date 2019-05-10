from global_config import Res, Prod, Properties, WarehouseStats


class InventoryCostCalculator:
    def __init__(self, inventory):
        self.inventory = inventory

    def _calculate_total_weight(self):
        weight = 0
        for item, count in self.inventory.items():
            # tier not in Properties
            if item in Properties:
                per_item_weight = Properties[item].weight
                weight += count * per_item_weight
        return weight

    def _calculate_total_volume(self):
        volume = 0
        for item, count in self.inventory.items():
            if item in Properties:
                per_item_volume = Properties[item].volume
                volume += count * per_item_volume
        return volume

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
        weight = Properties[item].weight
        cost += WarehouseStats.movein_cost[tier].weight * weight
        volume = Properties[item].volume
        cost += WarehouseStats.movein_cost[tier].volume * volume
        cost *= quantity
        return cost

    def moveout_cost(self, item, quantity):
        cost = 0
        tier = self.inventory['tier']
        weight = Properties[item].weight
        cost += WarehouseStats.moveout_cost[tier].weight * weight
        volume = Properties[item].volume
        cost += WarehouseStats.moveout_cost[tier].volume * volume
        cost *= quantity
        return cost


class Inventory:
    def __init__(self, inventory_values):
        self.inventory = inventory_values
        self.calculator = InventoryCostCalculator(inventory_values)

    def set_values(self, values):
    #   Should only be used for load/any other non-call functions.
    #   Can eventually be used for setting calculator values too,
    #   like warehouse tier
        for category, quantity in values.items():
            self.inventory[category] = quantity
        return True

    def return_data(self):
        return self.inventory

    def movein_cost(self, category, quantity):
        return self.calculator.movein_cost(category, quantity)

    def moveout_cost(self, category, quantity):
        return self.calculator.moveout_cost(category, quantity)

    def storage_cost(self):
        return self.calculator.storage_cost()

    def add(self, category, quantity):
        self.inventory[category] += quantity
        return True

    def sub(self, category, quantity):
        self.inventory[category] -= quantity
        return True

    def replace(self, category, quantity):
        self.inventory[category] = quantity
        return True

    def get(self, category):
        return self.inventory[category]
