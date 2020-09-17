# functions - to create reusable components

# function name is unique, no overloading with different parameters
def reverse_digits(a):  # declare signature of the function
    """ reverse digits for a given number """  # function doc
    return int(str(a)[::-1])  # return result or no return


print(reverse_digits(12345))


# this overrides the previous definition
def reverse_digits(a: int) -> int:  # add type hints
    return int(str(a)[::-1])


print(reverse_digits(12345))


# recursion
def factorial(up_to):
    if up_to == 1 or up_to == 2:
        return up_to

    return up_to * factorial(up_to - 1)


print(factorial(5))

# tail recursions can be converted to a for loop


# default values, need to be after parameters without default
def mod(n, m=10):
    return n % m


print(mod(32))
print(mod(32, 16))
print(mod(m=16, n=32))  # reverse parameter order with keys


# however, this is dangerous. m could change every call
def acc(n, m=[]):  # m is mutable
    m.append(n)
    return m


print(acc(10))
print(acc(20))


# None is the representation for nothing/no value. Functions by default return
# None if we don't overwrite to explicitly return values.
# one way to fix this:
def acc(n, m=None):
    if m is None:
        m = []
    m.append(n)
    return m


print(acc(10))
print(acc(20))


# None is not 0, empty string, or empty list
print(0 == None)  # False, though we should not use == for None, use next time.
print(0 is None)  # False


# one useful way is caching, between calls
def factorial(up_to, cache={}):
    if up_to in cache:
        return cache[up_to]

    if up_to == 1 or up_to == 2:
        return up_to

    prev = factorial(up_to - 1)

    print(f'compute {up_to}')
    res = up_to * prev
    cache[up_to] = res
    return res


# compute each factorial only once
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))


# function be parameter too
def f(a, b, func):
    return a * func(b)


import math
print(f(99, math.pi, math.sin))


# inner functions
def f(a, b):
    def g(x):
        return x ** 2

    return a * g(b)


print(f(2, 3))


# functions can be returned
def f(a):
    def g(x):  # closure since a is used here. If a is mutable, there is a side effect.
        return a + x

    return g


print(f(2)(3))


# counter example
def squared_funcs():
    ret = []
    for i in range(1, 3):
        def f():
            return i * i
        ret.append(f)
    return ret


# both return 4, not 1, 4 as expected since i is 2
f1, f2 = squared_funcs()
print(f1())
print(f2())


# to convert function to a partial function
def f(a, b):
    return math.sqrt(a ** 2 + b ** 2)


from functools import partial
g = partial(f, 3)  # replace a with 3 and leave b open
print(g(4))


# lamda for short/one liner functions
f = lambda x: x ** 2
print(f(5))


# *arg and **kwargs, used to pass down to other lib calls most of the time
def f(a, b, c):  # other functions called
    return a + b + c


def g(a, *args, **kwargs):
    return a + f(a, *args, **kwargs)  # 3 is for b from args, c=5 for kwargs


print(g(2, 3, c=5))


# another example:
def join(separator: str, *args):
    return separator.join(args)


a = join('-', 'pluto', 'mickey', 'goofy')
print(a)


# another example:
def avg(*args):  # naive implementation of average
    return sum(args) / len(args)


print(avg(1, 2, 3))
print(avg(1, 3, 5))
print(avg(*[1, 2, 3], *[4, 5, 6]))  # unpack all


# new feature - * means no positional parameters
def concat_with(x, y, *, sep=' '):
    return sep.join([x, y])


print(concat_with('Hello', 'World', sep=', '))  # need sep as key here
# print(concat_with('Hello', 'World', ', ')) This is not working anymore

# for >= 3.8, / means no keyed parameters before /
# def concat_with(x, y, /, sep=' '):
#     return sep.join([x, y])
#
# print(concat_with('Hello', 'World', sep=', '))  # This is fine
# print(concat_with(x='Hello', y='World', sep=', ')) This is not working


# the function parameters passed in are the copies, so if you change it inside
# the function, it's not reflected outside.
def add(a, b):
    a = a + 1  # we change a here, new value works only within this function.
    return a + b


a, b = 5, 3
print(add(a, b))  # print 9
print(a)  # still 5, so a is not changed


def list_sum(a):
    a = [1, 2, 3]  # we change a, won't be seen outside this function
    return sum(a)


a = [4, 5, 6]
print(list_sum(a))  # 6, since a is changed inside function
print(a)  # still [4, 5, 6]


# however, this is seen outside
def list_sum1(a):
    a.append(100)
    return sum(a)


a = [4, 5, 6]
print(list_sum(a))  # 6, since a is changed inside function
print(a)  # [4, 5, 6, 100]

# so the rule is that function parameters are passing by copy-of-references
# a in the list_sum1() is a copy of the reference, which still points to the
# list. Since it's the same list, so the value is seen outside.
# a in list_sum() is a copy of reference to [4, 5, 6], so if you change this
# reference copy to something else [1, 2, 3], the original reference is not
# changed.


# generators
def square():
    for i in range(2, 9):
        yield (i + 2) ** 2


a = square()
print(next(a))
print(next(a))
print(next(a))

for x in square():
    print(x)


# fib generator
from typing import Generator


# Generator[yield_type, send_type, return_type]
# Another way is Iterator[int], Iterator is in typing module too.
def fib(x: int) -> Generator[int, None, None]:
    """ return fib series up to x"""
    a, b = 1, 1
    for i in range(x):
        yield a
        a, b = b, a + b


print(list(fib(10)))

for i in fib(10):
    print(i)


# generator expression, in parallel to list comprehension
g = (x * 2 for x in range(5))
print(g)  # g is lazy

# iterator

# inspections
print(fib.__name__)
print(fib.__doc__)
print(fib.__module__)
print(fib.__annotations__)


# decorators, AOP - aspect oriented programming, a very powerful tool
def log(func):  # log interceptor
    def wrapper(*args, **kwargs):
        print(f'log before call to function {func.__name__}() ...')
        return func(*args, **kwargs)

    return wrapper


@log
def f(x):
    return x * 10


print(f('abc'))

# another example
import time
import functools


def timing(f):
    @functools.wraps(f)  # this carries f to wrapper, such as name, doc, signature
    def wrapper(*args, **kwargs):
        a = time.time()
        ret = f(*args, **kwargs)
        b = time.time()
        c = b - a
        print(f'function {f.__name__}() takes {c} seconds.')
        return ret
    return wrapper


@timing
def factorial(i: int) -> int:
    x = 1
    for y in range(2, i + 1):
        x *= y
    return x


print(factorial(3000))

# another example:
# https://chase-seibert.github.io/blog/2013/12/17/python-decorator-optional-parameter.html
# log with level parameters

# when we wrap the function, we need to carry some of the information from the original
# such as, name, doc, signature, and honor some of the functions, such as help() and
# inspection


# global vs local variables


# stack & heap, frame
# https://medium.com/datadriveninvestor/how-does-memory-allocation-work-in-python-and-other-languages-d2d8a9398543
