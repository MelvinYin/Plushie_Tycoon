from enum import Enum, auto, unique

###############################################################################

# Resource signal values for internal use
@unique
class Res(Enum):
    tag = hash("Res")
    cloth = 1
    stuff = 2
    accessory = 3
    packaging = 4

# Plushie signal values for internal use
@unique
class Prod(Enum):
    tag = hash("Prod")
    aisha = 1
    beta = 2
    chama = 3

# Resource price signal values for internal use
@unique
class ResPrice(Enum):
    tag = hash("ResPrice")
    cloth = 1
    stuff = 2
    accessory = 3
    packaging = 4

# Plushie price signal values for internal use
@unique
class ProdPrice(Enum):
    tag = hash("ProdPrice")
    aisha = 1
    beta = 2
    chama = 3

@unique
class Others(Enum):
    tag = hash("Others")
    next_turn = 1
    quit = 3

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

###############################################################################