def fib(x: int):
    a, b = 1, 1
    for i in range(x):
        yield a
        a, b = b, a + b


print(list(fib(10)))

for i in fib(20):
    print(i)