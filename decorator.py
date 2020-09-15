import math


def decorator(func):

    def wrapper():
        eps = 0.00000001
        result = 0
        b = func
        x = 1
        while eps <= math.fabs(b(x)):
            result += b(x)
            x += 1
        return result
    return wrapper


@decorator
def sumSeries(x):
    y = 1/x**2
    return y


print(sumSeries())
