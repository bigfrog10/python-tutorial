# list - position based index, similar to string
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[1])
print(a[1:5])  # slice and dice
print(a[3:])
print(a[:7])
print(a[-1])  # last element, no need to compute length of the list.
print(a[::2])  # every other item
print(a[::-1])  # reverse
print(len(a))  # aggregations
print(min(a))
print(max(a))
print(sum(a))
first, *_ = a  # we care only the first
print(first)
first, *middle, last = a  # unpack
print(first)
print(middle)
print(last)

print(a[1:7:2])
a[1:7:2] = [0, 0, 0]  # This is fast, list allow duplicate values, need to know the size first
print(a)

# mixed data types
b = ['abcd', 786, 2.23, 'john', 70.2]
print(b * 2)
print(a + b)  # same as a.extend(b)

b[1] = 1000  # change value
print(b)

print(list(reversed(a)))  # a is not change
a.reverse()  # change in place
print(a)
print(sorted(a))  # create new sorted list
a.sort()  # in place sort
print(a)

c = ['I', 'am', 'Sam']
print(', '.join(c))

f = [1, 2, 3]
g = f.copy()
print(g)
g[1] = 5
print(f)  # f is not changed
print(g)  # g is changed
f = [[1, 2, 3], [4, 5, 6]]
g = f.copy()
g[1][2] = 100
print(f)  # f is changed due to shallow copy, undesired effect
print(g)  # g is changed

f = [[1, 2, 3], [4, 5, 6]]
import copy
g = copy.deepcopy(f)
g[1][2] = 100
print(f)  # f is not changed due to deep copy
print(g)  # g is changed

# for loop
for item in b:
    print(item)

r = []
for i in range(10):  # loop 0 ... 9
    r.append(i)
print(r)

r = []
for i in range(1, 10):  # loop 1 ... 9
    r.append(i)
print(r)

r = []
for i in range(1, 10, 2):  # loop 1 3 5 7 9
    r.append(i)
print(r)
r.insert(0, 5)  # insert item at the given position 0
print(r)
r.remove(5)  # remove only the first occurrence of value 5
print(r)
r.insert(0, 5)  # insert item at the given position 0
print([x for x in r if x != 5])  # remove all 5's
r.clear()  # remove all elements
print(r)


for index, value in enumerate(c):  # both position index and value
    print(f'index={index}, value={value}')

for index, value in zip(range(len(c)), c):
    print(f'index={index}, value={value}')


# version comparison - a version has major, minor, and patch, such as 1.3.0.

# multi for loops

# list comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [x**2 for x in a if x % 2 == 0]  # filter
print(d)

a = [i if i % 2 == 0 else -i for i in range(1, 10)]
print(a)

print([x for x in range(9, 0, -1)])  # full permutations

print([m + n for m in 'ABCD' for n in '1234'])


# string is treated as list of chars, as we saw before
d = "I do not like green eggs and ham. Sam I am."
words = d.split(' ')  # split by space
print(words)
print('-'.join(d))
print('-'.join(words))

# tuple is immutable list
a = (1, 2, 3)
# a[1] = 4 is not working


# dict - key based index, unordered
grades = {'Ashley': 95, 'Gregory': 90, 'Rick': 70}
print(grades['Ashley'])
print(grades.get('Arthur', None))  # default to None
# print(grades['Arthur']) this is not working, KeyError
print(grades.keys)
print(grades.values())
print(grades.items())

for key, value in grades.items():
    print(f'key={key}, value={value}')
    print(key, value)  # print multi values

grades['Olivia'] = 87  # add key value pair
print(grades)

print({k: v for (k, v) in grades.items()})  # dict comprehension

prices = dict(iphone=100, nick=50, shirt=30)  # more like function parameters
print(prices['iphone'])

fruits = ['Apple', 'Banana', 'Orange']
print({k+1: v[:3] for (k, v) in zip(range(len(fruits)), fruits)})  # dict comprehension

# set and frozenset, distinct values
fruits = {'Apple', 'Banana', 'Orange'}

storage = set(a)  # create from a list/tuple

storage.add(4)
storage.update([5, 6])
print(storage)
storage.remove(5)
print(storage)


# tuple and frozenset are immutable.


print(list('abcd'))  # ['a', 'b', 'c', 'd']
print(tuple('abcd'))  # ('a', 'b', 'c', 'd')
print(set('abcd'))  # {'a', 'b', 'c', 'd'}


# we touched only the built-in collections. There are other widely used
# collections, such as queue, stack, trees and graphs.
# for linked list, queue, stack, check these:
#     built in queue
#     built in collections has a deque
# for trees:
#     https://github.com/mozman/bintrees
#     https://pypi.org/project/sortedcontainers/
#     https://treelib.readthedocs.io/en/latest/
# for graphs, check networkx
