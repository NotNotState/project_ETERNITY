import numpy as np
from math import factorial
from functions.helper_functions import abs_diff

"""
Custom implementation of sinh(x) using its Taylor series expansion
"""

def sinh_custom(x: float, TOL: float = 1e-8, N_max: int = 20) -> float:
    """
    Calculates sinh(x) using the Taylor series expansion:
    sinh(x) = x + x^3/3! + x^5/5! + ...
    """
    result = 0.0
    term = x  # First term in the series
    n = 1  # Start with the first term

    while abs_diff(term, 0) > TOL and n <= N_max:
        result += term
        n += 2
        term *= x**2 / ((n-1) * n)  # Calculate the next term in the series

    return result


if __name__ == "__main__":
    test_values = [0, 0.5, 1, 2, 5]
    for val in test_values:
        print(f"sinh_custom({val}) = {sinh_custom(val)}")
        print(f"np.sinh({val}) = {np.sinh(val)}")
