import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################

def solution(a,b,c,d):
    if a + b == c + d:
        return a + b
    return max(a + b, c + d)


t = int(input())
for tt in range(t):
    a, b, c, d = map(int, input().split())
    print(solution(a,b,c,d))


#####################################################

print('time',time.time_ns()-ptime)

