
def f(x, y):
    return x - y


def euler(f, x0, y0, xn, n):
    h = (xn - x0) / n
    x = x0
    y = y0
    for i in range(n):
        y += h * f(x, y)
        x += h
        print(f"x = {x}\t y = {y}")
    return y


x0 = 0
y0 = 1
xn = 1.2
n = 10

result = euler(f, x0, y0, xn, n)
