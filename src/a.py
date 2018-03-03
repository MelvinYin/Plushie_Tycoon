

def decorate(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception:
                continue
    return wrapper


@decorate
def func2():
    y = input("blah")
    if y == "123":
        return
    else:
        print("wrong")
        raise Exception

func2()