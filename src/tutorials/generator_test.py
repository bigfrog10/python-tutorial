def square():
    for i in range(2, 27):
        yield (i + 2) ** 2


a = square()
print(next(a))
print(next(a))
print(next(a))

print('-' * 80)

for x in square():
    print(x)