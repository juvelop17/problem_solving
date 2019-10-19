import sys
import time

prev_time = time.time_ns()
# sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution():
    que = []
    que.append([r, c, d])
    init_d = d
    while len(que) > 0:
        node = que.pop(0)
        node_r = node[0]
        node_c = node[1]
        node_d = node[2]

        # clean
        _map[node_r][node_c] = 2
        # printMap()

        if node_d == 0:
            new_d = 3
        else:
            new_d = node_d - 1

        new_r = node_r + dr[new_d]
        new_c = node_c + dc[new_d]
        if _map[new_r][new_c] == 0:
            que.append([new_r, new_c, new_d])
            init_d = new_d
        else:
            if init_d == new_d:
                back_r = node_r + dr[new_d-2]
                back_c = node_c + dc[new_d-2]
                if _map[back_r][back_c] == 2:
                    que.append([back_r,back_c,new_d])
                else:
                    break
            else:
                que.append([node_r, node_c, new_d])

    return getScore()


def checkRange(i,j):
    return i >= 0 and i < N and j >= 0 and j < M


def getScore():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 2:
                cnt += 1
    return cnt


def printMap():
    for i in range(N):
        for j in range(M):
            print(_map[i][j],end='')
        print()
    print()



N, M = map(int, read().strip().split())
r, c, d = map(int, read().strip().split())
## d : 북,동,남,서

_map = []
for _ in range(N):
    _map.append(list(map(int, read().strip().split())))

# memory_map = []
# for i in range(N):
#     memory_map[i] = _map[i][:]

print(solution())
# print('time', time.time_ns()-prev_time)
