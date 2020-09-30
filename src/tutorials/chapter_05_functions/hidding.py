# 人的视力不能看到掩体之后的事物，在一场战争中，我们希望对方尽可能的低估我方的战斗力这样才能出其不意。

# 某个军事参谋效仿孙膑，把某些小规模队隐藏在大规模部队中，这样，就使得军队数量看起来变少了。已知，
# 如果某部队A的人数小于等于另一支部队B人数的1/3， 则可以将A藏于B中，且不被人发现。不支持嵌套，
# 例如A小于B的三分之一，可将A藏于B, 如果又存在B是C的三分之一，不可再将B藏于C。

# 现在已知我方共有n支部队，且知道每支部队的人数，请问，在最优方案下，我们暴露给敌人的部队数量有几支。
# If we have 15, 9, 4, 2, if we hide 2 under 15, then we can hide 4 under 9.
# So we need to hide largest possible under largest.
# assume that we can only hide one number under another.
def hide(int_arr):
    arr = sorted(int_arr, reverse=True)
    size = len(arr)

    flags = [-1] * size
    for i in range(size):
        v = arr[i]
        c = [ind+i+1 for ind, x in enumerate(arr[i+1:]) if flags[ind] == -1 and x <= v / 3]
        if c:
            flags[c[0]] = i

    return list(zip(arr, flags))


print(hide([2, 9, 4, 15]))
