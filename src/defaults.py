import pandas as pd


# Resource signal values for internal use
res_index = ["cloth", "stuff", "accessory", "packaging"]
res = pd.Series(res_index, res_index, name="res")

# Plushie signal values for internal use
prod_index = ["aisha", "beta", "chama"]
prod = pd.Series(prod_index, prod_index, name="prod")

# Function signal values for internal use
func_index = ["buy_res", "sell_res", "buy_prod", "make_prod", "sell_prod",
              "show_stats", "show_prices", "save_game", "load_game",
              "quit_game", "save_quit", "next_turn", "show_history"]
func = pd.Series(func_index, func_index, name="func")

# Plushie Resource Cost
res_cost = dict(aisha=[3,6,2,1],
                beta=[1,4,1,2],
                chama=[2,5,1,4])
prod_res_cost = pd.DataFrame(res_cost, index=res_index)

# Plushie Production Hours
p_hours = [30, 24, 36]
prod_hours = pd.Series(p_hours, prod_index, name="prod_hours")

# Cost Per Production Hour
cost_per_hour = 3

# Starting Statistics
starting_budget = 10000000

s_res = [1000,1000,1000,1000]
starting_res = pd.Series(s_res, res_index, name="starting_res")

s_prod = [100,100,100]
starting_prod = pd.Series(s_prod, prod_index, name="starting_prod")

s_res_price = [10,20,18,12]
starting_res_price = pd.Series(s_res_price, res_index, name="starting_res_price")

s_prod_price = [80,76,52]
starting_prod_price = pd.Series(s_prod_price, prod_index, name="starting_prod_price")


# Split between delayed and active func.
# Copy of Function signal values above.
to_actual_delayed_i = ["buy_res", "sell_res", "buy_prod", "make_prod", "sell_prod",]

to_actual_now_i = ["show_stats", "show_prices", "save_game", "load_game",
                 "quit_game", "save_quit", "next_turn"]

to_tmp_i = ["show_stats", ]

func_to_actual_delayed = pd.Series(to_actual_delayed_i, to_actual_delayed_i, name="func_to_actual_delayed")
func_to_actual_now = pd.Series(to_actual_now_i, to_actual_now_i, name="func_to_actual_now")
func_to_tmp = pd.Series(to_tmp_i, to_tmp_i, name="func_to_tmp")

starting_time = 0

# TODO: some form of a signatures template for others to compare with,
# TODO: like using an isinstance