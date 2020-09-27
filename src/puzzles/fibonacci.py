import cProfile
from functools import lru_cache as cached


@cached(maxsize=None, typed=False)
def fib(n):
    if n <= 2:
        print(1)
        return 1
    else:
        s = fib(n-1)+fib(n-2)
        print(s)
        return s


print(fib(30))
# cProfile.run('print(fib(50))')
