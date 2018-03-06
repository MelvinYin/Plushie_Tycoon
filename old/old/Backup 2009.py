import csv
import random
import numpy as np
import re
import copy
import itertools

path = "C:/Users/Bai Lao Hu/Desktop/Plushie Tycoon/"


def Create_List():      # Intending to add all necessary default lists here.
    plushie_file = open("{}Data/Plushie_Price.csv".format(path), "w")
    resource_file = open("{}Data/Plushie_Resource.csv".format(path), "w")
    plushie_file.close()
    resource_file.close()
    return

def Plushie_Resource_List_Create():     # This create the text file with resource requirements for each plushie.
    file = open("{}Data/Plushie_Resource.csv".format(path), "w")
    file.write("Aisha =\t{}\n".format("1, 1, 1, 1"))
    file.write("Beta =\t{}\n".format("1, 1, 1, 1"))
    file.write("Chama =\t{}\n".format("2, 1, 1, 1"))
    file.write("Drogo =\t{}\n".format("2, 1, 1, 1"))
    file.write("Emma =\t{}\n".format("3, 1, 1, 1"))
    file.write("Frodo =\t{}\n".format("3, 1, 1, 1"))
    file.write("Gange =\t{}\n".format("4, 1, 1, 1"))
    file.write("Hippo =\t{}\n".format("4, 1, 1, 1"))
    file.write("Illia =\t{}\n".format("5, 1, 1, 1"))
    file.write("Lamma =\t{}\n".format("5, 1, 1, 1"))
    file.close()



def Create_Character():     # This create the specific game parameter file
    Num = 1
    Name = "Kanade"
    file = open("{}Data/Save_{}.csv".format(path,Num), "w")
    file.write("Character ID =\t{}\n".format(Num))
    file.write("Character Name =\t{}\n".format(Name))
    file.write("System Time =\t{}\n".format(0))
    file.write("Shipping Time =\t{}\n".format(5))
    file.write("Store Upgrade =\t{}\n".format("0"))
    file.write("Workers =\t{}\n".format("0"))
    file.write("Neopoints =\t{}\n".format(50000))
    file.write("Resources =\t{}\n".format("0, 0, 0, 0"))
    file.write("Shop Plushie Inventory =\t{}\n".format("0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"))
    file.write("Plushie Shipping =\t{}\n".format("0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"))
    file.write("Factory Order Log =\t{}\n".format("0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"))
    file.write("Factory Produced Log =\t{}\n".format("0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"))
    file.write("")
    file.write("Resource Price =\t{}\n".format("20, 20, 20, 20"))
    file.write("Resource Diff =\t{}\n".format("0, 0, 0, 0"))
    file.write("Plushie Price =\t{}\n".format("20, 20, 20, 20, 20, 20, 20, 20, 20, 20"))
    file.write("Plushie Diff =\t{}\n".format("0, 0, 0, 0, 0, 0, 0, 0, 0, 0"))
    file.close()
    print("Character {} ({}) created".format(Name, Num))
    return



def Plushie_Resource_List_Obtain():     # This extract from the .txt plushie resource file the resource requirements in a list
    file = open("{}Data/Plushie_Resource.csv".format(path), "r")
    resource_list = []
    for line in file:
        resource_string = line.split("\t")[1].split("\n")[0]
        resource_array_str = resource_string.split(", ")
        resource_array_int = np.array([i for i in resource_array_str], dtype = int)
        resource_list.append(resource_array_int)
    file.close()
    return resource_list    # [array([1, 1, 1, 1]), array([1, 1, 1, 1]), ...]


def Plushie_Price(resource_price):      # resource_price should be np.array
    plushie_resource_list = Plushie_Resource_List_Obtain()
    price = np.array(resource_price * plushie_resource_list)
    return price


def Extract_Values(csv_file, word):
    try:
        line = [s[0] for s in csv_file if "{}".format(word) in s[0]][0].split("\t")[1]  # The multiple [0] is just to extract str from list
    except IndexError:
        print(list(s for s in csv_file))
        print([s[0] for s in csv_file if "{}".format(word) in s[0]])
        return
    value_str = line.split(", ")
    value_float = np.array([i for i in value_str], dtype=float)
    return value_float


def New_Resource_Diff(resource_diff, resource_price, plushie_price, plushie_resource_list):
    difference = np.array([np.sum(x) for x in resource_price * plushie_resource_list]) / 100 - plushie_price
    return difference


def plushie_diff_calculator(plushie_price, plushie_diff, difference):
    new_diff = np.around((plushie_diff - 0.2 * difference) * (random.uniform(0.9,1.1) * plushie_price), decimals = 2)
    return new_diff

def resource_diff_calculator(resource_price, resource_diff, plushie_resource_list, difference):
    diff_resource_plushie = [difference[i] * np.array(plushie_resource_list)[i] for i in range(len(difference))]    # [array([-19.2, -19.2, -19.2, -19.2]), ...]
    diff_resource_sum = np.array([sum(x) for x in zip(*diff_resource_plushie)])
    new_diff = np.around((resource_diff - 0.02 * diff_resource_sum) * (random.uniform(0.9, 1.1) * resource_price), decimals = 2)
    return new_diff

def replace_line(data, trigger, replacement):   # Thought of using .replace, but decided to stick to something familiar
    new_data = []
    for line in data:
        if trigger in line[0]:
            new_data.append(["{} =\t{}".format(trigger, ", ".join(str(x) for x in replacement))])
        else:
            new_data.append(line)
    return new_data

