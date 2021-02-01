import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################


# p = ax
# x = bq + r (r != 0)
# p = a(bq + r)
#   = abq + ar







def solution(p, q):
    max_num = -1

    if p % q != 0:
        return p

    x = q
    while x > 1:
        for div in range(2,q+1):
            if x % div == 0:
                x = x // div
                if p % x == 0:
                    return x
                break

    return -1

t = int(input())
for tt in range(t):
    p, q = map(int, input().split())
    print(solution(p, q))


#####################################################

print('time',time.time_ns()-ptime)

