#!/usr/bin/env python3
"""Contains the function/method summation_i_squared."""


def summation_i_squared(n):
    """
        Function that calculates summ of i from 1 to n.
    """

    if type(n) is not int or n < 1:
        return None
    return int(n * (n + 1) * (2 * n + 1) / 6)
