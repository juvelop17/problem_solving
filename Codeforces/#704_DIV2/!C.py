import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

from collections import deque

def solution(n, m, s, t):
    totalmax = 0
    que = deque()

    que.append((0, 0, 0, -1))
    while que:
        curs, curt, curmax, prevs = que.popleft()

        if m - curt > n - curs:
            continue
        if curt == m:
            if totalmax < curmax:
                totalmax = curmax
            continue

        if s[curs] == t[curt]:
            nextmax = curmax
            if curmax < curs - prevs and prevs != -1:
                nextmax = curs - prevs
            que.append((curs+1,curt+1,nextmax,curs))
        que.append((curs + 1, curt, curmax, prevs))

    return totalmax

n, m = map(int, input().split())
s = input().strip()
t = input().strip()
print(solution(n, m, s, t))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
