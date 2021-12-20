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
