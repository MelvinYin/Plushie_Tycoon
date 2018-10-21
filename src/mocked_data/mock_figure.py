from config.global_config import Res, Prod
import random
from collections import defaultdict
import copy
random.seed(1)

mocked_time = [2,2,3,4,5,6,6,7,8,8]

def mocked_init():
    mocked = defaultdict(dict)
    for res in Res:
        mocked[Res][res.name] = list(random.randint(0, 30) for __ in range(10))
        mocked[Res]['time'] = copy.deepcopy(mocked_time)
    for prod in Prod:
        mocked[Prod][prod.name] = list(random.randint(0, 30) for __ in range(10))
        mocked[Prod]['time'] = copy.deepcopy(mocked_time)
    return mocked

def mocked_update1():
    mocked = defaultdict(dict)
    for res in Res:
        mocked[Res][res.name] = [random.randint(0, 30)]
        mocked[Res]['time'] = copy.deepcopy([8])
    for prod in Prod:
        mocked[Prod][prod.name] = [random.randint(0, 30)]
        mocked[Prod]['time'] = [8]
    return mocked

def mocked_update2():
    mocked = defaultdict(dict)
    for res in Res:
        mocked[Res][res.name] = [random.randint(0, 30)]
        mocked[Res]['time'] = [9]
    for prod in Prod:
        mocked[Prod][prod.name] = [random.randint(0, 30)]
        mocked[Prod]['time'] = [9]
    return mocked

mock_init = mocked_init()
mock_update1 = mocked_update1()
mock_update2 = mocked_update2()
mock_update3 = mocked_update2()