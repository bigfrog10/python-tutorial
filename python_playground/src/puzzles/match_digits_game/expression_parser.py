# https://blog.csdn.net/iteye_15612/article/details/81725858
# https://www.chris-j.co.uk/parsing.php
# https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html
import queue
import re

number_or_symbol = re.compile('(\d+|[^ 0-9])')
print(re.findall(number_or_symbol, '((81 * 6) / 42 + (3 - 1))'))
stack = []
output_queue = queue.Queue()

