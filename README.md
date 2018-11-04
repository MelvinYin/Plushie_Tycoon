Don't bother trying to get load to work, in that running load will refresh the figures. For some reason I can't get it to work, even when complying with the examples as shown, see bokeh stocks. 

Overall flow is along the lines of:
1. When next_turn is called, all actions taken during that turn are re-evaluated?
Make sense, since we also need to take into account what others will do during that turn. 

This means:
1. Each subclass will have a our_inventory object, that only tracks local changes. These are created at every next_turn. At the next next_turn, the change will be reported, and this is then fed to an actual inventory_object, same with market and budget...? Budget can take into account global changes such as change in interest rate, etc too. 

note: This means budget can go into negative, but we'll deal with that later. 

What we need then are bare-boned local objects, that have add and sub and etc, to track no-local-negative. 

Maybe a local gs vs a global gs...? 
