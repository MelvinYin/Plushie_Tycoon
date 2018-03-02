import csv
import random
import numpy as np
import re
import copy
import itertools

# Global variable for directory, adjust as necessary
path = "C:/Users/Bai Lao Hu/Desktop/Plushie Tycoon/"

'''
Conventions:

'''


'''
def Create_List():      # Intending to add all necessary default lists here.
    plushie_file = open("{}Data/Plushie_Price.csv".format(path), "w")
    resource_file = open("{}Data/Plushie_Resource.csv".format(path), "w")
    plushie_file.close()
    resource_file.close()
    return
'''
def plushie_resource_list_create():
    """
    This create the text file with resource requirements for each plushie.
    :return: None, file created
    """
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



def Create_Character():
    """
    This create the specific game parameter file
    :return: None, file created
    """
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



def Plushie_Resource_List_Obtain():
    """
    This extract from the .txt plushie resource file the resource requirements in a list
    :return: A list of np.array of resource requirements of each plushie
    """
    file = open("{}Data/Plushie_Resource.csv".format(path), "r")
    resource_list = []
    for line in file:
        resource_string = line.split("\t")[1].split("\n")[0]
        resource_array_str = resource_string.split(", ")
        resource_array_int = np.array([i for i in resource_array_str], dtype = int)
        resource_list.append(resource_array_int)
    file.close()
    return resource_list    # [array([1, 1, 1, 1]), array([1, 1, 1, 1]), ...]

'''
def Plushie_Price(resource_price):
    """
    This extract the cost price of the plushies, by multiplying the current resource prices with the resource
    requirements of each plushie
    :param resource_price: a np.array of the current resource price
    :return: A np.array containing cost price of each plushie as an element
    """
    plushie_resource_list = Plushie_Resource_List_Obtain()
    price = np.array(resource_price * plushie_resource_list)
    return price

'''
def Extract_Values(csv_file, word):
    """
    A value-extracting function used on the style of lists created. Type in a word as a str, and the function will
    extract the corresponding values, and output it in a np.array of floats.
    :param csv_file: File to be extracted, fill in full path name
    :param word: Str from file to be extracted
    :return: np.array of floated values
    """
    try:
        line = [s[0] for s in csv_file if "{}".format(word) in s[0]][0].split("\t")[1]  # The multiple [0] is just to extract str from list
    except IndexError:
        print(list(s for s in csv_file))
        print([s[0] for s in csv_file if "{}".format(word) in s[0]])
        return
    value_str = line.split(", ")
    value_float = np.array([i for i in value_str], dtype=float)
    return value_float


def Gain_Per_Plushie_Current_Price(resource_diff, resource_price, plushie_price, plushie_resource_list):
    """
    This calculate the new resource diff to be used, for the current time step.
    Cost of each 100 plushie = resource price * plushie_resource_list, and summing the array (over the 4 resources)
    Divide by 100 to get per plushie, take the current plushie price and minus the cost, and we get the gain per plushie
    at current resource and plushie prices.
    :param resource_diff:
    :param resource_price: Current resource price, in np.array
    :param plushie_price: Current plushie price, in np.array
    :param plushie_resource_list: Resource requirements for each plushie, see Plushie_Resource_List_Obtain()
    :return: np.array of gain per plushie, to be saved in Save_1
    """
    gain_per_plushie = plushie_price - np.array([np.sum(x) for x in resource_price * plushie_resource_list]) / 100
    return gain_per_plushie


def Plushie_Diff_Calculator(plushie_price, plushie_diff, gain_per_plushie):
    """
    This calculate the new plushie diff. The gain per plushie at current prices is subtracted from plushie_diff,
    so that the new plushie prices will be lower if gain is made per plushie. 0.2 to provide some slowing down.
    Random function then add a fluctuating factor dependent on current plushie price, so higher price lead to higher
    fluctuations.

    Need to add a compensatory mechanism so that on average there is profit to be made, since need to offset worker cost,
    rent, and etc

    :param plushie_price: Current plushie price, in np.array
    :param plushie_diff: Current plushie diff, in np.array
    :param gain_per_plushie: profit per plushie based on current resourse and plushie price, see Gain_Per_Plushie_Current_Price
    :return: New plushie diff, to be fed to Save_1
    """
    new_diff = np.around((plushie_diff - 0.2 * gain_per_plushie) + (random.uniform(-0.1,0.1) * plushie_price), decimals = 2)
    return new_diff

