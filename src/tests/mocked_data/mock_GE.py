import os
import sys

from exceptions import InvalidInputException
from logs import log
import inspect
from config.global_config import Res, Prod, Func, ResPrice, ProdPrice, \
    res_members, prod_members

class mock_ge:
    def __init__(self):
        self.data = self.create_init_data()
        self.res_cost = self.set_res_cost()
        self.store = self.create_init_store()

    def set_res_cost(self):
        res_cost = dict()
        for prod in prod_members:
            cost_for_prod = dict()
            for i, res in enumerate(res_members):
                cost_for_prod[res] = i+1
            res_cost[prod] = cost_for_prod
        return res_cost

    def make(self, call):
        category = call['category']
        if type(category) != Prod:
            raise InvalidInputException
        quantity = call['quantity']
        all_res_costs = self.res_cost[category]
        for res, cost in all_res_costs.items():
            self.data[Res][res] -= cost * quantity
        self.data[Prod][category] += quantity
        return

    def buy(self, call):
        category = call['category']
        quantity = call['quantity']
        if type(category) == Res:
            cost = self.data['price'][Res][category] * quantity
        elif type(category) == Prod:
            cost = self.data['price'][Prod][category] * quantity
        else:
            raise Exception
        self.data['budget'] -= cost
        self.data[type(category)][category] += quantity
        return

    def sell(self, call):
        category = call['category']
        quantity = call['quantity']
        if type(category) == Res:
            cost = self.data['price'][Res][category] * quantity
        elif type(category) == Prod:
            cost = self.data['price'][Prod][category] * quantity
        else:
            raise Exception
        self.data['budget'] += cost
        self.data[type(category)][category] -= quantity
        return

    def next(self, call):
        self.data['time'] += 1
        return

    def callback(self, call):
        log("mock_GE callback: {}".format(call), inspect.currentframe())
        if call['command'] == Func.make:
            self.make(call)
        elif call['command'] == Func.buy:
            self.buy(call)
        elif call['command'] == Func.sell:
            self.sell(call)
        elif call['command'] == Func.next:
            self.data['time'] += 1
        elif call['command'] == Func.quit:
            sys.exit()
        else:
            log("Command not implemented in mock_ge.", inspect.currentframe())
            raise InvalidInputException
        self.update_store()
        return self.store

    def create_init_data(self):
        data = dict()
        data[Res] = {item: 100 for item in res_members}
        data['time'] = 0
        data['budget'] = 100000
        data[Prod] = {item: 100 for item in prod_members}
        data['price'] = dict()
        data['price'][Res] = {item: i+1 for i, item in enumerate(
            res_members)}
        data['price'][Prod] = {item: 100+i+1 for i, item in enumerate(
            prod_members)}
        return data

    def get_init_data(self):
        return self.store

    def update_store(self):
        self.store['price'][Res] = dict()
        self.store['price'][Prod] = dict()
        for res in res_members:
            self.store[Res][res] = [self.data[Res][res]]
            self.store['price'][Res][res] = [self.data['price'][Res][res]]
        for prod in prod_members:
            self.store[Prod][prod] = [self.data[Prod][prod]]
            self.store['price'][Prod][prod] = [self.data['price'][Prod][
                                                        prod]]
        self.store['time'] = [self.data['time']]
        return

    def create_init_store(self):
        store = dict()
        store[Res] = {item: [100] for item in res_members}
        store[Prod] = {item: [100] for item in prod_members}
        store['price'] = dict()
        store['price'][Res] = {item: [i+1] for i, item in enumerate(
            res_members)}
        store['price'][Prod] = {item: [100+i+1] for i, item in enumerate(
            prod_members)}
        store['time'] = [0]
        return store