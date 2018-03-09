from abc import ABC
import os
import pickle
import logging
from exceptions import InsufficientQuantityError

class Base(ABC):

    def __str__(self):
        tmp = dict()
        for key, value in self.__dict__.items():
            tmp[str(key)] = str(value)
        return str(tmp)

    def __getitem__(self, item):
        try:
            return self.__dict__[item]
        except KeyError as e:
            logging.error(self.__dict__)
            raise e

    def __setitem__(self, key, value):
        if value < 0:
            logging.warning(f"Insufficient quantity in {self.__class__}. "
                            f"{value} in {key} is negative.")
            raise InsufficientQuantityError
        self.__dict__[key] = value
        return True

    def __setattr__(self, key, value):
        if value is int:
            if value < 0:
                logging.warning(f"Insufficient quantity in {self.__class__}. "
                                f"{value} in {key} is negative.")
                raise InsufficientQuantityError
        super().__setattr__(key, value)
        return

    def check_if_sufficient(self, category, quantity):
        if self[category] >= quantity:
            return True
        else:
            return False


class BaseInt(ABC):
    def __init__(self, item):
        self.item = item

    def __str__(self):
        return str(self.item)

    def __add__(self, other):
        self.item += other
        return self.item

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __sub__(self, other):
        self.item -= other
        if self.item < 0:
            logging.warning(f"Insufficient quantity in {self.__class__}. "
                            f"Attempting to deduct {other} from {self.item}.")
            raise InsufficientQuantityError
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
            logging.error(f"File path {file_path} does not exist.")
            raise FileNotFoundError
        if not os.path.isfile(file_path + file_name):
            logging.error(f"File {file_name} does not exist in specified "
                          f"directory {file_path}.")
            raise FileNotFoundError
        with open(file_path + file_name, "rb") as file:
            self.item = pickle.load(file)
        return True
