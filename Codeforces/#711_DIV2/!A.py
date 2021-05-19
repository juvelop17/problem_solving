import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(n):
    nsum = 0
    while n:
        nsum += n % 10
        n = n // 10
    print(nsum)
    print(gcd(n,nsum))
    return

t = int(input())
for tt in range(t):
    n = int(input())
    print(solution(n))



#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')














