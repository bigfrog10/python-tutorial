import math
from math import sqrt
print(math.sqrt(4))
print(sqrt(4))


def f(x):
    return x*x


x = []
if x:
    print(x)

if x is None:
    print(x)

name = input('What is your name?')
if name.startswith('Gumby'):
    print("Hello, Mr. Gumby")

if name.lower() == "gumby":
    print("Hello, Mr. gumby")

x = ['crocodile', 'alligator', 'dinosaur']
y = filter(lambda m: len(m) > 5 and m.startswith('d'), x)
print(list(y))


def g(m):
    return len(m) > 5 and m.startswith('d')


y = filter(g, x)
print(list(y))
