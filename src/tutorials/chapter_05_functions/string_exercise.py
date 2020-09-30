import difflib
import functools


# https://en.wikipedia.org/wiki/Longest_common_substring_problem
def lcs(s1: str, s2: str) -> str:
    sm = difflib.SequenceMatcher(None, s1, s2, autojunk=False)
    match = sm.find_longest_match(0, len(s1), 0, len(s2))
    return s1[match.a:match.a+match.size]


def lcsm(s: list) -> str:
    return functools.reduce(lcs, s)
