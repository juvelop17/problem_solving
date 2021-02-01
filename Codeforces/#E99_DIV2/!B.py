import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

cnt_list = [-1 for _ in range(10**6+1)]

def solution(x):
    cnt = -1
    for i in range(1,10**6):
        if i*(i+1)/2 >= x:
            cnt = i
            break
    cnt += int(cnt*(cnt+1)/2) - x

    return cnt

t = int(input())
for tt in range(t):
    x = int(input())
    print(solution(x))

#####################################################



print('time', time.time_ns() - ptime)

