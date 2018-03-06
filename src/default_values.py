import pandas as pd

starting_budget = 10000000

# Plushie Resource Cost
res_index = ["cloth", "stuff", "accessory", "packaging"]
aisha_res_cost = pd.Series([3,6,2,1], res_index, name="aisha")
beta_res_cost = pd.Series([1,4,1,2], res_index, name="beta")
chama_res_cost = pd.Series([2, 5, 1, 4], res_index, name="chama")

# Plushie Production Hours
aisha_prod_time = 30
beta_prod_time = 24
chama_prod_time = 36

# Cost Per Production Hour
cost_per_hour = 3

# Starting Statistics
starting_cloth = 1000
starting_stuff = 1000
starting_accessory = 1000
starting_packaging = 1000

starting_aisha = 100
starting_beta = 100
starting_chama = 100
