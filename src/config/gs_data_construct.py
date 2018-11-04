from init_values import InitValues


class GSConstructor:
    def __init__(self):
        self.production = None
        self.budget = None
        self.inventory = None
        self.market = None
        self.time = None

    def is_complete(self):
        all_full = True
        if None in (self.__dict__.values()):
            all_full = False
        return all_full

    def load_init(self, to_load=None):
        init_values = InitValues()
        for var_name, value in init_values.__dict__.items():
            if (to_load is None or var_name in to_load)\
                    and var_name in self.__dict__:
                self.__dict__[var_name] = value





