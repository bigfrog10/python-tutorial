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

    def move(self, direction):
        if direction == Direction.UP:
            self.x_coord -= 1
        elif direction == Direction.LEFT:
            self.y_coord -= 1
        elif direction == Direction.RIGHT:
            self.y_coord += 1
        elif direction == Direction.DOWN:
            self.x_coord += 1

    def occupied_spaces(self):
        return [(self.x_coord + i, self.y_coord + j) for i in range(self.length) for j in range(self.width)]

    def is_overlaid(self, sliding_block):
        os1 = self.occupied_spaces()
        os2 = sliding_block.occupied_spaces()
        intersection = set(os1) & set(os2)
        return len(intersection) > 0

    def is_occupied(self, x, y):
        return self.x_coord <= x < self.x_coord + self.length and self.y_coord <= y < self.y_coord + self.width

    def __str__(self):
        return '{name={}, x={}, y={}, len={}, wid={}}'.format(
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
        for block in sliding_blocks:
            exist_num = self.shape_to_num.get((block.length, block.width), None)
            if not exist_num:
                counter += 1
                self.shape_to_num[(block.length, block.width)] = counter

        self.steps = []
        self.zobrist_tbl = [[[random.randint(1, 2**64 - 1)
                              for _ in range(len(self.shape_to_num)+1)]  # 1 for empty space case
                             for _ in range(width)] for _ in range(length)]

    def is_out_of_bounds(self, sliding_block):
        for space in sliding_block.occupied_spaces():
            if space[0] < 0 or space[0] >= self.length:
                return True
            if space[1] < 0 or space[1] >= self.width:
                return True

        return False

    def get_layout(self):
        ret = [[0] * self.width for _ in range(self.length)]
        for b in self.sliding_blocks:
            spaces = b.occupied_spaces()
            for (x, y) in spaces:
                ret[x][y] = self.shape_to_num[(b.length, b.width)]

        return ret

    def is_overlaid(self, sliding_block):
        for block in self.sliding_blocks:
            if block == sliding_block:
                continue

            if block.is_overlaid(sliding_block):
                return True

        return False

    def __str__(self):
        return str(self.steps)

    def __repr__(self):  # without this, during debug, list of this class does not show str.
        return str(self.steps)

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

        return ret


def hash_board(board: SlidingGameBoard):
    hb = board.get_layout()

    ret = 0
    for i in range(board.length):
        for j in range(board.width):
            ret ^= board.zobrist_tbl[i][j][hb[i][j]]

    # we could also add symmetric board as well if we know board is symmetric/door location

    return ret


def solve(board: SlidingGameBoard):
    print("board shape: len={}, wid={}".format(board.length, board.width))

    results = []
    cache = {hash_board(board)}
    # use queue because we need to find the shortest path
    queue = collections.MyQueue()
    queue.enqueue(board)
    while queue:
        board1 = queue.dequeue()
        print('steps={}, queue size={}'.format(len(board1.steps), len(queue)))

        if len(board1.steps) >= 150:
            continue

        for block in board1.sliding_blocks:
            # we could use Direction for loop to shorten this
            move_to(Direction.UP, block, board1, cache, queue, results)
            move_to(Direction.DOWN, block, board1, cache, queue, results)
            move_to(Direction.LEFT, block, board1, cache, queue, results)
            move_to(Direction.RIGHT, block, board1, cache, queue, results)

    return results


def move_to(direction, block, board1, cache, queue, results):
    block.move(direction)
    if not board1.is_out_of_bounds(block) and not board1.is_overlaid(block):
        new_board = board1.deep_clone()
        new_board.steps.append((block.name, block.x_coord, block.y_coord, direction.name))
        hb = hash_board(board1)
        if new_board.finish_criteria(board1):
            results.append(new_board)
        elif hb not in cache:
            cache.add(hb)
            queue.enqueue(new_board)

    block.move(direction.opposite())


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


import cProfile
cProfile.run('test()')
