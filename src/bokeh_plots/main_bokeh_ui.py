from ui_interface import UIInterface
from ge import GEM
from defaults import Res, Prod, ResPrice, ProdPrice, Production, Func
from bokeh.plotting import curdoc, show
import defaults


# TODO: Don't bother too much with the UI for now, focus on the GE.

# TODO: Have perhaps an initial save file? that comes with default, and by
# TODO: default will be loaded. No, actually initial data has been coded into
# TODO: default.

# TODO: Try to decouple defaults from GEM. Perhaps feed in required defaults
# TODO: data at initialisation of GE. (but that still requires mapping of some
# TODO: sort?) If this can be done, then initial data can be fed in at
# TODO: initialisation. GE will then be completely generic, only defaults called
# TODO: will be at main, and possibly even UI_interface...?

# TODO: So only main deal with defaults, and main map between UI_interface
# TODO: and ge.

# TODO: make buy and sell generic in GE at least.

# TODO: Find some way to deal with temp_adapt_ge_to_ui in ui_interface.


def init_data():
    GSM_update = dict()
    GSM_update[Res.cloth] = list([defaults.starting_res[Res.cloth] for _ in range(3)])
    GSM_update[Res.stuff] = list([defaults.starting_res[Res.stuff] for _ in range(3)])
    GSM_update[Res.accessory] = list([defaults.starting_res[Res.accessory] for _ in range(3)])
    GSM_update[Res.packaging] = list([defaults.starting_res[Res.packaging] for _ in range(3)])

    GSM_update[Prod.aisha] = list([defaults.starting_prod[Prod.aisha] for _ in range(3)])
    GSM_update[Prod.beta] = list([defaults.starting_prod[Prod.beta] for _ in range(3)])
    GSM_update[Prod.chama] = list([defaults.starting_prod[Prod.chama] for _ in range(3)])

    GSM_update[ResPrice.cloth] = list([defaults.starting_res_price[Res.cloth] for _ in range(3)])
    GSM_update[ResPrice.stuff] = list([defaults.starting_res_price[Res.stuff] for _ in range(3)])
    GSM_update[ResPrice.accessory] = list([defaults.starting_res_price[Res.accessory] for _ in range(3)])
    GSM_update[ResPrice.packaging] = list([defaults.starting_res_price[Res.packaging] for _ in range(3)])

    GSM_update[ProdPrice.aisha] = list([defaults.starting_prod_price[Prod.aisha] for _ in range(3)])
    GSM_update[ProdPrice.beta] = list([defaults.starting_prod_price[Prod.beta] for _ in range(3)])
    GSM_update[ProdPrice.chama] = list([defaults.starting_prod_price[Prod.chama] for _ in range(3)])

    GSM_update["current_call"] = [0, 0, 0]
    GSM_update["time_steps"] = [0, 0, 1, 2]
    return GSM_update

GE = GEM()
ui = UIInterface(init_data(), GE.callback)
if __name__ == "__main__":
    ui.widget_callback((Func.buy_res, (Res.cloth, 10)))
    ui.widget_callback((Func.sell_res, (Res.accessory, 10)))

    ui.widget_callback((Func.buy_prod, (Prod.aisha, 10)))
    ui.widget_callback((Func.make_prod, (Prod.beta, 10)))
    ui.widget_callback((Func.sell_prod, (Prod.chama, 10)))

    ui.widget_callback((Func.next_turn,))
    show(ui.ui_layout)
else:
    curdoc().add_root(ui.ui_layout)