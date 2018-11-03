import scipy.special
import numpy as np
import matplotlib.pyplot as plt
import math
from actor_base import ActorBase

"""
Need another actor to deal with spikes and dips, and also a randomized actor. 

"""


class BaselineD(ActorBase):
    def __init__(self):
        super().__init__()
        self.plateau_p_lvl = 5
        self.plateau_q_lvl = 56
        self.halfway_p = self.plateau_p_lvl / 2.
        self.halfway_q = self.plateau_q_lvl / 2.

    def __call__(self, p):
        """ Every time when called, t should increase by 1. """
        p_gap = p - self.base_p_ref
        q = math.copysign(self.calc_q(abs(p_gap)), p_gap)
        return q

    def calc_q(self, abs_p_gap):
        if abs_p_gap > self.plateau_p_lvl:
            q = self.plateau_q_lvl
        else:
            factor = self.calc_factor(abs_p_gap)
            q = self.halfway_q * factor
        return q

    def calc_factor(self, abs_p_gap):
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
        if abs_p_gap < self.halfway_p:
            return (2 - (2 - (abs_p_gap / self.halfway_p)) ** 2)
        else:
            return (((abs_p_gap) / self.halfway_p) ** 2)

class Consumer(ActorBase):
    def __init__(self):
        self.prev_q = 0
        self.grad_factor = 0.2

    def __call__(self, p):
        subtraction = self.grad_factor * (p - self.base_p_ref)
        self.prev_q -= subtraction
        return self.prev_q

"""
to use actor_traders:
from actor_traders import ResTrader
# for demand
quantity_bought = ResTrader.to_hoard(category, p_gap, p_per_prod)

# for supply
quantity_sold = ResTrader.to_dump(category, p_gap)

"""