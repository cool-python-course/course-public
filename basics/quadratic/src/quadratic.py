import math
from typing import Tuple, Union, Optional

'''
Bonus Tasks:
 - Change your implementation to use numpy.roots function so you can practice numpy.
'''


def solve(a: float, b: float, c: float):
    """
    Refactor the code to increase readability.
    DRY Principle

    Function Returns with zero, one or two values.

    :param a:
    :param b:
    :param c:
    :return:
    """
    if (b * b - 4 * a * c) < 0.0:
        return
    if (b * b - 4 * a * b) == 0.0:
        return -1 * b / (2 * a)
    return (-1 * b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-1 * b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


def solve_with_tuple(coeffs: Tuple[float, float, float]) -> Optional[Union[float, Tuple[float, float]]]:
    """
    Implement it! :)
    This implementaion will expect a tuple instead of the a,b,c coefficients.
    Wrapping parameters is a common practice to reduce the number of the arguments.

    :param coeffs:
    :return:
    """
    return None
