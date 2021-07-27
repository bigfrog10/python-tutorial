digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n: int, base: int):
    res = ""
    while n >= base:  # iterative approach
        n, remainder = divmod(n, base)
        res += str(digits[remainder])
    if n > 0:
        res += str(digits[n])
    return res[::-1]


print(int(to_base(5, 2), 2))
print(int(to_base(653, 9), 9))
print(int(to_base(43794, 16), 16))
print(to_base(43794, 16))


def to_base1(n: int, base: int):
    def rec(n, base):  # recursive approach
        if n < base:
            return digits[n]

        q, r = divmod(n, base)
        return digits[r] + rec(q, base)

    return rec(n, base)[::-1]


print(int(to_base1(5, 2), 2))
print(int(to_base1(653, 9), 9))
print(int(to_base1(43794, 16), 16))


# LC371. Sum of Two Integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a


# LC43. Multiply Strings
class Solution1:
    def multiply(self, num1: str, num2: str) -> str:
        x, y = int(num1), int(num2)
        res = count = 0
        while x:
            if x & 1 == 1:
                res += y << count
            count += 1
            x = x >> 1

        return str(res)


# LC29. Divide Two Integers
class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        a, b = abs(dividend), abs(divisor)
        res = 0
        for x in range(32)[::-1]:
            if (a >> x) >= b:
                res += 1 << x
                a -= b << x
        return res if (dividend > 0) == (divisor > 0) else -res


# LC191. Number of 1 Bits
def hammingWeight(self, n: int) -> int:
    sum = 0
    while n:
        sum += 1
        n &= (n - 1)  # n & (n-1) erase least significant bit
    return sum


# LC868. Binary Gap  - 2 pointers
def binaryGap(self, n: int) -> int:
    res, last, step = 0, -1, 0
    while n:
        if n & 1: # have 1 in this bit
            if last >= 0: res = max(res, step - last)
            last = step
        n >>= 1
        step += 1
    return res


# LC190. Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for shift in range(31, -1, -1):
            ret += (n & 1) << shift  # & --> remainder, shift --> reverse
            n >>= 1  # quotient
        return ret
