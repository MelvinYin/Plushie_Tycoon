import sys
import os

from logs import log

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            log(f"{cls.__name__} should only be initialised once.", )
            raise Exception
        return cls._instances[cls]