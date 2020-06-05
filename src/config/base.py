from enum import Enum, auto, unique
from collections import namedtuple
###############################################################################

# Resource signal values for internal use
@unique
class Res(Enum):
    __order__ = 'cloth stuffing accessory packaging'
    cloth = 1
    stuffing = 2
    accessory = 3
    packaging = 4

# Plushie signal values for internal use
@unique
class Prod(Enum):
    __order__ = 'aisha beta chama'
    aisha = 1
    beta = 2
    chama = 3

# Function signal values for internal use
@unique
class Func(Enum):
    tag = hash("Func")
    buy = 1
    sell = 2
    make = 3
    save = 4
    load = 5
    quit = 6
    next = 7
    back = 8
    start = 9

# Production signal values for internal use
@unique
class Production(Enum):
    tag = hash("Production")
    hours_needed = auto()
    cost_per_hour = auto()
    res_cost = auto()

# ProductionTuple = namedtuple('ProductionTuple',
#                              'hours_needed res_ratio cost_per_hour')
# BudgetTuple = namedtuple('BudgetTuple', 'budget')

###############################################################################