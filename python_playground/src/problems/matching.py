from difflib import SequenceMatcher

first = input("enter the first word: ")
second = input("enter the second word: ")
# print(first, second)


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


print(similar(first, second))
