def cap_count(string: str):
    """Given a string s, return the count of capital letters"""
    return sum(1 for char in string if char.isupper())


print(cap_count('I do not like them, Sam-I-Am.'))  # 4


# ##############################################################################
def match_rate(str1: str, str2: str):
    """given 2 strings, return percentage of matched chars"""
    return sum(1 for c1, c2 in zip(str1, str2) if c1 == c2) / len(str1)


print(match_rate("I don't like Ham. Sam I am.", "I don't like Sam. Ham I am."))


# ##############################################################################
def pascal_triangle(level: int):
    """For a given integer, say 4, the pascal triangle is
                    1
                   1 1
                  1 2 1
                 1 3 3 1
                1 4 6 4 1
    First row is row 0. Every row starts and ends with 1. From row 2, every
    middle number is the sum of 2 shoulders. Each row is the coefficients of
    terms expanded from (x + y) ^ level, so it's called binomial coefficients.
    This function returns this formation, in terms of list of ints.
    https://medium.com/i-math/top-10-secrets-of-pascals-triangle-6012ba9c5e23
    """
    row = [1]  # top row, row 0
    while True:
        yield row
        size = len(row)
        if size > level:
            break

        row = [1] + [row[i] + row[i+1] for i in range(size - 1)] + [1]


for r in pascal_triangle(22):
    print(r)


def print_pt(level: int, pt_generator):
    # the number width is not even. So we make it even.
    # we scale width to be the largest number width. This is our unit.
    # Then layout numbers by this unit
    num_width = (level - 1) // 4 + 1  # 1, 5, 9, 13 ... are the jumps on the number of digits.
    space = ' ' * num_width  # this is our separator between numbers
    num_rows = level + 1
    num_slots = 2 * num_rows - 1  # how many slots in a line, including spaces
    for index, row in enumerate(pt_generator):
        # no skip on last row
        skip = (num_slots - 2 * len(row) + 1) // 2 if index < level else 0
        line = space * skip
        for n in row:
            line += str(n).center(num_width) + space  # str.ljust/rjust/center
        print(line)


print_pt(15, pascal_triangle(15))


# ##############################################################################
def josephus_circle(size: int, step: int):
    """
    There are n(n=size) people standing in a circle waiting to be called.
    Starting from first person(index 1 here), calling proceeds around the
    circle in fixed direction, skipping m-1(m=step) people(mth person called).
    The following recursion holds:
    https://medium.com/@rrfd/explaining-the-josephus-algorithm-11d0c02e7212
        josephus_circle(1, m) = 1  # if there is one person, he survives.
        josephus_circle(n, m) = (josephus_circle(n-1, m) + m - 1) % n + 1
    But we are going follow the process.
    """
    import itertools as it
    people = list(range(1, size + 1))  # people
    jc = it.cycle(people)
    while len(people) > 1:
        p = None
        for i in range(step):  # skip step -1 people, get step-th person
            p = next(jc)

        # form the new list from items after p plus before p
        p_ind = people.index(p)
        people = people[p_ind + 1:] + people[: p_ind]
        jc = it.cycle(people)

    return people[0]


print(josephus_circle(5, 2))  # 3
print(josephus_circle(7, 3))  # 4
print(josephus_circle(10, 4))  # 5
print(josephus_circle(14, 2))  # 13
print(josephus_circle(41, 3))  # 31


# ##############################################################################
def bubble_sort(value_list):
    print(value_list)
    size = len(value_list)
    for i in range(size):
        # bubble larger items to the right, all the way until it can't
        for j in range(size - i - 1):  # don't need to beyond, since they are good.
            if value_list[j + 1] < value_list[j]:
                value_list[j + 1], value_list[j] = value_list[j], value_list[j + 1]
                print(value_list)
    return value_list


bubble_sort([5, 1, 4, 2, 8])


# ##############################################################################
def binary_search(ascending_list, value):
    def bs(asc_list, val, low, high):
        if low > high:
            return -1  # not found

        mid = (low + high) // 2
        if asc_list[mid] == val:
            return mid
        elif asc_list[mid] > val:
            return bs(asc_list, val, low, mid - 1)
        else:
            return bs(asc_list, val, mid + 1, high)

    return bs(ascending_list, value, 0, len(ascending_list) - 1)


print(binary_search([2, 5, 9, 17, 44], 2))
print(binary_search([2, 5, 9, 17, 44], 5))
print(binary_search([2, 5, 9, 17, 44], 9))
print(binary_search([2, 5, 9, 17, 44], 17))
print(binary_search([2, 5, 9, 17, 44], 44))
print(binary_search([2, 5, 9, 17, 44], 50))


# ##############################################################################
def estimate_pi(num_tesets):
    import random
    in_cycles = in_squares = 0

    for i in range(num_tesets):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        d = x * x + y * y

        in_squares += 1
        if d <= 1:
            in_cycles += 1

    return 4 * in_cycles / in_squares


print(estimate_pi(10 ** 5))
import math
print(1 / math.sqrt(10 ** 5))  # error bound within a factor


# ##############################################################################
def monty_hall():
    """https://en.wikipedia.org/wiki/Monty_Hall_problem
       https://towardsdatascience.com/answering-monty-hall-problem-with-monte-carlo-6c6069e39bfe
    """
    from random import shuffle, choice

    GOAT = 0
    CAR = 1
    gifts = [CAR, GOAT, GOAT]
    doors = [0, 1, 2]

    shuffle(gifts)
    door_selected = choice(doors)

    # These are not needed for staying.
    # goat_not_selected_doors = [d for d in doors if d != door_selected and gifts[d] == GOAT]
    # door_opened = choice(goat_not_selected_doors)

    no_switch_win = gifts[door_selected] == CAR
    return no_switch_win


def mh_monte_carlo(num_tests):
    switch_wins = no_switch_wins = 0
    for i in range(num_tests):
        no_switch_win = monty_hall()
        switch_wins += not no_switch_win  # True is 1 and False is 0
        no_switch_wins += no_switch_win

    return switch_wins/num_tests, no_switch_wins/num_tests


sw, nsw = mh_monte_carlo(10 ** 4)
print(f'win/switch={sw:.2%}, win/stay={nsw:.2%}')  # close to 2/3, 1/3
# The logic is the following:
# When we pick a door initial, there is only 1/3 chance it has a car. So this
# means the other 2 doors together has 2/3 of chances. If one of those 2 doors
# reveals no car, then the other one has 2/3 chance to win. So we should switch
# this simulation is very close to 2/3 on switch.
print(1 / math.sqrt(10 ** 4))  # rough error bound
