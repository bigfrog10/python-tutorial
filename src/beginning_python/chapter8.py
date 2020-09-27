import traceback

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    traceback.print_exc()
    print("The second number can't be zero!")

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(x / y)
