

import inspect


class Cla:
    def __init__(self):
        self.one = 1
        self.two = 2

    def func(self):
        self.__dict__ = dict(one=12,two=234,three=344)

    def other(self):
        lines = inspect.getsourcelines(self.__setattr__)
        print("".join(lines[0]))
        print(dir(self))
x = Cla()
x.func()
print(x.__dict__)
x.other()