from singleton import Singleton

class Count(metaclass=Singleton):
    default_start = 0

    def __init__(self):
        self.count = default_start

    def __call__(self, *args, **kwargs):
        self.count += 1

    def reset(self):
        self.count = default_start
        