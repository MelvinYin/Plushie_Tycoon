from gs import GSM
from ge import GEM
import ui
import logs
import logging
import copy
from defaults import active_func, delayed_func


gsm = GSM()
actual_gem = GEM(gsm)
callstack = []
while True:
    gsm_tmp = copy.deepcopy(gsm)
    gem_tmp = GEM(gsm_tmp)
    action = ui.action()
    if action is ("next_step",):
        callstack.append(action)
        actual_gem(callstack)
        continue
    gem_tmp(action)
    if action in delayed_func:
        callstack.append(action)







callstack = [("show_stats",), ("buy_res","stuff", 20), ("sell_res","stuff", 20),
             ("buy_prod", "aisha", 10), ("make_prod", "beta", 5), ("sell_prod","chama", 7),
             ("save_game",), ("load_game",), ("show_stats",), ("quit_game",)]
