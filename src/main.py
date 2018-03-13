from exceptions import RepeatUIAction
from ge import GEM
import ui
import defaults
import logs
import logging
import copy

def main_func():
    GE = GEM()
    while True:
        action = ui.action()
        try:
            GE(action)
        except RepeatUIAction:
            pass
        continue


# callstack = [("show_stats",), ("buy_res","stuff", 20), ("sell_res","stuff", 20),
#              ("buy_prod", "aisha", 10), ("make_prod", "beta", 5), ("sell_prod","chama", 7),
#              ("save_game",), ("load_game",), ("show_stats",), ("quit_game",)]
main_func()