import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, k, balls):

    return

t = int(input())
for tt in range(t):
    n, k = map(int, input().split())
    balls = []
    for _ in range(n):
        balls.append(tuple(map(int,input().split())))
    print(solution(n, k, balls))

#####################################################



print('time', time.time_ns() - ptime)