def Resource_Diff_Calculator(resource_price, resource_diff, plushie_resource_list, gain_per_plushie):
    """
    Calculate the new resource_diff. The current gain per plushie is multiplied by the resource cost of each plushie.
    The array is then summed to give a parameter that indicate the cheapness of the resource. Justification is that if
    gain is high, then more people make that plushie in market, so more resources commensurate with the number of
    resources needed for that plushie is consumed. Therefore price of that resource should rise.
    The parameter is then multiplied by 0.02 (to be adjusted as needed) and added to resource diff. The current resource
    price is then multiplied with a random value to create fluctuations proportional to current resource price.
    :param resource_price: Current resource price
    :param resource_diff: Current resource diff
    :param plushie_resource_list: Resources per plushie
    :param gain_per_plushie: Profit per plushie, see Gain_Per_Plushie_Current_Price()
    :return: New resource diff, as np.array
    """
    diff_resource_plushie = [gain_per_plushie[i] * np.array(plushie_resource_list)[i] for i in range(len(gain_per_plushie))]    # [array([-19.2, -19.2, -19.2, -19.2]), ...]
    diff_resource_sum = np.array([sum(x) for x in zip(*diff_resource_plushie)])
    new_diff = np.around((resource_diff + 0.02 * diff_resource_sum) + (random.uniform(-0.1, 0.1) * resource_price), decimals = 2)
    return new_diff

def Replace_Line(data, trigger_array, replacement):   # Thought of using .replace, but decided to stick to something familiar. Learn?
    """
    Takes a list of the csv.reader object, see Open_Char_File(), and reproduce a copy, with altered values. Trigger is
    the string to be inserted, and it should match the words on the saved line to be replaced, while replacement will
    replace the values on the line.
    :param data: list(csv.reader()), list of Save_1 file, see Open_Char_File()
    :param trigger: A string array corresponding to the line(s) to be replaced
    :param replacement: Values to be replaced.
    :return: Altered data
    """
    for count, trigger in enumerate(trigger_array):
        new_data = []
        for line in data:
            if trigger in line[0]:
                new_data.append(["{} =\t{}".format(trigger, ", ".join(str(x) for x in replacement[count]))])
            else:
                new_data.append(line)
        data = copy.deepcopy(new_data)
    return


def Open_Char_File(num = 1):
    """
    This opens the Save_1 file and output the data as data, a list(csv.reader()) object
    :param num: Save file number, default is 1
    :return: list(csv.reader()) object of lines in file
    """
    file = open("{}Data/Save_{}.csv".format(path, num), "r")
    data = list(csv.reader(file, delimiter="\n"))  # list() converts csv.reader object to list, otherwise need to deal with reader pointer reset issue
    file.close()
    return data


def Update_Price():
    """
    Main update procedure for resource, plushie price and diff, to be called once per timestep. The Save_1 character
    file is first opened in data. Price, diff are taken from it. The plushie resource requirements are taken. The gain
    per plushie is then determined based on current resource and plushie price, and this is fed into the calculators for
    the diff. The new prices are then determined using the diff, and the price and diff values are written back into
    data. Finally the new data is written back to replace Save_1.

    There should be arguments to be inserted in the future. May return new_data in future so Open_Char_File() don't
    have to be run in the main function.

    :return: Prices updated in Save_1.
    """
    data = Open_Char_File()
    resource_diff = Extract_Values(data, "Resource Diff")
    resource_price = Extract_Values(data, "Resource Price")
    plushie_diff = Extract_Values(data, "Plushie Diff")
    plushie_price = Extract_Values(data, "Plushie Price")
    plushie_resource_list = Plushie_Resource_List_Obtain()
    gain_per_plushie = Gain_Per_Plushie_Current_Price(resource_diff, resource_price, plushie_price, plushie_resource_list)     # current selling price - cost price = gain
    new_plushie_diff = Plushie_Diff_Calculator(plushie_price, plushie_diff, gain_per_plushie)
    new_resource_diff = Resource_Diff_Calculator(resource_price, resource_diff, plushie_resource_list, gain_per_plushie)
    new_plushie_price = plushie_price + new_plushie_diff
    new_resource_price = resource_price + new_resource_diff
    trigger_array = ["Plushie Diff", "Resource Diff", "Resource Price", "Plushie Price"]
    replacement_array = [new_plushie_diff, new_resource_diff, new_resource_price, new_plushie_price]
    Replace_Line(data, trigger_array, replacement_array)
    Save_Data_Char_File(data)

def Save_Data_Char_File(data):
    """
    Flatten and save data file (from list(csv.reader())) to Save_1, by overwriting.
    :param data: Amended list(csv.reader()) object, will be flattened.
    :return: Save_1 rewritten
    """
    file = open("{}Data/Save_{}.csv".format(path, num), "w")
    data_flat = [x for x, in [y for y in data]]  # This flattens [["Resource Diff = ..."], ["..."], ...] into ["...", "..."]. It does not affect if it already is in that form, so it is safe. Use set() instead?
    for line in data_flat:
        file.write("{}\n".format(line))
    file.close()
    return

