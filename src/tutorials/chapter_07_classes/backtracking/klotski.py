import enum
import random

import tutorials.chapter_07_classes.backtracking.stack_queue_impl as collections


class Direction(enum.Enum):
    UP = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DOWN = (1, 0)

    def opposite(self):
        return Direction((-self.value[0], -self.value[1]))

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

    def occupied_spaces(self):
        if not self.occupied:
            self.occupied = [(self.x_coord + i, self.y_coord + j)
                             for i in range(self.length) for j in range(self.width)]
        return self.occupied

    def is_occupied(self, x, y):
        return self.x_coord <= x < self.x_coord + self.length and self.y_coord <= y < self.y_coord + self.width

    def __str__(self):
        return '{name={}, x_coord={}, y_coord={}, length={}, width={}}'.format(
            self.name, self.x_coord, self.y_coord, self.length, self.width)

    def __repr__(self):
        return 'SlidingBlock(name={}, x_coord={}, y_coord={}, length={}, width={})'.format(
            self.name, self.x_coord, self.y_coord, self.length, self.width)


class SlidingGameBoard:
    def __init__(self, length, width, sliding_blocks: list, finish_criteria):
        self.length = length
        self.width = width
        self.sliding_blocks = sliding_blocks
        self.finish_criteria = finish_criteria

        # Need to move these somewhere else, interfering with board copying.
        # Need to keep board lightweight for copying
        self.name_to_block = {x.name: x for x in sliding_blocks}

        self.shape_to_num = {}
        counter = 0  # 0 indicates empty
        for block in sliding_blocks:  # same shape should have same number, so reduce branches
            exist_num = self.shape_to_num.get((block.length, block.width), None)
            if not exist_num:
                counter += 1
                self.shape_to_num[(block.length, block.width)] = counter

        self.steps = []

        self.layout = None

    def get_layout(self):
        if not self.layout:
            self.layout = [[0] * self.width for _ in range(self.length)]
            for b in self.sliding_blocks:
                spaces = b.occupied_spaces()
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

    # for performance reason, we spill out details, so lengthy
    def is_movable(self, direction, block):
        layout = self.get_layout()
        if direction == Direction.UP:
            if block.x_coord == 0:  # out of bound check
                return False
            top_row = layout[block.x_coord-1]  # overlay check
            for i in range(block.width):
                if block.y_coord + i < self.width and top_row[block.y_coord + i] != 0:  # 0 means empty
                    return False
        elif direction == Direction.DOWN:
            if block.x_coord + block.length == self.length:
                return False
            bottom_row = layout[block.x_coord + block.length]
            for i in range(block.width):
                if block.y_coord + i < self.width and bottom_row[block.y_coord + i] != 0:
                    return False
        elif direction == Direction.LEFT:
            if block.y_coord == 0:
                return False
            for i in range(block.length):
                if block.x_coord + i < self.length and layout[block.x_coord + i][block.y_coord - 1] != 0:
                    return False
        elif direction == Direction.RIGHT:
            if block.y_coord + block.width == self.width:
                return False
            for i in range(block.length):
                if block.x_coord + i < self.length and layout[block.x_coord + i][block.y_coord + block.width] != 0:
                    return False

        return True

    def __str__(self):
        return str(self.steps) + ', ' + str(self.layout)

    def __repr__(self):  # without this, during debug, list of this class does not show str.
        return str(self.steps) + ', ' + str(self.layout)

    def deep_clone(self):
        # copy.deepcopy and pickle are slow since we have internal states
        # return pickle.loads(pickle.dumps(self))
        new_blocks = []
        for b in self.sliding_blocks:
            new_blocks.append(SlidingBlock(b.name, b.x_coord, b.y_coord, b.length, b.width))

        cls = self.__class__
        ret = cls.__new__(cls)
        ret.length = self.length
        ret.width = self.width
        ret.sliding_blocks = new_blocks
        ret.name_to_block = {x.name: x for x in new_blocks}
        ret.finish_criteria = self.finish_criteria

        ret.steps = self.steps.copy()
        ret.shape_to_num = self.shape_to_num
        ret.layout = None  # don't copy this field since block is moved.
        return ret


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
                    move_to(d, block, board, cache, queue, results, zobrist_tbl)

    return results


def move_to(direction, block, board, cache, queue, results, zobrist_tbl):
    block.move(direction)

    new_board = board.deep_clone()
    new_board.steps.append((block.name, block.x_coord, block.y_coord, direction.name))

    if new_board.finish_criteria(new_board):  # if it is a solution, add to result and stop
        results.append(new_board)
    else:
        hb = new_board.hash_board(zobrist_tbl)
        if hb not in cache:  # check if it is already dealt with. If not, add it as new case.
            cache.add(hb)
            queue.enqueue(new_board)

    block.move(direction.opposite())  # restore to last state for next try


# https://github.com/jeantimex/klotski
# https://www.jianshu.com/p/4a77d6253d33
# https://inst.eecs.berkeley.edu/~cs61c/fa14/projs/02/
# https://www.ixueshu.com/document/83b73e57dd554a55100410a5ba28df48318947a18e7f9386.html

# https://stackify.com/how-to-use-python-profilers-learn-the-basics/
# https://pythonspeed.com/articles/beyond-cprofile/
