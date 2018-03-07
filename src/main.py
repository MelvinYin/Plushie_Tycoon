from gs import GSM
from ge import GEM
import ui
import logs
import logging


gsm = GSM()

# while True:
#     callstack = [ui.action()]
#     gem = GEM(gsm)
#     gem(callstack)

callstack = [("show_stats",), ("buy_res","stuff", 20), ("sell_res","stuff", 20),
             ("buy_prod", "aisha", 10), ("make_prod", "beta", 5), ("sell_prod","chama", 7),
             ("load_game",), ("save_game",), ("quit_game",)]
gem = GEM(gsm)
gem(callstack)