def Store_Selling_Percentage_Calculator(upgrade):
    """
    This determine the percentage of stock that is sold by the store per timestep.
    :param upgrade: Upgrade level of shop, get from Save_1
    :return: np.array of ten floats, each with percentage of stock sold per timestep
    """
    plushie_percent_raw = np.array(random.sample(range(0,20), 10), dtype = float)   # 10 is total number of plushie, 0-20% of order sold per time step
    plushie_percent_full = plushie_percent_raw + 5.0 * upgrade      # simple model for now
    return plushie_percent_full


def Minus_Inventory_Comparison(inventory, deduction):
    """
    This compare values between deduction and inventory. If theoretical deduction is more than inventory, it will
    be set as the inventory value, with the expectation that later new_inventory = inventory - deduction, so it reaches
    zero. This is not done here to retain the deduction values.

    Inventory returned for possible addition to this function

    :param inventory: Current inventory stock
    :param deduction: Theoretical deducted value
    :return: Same inventory, altered deduction values
    """
    for i in range(len(inventory)):
        if deduction[i] >= inventory[i]:
            deduction[i] = inventory[i]
    return


def Shop_Stock_Money_Update():
    """
    This update the money due to revenue from selling plushies. Upgrade level, inventory, current plushie price, and
    neopoints are first extracted. Percentage of plushie sold is determined, and technical number of plushie sold is
    counted. This is compared with current inventory stock to avoid hitting negative inventory, the neopoints earned
    is determined, and the new neopoint and new plushie inventory are rewritten. This will run per timestep, and it
    effectively converts plushie inventory to neopoints.
    :return: Save_1 updated.
    """
    data = Open_Char_File()
    upgrade = Extract_Values(data, "Store Upgrade")
    plushie_inventory = Extract_Values(data, "Shop Plushie Inventory")
    plushie_price = Extract_Values(data, "Plushie Price")
    neopoints = Extract_Values(data, "Neopoints")
    percentage = Store_Selling_Percentage_Calculator(upgrade)   # combine this to plushie sold?
    plushie_sold = np.around(percentage * plushie_inventory / 100) + 5 + 5 * upgrade
    Minus_Inventory_Comparison(plushie_inventory, plushie_sold)
    revenue = np.sum(plushie_sold * plushie_price)
    new_plushie_inventory = plushie_inventory - plushie_sold
    new_neopoints = neopoints + revenue
    data = Replace_Line(data, "Shop Plushie Inventory", new_plushie_inventory)
    new_data = Replace_Line(data, "Neopoints", new_neopoints)
    Save_Data_Char_File(new_data)

def Worker_Produced(workers, needed):
    """
    This determine the amount that the factory produce, per timestep. Needed is a list containing the orders, while
    workers is taken from Save_1, based on the number hired. Absolute production is 5 times that of workers, it is the
    absolute part of produced. If this amount is higher than or equal to that needed, then all the needed are produced.
    If this is not, then there is an additional relative component, of 2% by each worker, for the remaining amount.

    :param workers: Number of workers hired, Save_1
    :param needed: Total ordered
    :return: list of amount produced, and list of adjusted order.
    """
    absolute_production = workers * 5
    produced = np.array([], dtype = int)
    new_needed = copy.deepcopy(needed)
    for index, item in enumerate(needed):
        if item == 0:
            produced = np.append(produced, 0)
        elif item > 0 and item <= absolute_production:
            produced = np.append(produced, item)
            new_needed[index] = 0
        elif item > absolute_production:
            produced_value = round((item - absolute_production) * 0.02 * workers) + absolute_production
            produced = np.append(produced, produced_value)
            new_needed[index] = item - produced_value
        else:
            print("error")
            return
    return produced, new_needed

def Addition_Inventory_Check(produced_log, plushie_inventory, order_log):
    """

    :param produced_log:
    :param plushie_inventory:
    :param order_log:
    :return:
    """
    for index, item in enumerate(produced_log):
        if item >= 100:
            quotient = item // 100
            deduction = quotient * 100
            plushie_inventory[index] -= deduction
            produced_log[index] -= deduction        # Are you sure it's minus and not plus?
            order_log[index] -= deduction
    return produced_log # if there's no need to return produced_log then so be it


def Factory_Stock_Update():
    """

    :return:
    """
    data = Open_Char_File()
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
4. Write tests?

Remove the zip? can just multiply np array together.
'''