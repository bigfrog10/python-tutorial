# higher order functions
from functools import reduce
from operator import mul

b = lambda x: -x[0]
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=b)
print(pairs)

a = list(range(1, 10, 2))
print(a)

b = [x for x in a if x > 3]
print(b)

c = filter(lambda x: x > 3, a)
print(list(c))


def f(x):
    return 3 < x < 9


d = filter(f, a)
print(list(d))
print(len(a))

e = list(range(10000))
r = True
for i in e:
    if i != e[0]:
        r = False
        break
print(r)

r = all(x == e[0] for x in e)
print(r)

r = any(x == 1.5 for x in e)
print(r)

evens = list(map(lambda n: n*2, range(20)))
print(evens)

a = range(1, 10)
b = reduce(mul, a)
print(b)


# median - the value separates the higher half from the lower half
nums = [16, 3, 2, 4, 11, 1, 12, 8, 9, 7, 10, 13, 15, 17]
import statistics
print(statistics.median(nums))


# manual way
def median(nums):
    s = sorted(nums)
    half_way = len(nums) // 2 - 1  # because index is 0 based
    if len(nums) % 2 == 0:  # even
        return (s[half_way] + s[half_way + 1]) / 2
    else:
        return s[half_way + 1]


print(median(nums))
print(median([1, 2, 3, 4, 5]))  # 3
print(median([1, 2, 3, 4]))  # 2.5


# generators
def square():
    for i in range(2, 9):
        yield (i + 2) ** 2


a = square()
print(next(a))
print(next(a))
print(next(a))
a.close()  # when we are done, we close it.


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


# coroutine
# https://dev.to/codemouse92/dead-simple-python-generators-and-coroutines-21ll
# https://stackabuse.com/coroutines-in-python/

def ret_gen(n):
    while n > 0:
        m = (yield n)
        print("receive value: ", m)
        n -= 1


import traceback
a = ret_gen(10)
next(a)
try:
    for i in a:
        print(i)
        a.send(i * 10)
    # while True:
    #     i = a.send(100)
    #     print(i)
except StopIteration:
    traceback.print_exc()


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

# map(func, list)
# filter(func, list)
# reduce(func, list)
map(lambda x: x.upper(), ['mickey', 'pluto'])

# data for testing
books = [ {'name': 'C# step by step', 'price':23.7, 'store':'amazon'},
          {'name': 'ASP.NET expert', 'price':44.5, 'store':'amazon'},
          {'name': 'C# step by step', 'price':24.7, 'store':'lulu'},
          {'name': 'ASP.NET expert', 'price':45.7, 'store':'lulu'},
          {'name': 'C# step by step', 'price':26.7, 'store':'Barns & Noble'},
          {'name': 'ASP.NET expert', 'price':55.7, 'store':'Barns & Noble'},
          ]

# find the store with the minimal price for the ASP.NET book
print(min([b for b in books if b['name'] == 'ASP.NET expert'], key=lambda b : b['price'])['store'])

# 50% discount on the price
print(map(lambda b: dict(name=b['name'], price=b['price'] * 0.5, store=b['store']), books))

# average price for the book "C# step by step"
print((lambda bs: sum(bs) / len(bs)) ([b['price'] for b in books if b['name'] == 'C# step by step']))

# average price for all the books
print(map(lambda bn: dict(name=bn, avg=((lambda bs: sum(bs) / len(bs))
          ([b['price'] for b in books if b['name'] == bn]))), list(set([b['name'] for b in books]))))


# https://www.codementor.io/@sheena/advanced-use-python-decorators-class-function-du107nxsv
# https://realpython.com/primer-on-python-decorators/
# https://github.com/mpkocher/Functional-Programming-Techniques-In-Python
