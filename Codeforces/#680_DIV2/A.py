import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################

def solution(n, x, a, b):
    answer = ''

    b.sort(reverse=True)
    pick = [False for _ in range(len(b))]

    for i in range(len(a)):
        is_pop = False
        for j in range(len(b)):
            if a[i] + b[j] <= x and pick[j] == False:
                pick[j] = True
                is_pop = True
                break
        if is_pop == False:
            return 'No'

    return 'Yes'


t = int(input())
for tt in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solution(n, x, a, b))
    if tt < t-1:
        input()


#####################################################

print('time',time.time_ns()-ptime)

