from defaults import res_index
import pandas as pd

class ResTrader:
    """ Semi-immediate linear response for now. Cannot be delta-fn because
    of potential instability and oscillation.
    """
    capacity = 100  # in dollar, to rise over time
    sell_lin_grad = 0.5
    buy_lin_grad = 0.5
    res_inventory = pd.Series([0 for __ in range(len(res_index))], res_index,
                              name="res_inventory")

    @classmethod
    def to_hoard(cls, category, p_gap, p_per_prod):
        if p_gap <= 0:
            return 0
        quantity_to_buy = p_gap * cls.buy_lin_grad
        cost = quantity_to_buy * p_per_prod
        if cost > cls.capacity:
            quantity_to_buy = cls.capacity / p_per_prod   # fraction allowed for now
            cost = cls.capacity
        cls.capacity -= cost
        cls.res_inventory[category] += quantity_to_buy
        return quantity_to_buy

    @classmethod
    def to_dump(cls, category, p_gap):
        if p_gap >= 0:
            return 0
        quantity_to_sell = p_gap * cls.buy_lin_grad
        current_inventory = cls.res_inventory[category]
        if quantity_to_sell > current_inventory:
            quantity_to_sell = cls.res_inventory[category]
        cls.res_inventory[category] -= quantity_to_sell
        return quantity_to_sell

