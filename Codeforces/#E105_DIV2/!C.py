import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

# 1 5 11 15
# 6 7 15


def solution(n, m, a, b):
    lcorrect = 0
    rcorrect = 0
    i = 0
    j = 0

    while i < n and j < m:
        if a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            if a[i] < 0:
                lcorrect += 1
            else:
                rcorrect += 1
            i += 1
            j += 1
    print(lcorrect, rcorrect)

    return

t = int(input())
for tt in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solution(n, m, a, b))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
