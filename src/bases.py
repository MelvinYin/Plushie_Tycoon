from abc import ABC
import os
import pickle
import logging
from exceptions import InsufficientQuantityError
import pandas as pd

class BaseInventory(ABC):

    def __init__(self, input_pd_series):
        """
        By sending a pd.Series object down, instance attributes corresponding
        to the key+value of the Series is added. This allows having an
        arbitrary set of instance attributes, that are set by a config file
        outside.

        Use Case:
        Inventory can obtain from defaults the set of res/prod to use.
        Subsequent __getattribute__ access will work for instances of the
        Inventory class. Changes to res/prod items, including adding of new
        items, will therefore not require changes to Inventory classes.
        """
        self.pd_data = input_pd_series
        for name, value in self.pd_data.iteritems():
            self.__dict__[name] = value

    def __str__(self):
        """
        Attempt to convert as many fields in __dict__ into str() form as
        possible. Doesn't work for values that do not have nice __str__ forms.
        """
        tmp = dict()
        for key, value in self.__dict__.items():
            tmp[str(key)] = str(value)
        return str(tmp)

    def __getitem__(self, item):
        """
        Allows the class instance to be treated like a dict (dict[key]).
        Use Case:
        where category is a str...

        def func(category):
            return class_inst[category]
        :param item: str form of instance attribute names.
        """
        try:
            return self.__dict__[item]
        except KeyError as e:
            logging.error(self.__dict__)
            raise e

    def __setitem__(self, key, value):
        """
        Allows setting of values when using (class_inst[key] += 123)
        """

        if value < 0:
            logging.warning(f"Insufficient quantity in {self.__class__}. "
                            f"{value} in {key} is negative.")
            raise InsufficientQuantityError
        self.__dict__[key] = value
        return True

    def __setattr__(self, key, value):
        """
        Only checks for negative values, do the same as usual otherwise.
        """
        if value is int:
            if value < 0:
                logging.warning(f"Insufficient quantity in {self.__class__}. "
                                f"{value} in {key} is negative.")
                raise InsufficientQuantityError
        super().__setattr__(key, value)
        return

    def __add__(self, other):
        """
        Allows adding via + when the other is a pd.Series with the same
        index. It therefore saves on the trouble of having to add a for loop.
        """
        if isinstance(other, pd.Series):
            assert tuple(other.index) == tuple(self.pd_data.index)
            item = []
            for name, value in other.iteritems():
                item.append(self.__dict__[name] + value)
            item = pd.Series(item, other.index, name=other.name)
            return item
        else:
            raise NotImplementedError

    def __iadd__(self, other):
        """
        Similar to __add__, but inplace changes. Note that self[name] will work
        too if __getitem__ is defined, but I don't want to create the
        dependency.
        """
        if isinstance(other, pd.Series):
            assert tuple(other.index) == tuple(self.pd_data.index)
            for name, value in other.iteritems():
                self.__dict__[name] += value
            return self
        else:
            raise NotImplementedError

    def __sub__(self, other):
        """ Same as __add__ """
        if isinstance(other, pd.Series):
            assert tuple(other.index) == tuple(self.pd_data.index)
            item = []
            for name, value in other.iteritems():
                item.append(self.__dict__[name] - value)
            item = pd.Series(item, other.index, name=other.name)
            return item
        else:
            raise NotImplementedError

    def __isub__(self, other):
        """ Same as __iadd__ """
        if isinstance(other, pd.Series):
            assert tuple(other.index) == tuple(self.pd_data.index)
            for name, value in other.iteritems():
                self.__dict__[name] -= value
            return self
        else:
            raise NotImplementedError




class BaseMarket(ABC):
    def __init__(self, pd_data):
        self.pd_data = pd_data

    def __str__(self):
        return str(self.pd_data)

    def __getitem__(self, item):
        try:
            return self.pd_data[item]
        except KeyError as e:
            logging.error(self.price)
            raise e

    def __getattr__(self, item):
        return self.pd_data[item]

    def __add__(self, other):
        if isinstance(other, pd.Series):
            assert tuple(other.index) == tuple(self.pd_data.index)
            item = self.pd_data + other
            return item
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, pd.Series):
            assert tuple(other.index) == tuple(self.pd_data.index)
            item = self.pd_data - other
            return item
        else:
            raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, pd.Series):
            assert tuple(other.index) == tuple(self.pd_data.index)
            item = self.pd_data * other
            return item
        else:
            raise NotImplementedError

    def __eq__(self, other):
        if isinstance(other, pd.Series):
            return self.pd_data.equals(other)
        else:
            return self == other


    # def __eq__(self, other):
    #     return self.item == other

    # def dump(self, file_path="../save/", file_name=None):
    #     if not file_name:
    #         file_name = self.__class__.__name__ + "_save.pkl"
    #     if not file_name.endswith(".pkl"):
    #         file_name += ".pkl"
    #     if not os.path.isdir(file_path):
    #         os.makedirs(file_path)
    #     with open(file_path + file_name, "wb") as file:
    #         pickle.dump(self.item, file, -1)
    #     return True
    #
    # def load(self, file_path="../save/", file_name=None):
    #     if not file_name:
    #         file_name = self.__class__.__name__ + "_save.pkl"
    #     if not os.path.isdir(file_path):
    #         logging.error(f"File path {file_path} does not exist.")
    #         raise FileNotFoundError
    #     if not os.path.isfile(file_path + file_name):
    #         logging.error(f"File {file_name} does not exist in specified "
    #                       f"directory {file_path}.")
    #         raise FileNotFoundError
    #     with open(file_path + file_name, "rb") as file:
    #         self.item = pickle.load(file)
    #     return True

"""

    def check_if_sufficient(self, category, quantity):
        if self[category] >= quantity:
            return True
        else:
            return False


"""


# class BaseInt(ABC):
#     def __init__(self, item):
#         self.item = item
#     #
#     # def __str__(self):
#     #     return str(self)
#
#     def __add__(self, other):
#         item = self.item + other
#         return item
#
#     def __iadd__(self, other):
#         self.item += other
#         return self
#
#     def __sub__(self, other):
#         item = self.item - other
#         if item < 0:
#             logging.warning(f"Insufficient quantity in {self.__class__}. "
#                             f"Attempting to deduct {other} from {self.item}.")
#             raise InsufficientQuantityError
#         return item
#
#     def __isub__(self, other):
#         self.item -= other
#         return self
#
#     def __mul__(self, other):
#         item = self.item * other
#         return item
#
#     def __imul__(self, other):
#         self.item *= other
#         return self
#
#     def __rmul__(self, other):
#         item = self.__mul__(other)
#         return item