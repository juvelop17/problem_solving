import sys
import time

prev_time = time.time_ns()
# sys.stdin = open('input1.txt', 'r')
read = sys.stdin.readline


def solution():
    min_score = 10 ** 9

    explore([])
    # print('res_explore', res_explore)
    for node in res_explore:
        memory_arr = [arr[r][:] for r in range(N)]
        for i in range(len(node)):
            node_dir = node[i]
            node_cctv_num = cctv_list[i][0]
            node_cctv_i = cctv_list[i][1]
            node_cctv_j = cctv_list[i][2]

            for dir in cctv_dir_list[node_cctv_num][node_dir]:
                mark(memory_arr, dir, node_cctv_i, node_cctv_j)

        min_score = min(min_score,getScore(memory_arr))
    return min_score


def explore(pick):
    n = len(pick)
    if n == len(cctv_list):
        res_explore.append(pick[:])
        return

    cctv_num = cctv_list[n][0]
    for c in range(len(cctv_dir_list[cctv_num])):
        pick.append(c)
        explore(pick)
        pick.pop()


def mark(memory_arr, dir, i, j):  # dir : 북 동 남 서
    new_i, new_j = i + di[dir], j + dj[dir]
    is_poss = True

    while is_poss:
        if not (checkRange(new_i, new_j) and memory_arr[new_i][new_j] != 6):
            break
        memory_arr[new_i][new_j] = '#'
        new_i += di[dir]
        new_j += dj[dir]


def checkRange(i, j):
    return i >= 0 and i < N and j >= 0 and j < M


def getScore(memory_arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if memory_arr[i][j] == 0:
                cnt += 1
    return cnt


def printMap(memory_arr):
    for i in range(N):
        for j in range(M):
            print(memory_arr[i][j],end='')
        print()
    print()


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cctv_dir_list = [0,
                 [[0],[1],[2],[3]],
                 [[0,2],[1,3]],
                 [[0,1],[1,2],[2,3],[3,0]],
                 [[3,0,1],[0,1,2],[1,2,3],[2,3,0]],
                 [[0,1,2,3]]]
res_explore = []

N, M = map(int, read().strip().split())
arr = [list(map(int, read().strip().split())) for _ in range(N)]

wall_list = []
cctv_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 6:
            wall_list.append([i, j])
        elif arr[i][j] in [1, 2, 3, 4, 5]:
            cctv_list.append([arr[i][j], i, j])
# print(wall_list)
# print(cctv_list)

print(solution())
# print('time', time.time_ns() - prev_time)
