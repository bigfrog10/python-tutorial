import copy

import puzzles.backtracking.stack_queue_impl as collections

# the maze is a double array of 0's and 1's where 1's are walls and 0's are
#     paths
# the maze is a rectangle
# look for entries and exits in the following way:
#     search in the order of top, left, right, bottom
#     assume first 0 on the border is the only entrance and the rest of the 0's
#         are exits

EMPTY = 0  # not wall nor visited
VISITED = 2


def find_entrance(maze):
    entrance = None
    exits = []

    top_wall = maze[0]
    width = len(top_wall)
    for index, value in enumerate(top_wall):
        if value == 0:
            if entrance is None:
                entrance = (0, index)
            else:
                exits.append((0, index))

    for index, row in enumerate(maze1):
        if row[0] == 0:
            if entrance is None:
                entrance = (index, 0)
            else:
                exits.append((index, 0))

    for index, row in enumerate(maze1):
        if row[-1] == 0:
            if entrance is None:
                entrance = (index, width - 1)
            else:
                exits.append((index, width - 1))

    bottom_wall = maze[-1]
    length = len(maze)
    for index, value in enumerate(bottom_wall):
        if value == 0:
            if entrance is None:
                entrance = (length - 1, index)
            else:
                exits.append((length - 1, index))

    if not entrance or not exits:
        raise ValueError("need entrance and exit: entrance={}, exits={}".format(entrance, exits))

    return entrance, exits


def check_exit(x, y, exits):
    for position in exits:
        if (x, y) == position:
            return True

    return False


def solve(maze):
    maze_length, maze_width = len(maze), len(maze[0])
    print("maze shape: len={}, wid={}".format(maze_length, maze_width))
    entrance, exits = find_entrance(maze)
    print("entrance={}, exits={}".format(entrance, exits))

    results = []
    stack = collections.MyStack()
    stack.push((maze, entrance))
    while stack:
        item = stack.pop()
        maze1 = item[0]
        x, y = item[1]
        if check_exit(x, y, exits):
            maze1[x][y] = VISITED
            results.append(maze1)
            continue

        x1 = x + 1
        if maze1[x1][y] == EMPTY:
            maze2 = copy.deepcopy(maze1)
            maze2[x][y] = VISITED
            stack.push((maze2, (x1, y)))

        x1 = x - 1
        if maze1[x1][y] == EMPTY:
            maze2 = copy.deepcopy(maze1)
            maze2[x][y] = VISITED
            stack.push((maze2, (x1, y)))

        y1 = y + 1
        if maze1[x][y1] == EMPTY:
            maze2 = copy.deepcopy(maze1)
            maze2[x][y] = VISITED
            stack.push((maze2, (x, y1)))

        y1 = y - 1
        if maze1[x][y1] == EMPTY:
            maze2 = copy.deepcopy(maze1)
            maze2[x][y] = VISITED
            stack.push((maze2, (x, y1)))

    return results


maze1 = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]
solutions = solve(maze1)
for s in solutions:
    for row in s:
        print(row)
    print('-' * 80)
