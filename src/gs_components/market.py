from global_config import Res, Prod

class Market:
    """
    Does not have external setting capabilities unless value
    explicitly called.
    """
    def __init__(self, market_values):
        self.market = market_values

    def set_values(self, values):
        for category, price in values.items():
            self.market[category] = price
        return True

    def get(self, category):
        return self.market[category]

    def return_data(self):
        return self.market


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
    def __init__(self, buyer, seller):
        self.seller = seller
        self.buyer = buyer

    def clear(self):
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
    def __init__(self, quantity):
        self.quantity = quantity
        pass

    def buy(self, price):
        return self.quantity

class Myseller:
    def __init__(self, quantity):
        self.quantity = quantity
        pass

    def sell(self, price):
        return self.quantity

# def main():
#     buyers = [Mybuyer(), LinearBuyer()]
#     sellers = [Myseller(), LinearSeller()]
#     con_buy = ConsolidatedBuyer(buyers)
#     con_sell = ConsolidatedSeller(sellers)
#     house = ClearingHouse(buyer=con_buy, seller=con_sell)

class GlobalMarket:
    """
    Does not have external setting capabilities unless value
    explicitly called.
    """
    def __init__(self, market_values):
        self.ind_markets = self.spawn_markets(market_values)

    def spawn_markets(self, values):
        ind_markets = dict()
        for category, price in values.items():
            ind_market = IndividualMarket(price)
            ind_markets[category] = ind_market
        return ind_markets

    def set_values(self, values):
        for category, price in values.items():
            self.ind_markets[category].current_price = price
        return True

    def return_data(self):
        output = dict()
        for category, ind_market in self.ind_markets.items():
            output[category] = ind_market.get()
        return output

    def get(self, category):
        return self.ind_markets[category].get()

    def clear_market(self, callstack):
        # assumed callstack already collapsed
        # this should be organised by category => action => quantity
        for category, remainder in callstack.items():
            buy_q = remainder['buy']
            sell_q = remainder['sell']
            self.ind_markets[category].clear_market(buy_q, sell_q)
        return True

class IndividualMarket:
    def __init__(self, price):
        self.current_price = price

    def get(self):
        return self.current_price

    def clear_market(self, buy_q, sell_q):
        buyers = [Mybuyer(buy_q), LinearBuyer(ref_p=self.current_price)]
        sellers = [Myseller(sell_q), LinearSeller(ref_p=self.current_price)]
        con_buy = ConsolidatedBuyer(buyers)
        con_sell = ConsolidatedSeller(sellers)
        house = ClearingHouse(buyer=con_buy, seller=con_sell)
        price = house.clear()
        self.current_price = price
        return price