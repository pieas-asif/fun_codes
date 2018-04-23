import copy

board = [
    "...6.1...",
    "..45.72..",
    "1.3...7.6",
    ".5.9.3.8.",
    "3...8...9",
    "28..5..73",
    "5..7.8..1",
    ".4.2.5.6.",
    "..23.48.."
]


def main():
    global board
    for idx, line in enumerate(board):
        board[idx] = list(line)

    solve()
    print_board()


def solve():
    global board

    try:
        fill_all_obvious()
    except:
        return False

    if is_complete():
        return True

    i, j = 0, 0
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == ".":
                i, j = row_index, col_index

    possibilities = get_possibilities(i, j)
    for value in possibilities:
        snapshot = copy.deepcopy(board)
        board[i][j] = value
        result = solve()

        if result:
            return True
        else:
            board = copy.deepcopy(snapshot)

    return False


def fill_all_obvious():
    global board
    while True:
        something_changed = False
        for i in range(0, 9):
            for j in range(0, 9):
                possibilities = get_possibilities(i, j)
                if not possibilities:
                    continue
                if len(possibilities) == 0:
                    raise RuntimeError("No Moves Left")
                if len(possibilities) == 1:
                    board[i][j] = possibilities[0]
                    something_changed = True

        if not something_changed:
            return


def get_possibilities(i, j):
    global board
    if board[i][j] != '.':
        return False
    possibilities = {str(n) for n in range(1, 10)}
    for val in board[i]:
        possibilities -= set(val)

    for idx in range(0, 9):
        possibilities -= set(board[idx][j])

    istart = (i // 3) * 3
    jstart = (j // 3) * 3

    sub_board = board[istart:istart+3]
    for idx, row in enumerate(sub_board):
        sub_board[idx] = row[jstart:jstart+3]

    for row in sub_board:
        for col in row:
            possibilities -= set(col)

    return list(possibilities)


def print_board():
    global board
    for row in board:
        for col in row:
            print(col, end="")
        print()


def is_complete():
    global board
    for row in board:
        for col in row:
            if col == ".":
                return False

    return True


main()
