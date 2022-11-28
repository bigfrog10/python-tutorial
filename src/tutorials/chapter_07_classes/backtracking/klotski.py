import enum
import random

import tutorials.chapter_07_classes.backtracking.stack_queue_impl as collections


class Direction(enum.Enum):
    UP = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DOWN = (1, 0)

class SlidingBlock:
    def __init__(self, name, x_coord, y_coord, length, width):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.length = length
        self.width = width

        self.occupied = []  # cache for performance

    def move(self, direction):
        self.x_coord += direction.value[0]
        self.y_coord += direction.value[1]

        self.occupied = []

    def border(self):
        if not self.occupied:
            self.occupied = [(self.x_coord + i, self.y_coord + j) 
                             for i in range(self.length) for j in range(self.width) 
                             if i == 0 or i + 1 == self.length or j == 0 or j + 1 == self.width
                             ]
        return self.occupied

    def is_occupied(self, x, y):
        return self.x_coord <= x < self.x_coord + self.length and self.y_coord <= y < self.y_coord + self.width

    def __str__(self):
        return '(name={}, x_coord={}, y_coord={}, length={}, width={})'.format(
            self.name, self.x_coord, self.y_coord, self.length, self.width)

    def __repr__(self):
        return 'SlidingBlock(name={}, x_coord={}, y_coord={}, length={}, width={})'.format(
            self.name, self.x_coord, self.y_coord, self.length, self.width)


class SlidingGameBoard:
    def __init__(self, length, width, sliding_blocks: list, finish_criteria, shape_to_num = None, steps = None):
        self.length = length
        self.width = width
        self.sliding_blocks = sliding_blocks
        self.finish_criteria = finish_criteria

        self.name_to_block = {x.name: x for x in sliding_blocks}
        self.shape_to_num = shape_to_num if shape_to_num else {shape:i+1 for i, shape in enumerate(set([(block.length, block.width) for block in sliding_blocks]))}
        self.steps = steps if steps else []
        self.layout = None

    def get_layout(self):
        if not self.layout:
            self.layout = [[0] * self.width for _ in range(self.length)]
            for b in self.sliding_blocks:
                spaces = b.border()
                for (x, y) in spaces:
                    self.layout[x][y] = self.shape_to_num[(b.length, b.width)]

        return self.layout

    def hash_board(self, zobrist_tbl):
        hb = self.get_layout()

        ret = 0
        for i in range(self.length):
            for j in range(self.width):
                ret ^= zobrist_tbl[i][j][hb[i][j]]

        # we could also add symmetric board as well if we know board is symmetric/door location
        # but rush hour game is not symmetric, so we leave this optimization out.
        return ret

    # since each move just has one step to one direction, collision can be detected by borders
    def is_movable(self, direction, block):
        layout = self.get_layout()
        for x,y in block.border():
            x += direction.value[0]
            y += direction.value[1]
            if x<0 or x >= self.length or y<0 or y>=self.width:
                return False
            if not block.is_occupied(x, y) and layout[x] and layout[x][y] and layout[x][y] != 0:
                return False
        return True

    def move(self, block_name, direction):
        block = self.name_to_block[block_name]
        block.move(direction)
        self.steps.append((block.name, block.x_coord, block.y_coord, direction.name))

    def __str__(self):
        return str(self.steps) + ', ' + str(self.layout)

    def __repr__(self):  # without this, during debug, list of this class does not show str.
        return str(self.steps) + ', ' + str(self.layout)

    def deep_clone(self):
        # copy.deepcopy and pickle are slow since we have internal states
        # return pickle.loads(pickle.dumps(self))
        return SlidingGameBoard(self.length, self.width,
            [SlidingBlock(b.name, b.x_coord, b.y_coord, b.length, b.width) for b in self.sliding_blocks],
            self.finish_criteria,
            self.shape_to_num,
            self.steps.copy())

def solve(board: SlidingGameBoard):
    print("board shape: len={}, wid={}".format(board.length, board.width))

    zobrist_tbl = [[[random.randint(1, 2**64 - 1)
                     for _ in range(len(board.shape_to_num)+1)]  # 1 for empty space case
                    for _ in range(board.width)] for _ in range(board.length)]
    dirs = list(Direction)  # avoid regenerate list everytime, for looping all directions
    results = []
    cache = {board.hash_board(zobrist_tbl)}  # filter out explored cases, cut branches
    queue = collections.MyQueue()  # this means breathe first search (BFS), find shortest paths
    queue.enqueue(board)
    while queue:
        board = queue.dequeue()
        print('queue size={}, steps={}'.format(len(queue), len(board.steps)))

        for block in board.sliding_blocks:
            for d in dirs:  # loop through UP, DOWN, LEFT and RIGHT in Direction
                if board.is_movable(d, block):
                    move_to(d, block.name, board, cache, queue, results, zobrist_tbl)

    return results


def move_to(direction, block_name, board, cache, queue, results, zobrist_tbl):
    new_board = board.deep_clone()
    new_board.move(block_name, direction)

    if new_board.finish_criteria(new_board):  # if it is a solution, add to result and stop
        results.append(new_board)
    else:
        hb = new_board.hash_board(zobrist_tbl)
        if hb not in cache:  # check if it is already dealt with. If not, add it as new case.
            cache.add(hb)
            queue.enqueue(new_board)



# https://github.com/jeantimex/klotski
# https://www.jianshu.com/p/4a77d6253d33
# https://inst.eecs.berkeley.edu/~cs61c/fa14/projs/02/
# https://www.ixueshu.com/document/83b73e57dd554a55100410a5ba28df48318947a18e7f9386.html

# https://stackify.com/how-to-use-python-profilers-learn-the-basics/
# https://pythonspeed.com/articles/beyond-cprofile/
