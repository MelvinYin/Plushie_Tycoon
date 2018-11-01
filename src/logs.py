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

def log(msg, curframe):
    # sys.path doesn't work when using bokeh server
    filepath = curframe.f_code.co_filename
    funcname = curframe.f_code.co_name
    # Trim preceding directory
    filepath = filepath.split("/", maxsplit=5)[-1]
    logged_msg = "\n\nThis:: " + filepath + ": " + funcname + " <" + str(msg)\
                 + ">\n"

    with open(log_filename, 'a') as file:
        file.write(logged_msg)
