# a stack is a container that obeys last-in first-out (LIFO) principle
# it has only 2 methods that operate on the top of the stack:
#     push item into stack, and
#     pop item out of stack
stack1 = ['snapple', 'coca cola', 'sprite', 'apple juice']

print(stack1.pop())  # prints 'apple juice'
stack1.append('coffee')  # stack push at the end which is the top of the stack
print(stack1.pop())  # prints 'coffee'
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
try:
    print(stack1.pop())  # raises error - no more item to pop
except IndexError as e:
    print('stack pop empty: ' + str(e))

# a queue is also a container that obeys the first-in first-out (FIFO) principle
# it has only 2 methods that operate on both ends of the stack:
#     enqueue item at the back, and
#     dequeue item at the front

import queue

queue1 = queue.Queue()
queue1.put('snapple')  # enqueue
queue1.put('coca cola')  # enqueue
print(queue1.get())  # prints first item: 'snapple'
print(queue1.get())  # prints second item: 'coca cola'
try:
    print(queue1.get(block=False))  # doesn't print anything
except queue.Empty as e:
    print('queue is empty' + str(e))