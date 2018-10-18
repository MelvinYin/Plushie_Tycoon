from global_config import Func, Res, Prod
import random
random.seed(1)
# from mocked import mock_init, mock_update1, mock_update2, mock_update3

def mocked_transaction_callbacks():
    callbacks = []
    for func in (Func.buy, Func.sell):
        for res in Res:
            callbacks.append([func, res, random.randint(0, 10)])
        for prod in Prod:
            callbacks.append([func, prod, random.randint(0, 10)])
    for prod in Prod:
        callbacks.append([Func.make, prod, random.randint(0, 10)])
    return callbacks

def mocked_button_callbacks():
    funcs = (Func.save, Func.load, Func.back, Func.next, Func.quit)
    callbacks = list([[func] for func in funcs])
    return callbacks


mock_callbacks = [*mocked_transaction_callbacks(), *mocked_button_callbacks()]