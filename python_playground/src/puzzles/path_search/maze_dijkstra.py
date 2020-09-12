import heapq
import copy
"""
This implementation is different from other maze solution 
(puzzles.backtracking.maze).
We use Move to link to previous move, so no copying of the maze.
"""

EMPTY = 0
WALL = 1
START = 2
END = 3
VISITED = 4


class Move:  # we need this for the linked list and cost func, a tuple is less readable
    def __init__(self, position, parent: 'Move' = None):
        self.position = position
        self.parent = parent

        # cost function f
        self.dist = 0 if parent is None else parent.dist + 1

    def __lt__(self, other):  # used by heapq
        return self.dist < other.dist

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__ and \
               self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __repr__(self):
        return f"({self.position}, {self.dist})"


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
        if loc == location and loc.dist <= location.dist:
            return False
    return True


def _solution_layout(move, start, maze):
    steps = move.dist
    maze_c = copy.deepcopy(maze)
    while move != start:
        maze_c[move.position[0]][move.position[1]] = VISITED
        move = move.parent

    return maze_c, steps


# we assume that there only one entry and one exit. Multi-entry or exit cases
# can be converted into this case.
def dijkstra_search(maze):
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

    solution = dijkstra_search(maze1)

    print(f'steps={solution[1]}')
    for r in solution[0]:
        print(r)


if __name__ == '__main__':
    import cProfile
    cProfile.run('_test()')


# References:
# https://www.annytab.com/dijkstras-search-algorithm-in-python/
# https://prog.world/python-learning-project-dijkstra-opencv-and-ui-algorithm-part-1/
# http://blog.labyrenth.com/prog/2017/07/26/PROG_Maze2D.html
# https://pythonawesome.com/a-maze-generator-and-solver-written-in-python/
# https://github.com/tonyjaimep/maze_solver
# https://www.codementor.io/blog/basic-pathfinding-explained-with-python-5pil8767c1
# https://py.checkio.org/blog/find-path/
# https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
# https://py.checkio.org/mission/open-labyrinth/publications/macfreek/python-3/re-useable-code/share/3e8556d514ca04502facb316b41ff49d/
# https://py.checkio.org/blog/find-path/
# http://bryukh.com/labyrinth-algorithms/

# maze generator:
# https://en.wikipedia.org/wiki/Maze_generation_algorithm
