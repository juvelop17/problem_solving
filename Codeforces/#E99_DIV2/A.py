import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n):
    return len(str(n))

t = int(input())
for tt in range(t):
    n = int(input())
    print(solution(n))

#####################################################

print('time', time.time_ns() - ptime)

