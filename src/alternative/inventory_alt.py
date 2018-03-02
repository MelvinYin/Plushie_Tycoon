from singleton import Singleton

class InsufficentQuantity(Exception):
    pass

class Inventory(metaclass=Singleton):
    def __init__(self):
        self.budget = 10000
        self.resource = self._default_resources()
        self.plushie = self._default_plushie()

    def _default_resources(self):
        resource = dict(cloth=0, stuff=0, accessory=0, packaging=0)
        return resource

    def _default_plushie(self):
        plushie = dict(Aisha=0, Beta=0, Chama=0)
        return plushie

    def _check_plushie(self, type):    # might be better to skip explicit checking, but eafp?
        if self.__plushie[type] < 0:
            raise InsufficentQuantity(
                f"Input plushie list has a negative value, {type} = {self.__plushie[type]}")

    def _check_resource(self, type):
        if self.__resource[type] < 0:
            raise InsufficentQuantity(
                f"Input resource list has a negative value, {type} = {self.__resource[type]}")

    @property
    def resource(self):
        for name in self.__resource.keys():
            self._check_resource(name)
        return self.__resource

    @resource.setter
    def resource(self, resource):
        self.__resource = resource

    @property
    def plushie(self):
        for name in self.__plushie.keys():
            self._check_plushie(name)
        return self.__plushie

    @plushie.setter
    def plushie(self, plushie):
        self.__plushie = plushie






