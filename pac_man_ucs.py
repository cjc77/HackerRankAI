# Credit to MaskRay for the idea of using a dynamic programming strategy to retrieve path taken

from queue import PriorityQueue

WALL = '%'
# [UP, LEFT, RIGHT, DOWN]
moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
m = n = 0


def find_path(p_pos, f_pos, board):
    global m, n
    q = PriorityQueue()
    pruned = []
    p_table = [[None] * n for _ in range(m)]

    pr, pc = p_pos
    q.put((0, (pr, pc)))
    p_table[pr][pc] = (pr, pc)

    while not q.empty():
        cost, (pr, pc) = q.get()
        if (pr, pc) == f_pos:
            break
        for m in moves:
            r, c = pr + m[0], pc + m[1]
            if board[r][c] != WALL and not p_table[r][c]:
                p_table[r][c] = (pr, pc)
                q.put((cost + 1, (r, c)))

    r, c = f_pos
    pr, pc = p_pos
    while (r, c) != p_pos:
        pruned.append((r, c))
        r, c = p_table[r][c]
    pruned.append((pr, pc))
    print(len(pruned) - 1)
    for r, c in reversed(pruned):
        print("{} {}".format(r, c))


def main():
    global m, n
    p_pos = tuple([int(x) for x in input().strip().split()])
    f_pos = tuple([int(x) for x in input().strip().split()])
    m, n = [int(x) for x in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(m)]
    find_path(p_pos, f_pos, board)


if __name__ == '__main__':
    main()
