import itertools
import pprint


# a and d can't be 1, otherwise e and h are 10, not digits 0-9
# if b = 1, then from f's expression: c = 10 / f + (a-1)(d-1).
# plug this into g: g = f * c = 10 + f(a-1)(d-1), so g is not digit 0-9.
# so non of a, b, c, d can be 1.
# since abcd and efgh are symmetric, efgh can't be 1 either.
def calc_next_4(a, b, c, d):
    deno = b * c - (a - 1) * (d - 1)
    if deno == 0:  # denominator can't be zero
        return None

    # see formula picture
    e = 10 - 10 * (d - 1) / deno
    f = 10 * b / deno
    g = 10 * c / deno
    h = 10 - 10 * (a - 1) / deno

    return e, f, g, h


def verify(sol):
    a, b, c, d, e, f, g, h = sol
    assert a * e + b * g == 10 * a + e
    assert a * f + b * h == 10 * b + f
    assert c * e + d * g == 10 * c + g
    assert c * f + d * h == 10 * d + h


def search():
    ret = []
    # instead of 4 for loops, use cartesian product
    for a, b, c, d in itertools.product(range(0, 10), range(0, 10), range(0, 10), range(0, 10)):
        res = calc_next_4(a, b, c, d)
        if res is None:
            continue

        e, f, g, h = res
        # check whether they are digits 0-9
        if e.is_integer() and f.is_integer() and g.is_integer() and h.is_integer():
            if 0 <= e <= 9 and 0 <= f <= 9 and 0 <= g <= 9 and 0 <= h <= 9:
                sol = (a, b, c, d, int(e), int(f), int(g), int(h))
                verify(sol)
                ret.append(sol)

    print(len(ret))  # 100
    pprint.pprint(ret)
    return ret


search()
