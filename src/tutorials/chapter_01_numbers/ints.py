# LC7. Reverse Integer
def reverse(self, x: int) -> int:
    pos = x if x >= 0 else -x
    res = 0
    while pos > 0:
        res = res * 10 + pos % 10
        if res > 2**31-1:
            return 0
        pos //= 10
    return res if x > 0 else -res


# LC9. Palindrome Number
def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x > 0 and x % 10 == 0): return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x = x // 10
    return x == rev or x == rev // 10


# LC50. Pow(x, n)
def myPow(self, x: float, n: int) -> float:  # minimize multiplications
    if n < 0:
        n = -n
        x = 1 / x
    ret = 1
    f = x
    while n > 0:
        if n % 2 != 0: ret *= f
        f = f * f
        n = n // 2
    return ret


# LC69. Sqrt(x)
def mySqrt(self, x: int) -> int:
    left, right = 0, (x + 1) // 2  # to handle x = 1 we need + 1
    while left <= right:
        middle = left + (right - left) // 2
        sqr = middle * middle
        if sqr > x: right = middle - 1  # middle is tested in sqr
        elif sqr < x: left = middle + 1
        else: return middle
    return right  # close to sqrt(x)


# LC279. Perfect Squares, top100. minimal -> BFS
def numSquares(self, n):
    square_nums = [i * i for i in range(1, int(n**0.5)+1)] # list of square numbers that are less than `n`
    queue, level = {n}, 0
    while queue:  # BFS
        level += 1
        next_queue = set()
        for remainder in queue:  # construct the queue for the next level
            for square_num in square_nums:
                if remainder == square_num:
                    return level  # find the node!
                elif remainder < square_num:
                    break  # overed, no need to go further, cut branches
                else: next_queue.add(remainder - square_num)
        queue = next_queue
    return level


# LC202. Happy Number
def isHappy(self, n: int) -> bool:
    if n == 1: return True  # O(logN)
    history = set()
    while n not in history and n != 1:
        history.add(n)
        square_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            square_sum += digit * digit
        n = square_sum
    return n == 1

