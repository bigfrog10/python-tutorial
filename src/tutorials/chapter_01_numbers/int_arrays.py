from typing import List
import math
import collections
import itertools


# LC287. Find the Duplicate Number  Floyd's Tortoise and Hare (Cycle Detection)
def findDuplicate(self, nums: List[int]) -> int:  # use +/- sing, O(n) time and O(1) space
    for num in nums:
        if nums[ abs(num) ] < 0:
            ans = abs(num)
            break
        nums[ abs(num) ] = -nums[ abs(num) ]
    # restore nums
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    return ans


# LC1295. Find Numbers with Even Number of Digits
def findNumbers(self, nums: List[int]) -> int:
    return sum(~len(str(x)) & 1 for x in nums)
def findNumbers1(self, nums: List[int]) -> int:
    return sum(int(math.log10(n)) % 2 for n in nums)  # log10(n) + 1 is the # of digits.


# LC238. Product of Array Except Self, top100
def productExceptSelf(self, nums: List[int]) -> List[int]:
    length = len(nums)
    ret = [0] * length
    ret[0] = 1
    for i in range(1, length): ret[i] = nums[i - 1] * ret[i - 1]
    tmp = 1
    for i in reversed(range(length)):
        ret[i] = ret[i] * tmp
        tmp *= nums[i]
    return ret


# LC41. First Missing Positive, top100
def firstMissingPositive(self, nums: List[int]) -> int:
    # missing is in [1 ..., len(nums)] and we care only positives
    positives = set(x for x in nums if 0 < x <= len(nums))
    n = len(positives)
    if n == 0: return 1 # if all nums are 0, then next is 1 and 1 is missing
    for i in range(1, n+1): # this order honors smallest missing
        if i not in positives: return i
    return n + 1


# LC846. Hand of Straights
def isNStraightHand(self, hand: List[int], W: int) -> bool:
    if len(hand) % W != 0: return False
    c = collections.Counter(hand)
    for i in sorted(c): # O(nlogn), order is no concern.
        if c[i] == 0: continue
        cnt = c[i]
        for j in range(W):
            c[i + j] -= cnt
            if c[i + j] < 0: return False
    return True


# LC189. Rotate Array
def rotate(self, nums: List[int], k: int) -> None:
    k = k % len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]


# LC66. Plus One
def plusOne(self, digits: List[int]) -> List[int]:
    for i in reversed(range(len(digits))):
        if digits[i] == 9: digits[i] = 0
        else:
            digits[i] += 1
            return digits # when we don't have carry
    return [1] + digits # when we have carry


# LC268. Missing Number
def missingNumber(self, nums: List[int]) -> int:
    s = sum(nums)
    n = len(nums)
    t = n * (n + 1) // 2
    return t - s
def missingNumber(self, nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


# LC679. 24 Game
def judgePoint24(self, nums: List[int]) -> bool:
    if len(nums) == 1:
        return math.isclose(nums[0], 24)
    return any(self.judgePoint24([x] + rest)
               for a, b, *rest in itertools.permutations(nums)
               for x in {a+b, a-b, a*b, b and a/b})


# LC349. Intersection of Two Arrays
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set2 & set1)


# LC448. Find All Numbers Disappeared in an Array
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])
    print(nums)
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# LC228. Summary Ranges
def summaryRanges(self, nums: List[int]) -> List[str]:
    ans = []
    pointer = 0
    for i, n in enumerate(nums):
        if i == len(nums) - 1 or nums[i+1] - nums[i] > 1:
            ans.append(str(nums[pointer]) + '->' + str(n) if nums[pointer] != n else str(n))
            pointer = i+1
    return ans


# LC315. Count of Smaller Numbers After Self  # BBG hard
import sortedcontainers
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_arr = sortedcontainers.SortedList() # O(nlogn)
        rst = []
        for num in nums[::-1]:
            idx = sorted_arr.bisect_left(num)  # this is O(logn)
            rst.append(idx)
            sorted_arr.add(num)  # this is O(logn)
        return rst[::-1]


# LC493. Reverse Pairs
from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, arr: List[int]) -> int:
        brr = SortedList(arr)
        count = 0
        # anything smaller before larger is discarded.
        for i in range(len(arr)): # O(nlogn), loop is n, logn inside
            brr.discard(arr[i])
            k = brr.bisect_left((arr[i]+1)//2)
            count += k
        return count


# LC1470. Shuffle the Array
def shuffle(self, nums: List[int], n: int) -> List[int]:
    res = [0] * (2*n)
    res[::2] = nums[:n]
    res[1::2] = nums[n:]
    return res
def shuffle(self, nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res


# LC412. Fizz Buzz
def fizzBuzz(self, n: int) -> List[str]:
    res = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0: res.append('FizzBuzz')
        elif i % 3 == 0: res.append('Fizz')
        elif i % 5 == 0: res.append('Buzz')
        else: res.append(str(i))
    return res


# LC697. Degree of an Array
def findShortestSubArray(self, nums: List[int]) -> int:
    dt = collections.defaultdict(list)
    for i, v in enumerate(nums): dt[v].append(i)
    degree = max(len(v) for v in dt.values())
    return min(v[-1] - v[0] + 1 for v in dt.values() if len(v) == degree)
def findShortestSubArray(self, nums: List[int]) -> int:
    left = right = 0
    degree = max(collections.Counter(nums).values())
    cnts = collections.Counter()
    res = float('inf')
    while right < len(nums):
        cnts[nums[right]] += 1
        maxc = max(cnts.values())
        while maxc == degree:
            res = min(res, right - left + 1)
            cnts[nums[left]] -= 1
            left += 1
            maxc = max(cnts.values())
        right += 1
    return res