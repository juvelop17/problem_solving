import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(k):
    g = gcd(100, k)
    volume = 100 // g
    k //= g
    water = volume - k

    return k + water

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        n = a % b
        a = b
        b = n
    return a

t = int(input())
for tt in range(t):
    k = int(input())
    print(solution(k))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
