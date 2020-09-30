# Dynamic Programming

# If we have only 1 ball, then we have to try each floor from bottom up.
#
# If we have 2 balls, then we can try on 14th, (14 + 13)th, (14 + 13 + 12)
# if not broken. If broken, then we try 13 times on 1st, 14th, 27th going up.
#
# If we have n balls, let W(n, k) is the minimal number of trials to identify
# the critical floor for n glass balls and k floors. Then
#     W(n, 1) = 1 for all n > 0, assuming there has to have a critical floor.
#     W(1, k) = k for all k >= 0, in worst case we have to try every floor
#                                 from bottom up since there is only 1 ball.
# The recursion is:
#     W(n, k) = 1 + min{ max(W(n-1, x-1), W(n, k-x) | x = 1, 2, ..., k}
# Here adding 1 is because we did a trial.
# When we try the drop on floor x:
#     if it breaks, then we have W(n-1, x-1)
#     if it doesn't break, then we have W(n, k-x), the floors above.
import functools


# Without this cache, it's super slow for large n and k.
@functools.lru_cache(maxsize=None)
def min_drops(glass_balls: int, floors: int) -> int:
    # print(f'glass balls: {glass_balls}, floors: {floors}')

    if floors == 0 or floors == 1:
        return floors

    if glass_balls == 1:
        return floors

    ret = floors * 2  # anything unreasonably large
    for f in range(1, floors):
        broken = min_drops(glass_balls - 1, f - 1)
        unbroken = min_drops(glass_balls, floors - f)

        min_trial = max(broken, unbroken)
        ret = min(min_trial, ret)

    return ret + 1  # we drop once


print(min_drops(2, 7))  # 4

# without decorator, this is very slow
print(min_drops(2, 30))  # 8
print(min_drops(2, 100))  # 14
print(min_drops(3, 30))  # 6
print(min_drops(4, 30))  # 5
print(min_drops(5, 30))  # 5
print(min_drops(6, 30))  # 5
print(min_drops(7, 30))  # 5
