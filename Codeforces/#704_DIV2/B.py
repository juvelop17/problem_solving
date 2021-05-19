import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

from collections import deque

def solution(n, p):
    reslist = deque()
    cur_idx = 0
    while cur_idx < len(p):
        # print('cur_idx',cur_idx)
        # print('p',p)
        idx = len(p)
        for i in range(cur_idx, len(p)):
            if p[cur_idx] < p[i]:
                idx = i
                break
        for i in range(idx-1,cur_idx-1,-1):
            reslist.appendleft(p[i])
        cur_idx = idx

    for num in reslist:
        print(num, end=' ')
    print()

    return

t = int(input())
for tt in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    solution(n, p)

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')

