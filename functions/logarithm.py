import math

def logarithm(base, x, tolerance=1e-7):
    y = 1.0

    while True:
        b_y = base ** y

        y_new = y - (b_y - x) / (b_y * (1 / base))

        if abs(y_new - y) < tolerance:
            break

        y = y_new

    return y

if __name__ == "__main__":
    b = 4
    x = 100

    print(logarithm(b, x))
    print(math.log(x, b))