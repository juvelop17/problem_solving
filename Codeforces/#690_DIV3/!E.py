import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, a):
    a.sort()
    numdic = {}
    for i in a:
        if i not in numdic:
            numdic[i] = 0
        numdic[i] += 1
    print(numdic)

    print()

    return

t = int(input())
for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solution(n, a))

#####################################################



print('time', time.time_ns() - ptime)

