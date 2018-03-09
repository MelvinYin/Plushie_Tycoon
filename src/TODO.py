# TODO: Build a back button


"""
Workflow of user:

They will key in several things to do for this turn.
Implicit checking to see if actions are valid.

Once fixed, they select next turn, and all actions are executed.

Then repeat.

Implement enum

History function of each variable, for subsequent plotting (of say budget over
turns)
With corresponding record of callstacks, etc.
Save the whole dict essentially, but in variable as column order.

Information reading from GSM should be perfectly fine, but modifications should
be fed to the respective classes for them to implement separately, as this may
change their internal state

Bases need to add an abstract method add, that all composed classes of GSM
should have.


"""