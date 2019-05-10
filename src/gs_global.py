from gs_subclass import Inventory, Market, Budget, Production
from global_config import Func
from collections import defaultdict

class GSGlobal:
    def __init__(self, GSDataClass):
        self.inventory = Inventory(GSDataClass.inventory)
        self.market = Market(GSDataClass.market)
        self.budget = Budget(GSDataClass.budget)
        self.production = Production(GSDataClass.production)
        self.current_time = GSDataClass.time
        self.history = defaultdict(list)
        self.callstack = None

    def format_output(self):
        output = ""
        output += "<br />[End of turn]<br />"
        output += "Commands implemented: "
        for action, cat_quantity in self.callstack.items():
            for category, quantity in cat_quantity.items():
                if 'name' in action.__dict__:
                    action = action.name
                if 'name' in category.__dict__:
                    category = category.name
                output += "<br />{} {} {}".format(action, category, quantity)
        output += "<br />End."
        return output

    def get(self, classification, *args):
        if classification == 'inventory':
            return self.inventory.get(*args)
        elif classification == 'market':
            return self.market.get(*args)
        elif classification == 'budget':
            return self.budget.get()
        elif classification == 'production':
            return self.production.get(*args)
        elif classification == 'time':
            return self.current_time
        else:
            raise Exception

    def sub(self, classification, *args):
        if classification == 'inventory':
            return self.inventory.sub(*args)
        elif classification == 'budget':
            return self.budget.sub(*args)
        else:
            raise Exception

    def add(self, classification, *args):
        if classification == 'inventory':
            return self.inventory.add(*args)
        elif classification == 'budget':
            return self.budget.add(*args)
        elif classification == 'time':
            self.current_time += 1
            return True
        else:
            raise Exception

    def implement_callstack(self):
        for action, cat_quantity in self.callstack.items():
            for category, quantity in cat_quantity.items():
                if action == Func.buy:
                    self.buy(category, quantity)
                elif action == Func.sell:
                    self.sell(category, quantity)
                elif action == Func.make:
                    self.make(category, quantity)
                else:
                    raise Exception
        self.current_time += 1
        return True

    # Taken from GE
    def buy(self, category, quantity):
        self.inventory.add(category, quantity)
        price = self.market.get(category)
        total_cost = price * quantity
        self.budget.sub('budget', total_cost)
        return 'update'

    def sell(self, category, quantity):
        self.inventory.sub(category, quantity)
        price = self.market.get(category)
        total_cost = price * quantity
        self.budget.add('budget', total_cost)
        return 'update'

    def make(self, category, quantity):
        cost, materials = self.production.get(category)
        for _category, material in materials.items():
            self.inventory.sub(_category, material * quantity)
        self.budget.sub('budget', cost * quantity)
        self.inventory.add(category, quantity)
        return 'update'

