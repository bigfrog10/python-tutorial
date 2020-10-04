import tutorials.chapter_07_classes.backtracking.stack_queue_impl as collections
import copy
# https://en.wikipedia.org/wiki/Eight_queens_puzzle

QUEEN = 1


def _no_attack(board, row, column):
    n = len(board)

    for row_num in range(row):  # check column
        if board[row_num][column] == QUEEN:
            return False

    for i in range(1, n):  # check diagonals
        r = row - i
        c = column - i  # upper left diagonal
        if 0 <= r < n and 0 <= c < n and board[r][c] == QUEEN:
            return False

        c = column + i  # upper right diagonal
        if 0 <= r < n and 0 <= c < n and board[r][c] == QUEEN:
            return False

    return True


def solve(size):
    # create empty chessboard
    chessboard = [[0] * size for _ in range(size)]

    states = collections.MyStack()
    states.push((chessboard, 0))
    result = []
    while states:
        board, row_num = states.pop()
        row = board[row_num]

        for index, value in enumerate(row):
            new_board = copy.deepcopy(board)
            new_board[row_num][index] = QUEEN

            if _no_attack(new_board, row_num, index):
                if row_num + 1 == size:
                    result.append(new_board)  # if you reached the end, save the result
                else:
                    states.push((new_board, row_num + 1))  # save the board for further exploration
            # otherwise ignore

    return result


res = solve(8)
print(len(res))
# for s in res:
#     for j in s:
#         print(j)
