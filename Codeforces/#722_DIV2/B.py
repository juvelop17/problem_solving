import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, a):
    a.sort()
    # print(a)

    min_diff = 10**10
    fin_idx = 0
    for i in range(1, len(a)):
        if abs(a[i]-a[i-1]) < min_diff :
            min_diff = abs(a[i]-a[i-1])
        if a[i] > 0:
            if a[i] > min_diff:
                break
            fin_idx = i
            break
        fin_idx = i
    return fin_idx + 1

t = int(input())
for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solution(n, a))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
