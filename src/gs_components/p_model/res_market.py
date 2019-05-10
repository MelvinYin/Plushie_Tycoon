def bound(value, low, high):
    return max(low, min(high, value))


import matplotlib.pyplot as plt

class GenericBuyer:
    def __init__(self):
        self.grad = 0.7
        self.min_q = 20
        self.max_p = 70
        self.max_q = 60

    def __call__(self, p):
        return self.demand_formula(p)

    def demand_formula(self, p):
        q = self.min_q + (self.max_p - p) * self.grad
        return bound(q, self.min_q, self.max_q)

class GenericSeller:
    def __init__(self):
        self.grad = 0.7
        self.min_q = 30
        self.min_p = 10
        self.max_q = 60

    def __call__(self, p):
        return self.supply_formula(p)

    def supply_formula(self, p):
        q = self.min_q + (p - self.min_p) * self.grad
        return bound(q, self.min_q, self.max_q)

class ConsolidatedBuyer:
    def __init__(self, buyers):
        self.buyers = buyers

    def buy(self, price):
        total_quantity = 0
        for buyer in self.buyers:
            total_quantity += buyer.buy(price)
        return total_quantity

class ConsolidatedSeller:
    def __init__(self, sellers):
        self.sellers = sellers

    def sell(self, price):
        total_quantity = 0
        for seller in self.sellers:
            total_quantity += seller.sell(price)
        return total_quantity

class LinearBuyer:
    def __init__(self, grad=0.9, ref_q=1000, ref_p=10):
        self.grad = grad
        self.ref_q = ref_q
        self.ref_p = ref_p

    def buy(self, price):
        quantity = self.ref_q + (self.ref_p - price) * self.grad
        return quantity

class LinearSeller:
    def __init__(self, grad=0.9, ref_q=1000, ref_p=10):
        self.grad = grad
        self.ref_q = ref_q
        self.ref_p = ref_p

    def sell(self, price):
        quantity = self.ref_q + (price - self.ref_p) * self.grad
        return quantity

class ClearingHouse:
    """
    For now, we sell all q at equilibrium q.
    In future, have test calls to buyer and seller before locking it in (and
    thereby locking long-term values)
    Price spiking and crashing should be handled by actors, not by clearinghouse.

    Implement an auction-house style in future, where purchase and selling bids
    are posted, then final price offered/quantity received is returned later.
    Quantity received/average price can then be a random function of the
    clearing. Generally close to bid price, if we start from min_p of seller.
    Maybe.

    Perhaps initiate fixed prices at the start, and then variable prices
    later on.
    """
    price_resolution = 0.1
    def __init__(self, buyer=GenericBuyer(), seller=GenericSeller()):
        self.seller = seller
        self.buyer = buyer

    def __call__(self):
        """ possibility of a endless loop...? from while.
        """
        current_price = 0
        past = ["low", "low", "low"]
        while True:
            buyer_q = self.buyer.buy(current_price)
            seller_q = self.seller.sell(current_price)
            if past[0] == past[2] and past[0] != past[1]:
                break
            if buyer_q > seller_q:
                current_price += self.price_resolution
                del past[0]
                past.append("low")
            elif buyer_q < seller_q:
                current_price -= self.price_resolution
                del past[0]
                past.append("high")
            else:
                break
        return current_price

class Mybuyer:
    def __init__(self):
        pass

    def buy(self, price):
        return 10


class Myseller:
    def __init__(self):
        pass

    def sell(self, price):
        return 8


def main():
    buyers = [Mybuyer(), LinearBuyer()]
    sellers = [Myseller(), LinearSeller()]
    con_buy = ConsolidatedBuyer(buyers)
    con_sell = ConsolidatedSeller(sellers)
    house = ClearingHouse(buyer=con_buy, seller=con_sell)

# buyer = GenericBuyer()
# seller = GenericSeller()
# input_p = range(100)
# demand_q = [buyer(p) for p in input_p]
# supply_q = [seller(p) for p in input_p]
#
# plt.figure(1)
# plt.plot(demand_q, "x-", color="r")
# plt.plot(supply_q, "x-", color="g")
# plt.show()



