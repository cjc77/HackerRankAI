# Method borrowed from Wikipedia [https://en.wikipedia.org/wiki/A*_search_algorithm]

from queue import PriorityQueue
from math import inf

WALL = '%'
# [UP, LEFT, RIGHT, DOWN]
moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
m = n = 0


def manhattan_est(p1, p):
    return abs(p1[0] - p[0]) + abs(p1[1] - p[1])


def init_score(score_map, board):
    global m, n
    for i in range(m):
        for j in range(n):
            if board[i][j] != WALL:
                score_map[(i, j)] = inf


def reconstruct_path(came_from, current, start):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
        if current == start:
            break
    print(len(total_path) - 1)
    for r, c in reversed(total_path):
        print("{} {}".format(r, c))


def find_path(start, goal, board):
    global m, n
    closed_set = set()
    open_set = PriorityQueue()
    open_set_inv = set()
    came_from = {}
    g_score = {}
    f_score = {}

    init_score(g_score, board)
    init_score(f_score, board)
    g_score[start] = 0
    f_score[start] = manhattan_est(start, goal)

    open_set.put(
        (f_score[start], start)
    )
    open_set_inv.add(start)
    came_from[start] = start

    while not open_set.empty():
        cost, curr = open_set.get()
        open_set_inv.remove(curr)

        if curr == goal:
            reconstruct_path(came_from, curr, start)
        closed_set.add(curr)
        for m in moves:
            neighbor = curr[0] + m[0], curr[1] + m[1]
            if board[neighbor[0]][neighbor[1]] != WALL and neighbor not in closed_set:
                t_g_score = g_score[curr] + 1
                if neighbor not in open_set_inv:
                    open_set.put(
                        (f_score[neighbor], neighbor)
                    )
                    open_set_inv.add(neighbor)

                if t_g_score >= g_score[neighbor]:
                    continue

                came_from[neighbor] = curr
                g_score[neighbor] = t_g_score
                f_score[neighbor] = g_score[neighbor] + manhattan_est(neighbor, goal)


def main():
    global m, n
    p_pos = tuple([int(x) for x in input().strip().split()])
    f_pos = tuple([int(x) for x in input().strip().split()])
    m, n = [int(x) for x in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(m)]
    find_path(p_pos, f_pos, board)


if __name__ == '__main__':
    main()
