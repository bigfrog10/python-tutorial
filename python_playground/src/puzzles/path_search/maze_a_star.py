# A* search is different from dijkstra in the heuristics f = g + h. dijkstra
# has only g and A* has g + h, where h is an estimate to goal.
import heapq
import copy

EMPTY = 0
WALL = 1
START = 2
END = 3
VISITED = 4


class Move:  # we need this for the linked list and cost func, a tuple is less readable
    def __init__(self, position, parent: 'Move' = None):
        self.position = position
        self.parent = parent

        # cost function f, this is different from dijkstra
        self.g = 0 if parent is None else parent.g + 1
        self.h = 0
        self.f = 0

    def __lt__(self, other):  # used by heapq
        return self.f < other.f

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__ and \
               self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __repr__(self):
        return f"({self.position}, {self.f}, {self.g}, {self.h})"


# these 4 are duplicated
def _find(maze, state):
    for row_num, row in enumerate(maze):
        for col_num, v in enumerate(row):
            if v == state:
                return Move((row_num, col_num))

    raise ValueError(f'{state} is not found!')


def _maze_info(maze):
    maze_length, maze_width = len(maze), len(maze[0])
    print(f'maze size: length={maze_length} width={maze_width}')

    start = _find(maze, START)
    print(f'start: ({start.position[0]}, {start.position[1]})')

    end = _find(maze, END)
    print(f'end: ({end.position[0]}, {end.position[1]})')

    return start, end


def _is_shorter(locations, location):
    for loc in locations:
        if loc == location and loc.f <= location.f:
            return False
    return True


def _solution_layout(move, start, maze):
    steps = move.g
    maze_c = copy.deepcopy(maze)
    while move != start:
        maze_c[move.position[0]][move.position[1]] = VISITED
        move = move.parent

    return maze_c, steps


def _heuristics(node, end):  # here we use Manhattan distance, don't overestimate
    return abs(node.position[0] - end.position[0]) + abs(node.position[1] - end.position[1])


def a_star_search(maze):
    start, end = _maze_info(maze)

    locations = []
    visited = set()

    heapq.heappush(locations, start)
    while locations:
        location = heapq.heappop(locations)  # smallest by the order
        visited.add(location.position)

        x = location.position[0]
        y = location.position[1]
        print(f"location=({x}, {y}), size={len(locations)}")

        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for n in neighbors:
            # this is not obvious, if n = (-1, 1), maze[-1] is on the other side
            if n not in visited and maze[n[0]][n[1]] == EMPTY:
                move = Move(n, location)
                move.h = _heuristics(move, end)  # new code here
                move.f = move.g + move.h
                if _is_shorter(locations, move):  # update with shorter distance
                    heapq.heappush(locations, move)
            elif maze[n[0]][n[1]] == END:
                print(f'visited: {len(visited)}')
                return _solution_layout(Move(n, location), start, maze)

    return None


def _test():
    maze1 = [
        [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    solution = a_star_search(maze1)

    print(f'steps={solution[1]}')
    for r in solution[0]:
        print(r)


if __name__ == '__main__':
    import cProfile
    cProfile.run('_test()')
    # saves a few visited locations


# http://bryukh.com/labyrinth-algorithms/
