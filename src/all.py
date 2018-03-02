from resources import ResourceCost
from inventory import ResourceInventory, PlushieInventory
from market import MarketResource, MarketPlushie
from production import ProductionCost
from budget import Budget
from singleton import Singleton

"""
Production cost may chane over quantity scale.
Selling of plushies may decrease price during transaction itself.
"""

def sell_plushie(type, quantity):
    curr_prices = get_curr_prices(type)
    plushies[type] -= quantity
    earnings = curr_prices * quantity
    budget += earnings

class GameEngine:
    __metaclass__ = Singleton
    print()
    def __init__(self):
        self.m_resource = MarketResource()
        self.m_plushie = MarketPlushie()
        self.resource_cost = ResourceCost()
        self.resources = ResourceInventory()
        self.plushies = PlushieInventory()
        self.budget = Budget()
        self.production_cost = ProductionCost()
        self.time_steps = 0

        print("Game Engine Initialised")

    def load_game(self):
        self.resources.load()
        self.plushies.load()
        self.budget.load()

    def start_game(self, load=True):
        if load:
            self.load_game()
        print("Game Started.")
        print("Initial Stats: ")
        self.show_stats()
        return True

    def save_game(self):
        self.resources.dump()
        self.plushies.dump()
        self.budget.dump()
        return True

    def query_buy_resource(self):
        cat_quan = input("How many of which?")
        tmp = cat_quan.strip().split(",")
        category = tmp[0].strip()
        quantity = int(tmp[1].strip())
        self.buy_res(category, quantity)
        print("Resources bought.")
        return True

    def query_make_plushie(self):
        cat_quan = input("How many of which?")
        tmp = cat_quan.strip().split(",")
        category = tmp[0].strip()
        quantity = int(tmp[1].strip())
        self.make_plushie(category, quantity)
        print("Plushies made.")
        return True

    def query_sell_plushie(self):
        cat_quan = input("How many of which?")
        tmp = cat_quan.strip().split(",")
        category = tmp[0].strip()
        quantity = int(tmp[1].strip())
        self.make_plushie(category, quantity)
        print("Plushies made.")
        return True

    def sell_plushie(self, type, quantity):
        curr_prices = self.m_plushie(type)
        self.plushies[type] -= quantity
        earnings = curr_prices * quantity
        self.budget += earnings
        return True

    def query_action(self):
        desired_action = input("What would you like to do? ")
        if desired_action == "buy resource":
            self.query_buy_resource()

        elif desired_action == "make plushie":
            self.query_make_plushie()

        elif desired_action == "sell plushie":
            self.query_sell_plushie()

        elif desired_action == "save game":
            self.save_game()
            print("Game Saved.")

        elif desired_action == "show stats":
            self.show_stats()

        elif desired_action == "show prices":
            self.show_prices()

        elif desired_action == "skip":
            self.next_turn()

        elif desired_action == "load game":
            self.load_game()

        elif desired_action == "quit":
            self.query_if_save()
            return
        else:
            print(f"Input '{desired_action}' not recognised.")
        return self.query_action()

    def query_if_save(self):
        to_save = input("Do you wish to save before quitting?")
        if to_save:
            self.save_game()
        return

    def buy_res(self, category, quantity):
        curr_res_p = self.m_resource[category]
        cost_to_buy = curr_res_p * quantity
        self.budget -= cost_to_buy
        self.resources[category] += quantity
        return True

    def make_plushie(self, type, quantity):
        res_for_type = self.resource_cost(type)
        total_res = res_for_type * quantity
        for category, quantity in total_res.items():
            self.resources[category] -= quantity
        cost_to_produce = self.production_cost(type, quantity)
        self.budget -= cost_to_produce
        self.plushies[type] += quantity
        return True

    def show_stats(self):
        print("Current Inventory:")
        print(self.resources)
        print(self.plushies)
        print("\n")

        print("Current Budget:")
        print(self.budget)
        print("\n")

        print("Current Market Prices:")
        print(self.m_plushie)
        print(self.m_resource)
        print("\n")

        print("Fixed Costs:")
        print(self.resource_cost)
        print(self.production_cost)
        print("\n")

        print("Time elapsed:")
        print(self.time_steps)
        print("\n")
        return

    def show_prices(self):
        print("Current Market Prices:")
        print(self.m_plushie)
        print(self.m_resource)
        print("\n")
        return



x = GameEngine()

x.query_action()













