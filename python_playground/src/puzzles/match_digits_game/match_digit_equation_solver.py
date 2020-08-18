# for all digits
#     for all matches
#         take this match and move it to somewhere
#             so that we have two new valid numbers
#         check whether the equality holds
#             if it holds, send out results.
import puzzles.match_digits_game.match_digits as match_digits


def f(s: str):
    ret = {}
    for i in range(len(s)):
        if s[i].isnumeric():
            ret[i] = match_digits.MatchDigit(int(s[i]))

    return ret


def g(s: str, r: dict):
    ret = []
    for pos, md in r.items():
        for match in md.all_matches():
            new_md = md.remove_match(match)
            if new_md is None:
                continue

            for pos1, md1 in r.items():
                for match1 in match_digits.MatchPosition:
                    new_md1 = md1.set_match(match1)
                    if new_md1 is None:
                        continue

                    s1 = s[:pos] + str(new_md.digit()) + s[pos + 1:]
                    s1 = s1[:pos1] + str(new_md1.digit()) + s[pos1 + 1:]

                    ind = s1.index('=')
                    left = s1[:ind]
                    right = s1[ind + 1:]

                    lv = eval(left)
                    rv = eval(right)
                    if lv == rv:
                        ret.append(s1)

    return ret


def solver(equation: str):
    pos_digits = f(equation)
    solutions = g(equation, pos_digits)
    print(solutions)


# solver("9 + 5 = 9")
# solver("19 + 5 = 19")
solver("2 * (9 + 5) = 18")