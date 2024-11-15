def nth_root(value, n, tolerance=1e-10):
    """Calculate the nth root of a value using the Newton-Raphson method."""
    if value == 0:
        return 0
    if n < 0:
        raise ValueError("nth_root does not support negative roots directly")
    
    approx = value / n  # Initial guess
    while True:
        better_approx = (1 / n) * ((n - 1) * approx + value / (approx ** (n - 1)))
        if abs(better_approx - approx) < tolerance:
            return better_approx
        approx = better_approx

def exponent(base, exp):
    # Handle zero exponent case
    if exp == 0:
        return 1
    
    # Separate integer and fractional parts of the exponent
    integer_part = int(exp)
    fractional_part = exp - integer_part
    
    # Integer part calculation
    result = 1
    abs_integer_part = abs(integer_part)
    for _ in range(abs_integer_part):
        result *= base
    
    # If the integer part is negative, invert the result
    if integer_part < 0:
        result = 1 / result

    # Fractional part calculation
    if fractional_part != 0:
        abs_fraction = abs(fractional_part)
        root_result = nth_root(base, 1 / abs_fraction)  # Handle the positive fractional part
        if fractional_part < 0:  # If fractional part is negative, invert the root result
            root_result = 1 / root_result
        result *= root_result
    
    return result

if __name__ == '__main__':
    print(exponent(40,0))        # Output: 1
    print(exponent(7,-3))        # Output: 0.002915
    print(exponent(100,0.5))     # Output: 10
    print(exponent(2,-3/4))      # Output: 0.594603
    print(exponent(4, 0.5))      # Output: 2
    print(exponent(8, 1/3))      # Output: 2
    print(exponent(100, -2.5))   # Output: 0.00001