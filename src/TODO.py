
"""
Workflow

Move show_stats and etc to GS

Plotting function using history.
Also, need history over turns too? For plotting.

Callstack shown should be the values themselves as well, not the enum values.

Maybe. Maybe focus on the plotting first. Price model, probably later, make a
working prototype first.

It is plausible that during next_turn or save_game, the entire history will then
be placed inside long-term storage. Or, next turn will wipe current callstack
and current history, but place them inside a long-term storage, with the time
elapsed as a marker. A dict of list maybe.

Then, plot can be made to run on this data structure. Maybe.
"""