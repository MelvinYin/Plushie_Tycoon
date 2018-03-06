import re
from exceptions import InvalidInputException

# TODO: We don't really want to make that tolerant a ui at this point,
# TODO: intention is to wrap it up in a gui afterwards.


buy_res_p = re.compile("buy[ _]res(ource(s)?)?(\.)?", re.IGNORECASE)
sell_res_p = re.compile("sell[ _]res(ource(s)?)?(\.)?", re.IGNORECASE)

buy_plush_p = re.compile("buy[ _]plush(ie(s)?)?(\.)?", re.IGNORECASE)
sell_plush_p = re.compile("sell[ _]plush(ie(s)?)?(\.)?", re.IGNORECASE)
make_plush_p = re.compile("make[ _]plush(ie(s)?)?(\.)?", re.IGNORECASE)

save_game_p = re.compile("save([ _]game)?(\.)?", re.IGNORECASE)
load_game_p = re.compile("load([ _]game)?(\.)?", re.IGNORECASE)
quit_game_p = re.compile("quit([ _]game)?(\.)?", re.IGNORECASE)

show_stats_p = re.compile("(show[ _])?stats(\.)?", re.IGNORECASE)
show_prices_p = re.compile("(show[ _])?price(s)?(\.)?", re.IGNORECASE)

next_turn_p = re.compile("((skip)|(next))([ _]turn)?(\.)?", re.IGNORECASE)

back_p = re.compile("((back)|(return))(\.)?", re.IGNORECASE)

def interpret_action(user_input):
    user_input = user_input.strip()
    if re.fullmatch(buy_res_p, user_input):
        return "buy_res"
    elif re.fullmatch(sell_res_p, user_input):
        return "sell_res"

    elif re.fullmatch(buy_plush_p, user_input):
        return "buy_plush"
    elif re.fullmatch(make_plush_p, user_input):
        return "make_plush"
    elif re.fullmatch(sell_plush_p, user_input):
        return "sell_plush"

    elif re.fullmatch(show_stats_p, user_input):
        return "show_stats"
    elif re.fullmatch(show_prices_p, user_input):
        return "show_prices"

    elif re.fullmatch(save_game_p, user_input):
        return "save_game"
    elif re.fullmatch(load_game_p, user_input):
        return "load_game"
    elif re.fullmatch(next_turn_p, user_input):
        return "next_turn"
    elif re.fullmatch(quit_game_p, user_input):
        return "quit_game"

    else:
        raise InvalidInputException(user_input)

aisha_p = re.compile("aisha", re.IGNORECASE)
beta_p = re.compile("beta", re.IGNORECASE)
chama_p = re.compile("chama", re.IGNORECASE)

def interpret_plushie(user_input):
    """
    For now this can be replaced with a simple .lower(), more for in case of
    future changes.
    """

    user_input = user_input.strip()
    plushie_name, quantity = re.split("[, ]+", user_input, maxsplit=2)
    if not re.fullmatch("[1-9][0-9]*", quantity):
        raise InvalidInputException(user_input)

    if re.fullmatch(aisha_p, plushie_name):
        matched_name = "aisha"
    elif re.fullmatch(beta_p, plushie_name):
        matched_name = "beta"
    elif re.fullmatch(chama_p, plushie_name):
        matched_name = "chama"
    else:
        raise InvalidInputException(user_input)

    return (matched_name, int(quantity))


cloth_p = re.compile("cloth(ing)?(s)?", re.IGNORECASE)
stuff_p = re.compile("stuff(ing)?(s)?", re.IGNORECASE)
accessory_p = re.compile("accessor(y|(ies))", re.IGNORECASE)
packaging_p = re.compile("packaging(s)?", re.IGNORECASE)


def interpret_resource(user_input):

    try:
        user_input = user_input.strip()
        field_a, field_b = re.split("[, ]+", user_input, maxsplit=2)
    except ValueError:
        raise InvalidInputException(user_input)

    if re.fullmatch("[1-9][0-9]*", field_a):
        quantity = field_a
        plushie_name = field_b
    elif re.fullmatch("[1-9][0-9]*", field_b):
        plushie_name = field_a
        quantity = field_b
    else:
        raise InvalidInputException(user_input)

    if re.fullmatch(cloth_p, plushie_name):
        matched_name = "cloth"
    elif re.fullmatch(stuff_p, plushie_name):
        matched_name = "stuff"
    elif re.fullmatch(accessory_p, plushie_name):
        matched_name = "accessory"
    elif re.fullmatch(packaging_p, plushie_name):
        matched_name = "packaging"
    else:
        raise InvalidInputException(user_input)

    return (matched_name, int(quantity))

yes_p = re.compile("y(es)?", re.IGNORECASE)
no_p = re.compile("n(o(pe)?)?", re.IGNORECASE)

def interpret_yes_no(user_input):
    user_input = user_input.strip()
    if re.fullmatch(yes_p, user_input):
        return True
    elif re.fullmatch(no_p, user_input):
        return False
    else:
        raise InvalidInputException(user_input)


