import math as m

CLEAN = "CLEAN"
RIGHT = "RIGHT"
LEFT = "LEFT"
UP = "UP"
DOWN = "DOWN"

dirty = []


def find_dirty_cells(posr, posc, h, w, board):
    global dirty
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'd':
                dist = m.sqrt((posr - i) ** 2 + (posc - j) ** 2)
                dirty.append([(i, j), dist])
    dirty.sort(key=lambda x: x[1])


def update_dists(posr, posc, board):
    global dirty
    for d in dirty:
        d[1] = m.sqrt((posr - d[0][0]) ** 2 + (posc - d[0][1]) ** 2)
    dirty.sort(key=lambda x: x[1])


def next_move(posr, posc, h, w, board):
    global dirty
    if (posr, posc) == dirty[0][0]:
        print(CLEAN)
        dirty.pop(0)
        update_dists(posr, posc, board)
        return

    target = dirty[0][0]
    if posr < target[0]:
        print(DOWN)
    elif posr > target[0]:
        print(UP)
    elif posc < target[1]:
        print(RIGHT)
    elif posc > target[1]:
        print(LEFT)
    update_dists(posr, posc, board)


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    find_dirty_cells(pos[0], pos[1], dim[0], dim[1], board)
    next_move(pos[0], pos[1], dim[0], dim[1], board)