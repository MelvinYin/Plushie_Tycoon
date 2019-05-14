class ProductionBackend:
    def __init__(self, init_values):
        self.hours_needed = init_values.hours_needed
        self.cost_per_hour = init_values.cost_per_hour
        self.res_cost = init_values.res_ratio

    def get_cost(self, category):
        hours = self.hours_needed[category]
        materials = self.res_cost[category]
        cost = hours * self.cost_per_hour
        return cost, materials

