import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################




def solution(n, m, s, t):
    totalmax = 0

    value = [-1 for _ in range(n)]



    return totalmax

n, m = map(int, input().split())
s = input().strip()
t = input().strip()
print(solution(n, m, s, t))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
