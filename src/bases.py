from abc import ABC
import os
import pickle

class Base(ABC):
    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return str(self.__repr__())

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        if value < 0:
            raise InsufficentQuantityError
        self.__dict__[key] = value
        return True

    def __setattr__(self, key, value):
        if value is int:
            if value < 0:
                raise InsufficentQuantityError
        super().__setattr__(key, value)
        return

    def dump(self, file_path="../save/", file_name=None):
        if not file_name:
            file_name = self.__class__.__name__ + "_save.pkl"
        if not file_name.endswith(".pkl"):
            file_name += ".pkl"
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        with open(file_path + file_name, "wb") as file:
            pickle.dump(self.__dict__, file, -1)
        return True

    def load(self, file_path="../save/", file_name=None):
        if not file_name:
            file_name = self.__class__.__name__ + "_save.pkl"
        if not os.path.isdir(file_path):
            print(f"File path {file_path} does not exist.")
            raise FileNotFoundError
        if not os.path.isfile(file_path + file_name):
            print(f"File {file_name} does not exist in specified directory {file_path}.")
            raise FileNotFoundError
        with open(file_path + file_name, "rb") as file:
            self.__dict__ = pickle.load(file)
        return True


class BaseInt(ABC):
    def __init__(self, item):
        self.item = item

    def __repr__(self):
        return self.item

    def __str__(self):
        return str(self.__repr__())

    def __add__(self, other):
        self.item += other
        return self.item

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __sub__(self, other):
        self.item -= other
        if self.item < 0:
            raise InsufficentQuantity
        return self.item

    def __isub__(self, other):
        self.__sub__(other)
        return self

    def __mul__(self, other):
        self.item *= other
        return self.item

    def __imul__(self, other):
        self.__mul__(other)
        return self

    def __rmul__(self, other):
        self.__mul__(other)
        return self.item

    def dump(self, file_path="../save/", file_name=None):
        if not file_name:
            file_name = self.__class__.__name__ + "_save.pkl"
        if not file_name.endswith(".pkl"):
            file_name += ".pkl"
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        with open(file_path + file_name, "wb") as file:
            pickle.dump(self.item, file, -1)
        return True

    def load(self, file_path="../save/", file_name=None):
        if not file_name:
            file_name = self.__class__.__name__ + "_save.pkl"
        if not os.path.isdir(file_path):
            print(f"File path {file_path} does not exist.")
            raise FileNotFoundError
        if not os.path.isfile(file_path + file_name):
            print(f"File {file_name} does not exist in specified directory {file_path}.")
            raise FileNotFoundError
        with open(file_path + file_name, "rb") as file:
            self.item = pickle.load(file)
        return True

# TODO: write tests for this

class Cla(BaseInt):
    def __init__(self):
        self.one = 1
        super().__init__(self.one)


x = Cla()
print(x)
y = x * 3
print(y)
