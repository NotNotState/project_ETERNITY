import math

def ln(x, iterations=1000):
    if x <= 0:
        raise ValueError("ln(x) is undefined for x <= 0")
    if x == 1:
        return 0

    n = 0
    while x > 2.0:
        x /= 2.0
        n += 1
    while x < 1.0:
        x *= 2.0
        n -= 1

    y = (x - 1) / (x + 1)
    y_squared = y*y
    result = 0
    term = y
    for i in range(1, iterations * 2, 2):
        result += term / i
        term *= y_squared

    # ln(2) ≈ 0.69314718055994530941723212145817656807550013436026 
    return n * 0.69314718055994530941723212145817656807550013436026 + 2 * result

def logarithm(base, x, iterations=1000):
    if base <= 0 or base == 1 or x <= 0:
        raise ValueError("Base must be > 0 and != 1, and x must be > 0.")
    lnx = ln(x, iterations)
    lnbase = ln(base, iterations)
    return round(lnx / lnbase, 10)

if __name__ == "__main__":
    print("Main start")
    b = 2
    x = 4

    print(logarithm(b, x))
    print(math.log(x, b)) 
