import logging
import sys

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

low_pass_stream = sys.stdout
high_pass_stream = sys.stderr
log_lvl = logging.DEBUG  # "DEBUG" < "INFO" < "WARNING" < "ERROR" < "CRITICAL"
log_filter_lvl = logging.WARNING  # Min inclusive log level for which messages will be sent to stderr

def set_logging_level(low_pass_stream="stdout", high_pass_stream="stderr",
                      log_lvl="debug", log_filter_lvl="warning"):
    """
    Allow output from logs below a certain level to be sent to stdout, and the rest to stderr (default for logging).
    Changing stdout/stderr allows for sending to alternative StreamHandler.
    Adapted from SO.
    """

    stream_mapping = dict(stdout=sys.stdout, stderr=sys.stderr)
    log_lvl_mapping = dict(debug=logging.DEBUG, info=logging.INFO,
                           warning=logging.WARNING, error=logging.ERROR,
                           critical=logging.CRITICAL)
    try:
        low_pass_stream = stream_mapping[low_pass_stream]
        high_pass_stream = stream_mapping[high_pass_stream]
        log_lvl = log_lvl_mapping[log_lvl]
        log_filter_lvl = log_lvl_mapping[log_filter_lvl]
    except KeyError:
        logging.error(f"Invalid Input {low_pass_stream}, {high_pass_stream}, "
              f"{log_lvl}, {log_filter_lvl} for set_logging_level.")
        raise Exception

    class LessThanFilter(logging.Filter):
        def __init__(self, max_level):
            super(LessThanFilter).__init__()
            self.max_level = max_level

        def filter(self, record):
            # Log if severity level lower than set level (LOG_FILTER_LVL).
            return record.levelno < self.max_level

    handler_low = logging.StreamHandler(low_pass_stream)
    handler_low.addFilter(LessThanFilter(log_filter_lvl))  # Responsible for logs below LOG_FILTER_LVL
    handler_low.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

    handler_high = logging.StreamHandler(high_pass_stream)
    handler_high.setLevel(log_filter_lvl)  # Responsible for logs LOG_FILTER_LVL and above
    handler_high.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

    logger = logging.getLogger()  # Get the root logger
    logger.setLevel(log_lvl)  # Defaults to logging.WARNING
    logger.addHandler(handler_low)
    logger.addHandler(handler_high)
    return

set_logging_level()
