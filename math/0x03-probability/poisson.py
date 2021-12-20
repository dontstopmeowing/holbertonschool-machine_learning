#!/usr/bin/env python3
"""Contains the Poisson class."""


class Poisson:
    """Represents poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Determinate whether it is positive or not."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """Calculates the value of the PMF for a given number"""
        if k:
            if type(k) != int:
                k = int(k)
            if k < 0:
                return 0
            return (pow(self.lambtha, k) *
                    pow(2.7182818285, -1 * self.lambtha) /
                    func_factorial(k))


def func_factorial(x):
    """Returns a factorial number"""
    if x < 0:
        return None
    if x == 0:
        return 1
    if x < 2:
        return 1
    return x * func_factorial(x - 1)
