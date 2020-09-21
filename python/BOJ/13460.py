# 구슬 탈출

import sys
import time

prev_time = time.time_ns()
# sys.stdin = open('input.txt', 'r')


# 상하좌우 이동
# return : red, blue 위치

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

def checkStatus(node):
    if node[0] < 0 or node[0] >= N or node[1] < 0 or node[1] >= M:
        return False
    return True


def move(dir, red, blue):
    if dir == 'up':
        i = 0
    elif dir == 'down':
        i = 1
    elif dir == 'right':
        i = 2
    else:
        i = 3

    _red = [red[0], red[1]]
    _blue = [blue[0], blue[1]]
    res = [False, False]
    for _ in range(max(N,M)):
        new_red = [_red[0] + di[i],_red[1] + dj[i]]
        if checkStatus(new_red):
            if _map[new_red[0]][new_red[1]] == '.' and new_red != _blue:
                _red[0] = new_red[0]
                _red[1] = new_red[1]
            elif _map[new_red[0]][new_red[1]] == 'O':
                _red[0] = new_red[0]
                _red[1] = new_red[1]
                res[0] = True

        new_blue = [_blue[0] + di[i],_blue[1] + dj[i]]
        if checkStatus(new_blue):
            if _map[new_blue[0]][new_blue[1]] == '.' and new_blue != _red:
                _blue[0] = new_blue[0]
                _blue[1] = new_blue[1]
            elif _map[new_blue[0]][new_blue[1]] == 'O':
                _blue[0] = new_blue[0]
                _blue[1] = new_blue[1]
                res[1] = True

    return _red, _blue, res


# red, blue, O 위치
def getPos():
    red = None
    blue = None
    hole = None
    for i in range(len(_map)):
        for j in range(len(_map[i])):
            if _map[i][j] == 'R':
                red = [i, j]
                _map[i][j] = '.'
            elif _map[i][j] == 'B':
                blue = [i, j]
                _map[i][j] = '.'
            elif _map[i][j] == 'O':
                hole = [i, j]

    return red, blue, hole


def print_map(red, blue):
    for i in range(N):
        for j in range(M):
            if red == [i, j]:
                print('R', end='')
            elif blue == [i, j]:
                print('B', end='')
            else:
                print(_map[i][j], end='')
        print()
    print()


def solution():
    red, blue, hole = getPos()

    # red, blue, res = move('left', red, blue)
    # red, blue, res = move('down', red, blue)
    # red, blue, res = move('up', red, blue)
    # print_map(red, blue)

    que = []
    que.append([red, blue, 0])
    while len(que) != 0:
        node = que.pop(0)
        node_red = node[0]
        node_blue = node[1]
        cnt = node[2]

        if _map_memory[node_red[0]][node_red[1]][node_blue[0]][node_blue[1]] == True:
            continue
        if cnt > 9:
            continue

        # print(cnt, '###########################################')
        # print_map(node_red,node_blue)

        new_red, new_blue, res = move('up', node_red, node_blue)
        if res == [True, False]:
            return cnt + 1
        elif res[1] != True:
            que.append([new_red, new_blue, cnt + 1])

        new_red, new_blue, res = move('down', node_red, node_blue)
        if res == [True, False]:
            return cnt + 1
        elif res[1] != True:
            que.append([new_red, new_blue, cnt + 1])

        new_red, new_blue, res = move('left', node_red, node_blue)
        if res == [True, False]:
            return cnt + 1
        elif res[1] != True:
            que.append([new_red, new_blue, cnt + 1])

        new_red, new_blue, res = move('right', node_red, node_blue)
        if res == [True, False]:
            return cnt + 1
        elif res[1] != True:
            que.append([new_red, new_blue, cnt + 1])

        _map_memory[node_red[0]][node_red[1]][node_blue[0]][node_blue[1]] = True

    return -1


_map = []
N, M = map(int, sys.stdin.readline().strip().split())
for _ in range(N):
    _map.append(list(sys.stdin.readline().strip()))

_map_memory = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

print(solution())
# print('time', time.time_ns() - prev_time)