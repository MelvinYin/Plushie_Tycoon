from gs import GSM
from ge import GEM
import ui


gsm = GSM()

while True:
    callstack = [ui.action()]
    gem = GEM(gsm)
    gem(callstack)

callstack = [("show_stats",), ("buy_res","stuff", 20)]
gem = GEM(gsm)
gem(callstack)