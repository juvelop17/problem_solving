import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, alist):
    min_num = min(alist)
    cnt = 0
    for i in range(len(alist)):
        if alist[i] == min_num:
            cnt += 1
    return len(alist) - cnt

t = int(input())
for tt in range(t):
    n = int(input())
    alist = list(map(int, input().split()))
    print(solution(n, alist))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
