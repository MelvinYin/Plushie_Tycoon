from global_config import Res, Prod

class InventoryCostCalculator:
    def __init__(self, warehouse_tier):
        self.warehouse_tier = warehouse_tier

    # def remove(self, category, quantity):
    #     if self.warehouse_tier == 0:
    #         price =

class InventoryBackend:
    def __init__(self, inventory_values):
        """
        :param inventory_values: InventoryTuple(res={res.cloth:1001,...})
        """
        self.res = inventory_values.res  # Maybe pd.series
        self.prod = inventory_values.prod
        self.type_map = self._get_type_map()

    def add(self, category, quantity):
        item_signal = type(category)
        item = self.type_map[item_signal]
        item[category] += quantity
        return True

    def sub(self, category, quantity):
        item_signal = type(category)
        item = self.type_map[item_signal]
        item[category] -= quantity
        return True

    def replace(self, category, quantity):
        item_signal = type(category)
        item = self.type_map[item_signal]
        item[category] = quantity
        return True

    def _get_type_map(self):
        mapping = dict()
        mapping[Res] = self.res
        mapping[Prod] = self.prod
        return mapping

    def get(self, category):
        item_signal = type(category)
        item = self.type_map[item_signal]
        return item[category]
