import os
import webbrowser
import bokeh.settings
# print(webbrowser._browsers)
# bokeh.settings.settings.browser(webbrowser._browsers['c:\\program files\\internet explorer\\iexplore.exe'][1])
# print(webbrowser._browsers['c:\\program files\\internet explorer\\iexplore.exe'][1])
# webbrowser.register('windows-default', None, webbrowser._browsers['c:\\program files\\internet explorer\\iexplore.exe'][1])


class Base(ABC):
    """ No longer used. """
    def __str__(self):
        tmp = dict()
        for key, value in self.__dict__.items():
            tmp[str(key)] = str(value)
        return str(tmp)

    def __getitem__(self, item):
        try:
            return self.__dict__[item]
        except KeyError as e:
            logging.error(self.__dict__)
            raise e

    def __setitem__(self, key, value):
        if value < 0:
            logging.warning(f"Insufficient quantity in {self.__class__}. "
                            f"{value} in {key} is negative.")
            raise InsufficientQuantityError
        self.__dict__[key] = value
        return True

    def __setattr__(self, key, value):
        if value is int:
            if value < 0:
                logging.warning(f"Insufficient quantity in {self.__class__}. "
                                f"{value} in {key} is negative.")
                raise InsufficientQuantityError
        super().__setattr__(key, value)
        return

