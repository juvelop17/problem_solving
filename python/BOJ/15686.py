import time
import sys
from itertools import combinations

prev_time = time.time_ns()
# sys.stdin = open('input.txt','r')
read = sys.stdin.readline

def solution():
    min_val = 10**9

    for co in comb_chi:
        house_val = [0 for _ in range(len(house_list))]

        for i in range(len(house_list)):
            min_dis = 10 ** 9
            for c in co:
                val_dis = abs(c[0]-house_list[i][0]) + abs(c[1]-house_list[i][1])
                if min_dis > val_dis:
                    min_dis = val_dis
            house_val[i] = min_dis
        min_val = min(min_val,sum(house_val))
    return min_val


N,M = map(int,read().strip().split())
map_arr = [list(map(int,read().strip().split())) for _ in range(N)]

house_list = []
chi_list = []
for i in range(N):
    for j in range(N):
        val = map_arr[i][j]
        if val == 1:
            house_list.append([i,j])
        elif val == 2:
            chi_list.append([i,j])

comb_chi = combinations(chi_list, M)

print(solution())
# print('time',time.time_ns()-prev_time)

