import enum
import copy

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
        if direction == Direction.LEFT:
            self.y_coord -= 1
        if direction == Direction.RIGHT:
            self.y_coord += 1
        if direction == Direction.DOWN:
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

    def __hash__(self):
        return hash((self.name, self.x_coord, self.y_coord, self.length, self.width))

    def __eq__(self, other):
        return self.name == other.name and self.x_coord == other.x_coord and \
               self.y_coord == other.y_coord and self.length == other.length \
               and self.width == other.width


class SlidingGameBoard:
    def __init__(self, length, width, sliding_blocks: list, finish_criteria):
        self.length = length
        self.width = width
        self.sliding_blocks = sliding_blocks
        self.name_to_block = {x.name: x for x in sliding_blocks}
        self.finish_criteria = finish_criteria

        self.num_steps = 0
        self.steps = []

    def is_out_of_bounds(self, sliding_block):
        for space in sliding_block.occupied_spaces():
            if space[0] < 0 or space[0] >= self.length:
                return True
            if space[1] < 0 or space[1] >= self.width:
                return True

        return False

    def is_overlaid(self, sliding_block):
        for block in self.sliding_blocks:
            if block == sliding_block:
                continue

            if block.is_overlaid(sliding_block):
                return True

        return False

    def __hash__(self):
        return hash((self.length, self.width,
                     hash(frozenset(self.sliding_blocks)), hash(frozenset(self.steps)),
                     hash(self.finish_criteria)))

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width and \
               set(self.sliding_blocks) == set(other.sliding_blocks) and \
               set(self.steps) == set(other.steps) and \
               self.finish_criteria == other.finish_criteria


def solve(board: SlidingGameBoard):
    print("board shape: len={}, wid={}".format(board.length, board.width))

    results = []
    cache = {board}
    stack = collections.MyStack()
    stack.push(board)
    while stack:
        board1 = stack.pop()

        if board1.num_steps >= 100:
            continue

        for block in board1.sliding_blocks:
            move_to(Direction.UP, block, board1, cache, stack, results)
            move_to(Direction.DOWN, block, board1, cache, stack, results)
            move_to(Direction.LEFT, block, board1, cache, stack, results)
            move_to(Direction.RIGHT, block, board1, cache, stack, results)

    return results


def move_to(direction, block, board1, cache, stack, results):
    block.move(direction)
    if not board1.is_out_of_bounds(block) and not board1.is_overlaid(block) and board1 not in cache:
        new_board = copy.deepcopy(board1)
        if new_board.finish_criteria(board1):
            results.append(new_board)
        else:
            cache.add(new_board)
            stack.push(new_board)

        new_board.num_steps += 1
        new_board.steps.append((block.name, block.x_coord, block.y_coord, direction))
    block.move(direction.opposite())


def finish_criteria1(board):
    block = board.name_to_block['boss']
    return block.is_occupied(4, 1) and block.is_occupied(4, 2)


game1 = SlidingGameBoard(5, 4, [SlidingBlock('boss', 0, 0, 2, 2)], finish_criteria1)
solution = solve(game1)
print(solution)
