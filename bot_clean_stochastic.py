import math as m


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


def nextMove(posr, posc, board):
    global d_pos
    # Clean?
    if board[posr][posc] == 'd':
        print(CLEAN)
        # Reset dirty position to not found
        d_pos = (-1, -1)
        return

    # Assess Board if dirty position has not been found
    if d_pos[0] == -1 or d_pos[1] == -1:
        find_dirty_cell(board)

    # Determine next move
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
    nextMove(pos[0], pos[1], board)