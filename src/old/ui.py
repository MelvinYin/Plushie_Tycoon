from interpreters import interpret_action, interpret_prod, interpret_resource, interpret_yes_no
from exceptions import InvalidInputException
import logging
from defaults import Func

def user_input(prompt=None):
    string = input(prompt)
    return string

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
                    logging.warning(f"Invalid input. Please try again.")
                continue
    return wrapper

def ask_cat_quan():
    return user_input("How many of which?")

def ask_if_save():
    return user_input("Do you wish to save before quitting?")

def ask_action():
    return user_input("What would you like to do?")

@repeat_if_invalid_input
def buy_resource():
    user_input = ask_cat_quan()
    interpreted = interpret_resource(user_input)
    category, quantity = interpreted
    return (Func.buy_res, category, quantity)

@repeat_if_invalid_input
def sell_resource():
    user_input = ask_cat_quan()
    interpreted = interpret_resource(user_input)
    category, quantity = interpreted
    return (Func.sell_res, category, quantity)

@repeat_if_invalid_input
def buy_prod():
    user_input = ask_cat_quan()
    interpreted = interpret_prod(user_input)
    category, quantity = interpreted
    return (Func.buy_prod, category, quantity)

@repeat_if_invalid_input
def make_prod():
    user_input = ask_cat_quan()
    interpreted = interpret_prod(user_input)
    category, quantity = interpreted
    return (Func.make_prod, category, quantity)

@repeat_if_invalid_input
def sell_prod():
    user_input = ask_cat_quan()
    interpreted = interpret_prod(user_input)
    category, quantity = interpreted
    return (Func.sell_prod, category, quantity)

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

    if desired_action == Func.buy_res:
        return buy_resource()
    if desired_action == Func.sell_res:
        return sell_resource()

    elif desired_action == Func.buy_prod:
        return buy_prod()
    elif desired_action == Func.make_prod:
        return make_prod()
    elif desired_action == Func.sell_prod:
        return sell_prod()

    elif desired_action == Func.show_stats:
        return (Func.show_stats,)
    elif desired_action == Func.show_prices:
        return (Func.show_prices,)
    elif desired_action == Func.show_history:
        return (Func.show_history,)

    elif desired_action == Func.save:
        return (Func.save,)
    elif desired_action == Func.load:
        logging.debug("Game Loaded.")
        return (Func.load,)
    elif desired_action == Func.next_turn:
        return (Func.next_turn,)
    elif desired_action == Func.quit:
        if if_save():
            return (Func.save_quit,)
        return (Func.quit,)
    else:
        raise InvalidInputException(user_input)

