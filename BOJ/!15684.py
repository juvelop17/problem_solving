import sys
import time
from itertools import combinations

prev_time = time.time_ns()
# sys.stdin = open('input1.txt', 'r')
read = sys.stdin.readline


def solution():
    memory_arr = [arr[i][:] for i in range(H+1)]
    if check(memory_arr) == True:
        return 0

    for co in comb1:
        # print(co)
        memory_arr = [arr[i][:] for i in range(H+1)]
        for c in co:
            memory_arr[c[0]][c[1]] = 1
        # printMap(memory_arr)
        if check(memory_arr) == True:
            return 1

    for co in comb2:
        # print(co)
        if co[0][0] == co[1][0] and abs(co[0][1] - co[1][1]) == 1:
            continue
        memory_arr = [arr[i][:] for i in range(H+1)]
        for c in co:
            memory_arr[c[0]][c[1]] = 1
        # printMap(memory_arr)
        if check(memory_arr) == True:
            return 2

    for co in comb3:
        # print(co)
        if (co[0][0] == co[1][0] and abs(co[0][1] - co[1][1]) == 1) or \
                (co[1][0] == co[2][0] and abs(co[0][1] - co[1][1]) == 1) or \
                (co[2][0] == co[0][0] and abs(co[0][1] - co[1][1]) == 1):
            continue
        memory_arr = [arr[i][:] for i in range(H+1)]
        for c in co:
            memory_arr[c[0]][c[1]] = 1
        # printMap(memory_arr)
        if check(memory_arr) == True:
            return 3

    return -1


def check(memory_arr):
    # for i in range(1,H):
    #     for j in range(1,N):
    #         if memory_arr[i][j] == 1 and memory_arr[i][j+1] == 1:
    #             print('위반')
    #             return False

    for i in range(1,N+1):
        curr_pos = [1, i]
        goal_pos = [H+1, i]

        while curr_pos[0] <= H:
            if curr_pos[1] - 1 >= 0 and memory_arr[curr_pos[0]][curr_pos[1] - 1] == 1:
                curr_pos = [curr_pos[0] + 1, curr_pos[1] - 1]
            elif curr_pos[1] + 1 <= N and memory_arr[curr_pos[0]][curr_pos[1]] == 1:
                curr_pos = [curr_pos[0] + 1, curr_pos[1] + 1]
            else:
                curr_pos = [curr_pos[0] + 1, curr_pos[1]]

        if curr_pos != goal_pos:
            return False
    return True



def printMap(memory_arr):
    for i in range(H+1):
        for j in range(N+1):
            print(memory_arr[i][j], end='')
        print()
    print()


N, M, H = map(int, read().strip().split())
M_list = [list(map(int, read().strip().split())) for _ in range(M)]

side_M_list = []
arr = [[0 for _ in range(N+1)] for _ in range(H+1)]
for m in M_list:
    a = m[0]
    b = m[1]
    arr[a][b] = 1

    side_M_list.append([a, b-1])
    side_M_list.append([a, b+1])
# printMap(arr)

point_list = []
for i in range(1,H+1):
    for j in range(1,N+1):
        if [i,j] not in M_list+side_M_list:
            point_list.append([i,j])

comb1 = list(combinations(point_list, 1))
comb2 = list(combinations(point_list, 2))
comb3 = list(combinations(point_list, 3))
# print(len(comb1),comb1)
# print(len(comb2),comb2)
# print(len(comb3),comb3)


print(solution())
# print('time', time.time_ns() - prev_time)
