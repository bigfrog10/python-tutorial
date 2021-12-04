from typing import List


# LC200. Number of Islands, top100
from itertools import product
def numIslands(self, board: List[List[str]]) -> int:
    if not board: return 0 # O(MN)
    rows, cols = len(board), len(board[0])
    seen = set()
    def dfs(i, j):
        seen.add((i, j))
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and board[i][j] == '1' and (x, y) not in seen:
                dfs(x, y)
    count = 0
    for i, j in product(range(rows), range(cols)):
        if board[i][j] == '1' and (i, j) not in seen:
            count += 1
            dfs(i, j)
    return count

# LC694. Number of Distinct Islands - transformations
def numDistinctIslands(self, grid: List[List[int]]) -> int:
    if not grid: return 0 # close to # 200
    n, m = len(grid), len(grid[0])
    seen = set()
    def explore(r, c, xo, yo, shape):
        if 0 <= r < n and 0 <= c < m and (r, c) not in seen and grid[r][c] != 0:
            seen.add((r, c))
            shape.add((r-xo, c-yo))
            for x, y in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                explore(x, y, xo, yo, shape)
    shapes = set()
    for i, j in product(range(n), range(m)):
        if grid[i][j] == 1 and (i, j) not in seen:
            shape = set()  # collection all island coordinates
            explore(i, j, i, j, shape)
            if shape: shapes.add(frozenset(shape))  # hash
    return len(shapes)


a = [4, 5, 6]
for i in range(len(a)):
    print(a[i])

b = [[1, 2], [3, 4]]
for i in range(len(b)):
    temp = b[i]
    for j in range(len(temp)):
        print(temp[j])
