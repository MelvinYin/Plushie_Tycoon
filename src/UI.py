from interpreters import interpret_action, interpret_plushie, interpret_resource, interpret_yes_no
from exceptions import InvalidInputException
import logging

def repeat_if_invalid_input(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                logging.debug("Performing " + func.__name__ + "\n")
                return func(*args, **kwargs)
            except InvalidInputException as e:
                if hasattr(e, "message"):
                    logging.warning(f"Invalid input. You have entered "
                                    f"{e.message}. Please try again.")
                else:
                    print(f"Invalid input. Please try again.")
                continue
    return wrapper

def ask_cat_quan():
    return input("How many of which?")

def ask_if_save():
    return input("Do you wish to save before quitting?")

def ask_action():
    return input("What would you like to do?")

@repeat_if_invalid_input
def buy_resource():
    user_input = ask_cat_quan()
    interpreted = interpret_resource(user_input)
    category, quantity = interpreted
    return ("buy_res", category, quantity)

@repeat_if_invalid_input
def sell_resource():
    user_input = ask_cat_quan()
    interpreted = interpret_resource(user_input)
    category, quantity = interpreted
    return ("sell_res", category, quantity)

@repeat_if_invalid_input
def buy_plushie():
    user_input = ask_cat_quan()
    interpreted = interpret_plushie(user_input)
    category, quantity = interpreted
    return ("buy_plush", category, quantity)

@repeat_if_invalid_input
def make_plushie():
    user_input = ask_cat_quan()
    interpreted = interpret_plushie(user_input)
    category, quantity = interpreted
    return ("make_plush", category, quantity)

@repeat_if_invalid_input
def sell_plushie():
    user_input = ask_cat_quan()
    interpreted = interpret_plushie(user_input)
    category, quantity = interpreted
    return ("sell_plush", category, quantity)

@repeat_if_invalid_input
def if_save():
    user_input = ask_if_save()
    to_save = interpret_yes_no(user_input)
    if to_save:
        return True
    return False

@repeat_if_invalid_input
def action():
    user_input = ask_action()
    desired_action = interpret_action(user_input)

    if desired_action == "buy_res":
        return buy_resource()
    if desired_action == "sell_res":
        return sell_resource()

    elif desired_action == "buy_plush":
        return buy_plushie()
    elif desired_action == "make_plush":
        return make_plushie()
    elif desired_action == "sell_plush":
        return sell_plushie()

    elif desired_action == "show_stats":
        return ("show_stats",)
    elif desired_action == "show prices":
        return ("show_prices",)

    elif desired_action == "save_game":
        return ("save_game",)
    elif desired_action == "load_game":
        logging.debug("Game Loaded.")
        return ("load_game",)
    elif desired_action == "next_turn":
        return ("next_turn",)
    elif desired_action == "quit_game":
        if if_save():
            return ("save_quit",)
        return ("quit_game",)
    else:
        raise InvalidInputException(user_input)

