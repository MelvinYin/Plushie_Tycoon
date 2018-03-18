import scipy.special
import numpy as np
import matplotlib.pyplot as plt
import math
from actor_base import ActorBase

class BaselineSup(ActorBase):
    def __init__(self):
        super().__init__()
        self.plateau_p_lvl = 5
        self.plateau_q_lvl = 56
        self.halfway_p = self.plateau_p_lvl / 2.
        self.halfway_q = self.plateau_q_lvl / 2.

    def __call__(self, p):
        """ Every time when called, t should increase by 1. """
        p_gap = self.base_p_ref - p
        if p_gap > 0:
            if abs(p_gap) >= 13:
                q = self.plateau_q_lvl
            else:
                factor = self.calc_factor(p_gap, self.halfway_p)
                q = self.halfway_q * factor
            return q

        else:
            if abs(p_gap) >= 13:
                q = self.plateau_q_lvl
            else:
                factor = self.calc_factor(p_gap, self.halfway_p)
                q = self.halfway_q * factor
            return q

    @staticmethod
    def calc_factor(p_gap, halfway_p):
        """
        We are aiming for something that has a sigmoid shape, with a matching
        value and first derivative to the two limits (0 and 2*halfway_p), and
        a matching value and opposite first derivative at the merge point
        (halfway_p).

        The formula as posed has value=0, first_deriv=0 at both limits, and
        a constant 2nd_deriv, which flips at the halfway point (2/(p**2)), with
        a matching 1st deriv at merge point of (2/p). It is thus sufficient for
        our purposes.

        Other preferences include a zero second deriv at both limits. However,
        ease of maintenance, extension through addition of factors to change
        gradient and curvature, and performance take precedence.

        Other formulas to consider are mainly the smoothstep function, or a
        sigmoid function.
        """
        if p_gap < halfway_p:
            return (2 - (2 - (p_gap / halfway_p)) ** 2)
        else:
            return (((p_gap) / halfway_p) ** 2)

class Producer(ActorBase):  # consider comsumer/producer base class
    def __init__(self):
        self.prev_q = 0
        self.grad_factor = 0.2

    def __call__(self, p):
        """ Should this not be a 2nd-order effect, so it changes grad
        additively, rather than a 1st-order for the current implementation?

        Consider switching to a more complicated algo eventually, perhaps
        something like a 1/T influence of past prices on current estimates.
        Or, in the far future, incorporate some speculative trading strategies.
        """
        addition = self.grad_factor * (p - self.base_p_ref)
        self.prev_q += addition
        return self.prev_q

class SpeculativeSell(ActorBase):
    # need to tie it in somehow with both d and s
    # include sub-actors in the future, like HFT, etc, each with their own
    # capacity, price-demand profile, time lag, perhaps.

    def __init__(self):
        self.capacity = 100 # in dollar, to rise over time
        self.lin_grad = 0.5
    def __call__(self, p):
        """ Semi-immediate linear response for now. Cannot be delta-fn because
        of potential instability and oscillation.
        """
        p_gap = p - self.base_p_ref
        if p_gap <= 0:
            return 0

        quantity_to_sell = p_gap * self.lin_grad
        if quantity_to_sell < self.capacity:
            self.capacity -= quantity_to_sell
            return quantity_to_sell
        else:
            self.capacity = 0
            return self.capacity