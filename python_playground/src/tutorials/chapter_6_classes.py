


# decorator with internal states
import time
import functools


class TimingDecorator:
    def __init__(self, function):
        self.function = function
        self.duration = 0
        functools.update_wrapper(self, function)
        # check more on these: composition is always hard unless we have the full scope
        # https://stackoverflow.com/questions/6394511/python-functools-wraps-equivalent-for-classes
        # https://hynek.me/articles/decorators/

    def __call__(self, *args, **kwargs):
        a = time.time()
        ret = self.function(*args, **kwargs)
        b = time.time()
        c = b - a
        self.duration += c
        print(f'function {self.function.__name__}() takes {self.duration} seconds.')
        print(self.duration)
        return ret


# need to fix meta data propagation
@TimingDecorator
def factorial(i: int) -> int:
    x = 1
    for y in range(2, i + 1):
        x *= y
    return x


print(factorial(3000))
print(factorial(3000))
