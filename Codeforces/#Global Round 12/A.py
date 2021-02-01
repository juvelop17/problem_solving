import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, a):
    cnt = 0
    prev = 0
    b = ''
    for i, ch in enumerate(a):
        if ch == 'b':
            cnt += 1
            b += a[prev:i]
            prev = i+1
    b += a[prev:]
    b = 'b' * cnt + b

    return b

t = int(input())
for tt in range(t):
    n = int(input())
    a = input()
    print(solution(n, a))

#####################################################



print('time', time.time_ns() - ptime)

