from resources import ResourceCost
from inventory import ResourceInventory, PlushieInventory
from market import MarketResource, MarketPlushie
from production import ProductionCost
from budget import Budget
from singleton import Singleton
from count import Count
import sys


    # create a GameState later

class GameEngine:
    __metaclass__ = Singleton
    def __init__(self):
        self.m_resource = MarketResource()
        self.m_plushie = MarketPlushie()
        self.resource_cost = ResourceCost()
        self.resources = ResourceInventory()
        self.plushies = PlushieInventory()
        self.budget = Budget()
        self.production_cost = ProductionCost()
        self.time_steps = 0


    def buy_res(self, category, quantity):
        curr_res_p = self.m_resource[category]
        cost_to_buy = curr_res_p * quantity
        self.budget -= cost_to_buy
        self.resources[category] += quantity
        return True

    def sell_res(self, category, quantity):
        curr_res_p = self.m_resource[category]
        earnings = curr_res_p * quantity
        self.budget += earnings
        self.resources[category] -= quantity
        return True

    def buy_plushie(self, category, quantity):
        curr_prices = self.m_plushie[category]
        cost_to_buy = curr_prices * quantity
        self.budget -= cost_to_buy
        self.plushies[category] += quantity
        return True

    def sell_plushie(self, category, quantity):
        curr_prices = self.m_plushie[category]
        self.plushies[category] -= quantity
        earnings = curr_prices * quantity
        self.budget += earnings
        return True

    def make_plushie(self, type, quantity):
        res_for_type = self.resource_cost[type]
        total_res = res_for_type * quantity
        for category, quantity in total_res.items():
            if not self.resources[category] >= quantity:
                raise InsufficentQuantityError

        cost_to_produce = self.production_cost(type, quantity)
        self.budget -= cost_to_produce
        for category, quantity in total_res.items():
            self.resources[category] -= quantity
        self.plushies[type] += quantity
        return True


    def show_stats(self):
        print("Current Inventory:")
        print(self.resources)
        print(self.plushies)

        print("Current Budget:")
        print(self.budget)

        print("Current Market Prices:")
        print(self.m_plushie)
        print(self.m_resource)

        print("Fixed Costs:")
        print(self.resource_cost)
        print(self.production_cost)

        print("Time elapsed:")
        print(self.time_steps)
        return

    def show_prices(self):
        print("Current Market Prices:")
        print(self.m_plushie)
        print(self.m_resource)
        print("\n")
        return


    def save_game(self):
        self.resources.dump()
        self.plushies.dump()
        self.budget.dump()
        return True

    def load_game(self):
        self.resources.load()
        self.plushies.load()
        self.budget.load()

    def next_turn(self):
        self.time_steps += 1

    def quit_game(self):
        print("Thank you for playing.")
        sys.exit()

    def save_quit(self):
        self.save_game()
        self.quit_game()

    def start_game(self, load=True):
        if load:
            self.load_game()
        print("Game Started.")
        print("Initial Stats: ")
        self.show_stats()
        return True






