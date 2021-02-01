import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

import math

def solution(n):
    cnt = 0
    while n > 1:
        is_prime = True
        for di in range(2, int(math.sqrt(n)) + 1):
            if n % di == 0:
                n = di
                is_prime = False
                break
        if is_prime:
            n -= 1
        cnt += 1

    return cnt

t = int(input())
for tt in range(t):
    n = int(input())
    print(solution(n))

#####################################################

print('time', time.time_ns() - ptime)

