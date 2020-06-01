from abc import ABC
import pandas as pd
from enum import Enum

class BaseInventory(ABC):
    def __init__(self, value):
        self.value = value

    def add(self, *args):
        add_error_msg = f"Invalid input argument form to " \
                        f"{self.__class__.__name__}.add. {args}"
        if len(args) == 1:
            val_add = args[0]
            assert isinstance(val_add, pd.Series), add_error_msg
            assert len(val_add) == len(self.value), add_error_msg
            pd.testing.assert_index_equal(val_add.index, self.value.index)
            self.value += val_add
        elif len(args) == 2:
            category, quantity = args
            assert isinstance(category, Enum), add_error_msg
            assert category in self.value.index, add_error_msg
            assert isinstance(quantity, int), add_error_msg
            self.value[category] += quantity
        else:
            raise AssertionError(add_error_msg)
        return True

    def sub(self, *args):
        sub_error_msg = f"Invalid input argument form to " \
                        f"{self.__class__.__name__}.sub. {args}"
        if len(args) == 1:
            val_sub = args[0]
            assert isinstance(val_sub, pd.Series), sub_error_msg
            assert len(val_sub) == len(self.value), sub_error_msg
            pd.testing.assert_index_equal(val_sub.index, self.value.index)
            self.value -= val_sub
        elif len(args) == 2:
            category, quantity = args
            assert isinstance(category, Enum), sub_error_msg
            assert category in self.value.index, sub_error_msg
            assert isinstance(quantity, int), sub_error_msg
            self.value[category] -= quantity
        else:
            raise AssertionError(sub_error_msg)
        return True

    def replace(self, *args):
        rep_error_msg = f"Invalid input argument form to " \
                        f"{self.__class__.__name__}.replace. {args}"
        if len(args) == 1:
            val_rep = args[0]
            assert isinstance(val_rep, pd.Series), rep_error_msg
            assert len(val_rep) == len(self.value), rep_error_msg
            pd.testing.assert_index_equal(val_rep.index, self.value.index)
            self.value = val_rep
        else:
            raise AssertionError(rep_error_msg)
        return True

class BaseMarket(ABC):
    def __init__(self, pd_data):
        self.pd_data = pd_data

    def value(self):
        return self.pd_data