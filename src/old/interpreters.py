import re
from exceptions import InvalidInputException
from defaults import Func, Prod, Res



# Functions
buy_res_p = re.compile("buy[ _]res(ource(s)?)?(\.)?", re.IGNORECASE)
sell_res_p = re.compile("sell[ _]res(ource(s)?)?(\.)?", re.IGNORECASE)

buy_prod_p = re.compile("buy[ _]((prod)|(plush))(ie(s)?)?(\.)?", re.IGNORECASE)
sell_prod_p = re.compile("sell[ _]((prod)|(plush))(ie(s)?)?(\.)?", re.IGNORECASE)
make_prod_p = re.compile("make[ _]((prod)|(plush))(ie(s)?)?(\.)?", re.IGNORECASE)

save_p = re.compile("save([ _]game)?(\.)?", re.IGNORECASE)
load_p = re.compile("load([ _]game)?(\.)?", re.IGNORECASE)
quit_p = re.compile("quit([ _]game)?(\.)?", re.IGNORECASE)

show_stats_p = re.compile("(show[ _])?stats(\.)?", re.IGNORECASE)
show_prices_p = re.compile("(show[ _])?price(s)?(\.)?", re.IGNORECASE)

next_turn_p = re.compile("((skip)|(next))([ _]turn)?(\.)?", re.IGNORECASE)

back_p = re.compile("((back)|(return))(\.)?", re.IGNORECASE)

show_history_p = re.compile("(show[ _])?((call(stack)?(s)?)|(history))(\.)?", re.IGNORECASE)

# Products
aisha_p = re.compile("aisha", re.IGNORECASE)
beta_p = re.compile("beta", re.IGNORECASE)
chama_p = re.compile("chama", re.IGNORECASE)

# Resources
cloth_p = re.compile("cloth(ing)?(s)?", re.IGNORECASE)
stuff_p = re.compile("stuff(ing)?(s)?", re.IGNORECASE)
accessory_p = re.compile("accessor(y|(ies))", re.IGNORECASE)
packaging_p = re.compile("packaging(s)?", re.IGNORECASE)

# Yes/No
yes_p = re.compile("y(es)?", re.IGNORECASE)
no_p = re.compile("n(o(pe)?)?", re.IGNORECASE)


def interpret_action(user_input):
    user_input = user_input.strip()
    if re.fullmatch(buy_res_p, user_input):
        return Func.buy_res
    elif re.fullmatch(sell_res_p, user_input):
        return Func.sell_res

    elif re.fullmatch(buy_prod_p, user_input):
        return Func.buy_prod
    elif re.fullmatch(make_prod_p, user_input):
        return Func.make_prod
    elif re.fullmatch(sell_prod_p, user_input):
        return Func.sell_prod

    elif re.fullmatch(show_stats_p, user_input):
        return Func.show_stats
    elif re.fullmatch(show_prices_p, user_input):
        return Func.show_prices
    elif re.fullmatch(show_history_p, user_input):
        return Func.show_history

    elif re.fullmatch(save_p, user_input):
        return Func.save
    elif re.fullmatch(load_p, user_input):
        return Func.load
    elif re.fullmatch(next_turn_p, user_input):
        return Func.next_turn
    elif re.fullmatch(quit_p, user_input):
        return Func.quit

    else:
        raise InvalidInputException(user_input)


def interpret_prod(user_input):
    """
    For now this can be replaced with a simple .lower(), more for in case of
    future changes.
    """
    user_input = user_input.strip()
    prod_name, quantity = re.split("[, ]+", user_input, maxsplit=2)
    if not re.fullmatch("[1-9][0-9]*", quantity):
        raise InvalidInputException(user_input)

    if re.fullmatch(aisha_p, prod_name):
        matched_name = Prod.aisha
    elif re.fullmatch(beta_p, prod_name):
        matched_name = Prod.beta
    elif re.fullmatch(chama_p, prod_name):
        matched_name = Prod.chama
    else:
        raise InvalidInputException(user_input)

    return (matched_name, int(quantity))


def interpret_resource(user_input):
    try:
        user_input = user_input.strip()
        field_a, field_b = re.split("[, ]+", user_input, maxsplit=2)
    except ValueError:
        raise InvalidInputException(user_input)

    if re.fullmatch("[1-9][0-9]*", field_a):
        quantity = field_a
        prod_name = field_b
    elif re.fullmatch("[1-9][0-9]*", field_b):
        prod_name = field_a
        quantity = field_b
    else:
        raise InvalidInputException(user_input)

    if re.fullmatch(cloth_p, prod_name):
        matched_name = Res.cloth
    elif re.fullmatch(stuff_p, prod_name):
        matched_name = Res.stuff
    elif re.fullmatch(accessory_p, prod_name):
        matched_name = Res.accessory
    elif re.fullmatch(packaging_p, prod_name):
        matched_name = Res.packaging
    else:
        raise InvalidInputException(user_input)

    return (matched_name, int(quantity))


def interpret_yes_no(user_input):
    user_input = user_input.strip()
    if re.fullmatch(yes_p, user_input):
        return True
    elif re.fullmatch(no_p, user_input):
        return False
    else:
        raise InvalidInputException(user_input)


