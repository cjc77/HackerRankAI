WALL = '%'
# [UP, LEFT, RIGHT, DOWN]
moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
m = n = 0


def find_path(p_pos, f_pos, board):
    p_r, p_c = p_pos
    dfs_expanded = []
    dfs_pruned = []
    stack = [(p_r, p_c)]
    # Using dynamic programming to retrieve final path taken
    p_table = [[None] * n for _ in range(m)]

    while stack:
        p_r, p_c = stack.pop()
        dfs_expanded.append((p_r, p_c))
        if (p_r, p_c) == f_pos:
            break
        for move in moves:
            r, c = p_r + move[0], p_c + move[1]
            if board[r][c] != WALL and not p_table[r][c]:
                p_table[r][c] = (p_r, p_c)
                stack.append((r, c))
    print(len(dfs_expanded))
    for r, c in dfs_expanded:
        print("{} {}".format(r, c))

    r, c = f_pos
    p_r, p_c = p_pos
    while (r, c) != (p_r, p_c):
        dfs_pruned.append((r, c))
        r, c = p_table[r][c]
    # Don't forget to append the first position
    dfs_pruned.append((p_r, p_c))
    # -1 since not counting starting out as a move
    print(len(dfs_pruned) - 1)
    for r, c in reversed(dfs_pruned):
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
