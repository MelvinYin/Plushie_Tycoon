# TODO: Build a back button


"""
Workflow of user:

They will key in several things to do for this turn.
Implicit checking to see if actions are valid.

Once fixed, they select next turn, and all actions are executed.

Then repeat.

Now they're two levels of nesting: GSM, GSI.

To merge the two with a history, of the dict of the GS. So, if need to roll back
by one, retrieve previous. If need to commit aka next turn, goto the last one
and refresh history. In case of exceptions, retrieve previous. If we wish
to look at the GS before the turn aka discard changes, goto the first history.

This can be implemented together with callstack? No need callstack anymore, it
will be saved as part of history in GE.


"""