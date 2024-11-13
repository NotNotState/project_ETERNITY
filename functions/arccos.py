def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def exponent(base, power):
    result = 1
    for _ in range(power):
        result *= base
    return result


def arcsin_taylor(x, terms=1000):
    # approximation of pi
    pi = 3.141592653589793

    if x == 1:
        return pi / 2
    if x == -1:
        return -pi / 2

    # taylor series starts with π/2
    result = 0

    # keeps tracks of x^(2n+1)
    # starts at x^1 = x because n = 0
    x_pow = x

    # keeps track of (2n)! in the numerator
    # starts at 1 because (2*0)! = 1
    factorial = 1

    # keeps track of (n!)^2 in denominator
    # starts at 1 because (0!)^2 = 1^2 = 1
    denom_factorial = 1

    # n starts at 0
    for n in range(terms):
        coeff = factorial / (exponent(4, n) * denom_factorial * (2 * n + 1))
        result += coeff * x_pow

        # calculate parts for next term in series
        x_pow *= x * x  # x^(2(n+1)+1) = x^(2n+1) * x^2 and so on
        factorial *= (2 * n + 2) * (2 * n + 1)  # (2n+2)! = (2n)! * (2n+2) * (2n+1)
        denom_factorial *= (n + 1) * (n + 1)  # (n+1)!^2 = (n!)^2 * (n+1)^2

    return result


def arccos_taylor(number: float) -> float:
    if number < -1 or number > 1:
        raise ValueError("arccos(x) is only defined in the range of [-1, 1]")

    # approximation of pi
    pi = 3.141592653589793

    # taylor series starts with π/2
    result = pi / 2 - arcsin_taylor(number)

    return result


if __name__ == '__main__':
    print_hi('PyCharm')
    x = -1  # Example input in the range [-1, 1]
    result = arccos_taylor(x)
    print("arccos(", x, ") =", result)
