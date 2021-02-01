import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n,m,r,c):
    mr = max(n-r, r-1)
    mc = max(m-c, c-1)
    # print(mr,mc)
    return mr + mc

t = int(input())
for tt in range(t):
    n, m, r, c = map(int,input().split())
    print(solution(n,m,r,c))

#####################################################

print('time', time.time_ns() - ptime)

