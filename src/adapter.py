from exceptions import InsufficentQuantityError
import UI as ui
from game_engine import GameEngine as GE

# TODO: check what exception is raised when negative quantity.


GE = GE()
def to_do(instruction="action", GE=GE):
    if instruction == "action":
        result = ui.action()
    else:
        raise Exception

    func_in_str = result[0]

    if func_in_str == "buy_res":
        func = GE.buy_res
    elif func_in_str == "sell_res":
        func = GE.sell_res

    elif func_in_str == "buy_plush":
        func = GE.buy_plushie
    elif func_in_str == "make_plush":
        func = GE.make_plushie
    elif func_in_str == "sell_plush":
        func = GE.sell_plushie

    elif func_in_str == "show_stats":
        func = GE.show_stats
    elif func_in_str == "show_prices":
        func = GE.show_prices

    elif func_in_str == "save_game":
        func = GE.save_game
    elif func_in_str == "load_game":
        func = GE.load_game
    elif func_in_str == "next_turn":
        func = GE.next_turn
    elif func_in_str == "save_quit":
        func = GE.save_quit
    elif func_in_str == "quit_game":
        func = GE.quit_game

    else:
        raise Exception

    try:
        if result[1:]:
            return_value = func(*result[1:])
        else:
            return_value = func()
    except InsufficentQuantityError:
        print("Insufficient Quantity")
        return

    return return_value

for _ in range(20):
    to_do()