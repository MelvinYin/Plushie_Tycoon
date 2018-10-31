import sys
import os

"""
Internal Logging Reference:
DEBUG: Debug messages, not shown to end user, for development purposes.
Example: "Calling function {function_name} with input {input}."
Continue?: Yes

INFO:       Standard output for users.
Example:    User selects show_statistics, standard output to console.
Continue?:  Yes

WARNING:    Potential error relating to input parameters. Also for tolerated 
            invalid user input values.
Example:    "Supplied directory does not have a save folder. Creating one."
            "Invalid input quantity value {value}. Please try again."
Continue?:  Yes, may require a repeat of input.

ERROR:      Error relating to invalid user input parameters that are not 
            tolerated, or invalid dev input parameters. Also for tolerated 
            breaking of architecture.
Example:    "Invalid logging level input values."
Continue?:  No

CRITICAL:   Definite breaking of code architecture. Should only be encountered
            during refactoring of code. Unexpected exceptions get sent to here.
            Do not commit to main. 
Example:    "Class/Type {class/type} does not have __add__ attribute."
Continue?:  No

"""
log_filename = "/home/melvin/Desktop/pipeline2/Prod-Disp/src/log.txt"

def log(sys_path, msg):
    # Doesn't work when using bokeh server

    # sys_path = sys_path[0]
    # nestled_layer = 0
    # while sys_path.rsplit("/", maxsplit=1)[-1] != 'src':
    #     sys_path = sys_path.rsplit("/", maxsplit=1)[0]
    #     nestled_layer += 1
    nestled_layer = 0
    with open(log_filename, 'a') as file:
        for __ in range(nestled_layer):
            file.write("    ")
        file.write("<{}>\n".format(msg))
