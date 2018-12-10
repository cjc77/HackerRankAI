pos = {'mr': -1, 'mc': -1, 'pr': -1, 'pc': -1}


def get_initial_pos():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                pos['mr'] = i
                pos['mc'] = j
            elif grid[i][j] == 'p':
                pos['pr'] = i
                pos['pc'] = j


def nextMove(n, r, c, grid):
    # if this is the first move, assess grid
    if pos['mr'] == -1 and pos['mc'] == -1:
        get_initial_pos()
    # Determine next move
    # Vertical
    if pos['mr'] > pos['pr']:
        pos['mr'] -= 1
        return 'UP'
    elif pos['mr'] < pos['pr']:
        pos['mr'] += 1
        return 'DOWN'
    # Horizontal
    if pos['mc'] > pos['pc']:
        pos['mc'] -= 1
        return 'LEFT'
    elif pos['mc'] < pos['pc']:
        pos['mc'] += 1
        return 'RIGHT'


n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())
print(nextMove(n, r, c, grid))
