import math

def next_move(posr, posc, board):
    # if bot is on a dirty cell, clean it
    if board[posr][posc] == 'd':
        print('CLEAN')
        return
    # Find the closest dirty cell (via euclidean distance)
    dists = []
    for i in range(len(board)):
        for j in range(len(board)):
            # find distances
            if board[i][j] == 'd':
                dist = math.sqrt((posr - i) ** 2 + (posc - j) ** 2)
                dists.append((dist, (i, j)))
    dists.sort(key=lambda x: x[0])
    loc = dists[0][1]
    if posr < loc[0]:
        print('DOWN')
    elif posr > loc[0]:
        print('UP')
    elif posc < loc[1]:
        print('RIGHT')
    elif posc > loc[1]:
        print('LEFT')

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)