class MyStack:
    def __init__(self):
        self.__storage = []

    def push(self, item):
        self.__storage.append(item)

    def pop(self):
        return self.__storage.pop()

    def peek(self):
        return self.__storage[-1]

    def __bool__(self):  # if / while condition check
        return len(self.__storage) != 0

    def __len__(self):
        return len(self.__storage)


class MyQueue:
    def __init__(self):
        self.__storage = []

    def enqueue(self, item):
        self.__storage.insert(0, item)

    def dequeue(self):
        return self.__storage.pop()  # pop last value in the list

    def peek(self):
        return self.__storage[-1]

    def __bool__(self):  # if / while condition check
        return len(self.__storage) == 0

    def __len__(self):
        return len(self.__storage)