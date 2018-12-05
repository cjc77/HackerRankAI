pos = {'mr': -1, 'mc': -1, 'pr': -1, 'pc': -1}
grid = []


def build_grid():
    m = int(input())
    for i in range(m):
        grid.append(input().strip())
    return m


def examine_grid(m):
    for i in range(m):
        for j in range(m):
            if grid[i][j] == 'm':
                pos['mr'] = i
                pos['mc'] = j
            if grid[i][j] == 'p':
                pos['pr'] = i
                pos['pc'] = j


def find_path():
    dist_r = pos['mr'] - pos['pr']
    dist_c = pos['mc'] - pos['pc']
    while abs(dist_r) > 0 or abs(dist_c) > 0:
        # print('Vertical Dist: {}'.format(dist_r))
        # print('Horizontal Dist: {}'.format(dist_c))
        # handle U/D *logic is reversed*
        if dist_r < 0:
            print('DOWN')
            dist_r += 1
        elif dist_r > 0:
            print('UP')
            dist_r -= 1
        # handle U/D
        if dist_c < 0:
            print('RIGHT')
            dist_c += 1
        elif dist_c > 0:
            print('LEFT')
            dist_c -= 1


def main():
    m = build_grid()
    examine_grid(m)
    find_path()


if __name__ == '__main__':
    main()
