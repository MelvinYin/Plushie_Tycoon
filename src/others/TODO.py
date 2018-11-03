
"""
Workflow

sub-class widget

Can use loc for efficient appending, and pop for efficient back.
https://stackoverflow.com/questions/41888080/python-efficient-way-to-add-rows-to-dataframe
http://pandas.pydata.org/pandas-docs/stable/indexing.html#setting-with-enlargement

When back is called, it is backed to the point where only one row remain.
When next is called, time_step is added by one.
there should therefore be a call associated with each and every commit, including
things like next_turn. First one will be start.

Also need a back function for bokeh plots.

# TODO: A GE dump line that can be called, to replace all plots using history

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


# TODO: Task 1: merge Res, Prod, Res Price, Prod Price
# TODO: Task 2: create a widget button that alternate between displaying
# TODO: each Res, prod, etc, with a display_all.