from typing import List
from collections import defaultdict


# LC64. Minimum Path Sum
def minPathSum(self, grid: List[List[int]]) -> int:
    M, N = len(grid), len(grid[0])
    dp = [0] + [float('inf')] * (N-1)
    for i in range(M):
        dp[0] = dp[0] + grid[i][0]
        for j in range(1, N):
            dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
    return dp[-1]

# LC73. Set Matrix Zeroes
def setZeroes(self, matrix):
    m, n = len(matrix), len(matrix[0])
    firstRowHasZero = not all(matrix[0])  # First row has zero?
    for i in range(1, m): # Use first row/column as marker, scan the matrix
        for j in range(n):
            if matrix[i][j] == 0: matrix[0][j] = matrix[i][0] = 0
    for i in range(1, m): # Set the zeros
        for j in range(n - 1, -1, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0
    # Set the zeros for the first row
    if firstRowHasZero: matrix[0] = [0] * n

# LC54. Spiral Matrix, top100
def spiralOrder(self, matrix):
    res = []
    while matrix:
        res.extend(matrix.pop(0))
        # zip rows to columns, flattern each column, reverse order
        matrix = [*zip(*matrix)][::-1]
    return res
# [[1,2,3],[4,5,6],[7,8,9]] ->  [(6, 9), (5, 8), (4, 7)] -.  [(8, 7), (5, 4)]
# -> [(4,), (5,)] -> [(5,)]


# LC48. Rotate Image
def rotate(self, A):
    A[:] = zip(*A[::-1])


# LC498. Diagonal Traverse
def findDiagonalOrder(self, matrix):
    if not matrix: return []
    m, n = len(matrix), len(matrix[0])
    ret = []
    row = col = 0
    for _ in range(m * n):
        ret.append(matrix[row][col])
        if (row + col) % 2 == 0: # start from row, move up
            if col == n - 1: row += 1 # hit right side for next sum = row + col
            elif row == 0: col += 1
            else:
                row -= 1
                col += 1
        else: # start from col, move down
            if row == m - 1: col += 1 # hit bottom for next sum = row + col
            elif col == 0: row += 1
            else:
                row += 1
                col -= 1
    return ret


# LC1424. Diagonal Traverse II
def findDiagonalOrder(self, A):
    res = defaultdict(list)
    for i, r in enumerate(A):
        for j, a in enumerate(r): res[i + j].append(a)
    return [a for _, r in res.items() for a in reversed(r)]