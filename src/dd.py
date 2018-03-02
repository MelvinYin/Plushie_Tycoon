class InsufficentQuantityError(Exception):
    pass

class Class:
    def __init__(self):
        self.one = 1
        self.two = 2

    def __repr__(self):
        return str(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.key = value
        if self.key < 0:
            raise InsufficentQuantityError
        return True

    def __getattr__(self, item):
        return self.item

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if self.__dict__[key] < 0:
            raise InsufficentQuantityError
        return
