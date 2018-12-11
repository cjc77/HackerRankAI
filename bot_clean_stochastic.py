CLEAN = "CLEAN"
RIGHT = "RIGHT"
LEFT = "LEFT"
UP = "UP"
DOWN = "DOWN"

d_pos = (-1, -1)


def find_dirty_cell(board):
    global d_pos
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'd':
                d_pos = (i, j)
                break


def next_move(posr, posc, board):
    global d_pos

    if d_pos == (-1, -1):
        find_dirty_cell(board)

    # Clean?
    if (posr, posc) == d_pos:
        print(CLEAN)
        d_pos = (-1, -1)
        return

    if posr < d_pos[0]:
        print(DOWN)
    elif posr > d_pos[0]:
        print(UP)
    elif posc < d_pos[1]:
        print(RIGHT)
    elif posc > d_pos[1]:
        print(LEFT)


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)