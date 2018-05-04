"""
In theory, buy/sell involves a difference in sign of quantity for now. But,
we're not combining them yet in case of future changes.

Action flow:
GE sees command, take the first one (buy), take the buy callback, and then
send it to another function, with that callback.

That function look at the second command (category), take the category,
attach it, and send it to another function

The final function merge the callback, and quantity, and check output. If
valid, then maybe raise a ActionCompleted back to GE. When GE sees that, GE
then calls figure_update, to update figures.

This means that Market classes need to obey a certain api (Market.price must
give price, for instance), and Inventory classes need to obey another
(add/subtract). Budget also need to obey a third api. This should be
documented, with a demo.

Commands to be concerned about:
1. Buy
2. Sell
3. Make

Other singular commands like next, save, load, should have a separate
execution thread.



"""