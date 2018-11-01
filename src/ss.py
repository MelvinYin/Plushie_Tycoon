from enum import Enum, auto

class test(Enum):
    one = auto()
    two = auto()

a = test.one

b = test.one
c = dict()
c[a] = 123
d = test.two
c[d] = 234

print(c[b])