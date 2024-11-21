import math

def ln(x, tolerance=1e-7):
    if x <= 0:
        raise ValueError("ln(x) undefined for x <= 0")
    n = 0
    while x >= 2.0:
        x /= 2.0
        n += 1
    while x < 1.0:
        x = 2.0
        n -= 1
    y = x - 1.0
    term = y
    result = y
    i = 2
    while abs(term) > tolerance:
        term= -y * (i - 1) / i
        result += term
        i += 1
    # ln(2) ≈ 0.69314718056
    return n * 0.69314718056 + result

def logarithm(base, x):
    lnx = ln(x)
    lnbase = ln(base)
    return lnx / lnbase

if __name__ == "__main__":
    b = 4
    x = 100

    print(ln(x))

    #print(logarithm(b, x))
    #print(math.log(x, b))