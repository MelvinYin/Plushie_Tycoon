from enum import Enum, auto, unique
from collections import namedtuple
###############################################################################

# Resource signal values for internal use
@unique
class Res(Enum):
    cloth = 1
    stuff = 2
    accessory = 3
    packaging = 4

# Plushie signal values for internal use
@unique
class Prod(Enum):
    # tag = hash("Prod")
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

res_members = [Res.cloth, Res.stuff, Res.accessory, Res.packaging]
prod_members = [Prod.aisha, Prod.beta, Prod.chama]

ProductionTuple = namedtuple('ProductionTuple',
                             'hours_needed res_ratio cost_per_hour')
# BudgetTuple = namedtuple('BudgetTuple', 'budget')

###############################################################################