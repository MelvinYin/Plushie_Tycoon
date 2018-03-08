"""
1. Splitting up the command section, and the execution

Description:
    Essentially to have a list of commands in a stack, that can be decoupled
    from the execution. Allows for delayed execution, and easy implementation of a
    "back" functionality perhaps. This also allows further decoupling between the
    UI and game engine. This also allows for one to break up the whole command
    sequence, so GE can independently make changes to game state, without having to
    do it sequentially...? ish.

    For this to occur, a more fixed architecture is probably needed, since there
    is a need to predict what's going to happen next, in terms of feedback
    responses to the user.

    How to build: We wish to first de-couple GE and GS, so that we can port as many
    errors that will be flagged by GE outside of GE (insufficient quantity, etc).
    A temp GS will be created at the start of every command stack, and test
    operations will be executed on that, to be able to identify any errors that
    will be flagged on the main GS.

    A GE instance is required, that takes in as input a command stack, and a GS,
    and output either the final GS, or any errors flagged in between.

Action flow:
    At start of each turn, a GS instance is obtained from the current GS. As
    commands flow in, the GS_i will be updated accordingly. This will allow
    flagging of any potential errors. At end of each turn, GS_main will then
    be replaced with GS_i. Nah, just do a variable update.

    pickle dump after every turn then? OK!. for now.

    So, we'll need a GS, that at every turn load, and end of every turn dump.

    QUESTION: where do you want the instance of GSMain to live? Currently will
    live in GE.


Inflation over time.

Current p_model has excessive counter-vailing force against price changes?

Replace singleton with borg design pattern, which will resolve the subclassing
metaclass thing, maybe.

First build a pricing model that relates demand to supply.
"""

# todo: ADD dict for function call from ge, otherwise need to change too
# TODO: many places at once