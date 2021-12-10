#!/usr/bin/env python3
"""Contains the function poly_derivative"""


def poly_derivative(poly):
    """
        Function that calculates the derivative of a polynomial.
    """

    if type(poly) != list or len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    if poly is None:
        return None

    derivative = list(range(len(poly)-1))

    for i in range(len(derivative)):

        if type(i) != int:
            return None

        derivative[i] = poly[i + 1] * (i + 1)

    return derivative
