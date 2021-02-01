import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, s):
    for i in range(5):
        if s[:i] + s[-4+i:] == '2020':
            return 'YES'
    return 'NO'

t = int(input())
for tt in range(t):
    n = int(input())
    s = input().strip()
    print(solution(n, s))

#####################################################



print('time', time.time_ns() - ptime)

