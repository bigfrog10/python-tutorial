if True:
    print('true')
else:
    print('false')

# fibonacci sequence
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

fruits = {'apple', 'orange', 'banana'}
for f in fruits:
    if f == 'apple':
        continue
    print(f)

for i in range(10):
    if i == 2:
        break
    else:
        print(i)


def join(separator: str, *args):
    return separator.join(args)


a = join('-', 'pluto', 'mickey', 'goofy')
print(a)

b = a.split('-')
print(b)