import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, a):
    opercnt = 0
    s = sum(a)
    mincnt = -1
    while opercnt < n:
        if s % (n - opercnt) != 0:
            opercnt += 1
            continue
        cursum = 0
        avg = s / (n - opercnt)
        issuccess = True
        for i in a:
            cursum += i
            if cursum > avg:
                issuccess = False
                break
            if cursum == avg:
                cursum = 0

        if issuccess:
            mincnt = opercnt
            break
        opercnt += 1

    return mincnt

t = int(input())
for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solution(n, a))

#####################################################



print('time', time.time_ns() - ptime)

