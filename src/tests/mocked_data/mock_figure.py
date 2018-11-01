from global_config import Res, Prod, res_members, prod_members
import random
from collections import defaultdict
import copy
random.seed(1)

mocked_time = [2,2,3,4,5,6,6,7,8,8]

def mocked_init():
    mocked = defaultdict(dict)
    for res in res_members:
        mocked[Res][res] = list(random.randint(0, 30) for __ in range(10))
    for prod in prod_members:
        mocked[Prod][prod] = list(random.randint(0, 30) for __ in range(10))
    mocked['time'] = copy.deepcopy(mocked_time)
    mocked = dict(mocked)
    return mocked

def mocked_update1():
    mocked = defaultdict(dict)
    for res in res_members:
        mocked[Res][res.name] = [random.randint(0, 30)]
    for prod in prod_members:
        mocked[Prod][prod.name] = [random.randint(0, 30)]
    mocked['time'] = [8]
    mocked = dict(mocked)
    return mocked

def mocked_update2():
    mocked = defaultdict(dict)
    for res in res_members:
        mocked[Res][res.name] = [random.randint(0, 30)]
        mocked[Res]['time'] = [9]
    for prod in prod_members:
        mocked[Prod][prod.name] = [random.randint(0, 30)]
        mocked[Prod]['time'] = [9]
    mocked['time'] = [9]
    mocked = dict(mocked)
    return mocked

mock_init = mocked_init()
mock_update1 = mocked_update1()
mock_update2 = mocked_update2()
mock_update3 = mocked_update2()