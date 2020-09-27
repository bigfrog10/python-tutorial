# https://en.wikipedia.org/wiki/24_Game
# given 4 numbers, using arithmetic operations, +, -, *, /, and parentheses
# create an expression such that the result is equal to 24

# there are 4! permutations for four numbers, A, B, C, and D
# there are 4**3 combinations for 3 operations among the four numbers
# so there are 4! * 4**3 expressions in total

# for each expression, we break the expression by operators to stimulate
# parentheses

import itertools

# for c in itertools.permutations('ABCD'):
#     print(c)
#
# for c in itertools.product(*['+-*/'] * 3):
#     print(c)


def exp_eval(expr: str):
    res = {}
    if expr.isnumeric():
        res[expr] = float(expr)  # float because operator could be /
        return res

    # loop all operators and breaks the expression at each operator (no need to
    # worry about order of operations)
    for i in range(len(expr)):
        if expr[i].isnumeric():
            continue

        prefix = expr[:i]
        suffix = expr[i+1:]

        x = exp_eval(prefix)
        y = exp_eval(suffix)

        for k1, v1 in x.items():
            for k2, v2 in y.items():
                if expr[i] == '+':
                    z = v1 + v2
                elif expr[i] == '-':
                    z = v1 - v2
                elif expr[i] == '*':
                    z = v1 * v2
                elif expr[i] == '/':
                    if v2 == 0:
                        continue
                    z = v1 / v2
                else:
                    raise Exception('unknown operator: ' + expr[i])

                k = k1 if k1.isnumeric() else '(' + k1 + ')'
                m = k2 if k2.isnumeric() else '(' + k2 + ')'
                n = k + expr[i] + m

                res[n] = z

        return res


def solve_24game(a: int, b: int, c: int, d: int):  # numbers preferably between 1-13 inclusive
    result = {}
    for c in itertools.permutations([str(a), str(b), str(c), str(d)]):
        for op in itertools.product(*['+-*/'] * 3):
            expr = c[0] + op[0] + c[1] + op[1] + c[2] + op[2] + c[3]
            x = exp_eval(expr)

            for k, v in x.items():
                if v == 24:
                    result[k] = v

    return result


print(solve_24game(10, 10, 4, 4))
print('-' * 80)
print(solve_24game(5, 5, 5, 1))
print('-' * 80)
print(solve_24game(6, 1, 3, 4))
print('-' * 80)
print(solve_24game(7, 7, 3, 3))
print('-' * 80)
print(solve_24game(1, 5, 7, 10))
