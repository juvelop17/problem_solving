import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################


def solution(n, a, b):

    sort_list = []
    for ai, bi in zip(a, b):
        sort_list.append((ai, bi))
    print(sort_list)
    sort_list.sort(reverse=True)
    print(sort_list)

    a_max = 10**9
    b_sum = 0
    for i in range(n):
        if a_max


    return

t = int(input())
for tt in range(t):
    n = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solution(n, a, b)

#####################################################

print('time', time.time_ns() - ptime)

