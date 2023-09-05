# $g(a, b) = 3 * a + 7 * b$
# $c() = 7$
# $h(x, y, z) = y * x**x + z$
# $m(x, y) = g(x, y) + h(2*x, x, y) + c()$
def g(a, b):
    return 3 * a + 7 * b


def c():
    return 7


def h(x, y, z):
    return y * x**x + z


def m(x, y):
    return g(x, y) + h(2 * x, x, y) + c()


def f(x):
    return 2 * x + 7


print("f(0) = " + f(0))
print("f(0) = " + f(1))
print("f(0) = " + f(-1))
print("f(0) = " + f(0.5))
