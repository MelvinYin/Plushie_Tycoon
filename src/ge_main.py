from gs import GSMain, GSInstance
from ge import GEInstance
import ui
import sys

GSM = GSMain(new_game=True)

def quit_game():
    sys.exit()

def ge_per_call():

    GSI = GSInstance(GSM.__dict__)
    GEI = GEInstance(GSI.__dict__)
    GEI_commands = dict(buy_res = GEI.buy_res,
                        sell_res = GEI.sell_res,
                        buy_plush = GEI.buy_plushie,
                        make_plush = GEI.make_plushie,
                        sell_plush = GEI.sell_plushie,
                        show_stats = GEI.show_stats,
                        show_prices = GEI.show_prices)

    GSI_commands = dict(load_game = GSI.load_game)

    GSM_commands = dict(save_game = GSM.save_game)

    result = ui.action()

    func_in_str = result[0]

    if func_in_str in GEI_commands:
        func = GEI_commands[func_in_str]

    elif func_in_str in GSI_commands:
        func = GSI_commands[func_in_str]
    elif func_in_str in GSM_commands:
        if result[1:]:
            GSM_commands[func_in_str](*result[1:])
        else:
            GSM_commands[func_in_str](*result[1:])
        return

    elif func_in_str == "quit_game":
        sys.exit()
    elif func_in_str == "next_turn":
        return

    else:
        raise Exception

    if result[1:]:
        func(*result[1:])
    else:
        func()

    GSM.update(GSI)
    GSM.time_steps += 1

    return

while True:
    ge_per_call()





"""
    # these are GS commands
    elif func_in_str == "save_game":
        func = GEI.save_game
    elif func_in_str == "load_game":
        func = GEI.load_game
    elif func_in_str == "next_turn":
        func = GEI.next_turn
    elif func_in_str == "save_quit":
        func = GEI.save_quit
    elif func_in_str == "quit_game":
        func = GEI.quit_game
"""
