import sys


def solution(R, C, T, dust_map):
    dust_position_list = []
    purifier_position_list = findPurifier(R, C, dust_map)

    for i in range(T):
        # dust 찾기
        dust_position_list = findDust(R, C, dust_map)

        # 미세먼지 확산
        dust_map = dustDiffuse(R, C, dust_map, dust_position_list, purifier_position_list)

        # 공기청정기 작동
        operatePurifier(R, C, dust_map, purifier_position_list)
        printMap(dust_map)


def findDust(R, C, dust_map):
    dust_position_list = []
    for r in range(R):
        for c in range(C):
            if dust_map[r][c] not in [0, -1]:
                dust_position_list.append([r, c])
    return dust_position_list


def findPurifier(R, C, dust_map):
    purifier_position_list = []
    for r in range(R):
        for c in range(C):
            if dust_map[r][c] == -1:
                purifier_position_list.append([r, c])
    return purifier_position_list


def dustDiffuse(R, C, dust_map, dust_position_list, purifier_position_list):
    new_map = []
    for i in range(R):
        new_map.append([0 for _ in range(C)])

    for r, c in purifier_position_list:
        new_map[r][c] = -1

    while len(dust_position_list) > 0:
        node = dust_position_list.pop()
        i, j = node
        val = dust_map[i][j]
        cnt = 0

        if mapConstraint(R, C, dust_map, i - 1, j):
            new_map[i - 1][j] += val // 5
            cnt += 1
        if mapConstraint(R, C, dust_map, i + 1, j):
            new_map[i + 1][j] += val // 5
            cnt += 1
        if mapConstraint(R, C, dust_map, i, j - 1):
            new_map[i][j - 1] += val // 5
            cnt += 1
        if mapConstraint(R, C, dust_map, i, j + 1):
            new_map[i][j + 1] += val // 5
            cnt += 1

        new_map[i][j] = val - cnt * (val // 5)

    printMap(new_map)
    return new_map


def mapConstraint(R, C, dust_map, i, j):
    if i < 0 or i >= R or j < 0 or j >= C:
        return False
    if dust_map[i][j] == -1:
        return False
    return True


def operatePurifier(R, C, dust_map, purifier_position_list):
    purifier_position = purifier_position_list[0]
    i, j = purifier_position
    next_i, next_j = nextDustPosition(R,C,purifier_position,i,j,'u')
    curr_i, curr_j = next_i, next_j
    curr_val = dust_map[curr_i][curr_j]
    dust_map[curr_i][curr_j] = 0

    while not (next_i == i and next_j == j):
        next_i, next_j = nextDustPosition(R, C, purifier_position, curr_i, curr_j,'u')
        next_val = dust_map[next_i][next_j]

        curr_i, curr_j = next_i, next_j
        dust_map[curr_i][curr_j] = curr_val
        curr_val = next_val

    purifier_position = purifier_position_list[1]
    i, j = purifier_position
    next_i, next_j = nextDustPosition(R,C,purifier_position,i,j,'d')
    curr_i, curr_j = next_i, next_j
    curr_val = dust_map[curr_i][curr_j]
    dust_map[curr_i][curr_j] = 0

    while not (next_i == i and next_j == j):
        next_i, next_j = nextDustPosition(R, C, purifier_position, curr_i, curr_j,'d')
        next_val = dust_map[next_i][next_j]

        curr_i, curr_j = next_i, next_j
        dust_map[curr_i][curr_j] = curr_val
        curr_val = next_val

def nextDustPosition(R, C, purifier_position,curr_i, curr_j,direction):
    next_i, next_j = -1, -1
    if direction == 'u':
        if curr_i == purifier_position[0] and curr_j != C-1:
            next_i, next_j = curr_i, curr_j + 1
        elif curr_j == C-1 and curr_i != 0:
            next_i, next_j = curr_i-1, curr_j
        elif curr_i == 0 and curr_j != 0:
            next_i, next_j = curr_i, curr_j - 1
        elif curr_j == 0:
            next_i, next_j = curr_i+1, curr_j

    elif direction == 'd':
        if curr_i == purifier_position[0] and curr_j != C-1:
            next_i, next_j = curr_i, curr_j + 1
        elif curr_j == C - 1 and curr_i != R - 1:
            next_i, next_j = curr_i + 1, curr_j
        elif curr_i == R - 1 and curr_j != 0:
            next_i, next_j = curr_i, curr_j - 1
        elif curr_j == 0:
            next_i, next_j = curr_i - 1, curr_j

    print('nextDustPosition',next_i, next_j)
    return next_i, next_j


def printMap(_map):
    for r in range(len(_map)):
        for c in range(len(_map[r])):
            print(_map[r][c], end='\t')
        print()
    print()


sys.stdin = open('input.txt', 'r')

dust_map = []
R, C, T = map(int, sys.stdin.readline().strip().split())
print(R, C, T)
for row in range(R):
    dust_map.append(list(map(int, sys.stdin.readline().strip().split())))
printMap(dust_map)

solution(R, C, T, dust_map)
