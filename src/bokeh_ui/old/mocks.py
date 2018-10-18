def mocked_ind_widget(callback, specs):
    import random
    random.seed(1)

    RBG1_keys = list(specs.RBG1.labels.keys())
    RBG2_keys = list(specs.RBG2.labels.keys())
    RBG3_keys = list(specs.RBG3.labels.keys())

    for key1 in RBG1_keys:
        for key2 in RBG2_keys:
            for key3 in RBG3_keys:
                callback([key1, key2, key3, random.randint(0, 100)])


def mocked_but_widget(callback, specs):
    RBG_keys = list(specs.RBG1.labels.keys())

    for key in RBG_keys:
        callback([key])

def mocked_

