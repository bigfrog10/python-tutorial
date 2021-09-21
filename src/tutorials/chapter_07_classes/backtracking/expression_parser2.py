from collections import deque
import re
token_re = re.compile('\d+|[^ 0-9]')

class Solution:
    def calculate(self, s: str) -> int:
        def parse(exp):
            stack = []
            postfix = deque()

            tokens = token_re.findall(exp)
            for t in tokens:
                if t.isnumeric():
                    postfix.append(t)
                elif t in '+-':
                    while stack: # pump everything before (
                        s = stack.pop()
                        if s in '+-':
                            postfix.append(s)
                        else: # (
                            stack.append(s)
                            break # need to break out on (

                    stack.append(t)
                elif t == '(':
                    stack.append(t)
                elif t == ')':
                    s = stack.pop()
                    while s != '(':
                        postfix.append(s)
                        s = stack.pop()

            while stack:
                postfix.append(stack.pop())

            return postfix

        def evaluate(postfix):
            operand_stack = [] # we need stack because we could have

            while postfix:
                p = postfix.popleft()
                if p.isnumeric():
                    operand_stack.append(int(p))
                elif p in '+-':
                    op1 = operand_stack.pop()
                    if len(operand_stack) == 0:
                        if p == '-':
                            operand_stack.append(-op1)
                        else:
                            operand_stack.append(op1)
                        continue
                    op2 = operand_stack.pop()
                    if p == '+':
                        operand_stack.append(op2 + op1)
                    elif p == '-':
                        operand_stack.append(op2 - op1)

            return operand_stack.pop()

        postfix = parse(s)
        return evaluate(postfix)

    # "1-(2+1)"
    # "-2+ 1"


print(Solution().calculate("-2+ 1"))
