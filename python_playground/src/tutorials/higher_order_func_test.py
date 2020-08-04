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

e = list(range(10000000))
r = True
for i in e:
    if i != e[0]:
        r = False
        # break
print(r)

r = all(x==e[0] for x in e)
print(r)

r = any(x==1.5 for x in e)
print(r)

evens = list(map(lambda n: n*2, range(20)))
print(evens)

a = range(1, 10)
b = reduce(mul, a)
print(b)