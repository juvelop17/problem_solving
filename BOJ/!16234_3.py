## list.pop : O
## deque : O(1)

import sys
import time
from collections import deque

prev_time = time.time_ns()
sys.stdin = open('input.txt','r')
read = sys.stdin.readline


def solution():
    is_succ = True
    total_cnt = -1
    while is_succ:
        total_cnt += 1
        is_succ = False
        memory_map = [[0 for _ in range(N)] for _ in range(N)]

        cnt = 0
        for i in range(N):
            for j in range(N):
                if memory_map[i][j] == 0:
                    cnt += 1
                    explore(memory_map, i, j, cnt, [])
        # printMap(memory_map)
        # printMap(country_map)
        if cnt != N * N:
            is_succ = True

    return total_cnt


def explore(memory_map, i, j, n, pick):
    deq = deque()
    deq.append([i, j])
    sum = 0
    while len(deq) > 0:
        node = deq.popleft()
        node_i = node[0]
        node_j = node[1]
        memory_map[node_i][node_j] = n
        pick.append([node_i, node_j])
        sum += country_map[node_i][node_j]

        for d in range(4):
            new_i = node_i + di[d]
            new_j = node_j + dj[d]
            if 0 <= new_i < N and 0 <= new_j < N and \
                    L <= abs(country_map[node_i][node_j] - country_map[new_i][new_j]) <= R and \
                    memory_map[new_i][new_j] == 0:

                memory_map[new_i][new_j] = n
                deq.append([new_i, new_j])

    for p in pick:
        country_map[p[0]][p[1]] = sum // len(pick)


def checkRange(i, j):
    return 0 <= i < N and 0 <= j < N


def checkLR(i, j, new_i, new_j):
    return L <= abs(country_map[i][j] - country_map[new_i][new_j]) <= R


def printMap(memory_map):
    for i in range(N):
        for j in range(N):
            print(memory_map[i][j], end=' ')
        print()
    print()


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, L, R = map(int, read().strip().split())
country_map = [list(map(int, read().strip().split())) for _ in range(N)]

print(solution())
print('time',time.time_ns()-prev_time)
