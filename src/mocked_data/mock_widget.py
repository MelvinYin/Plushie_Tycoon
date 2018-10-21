from config.global_config import Func, Res, Prod
import random
random.seed(1)
# from mocked import mock_init, mock_update1, mock_update2, mock_update3

def mocked_transaction_callbacks():
    callbacks = []
    for func in (Func.buy, Func.sell):
        for res in Res:
            callback = dict(command=func, category=res,
                            quantity=random.randint(0, 10))
            callbacks.append(callback)
        for prod in Prod:
            callback = dict(command=func, category=prod,
                            quantity=random.randint(0, 10))
            callbacks.append(callback)
    for prod in Prod:
        callback = dict(command=Func.make, category=prod,
                        quantity=random.randint(0, 10))
        callbacks.append(callback)
    return callbacks

def mocked_button_callbacks():
    funcs = (Func.save, Func.load, Func.back, Func.next, Func.quit)
    callbacks = list([dict(command=func) for func in funcs])
    return callbacks


mock_callbacks = mocked_transaction_callbacks() + mocked_button_callbacks()