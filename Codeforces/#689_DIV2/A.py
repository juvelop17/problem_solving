import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, k):
    nstr = 'a' * k
    for i in range(n-k):
        if i % 3 == 0:
            nstr += 'b'
        elif i % 3 == 1:
            nstr += 'c'
        else:
            nstr += 'a'
    return nstr

t = int(input())
for tt in range(t):
    n, k = map(int, input().split())
    print(solution(n, k))

#####################################################

print('time', time.time_ns() - ptime)