def Open_Char_File(num):
    file = open("{}Data/Save_{}.csv".format(path, num), "r")
    data = list(csv.reader(file, delimiter="\n"))  # list() converts csv.reader object to list, otherwise need to deal with reader pointer reset issue
    file.close()
    return data


def Update_Price():
    Num = 1
    data = Open_Char_File(Num)
    resource_diff = Extract_Values(data, "Resource Diff")
    resource_price = Extract_Values(data, "Resource Price")
    plushie_diff = Extract_Values(data, "Plushie Diff")
    plushie_price = Extract_Values(data, "Plushie Price")
    plushie_resource_list = Plushie_Resource_List_Obtain()
    difference = New_Resource_Diff(resource_diff, resource_price, plushie_price, plushie_resource_list)     # cost price - current selling price = loss
    new_plushie_diff = plushie_diff_calculator(plushie_price, plushie_diff, difference)
    new_resource_diff = resource_diff_calculator(resource_price, resource_diff, plushie_resource_list, difference)
    new_plushie_price = plushie_price + new_plushie_diff
    new_resource_price = resource_price + new_resource_diff
    data = replace_line(data, "Plushie Diff", new_plushie_diff)
    data = replace_line(data, "Resource Diff", new_resource_diff)
    data = replace_line(data, "Resource Price", new_resource_price)
    new_data = replace_line(data, "Plushie Price", new_plushie_price)   # give replace_line ability to accept and make multiple changes together? Complicate code though
    save_data_char_file(new_data)

def save_data_char_file(data):
    file = open("{}Data/Save_{}.csv".format(path, num), "w")
    data_flat = [x for x, in [y for y in data]]  # This flattens [["Resource Diff = ..."], ["..."], ...] into ["...", "..."]. It does not affect if it already is in that form, so it is safe.
    for line in data_flat:
        file.write("{}\n".format(line))
    file.close()

def Store_Selling_Percentage_Calculator(upgrade):
    plushie_percent_raw = np.array(random.sample(range(0,20), 10), dtype = float)   # 10 is total number of plushie, 0-20% of order sold per time step
    plushie_percent_full = plushie_percent_raw + 5.0 * upgrade      # simple model for now
    return plushie_percent_full


def Minus_Inventory_Comparison(inventory, deduction):   # Can use np.less_equal, but it's too tedious
    for i in range(len(inventory)):
        if deduction[i] >= inventory[i]:
            deduction[i] = inventory[i]
    return inventory, deduction


def Shop_Stock_Money_Update():
    Num = 1
    data = Open_Char_File(Num)
    upgrade = Extract_Values(data, "Store Upgrade")
    plushie_inventory = Extract_Values(data, "Shop Plushie Inventory")
    plushie_price = Extract_Values(data, "Plushie Price")
    neopoints = Extract_Values(data, "Neopoints")
    percentage = Store_Selling_Percentage_Calculator(upgrade)
    plushie_sold = np.around(percentage * plushie_inventory / 100) + 5 + 5 * upgrade
    plushie_inventory, plushie_sold = Minus_Inventory_Comparison(plushie_inventory, plushie_sold)
    revenue = np.sum(plushie_sold * plushie_price)
    new_plushie_inventory = plushie_inventory - plushie_sold
    new_neopoints = neopoints + revenue
    data = replace_line(data, "Shop Plushie Inventory", new_plushie_inventory)
    new_data = replace_line(data, "Neopoints", new_neopoints)
    save_data_char_file(new_data)

def Worker_Produced(workers, needed):
    absolute_production = workers * 5   # we are going to do it explicitly, for speed and clarity, instead of enumerate
    index = 0
    produced = np.array([], dtype = int)
    new_needed = copy.deepcopy(needed)
    for item in needed:
        if item == 0:
            produced = np.append(produced, 0)
        elif item > 0 and item <= absolute production:
            produced = np.append(produced, item)
            new_needed[index] = 0
        elif item > absolute_production:
            produced_value = round((item - absolute_production) * 0.05 * workers)
            produced = np.append(produced, produced_value)
            new_needed[index] = item - produced_value
        else:
            print("error")
        index += 1
    return produced, new_needed

def Addition_Inventory_Check(produced_log, plushie_inventory, order_log):
    index = 0
    new_produced_log = copy.deepcopy(produced_log)
    for item in produced_log:
        if item >= 100:
            quotient = item // 100
            deduction = quotient * 100
            plushie_inventory[index] = plushie_inventory[index] - deduction
            new_produced_log[index] = item - deduction
            order_log[index] -= deduction
        index += 1
    return new_produced_log


def Factory_Stock_Update():
    Num = 1
    data = Open_Char_File(Num)
    workers = Extract_Values(data, "Workers")
    order_log = Extract_Values(data, "Factory Order Log")       # assume infinite factory size for now, same as shop. Note that later on do sum of factory
    produced_log = Extract_Values(data, "Factory Produced Log")     # assume immediate free shipping for now. 100 plushie per order.
    plushie_inventory = Extract_Values(data, "Shop Plushie Inventory")      # assume worker focus on the order closest to completion for now
    needed = order_log - produced_log
    produced, needed = Worker_Produced(workers, needed)
    new_produced_log = produced_log + produced
    final_produced_log = Addition_Inventory_Check(new_produced_log, plushie_inventory, order_log)









'''
Things to do:
1. Currently some of the resource and plushie values go to infinity with long timesteps. Need to determine some kind of
equilibrium natural value, and then create a gaussian perhaps tendency towards that value with variation. A weak scaling
effect will do.
2. Demand and supply affecting price and rate of selling of plushie, and of resources too? Or is that already taken
care of by plushie price dependence
3. Changes in plushie price as a result of shop selling.

Remove the zip? can just multiple np array together.
'''