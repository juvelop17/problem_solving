import sys
import time
from itertools import combinations

prev_time = time.time_ns()
# sys.stdin = open('input1.txt', 'r')
read = sys.stdin.readline


def solution():


def solve(c, )


def printMap(memory_arr):
    for i in range(H+1):
        for j in range(N+1):
            print(memory_arr[i][j], end='')
        print()
    print()


N, M, H = map(int, read().strip().split())
M_list = [list(map(int, read().strip().split())) for _ in range(M)]


print(solution())
# print('time', time.time_ns() - prev_time)
