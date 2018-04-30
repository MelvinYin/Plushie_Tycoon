
"""
Workflow

2. All plots in one plot figure, with a slider/widget below to turn on/off
certain plots, so cross-comparison can be made?

Implement 2 and 3 then. Then, figure out how to integrate into GS.

Plotting function using history.
Also, need history over turns too? For plotting.

Maybe. Maybe focus on the plotting first. Price model, probably later, make a
working prototype first.

Also, maybe add comments now? or nah?

Integrate bokeh into UI once buttons corresponding to each function work.

sub-class widget

# TODO: First, go back to gs and reformat it such that commit_history can
# TODO: be represented as a dict.
For now, do for long_term_storage first, but cannot. Erm.

Convert __str__ in bases to another print function, this is way too messy.
Maybe a formatting function.

The problem is that long_term_storage cannot be a different item from
value_history. Also, callstack need to be part of it.
What we can do, is for a pd.DataFrame of time_steps. index=time_step, call is
a part of value, as a pd.DataFrame. Input can be done on a adding-row basis, while
extraction can be done on a column-basis.

No, time_step should be a separate column. This allows getting a number of
calls called so far in index. Back will need to be changed accordingly.

Can use loc for efficient appending, and pop for efficient back.
https://stackoverflow.com/questions/41888080/python-efficient-way-to-add-rows-to-dataframe
http://pandas.pydata.org/pandas-docs/stable/indexing.html#setting-with-enlargement

When back is called, it is backed to the point where only one row remain.
When next is called, time_step is added by one.
there should therefore be a call associated with each and every commit, including
things like next_turn. First one will be start.

Also need a back function for bokeh plots.
# TODO: each figure need a separate dict column, instead of splitting it at
# TODO: the figureset level again.

# TODO: A GE dump line that can be called, to replace all plots using history

# TODO: Third, an interpretor between GS and figures(), need to exist, to break
# TODO: down the dict values into the individual figures, and send them to
# TODO: each, through the main input arg when constructing FigureSet.

# TODO: Fourth, a hashing map between what will be shown on the screen, vs
# TODO: what they actually mean (e.g. BR, SR, BP, MP, SP)

# TODO: Fifth, a link between the widget callback values and the appropriate
# TODO: commands to be sent to GE. A new UI perhaps then? Two different UIs, one
# TODO: console-based, and one through the bokeh. Do a factory method of that.

# TODO: figure need to update with new plots. Or change defaults for that.

# https://bokeh.pydata.org/en/latest/docs/gallery/bar_colormapped.html
prettyp is a temp solution. with plots, there won't be a need for the function
show_stats anymore.

# Changing of structure: Nested widget, with RBG_labels updated every time
preceding RBG is selected. So, buy => item category: Res => Res category:
cloth, then TI.

Also, change GE such that call first commits. Then, GE take first command
out (buy), and send it to buy(). Buy then take the next command out (Res), and
send it to either buy_res, or to a generic buy algorithm, with certain
values substituted (e.g. self.res_price, to identify which price would Res
correspond to.).

Therefore, a nested variable type? That say send to Res, and Res class in turn
has a price() and cost(), maybe, then it execute buy().

Structure of the code can be as such:

First, separate Inventory, Market (for prices) objects.

Then, each of them will have a generic callback function.

When GS creates them, it retrieves these callback functions. These functions
can be used to get information about prices, inventory levels, etc.

Now, GE will have product classes, such as Res and Prod.

When GE creates them, it will supply them with these callback functions, the
relevant ones for each.

Later on, when say buy_res called:
GE sees buy_res, call Res.buy(*args)

Res implement buy by using the callback functions supplied to do stuff, either
retrieve prices and update inventory.

So, GE only deal with these product objects. These are methods to implement
what the UI wants.

While GS will deal with things like commit, and with the "backend" functions,
such as Inventory updating itself and market modelling and etc.


"""