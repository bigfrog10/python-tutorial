import time


def timing(f):
    def wrap(*args, **kwargs):
        a = time.time()
        ret = f(*args, **kwargs)
        b = time.time()
        c = b - a
        print(f'function {f} takes {c} seconds.')
        return ret
    return wrap


class TimingDecorator:
    def __init__(self, function):
        self.function = function
        self.duration = 0

    def __call__(self, *args, **kwargs):
        a = time.time()
        ret = self.function(*args, **kwargs)
        b = time.time()
        c = b - a
        self.duration += c
        print(self.duration)
        return ret


@TimingDecorator
def factorial(i: int) -> int:
    x = 1
    for y in range(2, i + 1):
        x *= y
    return x


print(factorial(100))
print(factorial(100))
print(factorial(100))
# a = time.time()
# print(factorial(200))
# b = time.time()
# print((b - a))
