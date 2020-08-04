a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[1])

b = [x**2 for x in a if x % 2 == 0]
print(b)

list1 = ['abcd', 786, 2.23, 'john', 70.2]
print(list1 * 2)

frog = '10893346'
print(frog * 2)
print(frog[1:7:2])
a[1:7:2] = [0, 0, 0]
print(a)

list1[1] = 1000
print(list1)

num = [x for x in range(1, 10)]
print(num)

print('-' * 80)

print(num[::-1])
print(list(reversed(num)))
print(num)
num.reverse()
print(num)
print([x for x in range(9, 0, -1)])

print(len(num))
print(min(num))
print(max(num))

print('.'.join('hello'))