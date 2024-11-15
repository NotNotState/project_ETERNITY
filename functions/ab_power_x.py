from functions.exponent import exponent

def ab_power_x(a, b, x):
    """Calculate the value of ab^x using the imported exponent function"""
    if b <= 0:
        raise ValueError("Base 'b' must be greater than 0 for exponential calculations.")
    
    # Compute b^x using the imported exponent function
    exponential_result = exponent(b, x)
    
    # Multiply by a
    return a * exponential_result

if __name__ == "__main__":
    print(ab_power_x(2, 3, 4))     # 2 * 3^4 = 162
    print(ab_power_x(1, 5, 2))     # 1 * 5^2 = 25
    print(ab_power_x(0, 3, 4))     # 0 * 3^4 = 0
    print(ab_power_x(5, 2, 0))     # 5 * 2^0 = 5
    print(ab_power_x(1.5, 3, -2))  # 1.5 * 3^(-2) = 0.166666...
    print(ab_power_x(10, 0.5, 2))  # 10 * (0.5)^2 = 2.5
