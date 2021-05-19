import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def wait_time(p, x):
    if p % x == 0:
        return 0
    return x*(p//x+1)-p

def solution(p, a, b, c):
    return min(wait_time(p, a), wait_time(p, b), wait_time(p, c))

t = int(input())
for tt in range(t):
    p, a, b, c = list(map(int, input().split()))
    print(solution(p, a, b, c))

#####################################################



print('time', time.time_ns() - ptime)

