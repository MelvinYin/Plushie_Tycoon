from singleton import Singleton

class InsufficentQuantity(Exception):
    pass

class Inventory(metaclass=Singleton):
    def __init__(self):
        self.budget = self._default_budget()
        self.resource = self._default_resources()
        self.plushie = self._default_plushie()

    def _default_resources(self):
        resource = dict(cloth=0, stuff=0, accessory=0, packaging=0)
        return resource

    def _default_plushie(self):
        plushie = dict(Aisha=0, Beta=0, Chama=0)
        return plushie
    
    def _default_budget(self):
        return 10000

    def check_plushie(self, type):
        if self.plushie[type] < 0:
            raise InsufficentQuantity

    def check_resource(self, type):
        if self.resource[type] < 0:
            raise InsufficentQuantity



