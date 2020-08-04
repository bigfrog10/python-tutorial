def f(s):
    print(s)


x = f('hello')
print(x)


def try_to_change(n):
    n = 'Mr. Gumby'


name = 'Mrs. Entity'
try_to_change(name)
print(name)


def try_to_change1(n):
    n['m'] = 'hello'


mydict = {"m": "world"}
print(mydict)
try_to_change1(mydict)
print(mydict)

w = 42


def calc(x):
    global w
    x = w + 1 + x
    print(x)
    w = x


calc(5)
print(w)