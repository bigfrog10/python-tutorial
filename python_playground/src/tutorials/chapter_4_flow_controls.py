# Boolean values: True, False
# comparison
print(5 > 3)

c = [1, 2, 3]
print(1 in c)
print(4 in c)

a = 5 == 3
b = 6 < 4
print(a)
print(not a)
print(a and b)
print(a or b)

# if, if-else, if-elif-else

# embedded control, no more than 3

# while
# fibonacci sequence
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# break, continue
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
