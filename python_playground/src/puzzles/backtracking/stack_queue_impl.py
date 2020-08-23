class MyStack:
    def __init__(self):
        self._storage = []

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        return self._storage.pop()

    def peek(self):
        return self._storage[-1]

    def __bool__(self):  # if / while condition check
        return len(self._storage) != 0

    def __len__(self):
        return len(self._storage)


class MyQueue:
    def __init__(self):
        self._storage = []

    def enqueue(self, item):
        self._storage.insert(0, item)

    def dequeue(self):
        return self._storage.pop()  # pop last value in the list

    def peek(self):
        return self._storage[-1]

    def __bool__(self):  # if / while condition check
        return len(self._storage) == 0

    def __len__(self):
        return len(self._storage)