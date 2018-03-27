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



# Split between delayed and active func.
# Copy of Function signal values above.
# to_actual_delayed_i = ["buy_res", "sell_res", "buy_prod", "make_prod", "sell_prod",]
#
# to_actual_now_i = ["show_stats", "show_prices", "save", "load",
#                  "quit", "save_quit", "next_turn"]
#
# to_tmp_i = ["show_stats", ]

# func_to_actual_delayed = pd.Series(to_actual_delayed_i, to_actual_delayed_i, name="func_to_actual_delayed")
# func_to_actual_now = pd.Series(to_actual_now_i, to_actual_now_i, name="func_to_actual_now")
# func_to_tmp = pd.Series(to_tmp_i, to_tmp_i, name="func_to_tmp")


# def generic_str_fn(self):
#     print("String printed for ")
#     print(self.__class__)
#     string = f"Class: {self.__class__.__name__}\n"
#     for key, value in self.__dict__.items():
#         tmp = "\tAttr: " + key + "\n\t" + str(value).replace("\n", "\n\t") + "\n"
#         string += tmp
#     return string



# loaded_figures = [Res.cloth, Res.stuff, Res.accessory, Res.packaging,
# Prod.aisha, Prod.beta, Prod.chama, ResPrice.cloth, ResPrice.stuff,
# ResPrice.accessory, ResPrice.packaging, ProdPrice.aisha, ProdPrice.beta,
# ProdPrice.chama, Production.hours_needed, Production.cost_per_hour,
# Production.res_cost, "current_call", "time_steps"]
