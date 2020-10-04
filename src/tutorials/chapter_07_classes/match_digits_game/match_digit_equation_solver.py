# https://blog.csdn.net/iteye_15612/article/details/81725858

import tutorials.chapter_07_classes.match_digits_game.match_digits as match_digits

# for all digits
#     for all matches
#         take this match and move it to somewhere
#             so that we have two new valid numbers
#         check whether the equality holds
#             if it holds, send out results.


def _index_to_digit(s: str):
    ret = {}
    for i in range(len(s)):
        if s[i].isnumeric():
            ret[i] = match_digits.MatchDigit(int(s[i]))

    return ret


def solve(s: str):
    ret = []
    if _check_result(s):
        ret.append(s)

    r = _index_to_digit(s)

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

                    if _check_result(s1):
                        ret.append(s1)
                        print('input expr: ' + s + ' new expr: ' + s1)
                        print('    move match ' + match.name + ' in digit ' +
                              str(md.digit()) + "(index: " + str(pos) +
                              ') to the position ' + match1.name + ' in digit '
                              + str(md1.digit()) + "(index: " + str(pos1) + ')')

    return ret


def _check_result(s1):
    ind = s1.index('=')
    left = s1[:ind]
    right = s1[ind + 1:]

    lv = eval(left)
    rv = eval(right)
    return lv == rv


print(solve("9 + 5 = 9"))  # ['3 + 6 = 9', '3 + 5 = 8']
print(solve("19 + 5 = 19"))  # ['13 + 6 = 19', '13 + 5 = 18']
print(solve("2 * (9 + 5) = 18"))  # ['2 * (3 + 6) = 18']
print(solve("4 + 5 = 9"))  # ['4 + 5 = 9']
