import enum
import random

import puzzles.backtracking.stack_queue_impl as collections


class Direction(enum.Enum):
    UP = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3

    def opposite(self):
        if self == self.UP:
            return self.DOWN
        elif self == self.DOWN:
            return self.UP
        elif self == self.RIGHT:
            return self.LEFT
        elif self == self.LEFT:
            return self.RIGHT


class SlidingBlock:
    def __init__(self, name, x_coord, y_coord, length, width):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.length = length
        self.width = width

        self.occupied = []  # cache for performance

    def move(self, direction):
        if direction == Direction.UP:
            self.x_coord -= 1
            self.occupied = []
            return self.x_coord, self.y_coord
        elif direction == Direction.LEFT:
            self.y_coord -= 1
            self.occupied = []
            return self.x_coord, self.y_coord
        elif direction == Direction.RIGHT:
            self.y_coord += 1
            self.occupied = []
            return self.x_coord, self.y_coord
        elif direction == Direction.DOWN:
            self.x_coord += 1
            self.occupied = []
            return self.x_coord, self.y_coord

        return None

    def occupied_spaces(self):
        if not self.occupied:
            self.occupied = [(self.x_coord + i, self.y_coord + j)
                             for i in range(self.length) for j in range(self.width)]
        return self.occupied

    # def is_overlaid(self, sliding_block):
    #     if not self.occupied:
    #         self.occupied = [(self.x_coord + i, self.y_coord + j)
    #                          for i in range(self.length) for j in range(self.width)]
    #
    #     other_occupied = sliding_block.occupied_spaces()
    #     intersection = set(self.occupied) & set(other_occupied)
    #     return len(intersection) > 0

    def is_occupied(self, x, y):
        return self.x_coord <= x < self.x_coord + self.length and self.y_coord <= y < self.y_coord + self.width

    def __str__(self):
        return '{name={}, x={}, y={}, len={}, wid={}}'.format(
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
        # this field shouldn't be here, need to move to solver
        self.zobrist_tbl = [[[random.randint(1, 2**64 - 1)
                              for _ in range(len(self.shape_to_num)+1)]  # 1 for empty space case
                             for _ in range(width)] for _ in range(length)]

        self.layout = None

    # def is_out_of_bounds(self, sliding_block):
    #     for space in sliding_block.occupied_spaces():
    #         if space[0] < 0 or space[0] >= self.length:
    #             return True
    #         if space[1] < 0 or space[1] >= self.width:
    #             return True
    #
    #     return False

    def get_layout(self):
        if not self.layout:
            self.layout = [[0] * self.width for _ in range(self.length)]
            for b in self.sliding_blocks:
                spaces = b.occupied_spaces()
                for (x, y) in spaces:
                    self.layout[x][y] = self.shape_to_num[(b.length, b.width)]

        return self.layout

    # def is_overlaid(self, sliding_block):
    #     for block in self.sliding_blocks:
    #         if block == sliding_block:
    #             continue
    #
    #         if block.is_overlaid(sliding_block):
    #             return True
    #
    #     return False

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

        ret.zobrist_tbl = self.zobrist_tbl  # random is slow

        ret.layout = None  # don't copy this field since block is moved.
        return ret


def hash_board(board: SlidingGameBoard):
    hb = board.get_layout()

    ret = 0
    for i in range(board.length):
        for j in range(board.width):
            ret ^= board.zobrist_tbl[i][j][hb[i][j]]

    # we could also add symmetric board as well if we know board is symmetric/door location
    # but rush hour game is not symmetric, so we leave this optimization out.
    return ret


def solve(board: SlidingGameBoard):
    print("board shape: len={}, wid={}".format(board.length, board.width))

    results = []
    cache = {hash_board(board)}
    # use queue because we need to find the shortest path
    queue = collections.MyQueue()
    queue.enqueue(board)
    while queue:
        board = queue.dequeue()
        print('queue size={}, steps={}'.format(len(queue), len(board.steps)))

        for block in board.sliding_blocks:
            # we could use Direction for loop to shorten this
            if is_movable(Direction.UP, block, board):
                move_to(Direction.UP, block, board, cache, queue, results)
            if is_movable(Direction.DOWN, block, board):
                move_to(Direction.DOWN, block, board, cache, queue, results)
            if is_movable(Direction.LEFT, block, board):
                move_to(Direction.LEFT, block, board, cache, queue, results)
            if is_movable(Direction.RIGHT, block, board):
                move_to(Direction.RIGHT, block, board, cache, queue, results)

    return results


# for performance reason, we spill out details, so lengthy
def is_movable(direction, block, board):
    layout = board.get_layout()
    if direction == Direction.UP:
        if block.x_coord == 0:
            return False
        top_row = layout[block.x_coord-1]
        for i in range(block.width):
            if block.y_coord + i < board.width and top_row[block.y_coord + i] != 0:  # 0 means empty
                return False
    elif direction == Direction.DOWN:
        if block.x_coord + block.length == board.length:
            return False
        bottom_row = layout[block.x_coord+block.length]
        for i in range(block.width):
            if block.y_coord + i < board.width and bottom_row[block.y_coord + i] != 0:
                return False
    elif direction == Direction.LEFT:
        if block.y_coord == 0:
            return False
        for i in range(block.length):
            if block.x_coord + i < board.length and layout[block.x_coord + i][block.y_coord - 1] != 0:
                return False
    elif direction == Direction.RIGHT:
        if block.y_coord + block.width == board.width:
            return False
        for i in range(block.length):
            if block.x_coord + i < board.length and layout[block.x_coord + i][block.y_coord + block.width] != 0:
                return False

    return True


def move_to(direction, block, board, cache, queue, results):
    block.move(direction)
    # if not board1.is_out_of_bounds(block) and not board1.is_overlaid(block):
    new_board = board.deep_clone()
    new_board.steps.append((block.name, block.x_coord, block.y_coord, direction.name))

    if new_board.finish_criteria(new_board):  # if it is a solution, add to result and stop
        results.append(new_board)
    else:
        hb = hash_board(new_board)
        if hb not in cache:  # check if it is already dealt with. If not, add it as new case.
            cache.add(hb)
            queue.enqueue(new_board)

    block.move(direction.opposite())  # restore to last state for next try


# ## testing
def finish_criteria1(board):
    block = board.name_to_block['boss']
    return block.is_occupied(4, 1) and block.is_occupied(4, 2)


def test():
    # game1 = SlidingGameBoard(5, 4, [
    #     SlidingBlock('boss', 0, 1, 2, 2),
    #     SlidingBlock('general1', 2, 1, 1, 2),
    #     SlidingBlock('general2', 0, 0, 2, 1),
    # ], finish_criteria1)

    game1 = SlidingGameBoard(5, 4, [
        SlidingBlock('boss', 0, 1, 2, 2),

        SlidingBlock('general1', 2, 1, 1, 2),
        SlidingBlock('general2', 0, 0, 2, 1),
        SlidingBlock('general3', 0, 3, 2, 1),
        SlidingBlock('general4', 2, 0, 2, 1),
        SlidingBlock('general5', 2, 3, 2, 1),

        SlidingBlock('solder1', 3, 1, 1, 1),
        SlidingBlock('solder2', 3, 2, 1, 1),
        SlidingBlock('solder3', 4, 0, 1, 1),
        SlidingBlock('solder4', 4, 3, 1, 1),
    ], finish_criteria1)

    solution = solve(game1)
    for s in solution:
        print('-' * 80)
        print(len(s.steps))
        print(s)


# from pyinstrument import Profiler
#
# profiler = Profiler()
# profiler.start()
#
# test()
#
# profiler.stop()
# print(profiler.output_text(unicode=True, color=True))

import cProfile
cProfile.run('test()')
