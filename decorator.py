# декотрато с элементами оборачиваемой функции
def square(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res ** 2

    return wrapper


# декоратор, который сам может принимать элементы нанписать декоратор, который находтиь сумму ряда с какой-то  точностью
def pow(k):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = 0
            s = 0
            delX = 0.000000001
            for i in range(1, k + 1):
                s += i
            return s

        return wrapper

    return decorator
    # for i in range(power):


pow(1)


@square
def f2(a, b, c):
    return a + b + c


@pow(k=2)
def f4(x):
    return x


print(f2(1, 3, 0))
print(f4())
