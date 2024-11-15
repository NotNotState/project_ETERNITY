import numpy as np
from functions.helper_functions import exponential

"""
Calculates sinh(x) using the exponential definition: sinh(x) = (e^x - e^(-x)) / 2
"""

def sinh(x: float) -> float:
    """
    Calculate sinh(x) using the exponential definition.
    """
    return (exponential(x) - exponential(-x)) / 2


def exponential(x: float, TOL: float = 1e-8, N_max: int = 50) -> float:
    """
    Approximates e^x using the Taylor series:
    e^x = 1 + x + x^2/2! + x^3/3! + ...
    """
    result = 1.0  # First term in the series
    term = 1.0  # Term starts as 1 (x^0 / 0!)
    n = 1  # Counter for factorial in denominator

    while abs(term) > TOL and n <= N_max:
        term *= x / n  # Calculate the next term in the series
        result += term
        n += 1

    return result


if __name__ == "__main__":
    # Test values for sinh(x)
    test_values = [0, 0.5, 1, 2, 5]
    for val in test_values:
        print(f"sinh({val}) = {sinh(val)}")
        print(f"np.sinh({val}) = {np.sinh(val)}")  # Compare with numpy's sinh
