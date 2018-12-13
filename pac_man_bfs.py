# Credit to MaskRay for the idea of using a dynamic programming strategy to retrieve path taken

WALL = '%'
# [UP, LEFT, RIGHT, DOWN]
moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
m = n = 0


def find_path(p_pos, f_pos, board):
    pr, pc = p_pos
    bfs_expanded = []
    bfs_pruned = []
    q = [(pr, pc)]
    # Using dynamic programming to retrieve final path taken
    p_table = [[None] * n for _ in range(m)]
    p_table[pr][pc] = (pr, pc)

    while q:
        pr, pc = q.pop(0)
        bfs_expanded.append((pr, pc))
        if (pr, pc) == f_pos:
            break
        for move in moves:
            r, c = pr + move[0], pc + move[1]
            if board[r][c] != WALL and not p_table[r][c]:
                p_table[r][c] = (pr, pc)
                q.append((r, c))

    print(len(bfs_expanded))
    for r, c in bfs_expanded:
        print("{} {}".format(r, c))

    r, c = f_pos
    pr, pc = p_pos
    while (r, c) != p_pos:
        bfs_pruned.append((r, c))
        r, c = p_table[r][c]
    # Don't forget about the first position
    bfs_pruned.append((pr, pc))
    # -1 since do not count starting out as a move
    print(len(bfs_pruned) - 1)
    for r, c in reversed(bfs_pruned):
        print("{} {}".format(r, c))


def main():
    global m, n
    # read board
    p_pos = tuple([int(x) for x in input().strip().split()])
    f_pos = tuple([int(x) for x in input().strip().split()])
    m, n = [int(x) for x in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(m)]
    find_path(p_pos, f_pos, board)


if __name__ == '__main__':
    main()
