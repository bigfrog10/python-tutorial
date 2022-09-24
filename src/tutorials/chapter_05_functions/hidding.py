# 人的视力不能看到掩体之后的事物，在一场战争中，我们希望对方尽可能的低估我方的战斗力这样才能出其不意。

# 某个军事参谋效仿孙膑，把某些小规模队隐藏在大规模部队中，这样，就使得军队数量看起来变少了。已知，
# 如果某部队A的人数小于等于另一支部队B人数的1/3， 则可以将A藏于B中，且不被人发现。不支持嵌套，
# 例如A小于B的三分之一，可将A藏于B, 如果又存在B是C的三分之一，不可再将B藏于C。

# 现在已知我方共有n支部队，且知道每支部队的人数，请问，在最优方案下，我们暴露给敌人的部队数量有几支。
# If we have 15, 9, 4, 2, if we hide 2 under 15, then we cannot hide 4 under 9.
# So we need to hide largest possible under largest.
# However, if we have 18, 6, 5, 2, if we hide 6 under 18, then we cannot hide 2 under 6.
# So we need to scan troops with fewer soldiers first and hide it within another of smallest size possible
# assume that we can only hide one number under another.
def hide(int_arr):
    arr = sorted(int_arr)
    size = len(arr)

    flags = [-1] * size
    for i in range(size):
        v = arr[i]
        c = [ind+i+1 for ind, x in enumerate(arr[i+1:]) if flags[ind] == -1 and x >= v * 3]
        if c:
            flags[c[0]] = i

    return list(zip(arr, flags))


print(hide([2, 9, 4, 15]))
print(hide([2, 5, 6, 18]))

# use binary search to replace linear search
from bisect import bisect_left
def hide2(int_arr):
    arr = sorted(int_arr)
    size = len(arr)

    flags = [-1] * size
    for i in range(size):
        v = arr[i]*3
        p = bisect_left(arr, v, lo=i+1)
        if p < size and arr[p] != v:
            p += 1
        if p < size:
            flags[p] = i

    return list(zip(arr, flags)) 

print(hide2([2, 5, 6, 18]))

# above optimization is to minimize the total number of troops exposed

# Further open question: 
# if we want to minimize the total number of soldiers exposed, where assume 
# the number of soldiers are hidden if and only if the troop is nested
# i.e. 
# If we have 15, 9, 4, 2, if we hide 4 under 15, 2 under 9, exposed soldiers are 24=18+9
# If we have 18, 6, 5, 2, 
#   if we hide 6 under 18, exposed soldiers are 25=18+5+2
#   if we hide 2 under 6 and 5 under 18, exposed soldiers are 24=18+6
# If we have 18, 6, 3, 2, 
#   if we hide 6 under 18, exposed soldiers are 23=18+3+2
#   if we hide 2 under 6 and 5 under 18, exposed soldiers are 24=18+6
# it seems no greedy algorithm for this